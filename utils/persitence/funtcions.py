from win32api import GetModuleFileName, RegCloseKey, RegDeleteValue, RegOpenKeyEx, RegSetValueEx

from win32con import HKEY_LOCAL_MACHINE, KEY_WRITE, REG_SZ

SUBKEY = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"

def run_at_startup_set(app_name, path):
    """
    Sets the key to run at startup
    """
    key = RegOpenKeyEx(HKEY_LOCAL_MACHINE, SUBKEY, 0, KEY_WRITE)
    RegSetValueEx(key, app_name, 0, REG_SZ, path)
    RegCloseKey(key)
    print("Key set")

def run_script_at_startup_set(app_name, script):
    path = "%s %s" % (GetModuleFileName(0), script)
    run_at_startup_set(app_name, path)

def run_at_startup_remove(app_name):
    key = RegOpenKeyEx(HKEY_LOCAL_MACHINE, SUBKEY, 0, KEY_WRITE)
    RegDeleteValue(key, app_name)
    RegCloseKey(key)