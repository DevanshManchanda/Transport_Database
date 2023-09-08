from tkinter import *
import mysql.connector as ms


from Options import *


mydb = ms.connect(host="localhost",user="root",passwd="Devansh#03",database="world")
cursor = mydb.cursor()


def DMIG():

    def Teacher_login():

        def Teacher_check():
            
            user=username_entry.get()
            pas=password_entry.get()

            #str = "select * from teacher_login where username = '" + user + "'" + " and passwrd = '" + pas + "';" 
            str = "select * from teacher_login where username = 'Teacher 1'  and passwrd = '4424';"
            cursor.execute(str)
            row = cursor.fetchone()
            
            if row == None:
                print("Username/ Password doesn't match")
            else:
                window.destroy()
                Teacher_options()
        
        window=Tk()
        window.title("Teacher's Login")
        window.geometry("500x500")
        window.configure(bg='#262c38')
        
        Label(window,text="Welcome",bg="#262c38",fg="#7369e3",width="100",height="1",font=("Cascadia Code",25)).pack()
        Label(text=" ",bg="#262c38").pack() 
        Label(window,text="Enter your login details",bg="#262c38",fg="#98dea2",width="100",height="1",font=("Cascadia Code",25)).pack()
        Label(text=" ",bg="#262c38").pack()

        username=StringVar()    
        username_label=Label(window,text="Username",bg='#262c38',fg="pink",font=("Cascadia Code",20))
        username_label.pack()
        username_entry=Entry(window,textvariable=username,font=("Cascadia Code",15))
        username_entry.pack()

        Label(text=" ",bg="#262c38").pack()

        password=StringVar()
        password_label=Label(window,text="Password",bg='#262c38',fg="pink",font=("Cascadia Code",20))
        password_label.pack()
        password_entry=Entry(window,textvariable=password,font=("Cascadia Code",15))
        password_entry.pack()

        
        Label(text=" ",bg="#262c38").pack()  
        Label(text=" ",bg="#262c38").pack()
        Button(window,text="Login",height="1",width="5",bg ='red',font=("Cascadia Code",30),command =lambda: Teacher_check()).pack()

        window.mainloop()

    def Student_login():

        def Student_check():
            user=username_entry.get()
            pas=password_entry.get()

            str = "select * from student_login where username = '" + user + "'" + " and passwrd = '" + pas + "';" 
            #str = "select * from student_login where username = 'devansh'  and  passwrd = '1869';"
            
            cursor.execute(str)
            row = cursor.fetchone()
            
            if row == None:
                print("Username/ Password doesn't match")
            else:
                window.destroy()
                Student_options()

        window=Tk()
        window.title("Student's Login")
        window.geometry("500x500")
        window.configure(bg='#262c38')
        
        Label(window,text="Welcome",bg="#262c38",fg="#7369e3",width="100",height="1",font=("Cascadia Code",20)).pack()
        Label(text=" ",bg="#262c38").pack() 
        Label(window,text="Enter your login details",bg="#262c38",fg="#98dea2",width="100",height="1",font=("Cascadia Code",20)).pack()
        Label(text=" ",bg="#262c38").pack()

        username=StringVar()    
        username_label=Label(window,text="Username",bg='#262c38',fg="pink",font=("Cascadia Code",20))
        username_label.pack()
        username_entry=Entry(window,textvariable=username,font=("Cascadia Code",15))
        username_entry.pack()

        Label(text=" ",bg="#262c38").pack()

        password=StringVar()
        password_label=Label(window,text="Password",bg='#262c38',fg="pink",font=("Cascadia Code",20))
        password_label.pack()
        password_entry=Entry(window,textvariable=password,font=("Cascadia Code",15))
        password_entry.pack()

        
        Label(text=" ",bg="#262c38").pack()  
        Label(text=" ",bg="#262c38").pack()
        Button(window,text="Login",height="2",width="30",bg ='red',font=("Cascadia Code",15),command =lambda: Student_check()).pack()
        

        window.mainloop()
    
    
    window1=Tk()
    window1.title("Login Options")
    window1.geometry("400x300")
    window1.configure(bg="#231A61")


    Label(window1,text="Login",fg='#37FF8B',bg="#231A61",font=("Cascadia Code",30)).pack()

    radio_v=StringVar()
    radio_v.set('x')
    b1=Radiobutton(window1,text='Teachers', variable=radio_v, width=10,value='0',fg="#E0777D",bg = "#231A61",activebackground="orange",activeforeground="blue",font=("Cascadia Code",20),command=window1.destroy)
    b1.place(x=10,y=60)

    b2=Radiobutton(window1,text='Students', variable=radio_v, width=10,value='1',fg="#E0777D",bg="#231A61",activebackground="orange",activeforeground="blue",font=("Cascadia Code",20),command=window1.destroy)
    b2.place(x=10,y=160)

    window1.mainloop()

    my_ch=radio_v.get()
    if my_ch=='0':
        Teacher_login()
    elif my_ch=='1':
        Student_login()
