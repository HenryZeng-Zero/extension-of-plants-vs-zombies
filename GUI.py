from tkinter import *
from Back import Back

class Application():
    def __init__(self):
        self.Controling = None
        self.root = Tk()
        self.root.title("植物大战僵尸扩展")
        self.root.maxsize(500, 300)
        self.root.minsize(500, 300)

        self.success = Frame(self.root)
        self.errors = Frame(self.root)

        self.create_widgets()
        self.error()

        self.appear()

    def appear(self):
        if self.CheckRunning() == False:
            print(1)
            self.success.place_forget()
            self.errors.place(anchor='center', x=250, y=150, width=500, height=300)
        else:
            print(2)
            self.errors.place_forget()
            self.success.place(anchor='center', x=250, y=150, width=500, height=300)

    def create_widgets(self):
        self.Button_SunLight = Button(self.success)
        self.Button_SunLight['text'] = "设置阳光数为99999"
        self.Button_SunLight['command'] = self.ChangeSunLight
        self.Button_SunLight.place(anchor='center', x=250, y=150, width=130, height=30)

    def error(self):
        self.Retry = Button(self.errors)
        self.Retry['text'] = "重试一下"
        self.Retry['command'] = self.appear
        self.Retry.place(anchor='center', x=250, y=150, width=60, height=30)

        self.label1 = Label(self.errors)
        self.label1['text'] = '出现异常，您可能没有启动植物大战僵尸。'
        self.label1.place(anchor='center', x=250, y=120, width=500, height=30)
    # Control ###################################################################
    def CheckRunning(self):
        try:
            self.Controling = Back()
            return True
        except:
            return False

    def ChangeSunLight(self):
        if self.CheckRunning() == False:
            self.appear()
        print("ChangeSunLight")
        self.Controling.ValueOfSunLight(99999)
