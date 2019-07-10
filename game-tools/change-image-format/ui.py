import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import StringVar
class MainUI:
    def __init__(self):
        self._path = tk.StringVar()
        self._win = tk.Tk()
        self._win.title('图片格式转换')
        self._win.geometry('720x460')
        tk.Label(self._win, text="目标路径").gird(row=0,column=0)
        tk.Entry(self._win, textvariable=path).girdd(row = 0, column = 1)
        tk.Button(self._win, text='路径选择',command=self._selectPath).gird(row=0,column=2)

    def run(self):
        self._win.mainloop()
    def _selectPath(self):
        pass


