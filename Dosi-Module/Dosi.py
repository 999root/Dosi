
import winreg
import uuid
import os
import shutil


class DosiRegisterEditor:
    def __init__(self, regedit_path: str | None) -> None:
        self.path = regedit_path

    def read(self, key_name):
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.path) as key:
                value, _ = winreg.QueryValueEx(key, key_name)
                return value
        except FileNotFoundError:
            return "ERR"
        except Exception as ex:
            print("Error accessing the Registry:", ex)
            return "ERR"

    def write(self, key_name, value):
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.path, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, key_name, 0, winreg.REG_SZ, str(value))
                return True
        except FileNotFoundError:
            return False
        except Exception as ex:
            print("Error accessing the Registry:", ex)
            return False
        

class Checker:
    def __init__(self) -> None:
        pass

    def check_registry_keys(self):
        try:
            self.check_registry_key("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "InstallationID")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ComputerName", "ComputerName")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ComputerName", "ActiveComputerName")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ComputerNamePhysicalDnsDomain", "")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ActiveComputerName", "ComputerName")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ActiveComputerName", "ActiveComputerName")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ActiveComputerName", "ComputerNamePhysicalDnsDomain")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "Hostname")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "NV Hostname")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces", "Hostname")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces", "NV Hostname")
            self.check_registry_key("HARDWARE\\DEVICEMAP\\Scsi", "")  # ScsiPorts
            self.check_registry_key("HARDWARE\\DEVICEMAP\\Scsi\\{port}", "")  # ScsiBuses
            self.check_registry_key("HARDWARE\\DEVICEMAP\\Scsi\\{port}\\{bus}\\Target Id 0\\Logical Unit Id 0", "DeviceIdentifierPage")
            self.check_registry_key("HARDWARE\\DEVICEMAP\\Scsi\\{port}\\{bus}\\Target Id 0\\Logical Unit Id 0", "Identifier")
            self.check_registry_key("HARDWARE\\DEVICEMAP\\Scsi\\{port}\\{bus}\\Target Id 0\\Logical Unit Id 0", "InquiryData")
            self.check_registry_key("HARDWARE\\DEVICEMAP\\Scsi\\{port}\\{bus}\\Target Id 0\\Logical Unit Id 0", "SerialNumber")
            self.check_registry_key("HARDWARE\\DESCRIPTION\\System\\MultifunctionAdapter\\0\\DiskController\\0\\DiskPeripheral", "")  # DiskPeripherals
            self.check_registry_key("HARDWARE\\DESCRIPTION\\System\\MultifunctionAdapter\\0\\DiskController\\0\\DiskPeripheral\\{disk}", "Identifier")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001", "HwProfileGuid")
            self.check_registry_key("SOFTWARE\\Microsoft\\Cryptography", "MachineGuid")
            self.check_registry_key("SOFTWARE\\Microsoft\\SQMClient", "MachineId")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "BIOSReleaseDate")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "BIOSVersion")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "ComputerHardwareId")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "ComputerHardwareIds")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "ComputerManufacturer")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "ComputerModel")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "InstallDate")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemBiosMajorVersion")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemBiosMinorVersion")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemBiosVersion")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemManufacturer")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemProductName")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemSku")
            self.check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemVersion")
        except Exception as ex:
            print("Error checking the Registry-Keys:", ex)

    def check_registry_key(self, key_path, value_name):
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)
        if key is not None:
            if value_name:
                try:
                    value = winreg.QueryValueEx(key, value_name)
                    if value is None:
                        print("Registry-Key not found:", key_path + "\\" + value_name)
                except FileNotFoundError:
                    print("Registry-Key not found:", key_path + "\\" + value_name)
            else:
                subkey_count, _, _ = winreg.QueryInfoKey(key)
                if subkey_count == 0:
                    print("Registry-Key not found:", key_path)
        else:
            print("Registry-Key not found:", key_path)
        

