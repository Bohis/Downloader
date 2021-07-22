from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from VideoDownload import Loader
from Convector import Convector
import os

directory = ""
loader = Loader()
convector = Convector()

window = Tk()
window.title("Загрузчик видео")
#window.geometry("500x350")
window.resizable(False,False)
#window.iconbitmap("AppLoader.ico")
window.configure(background = "#60D4AE")

tabControl = ttk.Notebook(window)

tabLoad = ttk.Frame(tabControl)
tabConvert = ttk.Frame(tabControl)

tabControl.add(tabLoad,text = "Загрузка")
tabControl.add(tabConvert,text = "Конвектор")
tabControl.pack(expand=1,fill="both")

# ========= Загрузка видео ===============

# listBox ==============
listQualityAliases = ["Лучшее","Худшее","Лучшие видео","Худшие видео","Лучшие аудио","Худшие аудио"]

lbQuality = Listbox(tabLoad,selectmode=SINGLE)
lbQuality.grid(column=0,row=1,rowspan=5,sticky="we",padx=2,pady=2)

for quality in listQualityAliases:
    lbQuality.insert(END,quality)
# ======================

# URL and Folder =======

Label(tabLoad,text = "Ссылка").grid(column=1,row=0,sticky="we",padx=2,pady=2)
Label(tabLoad,text = "Папка").grid(column=1,row=2,sticky="we",padx=2,pady=2)
Label(tabLoad,text = "Имя файла").grid(column=1,row=4,sticky="we",padx=2,pady=2)

urlEntry = Entry(tabLoad,width=50,font = "serif 10")
urlEntry.grid(column=1,row=1,sticky="we",padx=2,pady=2)

folderEntry = Entry(tabLoad,width=50,font = "serif 10")
folderEntry.grid(column=1,row=3,sticky="we",padx=2,pady=2)

nameEntry = Entry(tabLoad,width=50,font = "serif 10")
nameEntry.grid(column=1,row=5,sticky="we",padx=2,pady=2)

# ======================


# FolderDialog ========

def OpenDirectory():
    global directory
    directory = filedialog.askdirectory()
    folderEntry.delete(0)
    folderEntry.insert(END,directory)
    
def Download():
    global directory
    quality = Loader.listQual[lbQuality.curselection()[0]]
    url = urlEntry.get()
    name = nameEntry.get()
    directory = folderEntry.get()
    messagebox.showinfo("Результат загрузки", loader.Load(url,directory,name,quality))

# =====================


# Buttons ==============

BtLoad = Button(tabLoad,text="Загрузить",font="serif 10",command=Download)
BtLoad.grid(column=0,row=6, sticky="we",padx=2,pady=2)

BtFolderDialog = Button(tabLoad,text="Выбрать папку для загрузки",font="serif 10", command=OpenDirectory)
BtFolderDialog.grid(column=1,row=6,sticky="we",padx=2,pady=2)

# ======================

# ========= Конвектор видео ===============

# Label ================
Label(tabConvert,text = "Файл для конвертации").grid(column=0,row=0,sticky="we",padx=2,pady=2)
Label(tabConvert,text = "Результат").grid(column=1,row=0,sticky="we",padx=2,pady=2)
# ======================

# Entry ================
fileSourceEntry = Entry(tabConvert,width=50,font = "serif 10")
fileSourceEntry.grid(column=0,row=2,sticky="we",padx=2,pady=2)
fileConvertEntry = Entry(tabConvert,width=50,font = "serif 10")
fileConvertEntry.grid(column=1,row=2,sticky="we",padx=2,pady=2)
# ======================

fileFullName = ""

# Convernt =============
def SelectFolder():
    global fileFullName
    fileFullName = filedialog.askopenfilename()
    fileSourceEntry.delete(0)
    fileSourceEntry.insert(END,fileFullName)
    
    temp = fileFullName[:-4]
    fileConvertEntry.delete(0)
    fileConvertEntry.insert(END,temp)
    
    
def Convert():
    global fileFullName,convector
    newFileName = fileConvertEntry.get()
    messagebox.showinfo("Результат конвертации", convector.Convert(fileFullName,newFileName))
# ======================

# Button ===============
btSelectFile = Button(tabConvert,text="Выбрать файл",font="serif 10", command=SelectFolder)
btSelectFile.grid(column=0,row=3,sticky="we",padx=2,pady=2)
btConvertFile = Button(tabConvert,text="Конвертировать",font="serif 10", command=Convert)
btConvertFile.grid(column=1,row=3,sticky="we",padx=2,pady=2)
# ======================


window.mainloop()