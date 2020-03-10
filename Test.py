import win32process,win32gui,win32api,ctypes
Process_All_Access = (0x000F0000 | 0x00100000 | 0xFFF)
Process = win32gui.FindWindow('MainWindow','Plants vs. Zombies')
hid,pid = win32process.GetWindowThreadProcessId(Process)
phandle = win32api.OpenProcess(Process_All_Access,False,pid)
dll = ctypes.windll.LoadLibrary("C:\\Windows\\System32\\kernel32.dll")

value1 = ctypes.c_long()
dll.ReadProcessMemory(int(phandle),0x00755E0C,ctypes.byref(value1),4,None)
print(value1.value)

value2 = ctypes.c_long()
dll.ReadProcessMemory(int(phandle),value1.value+2152,ctypes.byref(value2),4,None)
print(value2.value)

value3 = ctypes.c_long(99999)
dll.WriteProcessMemory(int(phandle),value2.value+21880,ctypes.byref(value3),4,None)

