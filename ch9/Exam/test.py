# _*_ coding:utf-8 _*_ 
import time
import string
import sys
import os
import Tkinter
import tkMessageBox
import hashlib
import shelve

from PIL import Image, ImageTk

userlist_filename = "user_datebase"

def newuser():
    userlist = shelve.open(userlist_filename)
    namelist = string.lowercase + string.digits
    name = Tkinter.Entry.get(name_entry)

    name_pass = True
    for i in name:
        if i not in namelist:
            label = tkMessageBox.showinfo("Error", "用户名仅可由小写字母和数字组成。")
            name_pass = False

    if name in userlist:
        label = tkMessageBox.showinfo("Error", "换一个吧，这个已经被使用了。")
        name_pass = False
    if name_pass:
        pwd = Tkinter.Entry.get(pwd_entry)
        if len(pwd) < 6:
            label = tkMessageBox.showinfo("Error", "密码太短了……")
        else:
            pwd = hashlib.sha224(pwd).hexdigest() # encrypt
            label = tkMessageBox.showinfo("Success", "注册成功，请登录。")
            userlist[name] = [pwd, None, None]
            userlist.close()

def olduser():
    userlist = shelve.open(userlist_filename)
    name = Tkinter.Entry.get(name_entry)
    pwd = Tkinter.Entry.get(pwd_entry)

    if len(name) == 0:
        label = tkMessageBox.showinfo("Error", "用户名无效！")
    elif len(pwd)== 0:
        label = tkMessageBox.showinfo("Error", "密码无效！")
    else:
        try:
            passwd = userlist[name][0]
        except:
            passwd = None

        pwd = hashlib.sha224(pwd).hexdigest() # decrypt

        if passwd == pwd:
            label = tkMessageBox.showinfo("Info", "欢迎回来，%s" % name)

            try:
                last = userlist[name][1]
                now = time.time()
                passtime = int(now - last)

                if passtime > 1:
                    label = tkMessageBox.showinfo("Info", "上次登录时间为: %s" % userlist[name][2])
            except:
                pass

            temp = userlist[name]
            temp[1] = time.time()
            temp[2] = time.asctime()
            userlist[name] = temp
            userlist.close()

        else:
            if tkMessageBox.askokcancel("Error", "登录失败，是否还未注册，请点击确定注册新用户。"):
                newuser()


def del_user():
    top = Tkinter.Toplevel()
    top.geometry("400x100+400+500")

    global del_entry

    del_label = Tkinter.Label(top, text="输入要删除的用户名")
    del_entry = Tkinter.Entry(top)
    del_bt = Tkinter.Button(top, text="Delete", command=del_this_user)
    del_label.pack()
    del_entry.pack()
    del_bt.pack()

def del_this_user():
    userlist = shelve.open(userlist_filename)
    name = Tkinter.Entry.get(del_entry)
    try:
        del userlist[name]
        label = tkMessageBox.showinfo("Info", "删除成功")
    except:
        label = tkMessageBox.showinfo("Error", "Something Wrong!")

    userlist.close()


def show_user():
    userlist = shelve.open(userlist_filename)

    top = Tkinter.Toplevel()
    top.geometry("800x300+400+500")

    show_list = []
    for name in userlist.keys():
        show_list.append((name, userlist[name][0], userlist[name][1]))
    userlist.close()

    show_userlist = Tkinter.Label(top, text=show_list)
    show_userlist.pack()

def resource_path(relative_path):
    """
    定义一个读取相对路径的函数
    引用文件用如下格式：resource_path('resources/complete.wav')
    然后在生成的.spec文件exe = EXE()中加入下面这行：
    [('resources/complete.wav',r'C:\Users\Administrator\resources\complete.wav','music'),],
    列表中的三项分别为代码中的引用，文件实际的地址，类别
    这样打包后文件会被正确引用
    """
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


root = Tkinter.Tk()
root.geometry('500x250+300+100')
root.title('PP')

root.columnconfigure(0, pad=5)
root.columnconfigure(1, pad=5)
root.columnconfigure(2, pad=5)
root.columnconfigure(3, pad=5)
root.columnconfigure(4, pad=5)
root.columnconfigure(5, pad=5)
root.columnconfigure(6, pad=5)
root.columnconfigure(7, pad=5)
root.rowconfigure(0, pad=5)
root.rowconfigure(1, pad=5)
root.rowconfigure(2, pad=5)
root.rowconfigure(3, pad=5)
root.rowconfigure(4, pad=5)
root.rowconfigure(5, pad=5)
root.rowconfigure(6, pad=5)
root.rowconfigure(7, pad=5)

# I put a pic here (head.jpg)
img = Image.open(resource_path('head.jpg'))
icon = ImageTk.PhotoImage(img)
head = Tkinter.Label(root, image=icon)
head.image = icon
head.grid(rowspan=3, columnspan=5)

name_entry = Tkinter.Entry(root)
name_entry.grid(row=4, column=0, columnspan=5, ipadx=15, ipady=3)
name_entry.focus_get()

lb1 = Tkinter.Label(root, text="帐号", fg="#33a0ff", width=6)
lb1.grid(row=4, column=1)

pwd_entry = Tkinter.Entry(root,show="•")
pwd_entry.grid(row=5, columnspan=5,  ipadx=15, ipady=3)

lb2 = Tkinter.Label(root, text="密码", fg="#33a0ff", width=6)
lb2.grid(row=5, column=1)

bt1 = Tkinter.Button(root, text="登 录", command=olduser, bg="#33a0ff", fg="white")
bt1.grid(row=7, column=2, columnspan=1, ipadx=30, ipady=2, pady=5)

menubar = Tkinter.Menu(root)
root.config(menu=menubar)
managemenu = Tkinter.Menu(menubar)
menubar.add_cascade(label="管理", menu=managemenu)

managemenu.add_command(label="删除用户", command=del_user)
managemenu.add_command(label="用户列表", command=show_user)
root.mainloop()