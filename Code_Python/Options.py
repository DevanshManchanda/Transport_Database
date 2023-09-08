from Functions import *


def Teacher_options():
    window7=Tk()
    window7.title("Teacher Options")
    window7.geometry("500x500")
    window7.configure(bg='#203d57')

    radio_v=StringVar()
    radio_v.set(' ')

    b1=Radiobutton(window7,text='Add New Record', variable=radio_v, width=50,value='0',fg="#EE6123",bg="#203d57",font=("Cascadia Code",30),command=window7.destroy)
    b1.pack()

    b2=Radiobutton(window7,text='Delete Record', variable=radio_v, width=50,value='1',fg="#EE6123",bg="#203d57",font=("Cascadia Code",30),command=window7.destroy)
    b2.pack()

    b3=Radiobutton(window7,text='Modify Record', variable=radio_v, width=50,value='2',fg="#EE6123",bg="#203d57",font=("Cascadia Code",30),command=window7.destroy)
    b3.pack()

    b4=Radiobutton(window7,text='Search Record', variable=radio_v, width=50,value='3',fg="#EE6123",bg="#203d57",font=("Cascadia Code",30),command=window7.destroy)
    b4.pack()

    b5=Radiobutton(window7,text='View Report', variable=radio_v, width=50,value='4',fg="#EE6123",bg="#203d57",font=("Cascadia Code",30),command=window7.destroy)
    b5.pack()

    b6=Radiobutton(window7,text='Sign Out', variable=radio_v, width=50,value='5',fg="#EE6123",bg="#203d57",font=("Cascadia Code",30),command=window7.destroy)
    b6.pack()

    window7.mainloop()

    my_ch=radio_v.get()
    if my_ch=='0':
        add_data()
        Teacher_options()
    elif my_ch=='1':
        del_data()
        Teacher_options()
    elif my_ch=='2':
        modify_data()
        Teacher_options()
    elif my_ch=='3':
        search_data()
        Teacher_options()
    elif my_ch=='4':
        report_data()
        Teacher_options()
    elif my_ch=='5':
        exit()


def Student_options():
    window8=Tk()
    window8.title("Student Options")
    window8.geometry("500x500")
    window8.configure(bg='#203d57')

    radio_v=StringVar()
    radio_v.set(' ')

    a1=Radiobutton(window8,text='Add New Record', variable=radio_v, width=50,value='0',fg="#EE6123",bg="#203d57",font=("Cascadia Code",30),command=window8.destroy)
    a1.pack()

    a2=Radiobutton(window8,text='Search Record', variable=radio_v, width=50,value='3',fg="#EE6123",bg="#203d57",font=("Cascadia Code",30),command=window8.destroy)
    a2.pack()

    a3=Radiobutton(window8,text='Modify Record', variable=radio_v, width=50,value='2',fg="#EE6123",bg="#203d57",font=("Cascadia Code",30),command=window8.destroy)
    a3.pack()

    a4=Radiobutton(window8,text='Sign Out', variable=radio_v, width=50,value='5',fg="#EE6123",bg="#203d57",font=("Cascadia Code",30),command=window8.destroy)
    a4.pack()

    window8.mainloop()

    my_ch=radio_v.get()
    if my_ch=='0':
        add_data()
        Student_options()
    elif my_ch=='2':
        modify_data()
        Student_options()
    elif my_ch=='3':
        search_data()
        Student_options()
    elif my_ch=='5':
        exit()
