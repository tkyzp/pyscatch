#全屏截图
#   全屏窗口显示截图
#选择区域
#   小窗口显示选取截图
#扫码
#弹出扫码结果


import tkinter, tkinter.messagebox
import pyperclip
from PIL import ImageGrab, ImageTk

import QRcode

def getScreenShoot():
    return ImageGrab.grab()

def exit(key):
    global mainWindow
    mainWindow.destroy()

#绘图事件
startx = 0
starty = 0
endx = 0
endy = 0
flag = 0
last = None
def onButtonDown(key):
    global flag, startx, starty, endx, endy, last
    if flag == 0:
        flag = 1
        startx = key.x_root
        starty = key.y_root
    endx = key.x_root
    endy = key.y_root
    if last is not None:
        bg.delete(last)
    last = bg.create_rectangle(startx, starty, endx, endy, outline = "red", width = 2)
    
    

def onButtonUp(key):
    global flag, startx, starty, endx, endy
    qr = sh.crop((startx, starty, endx, endy))
    result = QRcode.Decode(qr)
    if len(result) > 0:
        pyperclip.copy(result[0].data.decode())
        tkinter.messagebox.showinfo("结果", result[0].data.decode() +"\n内容已复制到剪贴板")
    else:
        tkinter.messagebox.showerror("结果", "没有发现二维码")
    startx = 0
    starty = 0
    endx = 0
    endy = 0
    flag = 0
    mainWindow.destroy()


#设置主窗口
mainWindow = tkinter.Tk()
w = mainWindow.winfo_screenwidth()
h = mainWindow.winfo_screenheight()
mainWindow.geometry("%dx%d"%(w,h))
mainWindow.attributes("-topmost", True)
mainWindow.overrideredirect(True)

#截图并显示
bg = tkinter.Canvas(mainWindow, width = w, height = h)
sh = getScreenShoot()
bgim = ImageTk.PhotoImage(sh)
bg.create_image(0, 0, anchor=tkinter.NW ,image = bgim)
bg.pack()

#绑定按键
mainWindow.bind(sequence="<Escape>",func=exit)
bg.bind(sequence="<B1-Motion>", func=onButtonDown)
bg.bind(sequence="<ButtonRelease-1>", func=onButtonUp)


mainWindow.mainloop()