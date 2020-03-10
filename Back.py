import win32process, win32api, ctypes, win32gui
class Back():
    # init ########################################################################################################
    def __init__(self):
        PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
        Process = win32gui.FindWindow('MainWindow', 'Plants vs. Zombies')
        # 寻找进程
        hid, pid = win32process.GetWindowThreadProcessId(Process)
        # 进程号
        self.phandle = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        self.dll = ctypes.windll.LoadLibrary('C:\\Windows\\System32\\kernel32.dll')

        self.SunLight_index=int()
        self.GetSunLight_index()

    def GetSunLight_index(self):
        Value1 = ctypes.c_long()
        Value2 = ctypes.c_long()
        ValueOfSun = ctypes.c_long()
        # 取得一级地址0x00755E0C中的值
        self.dll.ReadProcessMemory(int(self.phandle), 0x00755E0C, ctypes.byref(Value1), 4, None)
        # 偏移量868[十六进制] （十进制下是2152） 一级地址中的值+偏移量=二级地址
        self.dll.ReadProcessMemory(int(self.phandle), Value1.value + 2152, ctypes.byref(Value2), 4, None)
        # 偏移量5578[十六进制] （十进制下是21880） 二级地址中的值+偏移量=三级地址
        # 三级地址即为阳光存储的指针 Value2.value + 21880
        # self.dll.ReadProcessMemory(int(self.phandle), Value2.value + 21880, ctypes.byref(ValueOfSun), 4, None)
        self.SunLight_index=Value2.value + 21880
    # Active ########################################################################################################
    def ValueOfSunLight(self, Values):
        Value = ctypes.c_long(Values)
        self.dll.WriteProcessMemory(int(self.phandle), self.SunLight_index, ctypes.byref(Value), 4, None)
