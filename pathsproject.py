from tkinter import *
from tkinter import scrolledtext, messagebox
import os


def get_files():
    """Возвращает файлы, хранящиеся по пути path"""
    txt2.delete(1.0, END)
    if txt.get() == '':
        messagebox.showwarning('Ошибка', 'Путь не введен!')
    else:
        try:
            paths = os.listdir(txt.get())
        except FileNotFoundError:
            messagebox.showerror('Ошибка', 'Путь не найден! Попробуйте еще раз')
        except OSError:
            messagebox.showerror('Ошибка', 'Путь не найден! Попробуйте еще раз')
        else:
            files = '\n'.join(paths)
            txt2.insert(INSERT, files)


def get_clear():
    """Сброс входных и выходных данных"""
    txt.delete(0, END)
    txt2.delete(1.0, END)


window = Tk()
window.title('Файлы')
window.geometry('400x300')
lbl = Label(window, text='Введите путь:', font=('Arial Black', 12))
lbl.grid(column=1, row=0)
txt = Entry(window, width=50)
txt.focus()
txt.grid(column=1, row=1)
btn = Button(window, text='Готово', bg='white', fg='black', command=get_files)
btn.grid(column=3, row=1)
lbl2 = Label(window, text='Список файлов:', font=('Arial Black', 12))
lbl2.grid(column=1, row=2)
txt2 = scrolledtext.ScrolledText(window, width=40, height=13)
txt2.grid(column=1, row=3)
btn2 = Button(window, text='Сброс ', bg='white', fg='black', command=get_clear)
btn2.grid(column=3, row=2)
window.mainloop()