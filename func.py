def save():
    if first_name.get() == '' or last_name.get() == '' or home.get() == '' or phone_number.get() == '' or sex.get() == '' or hobby.get() == '' :
        msgbox.showwarning('Анхаар! Мэдээллийг бүрэн оруулна уу')

    else: 
        msgbox.askyesno('Мэдээллийг хадгалах уу?')
        msgbox.YES == list_data.insert(END, first_name.get()+ ', ' + last_name.get()+ ', ' + home.get()+ ', ' + phone_number.get()+ ', ' + sex.get()+ ', ' + hobby.get())
        msgbox.NO == clear()
        
            
    
   
def update():
    pass
    if first_name.get() == '' or last_name.get() == '' or home.get() == '' or phone_number.get() == '' or sex.get() == '' or hobby.get() == '' :
        msgbox.askyesno('Та мэдээллийг засахдаа итгэлтэй байна уу?')
               
    else :
    
        list_data.delete(selected_index)
        list_data.insert(selected_index, first_name.get()+ ',' + last_name.get()+ ',' + home.get()+ ',' + phone_number.get()+ ',' + sex.get()+ ',' + hobby.get())
        clear()


def delete():
    list_data.delete(list_data.curselection()[0])
    clear()
    
def clear():
    first_name.set('')
    last_name.set('')
    home.set('')
    phone_number.set('')
    sex.set('')
    hobby.set('')

def search():
    if last_name.get() != list_data or home.get() != list_data or phone_number.get() != list_data or sex.get() !=  list_data or hobby.get() :
        msgbox.showwarning("Хайсан мэдээлэл байхгүй байна!")
    else:
        list_data.curselection()

def user_select(event):
    select = list_data.get(list_data.curselection()[0])
    
    index = list_data.curselection()[0]
    selected_user = list_data.get(index)
    selected_index = index

    data=select.split(',')
    first_name.set(data[0])
    last_name.set(data[1])
    home.set(data[2])
    phone_number.set(data[3])
    sex.set(data[4])
    hobby.set(data[5])