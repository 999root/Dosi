import winreg

def check_registry_keys():
    try:
        check_registry_key("SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "InstallationID")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ComputerName", "ComputerName")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ComputerName", "ActiveComputerName")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ComputerNamePhysicalDnsDomain", "")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ActiveComputerName", "ComputerName")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ActiveComputerName", "ActiveComputerName")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ActiveComputerName", "ComputerNamePhysicalDnsDomain")
        check_registry_key("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "Hostname")
        check_registry_key("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters", "NV Hostname")
        check_registry_key("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces", "Hostname")
        check_registry_key("SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces", "NV Hostname")
        check_registry_key("HARDWARE\\DEVICEMAP\\Scsi", "")  # ScsiPorts
        check_registry_key("HARDWARE\\DEVICEMAP\\Scsi\\{port}", "")  # ScsiBuses
        check_registry_key("HARDWARE\\DEVICEMAP\\Scsi\\{port}\\{bus}\\Target Id 0\\Logical Unit Id 0", "DeviceIdentifierPage")
        check_registry_key("HARDWARE\\DEVICEMAP\\Scsi\\{port}\\{bus}\\Target Id 0\\Logical Unit Id 0", "Identifier")
        check_registry_key("HARDWARE\\DEVICEMAP\\Scsi\\{port}\\{bus}\\Target Id 0\\Logical Unit Id 0", "InquiryData")
        check_registry_key("HARDWARE\\DEVICEMAP\\Scsi\\{port}\\{bus}\\Target Id 0\\Logical Unit Id 0", "SerialNumber")
        check_registry_key("HARDWARE\\DESCRIPTION\\System\\MultifunctionAdapter\\0\\DiskController\\0\\DiskPeripheral", "")  # DiskPeripherals
        check_registry_key("HARDWARE\\DESCRIPTION\\System\\MultifunctionAdapter\\0\\DiskController\\0\\DiskPeripheral\\{disk}", "Identifier")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001", "HwProfileGuid")
        check_registry_key("SOFTWARE\\Microsoft\\Cryptography", "MachineGuid")
        check_registry_key("SOFTWARE\\Microsoft\\SQMClient", "MachineId")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "BIOSReleaseDate")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "BIOSVersion")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "ComputerHardwareId")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "ComputerHardwareIds")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "ComputerManufacturer")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "ComputerModel")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "InstallDate")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemBiosMajorVersion")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemBiosMinorVersion")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemBiosVersion")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemManufacturer")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemProductName")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemSku")
        check_registry_key("SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemVersion")
    except Exception as ex:
        print("Error checking the Registry-Keys:", ex)

def check_registry_key(key_path, value_name):
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