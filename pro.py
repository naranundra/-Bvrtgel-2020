from tkinter import *
import tkinter.messagebox as msgbox
import tkinter
from func import save, update, delete, clear, search, user_select

window  = Tk()
window.title('Бүртгэл 2020')
window.geometry('650x450')
window.resizable(0,0)

selected_index = -1

# first_name, last_name, home, phone_number, sex, hobby
first_name = StringVar()
last_name = StringVar()
home = StringVar()
phone_number = StringVar()
sex = StringVar()
hobby = StringVar()

Label(window, text='Овог').grid(row=0, column=1)
Entry(window, textvariable=first_name).grid(row=0, column=2)

Label(window, text='Нэр').grid(row=1, column=1)
Entry(window, textvariable=last_name).grid(row=1, column=2)

Label(window, text='Гэрийн хаяг').grid(row=2, column=1)
Entry(window, textvariable=home).grid(row=2, column=2)

Label(window, text='Утасны дугаар').grid(row=3, column=1)
Entry(window, textvariable=phone_number).grid(row=3, column=2)

Label(window, text='Хүйс').grid(row=4, column=1)
Entry(window, textvariable=sex).grid(row=4, column=2)

Label(window, text='Спортын төрөл').grid(row=5, column=1)
Entry(window, textvariable=hobby).grid(row=5, column=2)




Button(window, text='Хадгалах', command=save).grid(row=0, column=3)
Button(window, text='Засварлах', command=update).grid(row=1, column=3)
Button(window, text='Хайх', command=search).grid(row=2, column=3)
Button(window, text='Арилгах', command=clear).grid(row=3, column=3)
Button(window, text='Устгах', command=delete).grid(row=4, column=3) 


list_data= Listbox(window, width=60, height=10)
list_data.grid(row=6, rowspan=1, column=0, columnspan=6)
list_data.bind('<<ListboxSelect>>', user_select)

scroll = Scrollbar(window)
scroll.grid(row=6, column=7)
list_data.configure(yscrollcommand=scroll.set)
scroll.configure(command=list_data.yview)

window.mainloop()




