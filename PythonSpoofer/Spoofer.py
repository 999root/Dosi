
import Registry
import uuid
        

        
class HWID:
    regeditOBJ = Registry.Regedit(r"SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001")
    Key = "HwProfileGuid"

    @staticmethod
    def GetValue():
        return HWID.regeditOBJ.read(HWID.Key)

    @staticmethod
    def SetValue(value):
        return HWID.regeditOBJ.write(HWID.Key, value)

    @staticmethod
    def Spoof():
        Log = []
        old_value = HWID.GetValue()
        new_value = "{" + str(uuid.uuid4()) + "}"
        result = HWID.SetValue(new_value)
        if result:
            Log.append(f"[SPOOFER] HWID Changed from {old_value} to {new_value}")
        else:
            Log.append("[SPOOFER] Error accessing the Registry... Maybe run as admin")
        return result, Log
    


class GUID:
    regeditOBJ = Registry.Regedit(r"SOFTWARE\\Microsoft\\Cryptography")
    Key = "MachineGuid"

    @staticmethod
    def GetValue():
        return HWID.regeditOBJ.read(HWID.Key)

    @staticmethod
    def SetValue(value):
        return HWID.regeditOBJ.write(HWID.Key, value)

    @staticmethod
    def Spoof():
        Log = []
        old_value = HWID.GetValue()
        new_value = "{" + str(uuid.uuid4()) + "}"
        result = HWID.SetValue(new_value)
        if result:
            Log.append(f"[SPOOFER] GUID Changed from {old_value} to {new_value}")
        else:
            Log.append("[SPOOFER] Error accessing the Registry... Maybe run as admin")
        return result, Log
    


class PCNAME:
    regeditOBJ = Registry.Regedit(r"SYSTEM\\CurrentControlSet\\Control\\ComputerName\\ActiveComputerName")
    Key = "ComputerName"

    @staticmethod
    def GetValue():
        return HWID.regeditOBJ.read(HWID.Key)

    @staticmethod
    def SetValue(value):
        return HWID.regeditOBJ.write(HWID.Key, value)

    @staticmethod
    def Spoof():
        Log = []
        old_value = HWID.GetValue()
        new_value = "{" + str(uuid.uuid4()) + "}"
        result = HWID.SetValue(new_value)
        if result:
            Log.append(f"[SPOOFER] Computer Name Changed from {old_value} to {new_value}")
        else:
            Log.append("[SPOOFER] Error accessing the Registry... Maybe run as admin")
        return result, Log
    


class PRODUCTID:
    regeditOBJ = Registry.Regedit(r"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion")
    Key = "ProductId"

    @staticmethod
    def GetValue():
        return HWID.regeditOBJ.read(HWID.Key)

    @staticmethod
    def SetValue(value):
        return HWID.regeditOBJ.write(HWID.Key, value)

    @staticmethod
    def Spoof():
        Log = []
        old_value = HWID.GetValue()
        new_value = "{" + str(uuid.uuid4()) + "}"
        result = HWID.SetValue(new_value)
        if result:
            Log.append(f"[SPOOFER] Product Id Changed from {old_value} to {new_value}")
        else:
            Log.append("[SPOOFER] Error accessing the Registry... Maybe run as admin")
        return result, Log