class Spoof:
    def __init__(self) -> None:
        self.dre = DosiRegisterEditor()
        self.obj = None
        self.key = None
        self.path = None

    def SpoofHWID(self) -> tuple:
        """
        Spoofs your HWID

        Key: HwProfileGuid
        Path: SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001

        Returns your result and a log in a tuple
        """

        obj = self.dre.Regedit(r"SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001")
        Key = "HwProfileGuid"

        Log = []
        old_value = obj.read(Key)
        new_value = "{" + str(uuid.uuid4()) + "}"
        result = obj.write(Key, new_value)
        if result:
            Log.append(f"[SPOOFER] HWID Changed from {old_value} to {new_value}")
        else:
            Log.append("[SPOOFER] Error accessing the Registry... Maybe run as admin")
        return result, Log
    
    def SpoofGUID(self) -> tuple:
        """
        Spoofs your PCGUID

        Key: MachineGuid
        Path: SOFTWARE\\Microsoft\\Cryptography

        Returns your result and a log in a tuple
        """
        self.obj = self.dre.Regedit(r"SOFTWARE\\Microsoft\\Cryptography")
        self.key = "MachineGuid"

        Log = []
        old_value = self.obj.read(self.key)
        new_value = "{" + str(uuid.uuid4()) + "}"
        result = self.obj.write(self.key, new_value)
        if result:
            Log.append(f"[SPOOFER] GUID Changed from {old_value} to {new_value}")
        else:
            Log.append("[SPOOFER] Error accessing the Registry... Maybe run as admin")
        return result, Log
    
    def SpoofPCNAME(self) -> tuple:
        """
        Spoofs your PC's hostname

        Key: ComputerName
        Path: SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ActiveComputerName

        Returns your result and a log in a tuple
        """
        self.obj = self.dre.Regedit(r"SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ActiveComputerName")
        self.key = "ComputerName"

        Log = []
        old_value = self.obj.read(self.key)
        new_value = "{" + str(uuid.uuid4()) + "}"
        result = self.obj.write(self.key, new_value)
        if result:
            Log.append(f"[SPOOFER] PCNAME Changed from {old_value} to {new_value}")
        else:
            Log.append("[SPOOFER] Error accessing the Registry... Maybe run as admin")
        return result, Log
    
    def SpoofPRODUCTID(self) -> tuple:
        """
        Spoofs your PC's ProductId

        Key: ProductId
        Path: SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion

        Returns your result and a log in a tuple
        """
        self.obj = self.dre.Regedit(r"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion")
        self.key = "ProductId"

        Log = []
        old_value = self.obj.read(self.key)
        new_value = "{" + str(uuid.uuid4()) + "}"
        result = self.obj.write(self.key, new_value)
        if result:
            Log.append(f"[SPOOFER] ProductId Changed from {old_value} to {new_value}")
        else:
            Log.append("[SPOOFER] Error accessing the Registry... Maybe run as admin")
        return result, Log


class Cache:
    def __init__(self):
        pass

    def FullClean(self):
        """
        Clears both Ubisoft and Valorant Cache Stores
        """
        self.clear_ubisoft_cache()
        print('\n\n')
        self.clear_valorant_cache()

    def clear_ubisoft_cache(self) -> None:
        """
        Clears Ubisoft Cache
        """
        app_data_path = os.path.join(os.environ["LOCALAPPDATA"], "Ubisoft Game Launcher")
        ubisoft_path = os.path.join(app_data_path, "cache")
        ubisoft_logs_path = os.path.join(app_data_path, "logs")
        ubisoft_savegames_path = os.path.join(app_data_path, "savegames")
        ubisoft_spool_path = os.path.join(app_data_path, "spool")

        for path in [ubisoft_path, ubisoft_logs_path, ubisoft_savegames_path, ubisoft_spool_path]:
            if os.path.exists(path):
                try:
                    shutil.rmtree(path)
                    print("Successfully cleared:", path)
                except Exception as e:
                    print("Error while clearing", path, ":", e)

    def clear_valorant_cache(self) -> None:
        """
        Clears Valorant Cache
        """
        valorant_path = os.path.join(os.environ["LOCALAPPDATA"], "VALORANT", "saved")
        
        if os.path.exists(valorant_path):
            try:
                shutil.rmtree(valorant_path)
                print("Successfully cleared Valorant cache")
            except Exception as e:
                print("Error while clearing Valorant cache:", e)
        else:
            print("Valorant cache directory not found")
