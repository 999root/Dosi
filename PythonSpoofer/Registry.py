
import winreg

class Regedit:
    def __init__(self, regedit_path):
        self.regedit_path = regedit_path

    def read(self, key_name):
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.regedit_path) as key:
                value, _ = winreg.QueryValueEx(key, key_name)
                return value
        except FileNotFoundError:
            return "ERR"
        except Exception as ex:
            print("Error accessing the Registry:", ex)
            return "ERR"

    def write(self, key_name, value):
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.regedit_path, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, key_name, 0, winreg.REG_SZ, str(value))
                return True
        except FileNotFoundError:
            return False
        except Exception as ex:
            print("Error accessing the Registry:", ex)
            return False