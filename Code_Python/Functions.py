from tkinter import *
from tkinter import ttk
import mysql.connector as ms


from Table import *


mydb = ms.connect(host="localhost",user="root",passwd="Devansh#03",database="world")


def add_data():
    def add_record():
        admno=Admno.get()
        name=Name.get()
        clas=options.get()
        pname=P_Name.get()
        pno=P_num.get()
        trans=radio_tr.get()
    
        van_det=0
        if trans=='Van':
            no=options1.get()
            s=["VAN01(DL1CT 7856)","VAN02(DL1CT 7696)","VAN03(DL1CT 8796)","VAN04(DL2CT 7796)"]
            lst=["VAN01","VAN02","VAN03","VAN04"]
            ind=s.index(no)
            van_det=lst[ind]

        elif trans=='Self':
            van_det=""
        if admno=="" or name=="" or clas=="" or pname=="" or pno=="" or trans=="":
            Label(window2,text="All fields are not filled, Can't add new record ",fg="red",bg='#06283D',font=("Cascadia Code",25)).place(x=50,y=450)

        else:
            cursor = mydb.cursor()
            st="insert into student_details (Admno, Name, Class, P_name, P_number, Transport,Van_No) values ('" + admno + "','" + name + "','" + clas + "','" + pname + "','" + pno + "','" + trans + "','" + van_det +"');"
            cursor.execute(st)
            mydb.commit()
            window2.destroy()



    window2=Tk()
    window2.title(" Adding Record ")
    window2.geometry("850x600")
    window2.configure(bg='#06283D')

    Label(window2,text="Enter Personal Details",bg="#06283D",fg="#FFA500",width="100",height="1",font=("Cascadia Code",35)).pack()

    Admno=StringVar()    
    Admno_label=Label(window2,text="Admisson Number of Student -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
    Admno_label.place(x=85,y=60,width=450)
    Admno_entry=Entry(window2,textvariable=Admno,font=("Cascadia Code",15))
    Admno_entry.place(x=550,y=60,width=250)

    Name=StringVar()
    Name_label=Label(window2,text="Name of Student -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
    Name_label.place(x=245,y=110,width=300)
    Name_entry=Entry(window2,textvariable=Name,font=("Cascadia Code",15))
    Name_entry.place(x=550,y=110,width=250)
   
    Class_label=Label(window2,text="Class -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
    Class_label.place(x=375,y=160,width=200)
    options = StringVar()
    op1=["XII-A","XII-B","XII-C"]
    Class_entry = ttk.Combobox(window2,textvariable=options,value=op1,state='readonly')
    Class_entry.bind("<<<ComboboxSelect>>>")
    Class_entry.place(x=550,y=160,width=250,height=35)

    P_Name=StringVar()
    P_Name_label=Label(window2,text="Parent Name -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
    P_Name_label.place(x=315,y=210,width=220)
    P_Name_entry=Entry(window2,textvariable=P_Name,font=("Cascadia Code",15))
    P_Name_entry.place(x=550,y=210,width=250)

    P_num=StringVar()    
    P_num_label=Label(window2,text="Parent Number -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
    P_num_label.place(x=285,y=260,width=250)
    P_num_entry=Entry(window2,textvariable=P_num,font=("Cascadia Code",15))
    P_num_entry.place(x=550,y=260,width=250)

    tr_label=Label(window2,text="Transport -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
    tr_label.place(x=345,y=310,width=200)

    radio_tr=StringVar()
    radio_tr.set('x')

    b1=Radiobutton(window2,text='Self', variable=radio_tr, width=10,value='Self',bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
    b1.place(x=550,y=310,width=125)
    b2=Radiobutton(window2,text='Van', variable=radio_tr, width=10,value='Van',bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
    b2.place(x=675,y=310,width=125)

    Van_label=Label(window2,text="Van Number -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
    Van_label.place(x=345,y=360,width=200)
    options1 = StringVar()
    op=["Selct","VAN01(DL1CT 7856)","VAN02(DL1CT 7696)","VAN03(DL1CT 8796)","VAN04(DL2CT 7796)"]
    Van_entry = ttk.Combobox(window2,textvariable=options1,value=op,state='readonly')
    Van_entry.bind("<<<ComboboxSelect>>>")
    Van_entry.place(x=550,y=360,width=250,height=35)

    Button(window2,text="Add New Record",bg ='#00916E',font=("Cascadia Code",20),command=lambda :add_record()).place(x=400,y=410,width=250)
    window2.mainloop()

def del_data():

    def del_record():
        admno=Admno.get()
        cursor = mydb.cursor()
        st="delete from student_details where Admno = '" + admno + "';"
        cursor.execute(st)
        mydb.commit()
        window.destroy()


    window=Tk()
    window.title(" Deleting Record ")
    window.geometry("850x300")
    window.configure(bg='#06283D')

    Label(window,text="Enter Admission Number",bg="#06283D",fg="#FFA500",width="100",height="1",font=("Cascadia Code",35)).pack()

    Admno=StringVar()    
    Admno_label1=Label(window,text="Admisson Number of Student -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
    Admno_label1.place(x=85,y=100,width=450)
    Admno_entry1=Entry(window,textvariable=Admno,font=("Cascadia Code",15))
    Admno_entry1.place(x=550,y=100,width=250)

    Button(window,text="Delete Record",height="2",width="1",bg ='#00916E',font=("Cascadia Code",18),command= lambda :del_record()).place(x=400,y=200,width=250)
    window.mainloop()

def modify_data():
    window=Tk()
    window.title(" Modifying Record ")
    window.geometry("1000x600")
    window.configure(bg='#06283D')

    Label(window,text="Enter Admission Number",bg="#06283D",fg="#FFA500",width="100",height="1",font=("Cascadia Code",35)).pack()

    Admno=StringVar()    
    Admno_label1=Label(window,text="Admisson Number of Student -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
    Admno_label1.place(x=85,y=100,width=450)
    Admno_entry1=Entry(window,textvariable=Admno,font=("Cascadia Code",15))
    Admno_entry1.place(x=550,y=100,width=250)
    Button(window,text="Search Record",height="2",width="1",bg ='#00916E',font=("Cascadia Code",10),command= lambda: get_record()).place(x=825,y=100,width=150)

    def get_data(lst):
        Van_entry = ttk.Combobox(window,value=["Select","VAN01","VAN02","VAN03","VAN04"],state='readonly')

        def change_Transport(current_Sel):
            if current_Sel == "Self":
                Van_entry.current(0)

        Name=StringVar()
        Name_label=Label(window,text="Name of Student -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
        Name_label.place(x=245,y=150,width=300)
        Name_entry=Label(window,text=(lst[0]),font=("Cascadia Code",15))
        Name_entry.place(x=550,y=150,width=250)

        P_Name=StringVar()
        P_Name_label=Label(window,text="Parent Name -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
        P_Name_label.place(x=315,y=200,width=220)
        P_Name_entry=Label(window,text=(lst[2]),font=("Cascadia Code",15))
        P_Name_entry.place(x=550,y=200,width=250)

        Class=StringVar()    
        Class_label=Label(window,text="Class -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
        Class_label.place(x=375,y=250,width=200)
        options = StringVar()
        op1=["XII-A","XII-B","XII-C"]
        Class_entry = ttk.Combobox(window,textvariable=options,value=op1,state='readonly')
        Class_entry.bind("<<<ComboboxSelect>>>")
        op_index = op1.index(lst[1])
        Class_entry.current(op_index)
        Class_entry.place(x=550,y=250,width=250,height=35)

        P_num=StringVar()    
        P_num_label=Label(window,text="Parent Number -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
        P_num_label.place(x=285,y=300,width=250)
        P_num_entry=Entry(window,textvariable=P_num,font=("Cascadia Code",15))
        P_num_entry.place(x=550,y=300,width=250)
        P_num_entry.insert(END,lst[3])

        Transport=StringVar()
        Transport_label=Label(window,text="Transport -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
        Transport_label.place(x=345,y=350,width=200)

        Transport_entry = ttk.Combobox(window,value=["Self","Van"],state='readonly')
        if lst[4]=="Self":
            Transport_entry.current(0)
        else:
            Transport_entry.current(1)
        Transport_entry.bind("<<ComboboxSelected>>",lambda _ : change_Transport(Transport_entry.get()))
        Transport_entry.place(x=550,y=350,width=250,height=35)

        Van_no=StringVar()
        Van_no_label=Label(window,text="Van No. -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
        Van_no_label.place(x=345,y=400,width=200)

        if lst[4]=="Van":
            op_index = int(lst[5][4])
            Van_entry.current(op_index)

        else:
            Van_entry.current(0)

        Van_entry.bind("<<<ComboboxSelected>>>")
        Van_entry.place(x=550,y=400,width=250,height=35)

        def modify():
            admno=Admno.get()
            clas=options.get()
            pno=P_num.get()
            trans=Transport_entry.get()
            van_det=Van_entry.get()
            if trans=="Self":
                van_det=""

            cursor = mydb.cursor()
            st="update student_details set Class = '" + clas + "', P_number= '"+ pno +"',Transport= '" + trans + "', Van_No= '" + van_det + "' where Admno = '" + admno + "';"
            cursor.execute(st)
            mydb.commit()


        Button(window,text="Modify Record",height="2",width="1",bg ='#00916E',font=("Cascadia Code",18),command= lambda: modify()).place(x=400,y=500,width=200)
        Button(window,text="Exit",height="2",width="1",bg ='#00916E',fg="red",font=("Cascadia Code",18),command= lambda: window.destroy()).place(x=150,y=500,width=200)
    
    def get_record():
        admno=Admno.get()
        cursor = mydb.cursor()
        st="select st.Name,st.Class, st.P_name, st.P_number, st.Transport , van.Van_No from student_details st left outer join van_details van on st.Van_No= van.Van_No where Admno = '" + admno + "';"
    

        x=cursor.execute(st)
        row = cursor.fetchone()
        if row == None:
            Label(window,text="No Record Found",bg='#06283D',fg="red",font=("Cascadia Code",35)).pack()
            
        else:
            get_data(row)
               
    window.mainloop()

def search_data():
    window=Tk()
    window.title(" Searching Record ")
    window.geometry("1000x700")
    window.configure(bg='#06283D')

    Label(window,text="Enter Admission Number",bg="#06283D",fg="#FFA500",width="100",height="1",font=("Cascadia Code",35)).pack()

    Admno=StringVar()    
    Admno_label1=Label(window,text="Admisson Number of Student -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
    Admno_label1.place(x=85,y=100,width=450)
    Admno_entry1=Entry(window,textvariable=Admno,font=("Cascadia Code",15))
    Admno_entry1.place(x=550,y=100,width=250)
    Button(window,text="Search Record",height="2",width="1",bg ='#00916E',font=("Cascadia Code",10),command= lambda: get_record()).place(x=825,y=100,width=150)

    def get_record():
        admno=Admno.get()
        cursor = mydb.cursor()
        st="select st.Name,st.Class, st.P_name, st.P_number, st.Transport , van.Van_No, van.Drv_Name, van.Drv_Contact, van.Van_Reg_No from student_details st left outer join van_details van on st.Van_No= van.Van_No where Admno = '" + admno + "';"
        x=cursor.execute(st)
        row = cursor.fetchone()
        if row == None:
            new=Label(window,text="No Record Found",bg='#06283D',fg="red",font=("Cascadia Code",20)).pack()
            
        else:

            Name=StringVar()
            Name_label=Label(window,text="Name of Student -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
            Name_label.place(x=245,y=150,width=300)
            Name_entry=Label(window,text=(row[0]),font=("Cascadia Code",15))
            Name_entry.place(x=550,y=150,width=250)

            Class=StringVar()    
            Class_label=Label(window,text="Class -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
            Class_label.place(x=375,y=200,width=200)
            Class_entry =Label(window,text=(row[1]),font=("Cascadia Code",15))
            Class_entry.place(x=550,y=200,width=250)

            P_Name=StringVar()
            P_Name_label=Label(window,text="Parent Name -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
            P_Name_label.place(x=315,y=250,width=220)
            P_Name_entry=Label(window,text=(row[2]),font=("Cascadia Code",15))
            P_Name_entry.place(x=550,y=250,width=250)

            P_num=StringVar()    
            P_num_label=Label(window,text="Parent Number -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
            P_num_label.place(x=285,y=300,width=250)
            P_num_entry=Label(window,text=(row[3]),font=("Cascadia Code",15))
            P_num_entry.place(x=550,y=300,width=250)
        

            Transport=StringVar()
            Transport_label=Label(window,text="Transport -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
            Transport_label.place(x=345,y=350,width=200)
            Transport_entry=Label(window,text=(row[4]),font=("Cascadia Code",15))
            Transport_entry.place(x=550,y=350,width=250)
            
            # Van_no=StringVar()
            # Van_no_label=Label(window,text="Van No. -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
            # Van_no_entry=Label(window,text=(row[5]),font=("Cascadia Code",15))

            # Drv_Name=StringVar()
            # Drv_Name_label=Label(window,text="Drv_Name -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
            # Drv_Name_entry=Label(window,text=(row[6]),font=("Cascadia Code",15))

            # Drv_Contact=StringVar()
            # Drv_Contact_label=Label(window,text="Drv_Contact -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
            # Drv_Contact_entry=Label(window,text=(row[7]),font=("Cascadia Code",15))

            # Van_Reg_No=StringVar()
            # Van_Reg_No_label=Label(window,text="Van_Reg_No. -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
            # Van_Reg_No_entry=Label(window,text=(row[8]),font=("Cascadia Code",15))

            Van_no=StringVar()
            Van_no_label=Label(window,text="Van No. -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
            Van_no_label.place(x=345,y=400,width=200)
            Van_no_entry=Label(window,text=(row[5]),font=("Cascadia Code",15))
            Van_no_entry.place(x=550,y=400,width=250)

            Drv_Name=StringVar()
            Drv_Name_label=Label(window,text="Drv_Name -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
            Drv_Name_label.place(x=345,y=450,width=200)
            Drv_Name_entry=Label(window,text=(row[6]),font=("Cascadia Code",15))
            Drv_Name_entry.place(x=550,y=450,width=250)

            Drv_Contact=StringVar()
            Drv_Contact_label=Label(window,text="Drv_Contact -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
            Drv_Contact_label.place(x=345,y=500,width=200)
            Drv_Contact_entry=Label(window,text=(row[7]),font=("Cascadia Code",15))
            Drv_Contact_entry.place(x=550,y=500,width=250)

            Van_Reg_No=StringVar()
            Van_Reg_No_label=Label(window,text="Van_Reg_No. -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
            Van_Reg_No_label.place(x=345,y=550,width=200)
            Van_Reg_No_entry=Label(window,text=(row[8]),font=("Cascadia Code",15))
            Van_Reg_No_entry.place(x=550,y=550,width=250)
            if row[4] !="Van":
                if not row[5] or row[5] =='':
                    Van_no_entry=Label(window,text="",font=("Cascadia Code",15))
                    Van_no_entry.place(x=550,y=400,width=250)
                    Drv_Name_entry=Label(window,text="",font=("Cascadia Code",15))
                    Drv_Name_entry.place(x=550,y=450,width=250)
                    Drv_Contact_entry=Label(window,text="",font=("Cascadia Code",15))
                    Drv_Contact_entry.place(x=550,y=500,width=250)
                    Van_Reg_No_entry=Label(window,text="",font=("Cascadia Code",15))
                    Van_Reg_No_entry.place(x=550,y=550,width=250)

    Button(window,text="Exit",height="2",width="1",bg ='#00916E',fg="red",font=("Cascadia Code",18),command= lambda: window.destroy()).place(x=50,y=600,width=200)
    window.mainloop()

def report_data():

    def clas():
        window4=Tk()
        window4.title("Class")
        window4.geometry("500x300")
        window4.configure(bg='#06283D')

        radio_v=StringVar()
        radio_v.set(' ')
        b1=Radiobutton(text='XII-A', variable=radio_v, width=10,value='XII-A',bg='#06283D',fg="#FF4949",font=("Cascadia Code",20),command=window4.destroy)
        b1.pack()

        b2=Radiobutton(text='XII-B', variable=radio_v, width=10,value='XII-B',bg='#06283D',fg="#FF4949",font=("Cascadia Code",20), command=window4.destroy)
        b2.pack()

        b3=Radiobutton(text='XII-C', variable=radio_v, width=10,value='XII-C',bg='#06283D',fg="#FF4949",font=("Cascadia Code",20),  command=window4.destroy)
        b3.pack()

        window4.mainloop()

        my_ch=radio_v.get()
        Display_Data("class",my_ch,"")

    def transport():
        window5=Tk()
        window5.title("Transport")
        window5.geometry("500x300")
        window5.configure(bg='#06283D')

        radio_v=StringVar()
        radio_v.set(' ')
        b1=Radiobutton(text='Self', variable=radio_v, width=10,value='Self',bg='#06283D',fg="#FF4949",font=("Cascadia Code",20),command=window5.destroy)
        b1.pack()

        b2=Radiobutton(text='Van', variable=radio_v, width=10,value='Van',bg='#06283D',fg="#FF4949",font=("Cascadia Code",20),command= lambda: window5.destroy())
        b2.pack()



        window5.mainloop()

        my_ch=radio_v.get()
        if my_ch=='Self':
            Display_Data("transport",my_ch,"")
        else:
            window7=Tk()
            window7.title("Van No.")
            window7.geometry("500x300")
            window7.configure(bg='#06283D')
            Van_no_label=Label(window7,text="Van No. -",bg='#06283D',fg="#FF4949",font=("Cascadia Code",20))
            Van_no_label.place(x=50,y=50,width=200)

            options2 = StringVar()
            op=["Selct","All","VAN01(DL1CT 7856)","VAN02(DL1CT 7696)","VAN03(DL1CT 8796)","VAN04(DL2CT 7796)"]
            Van_entry = ttk.Combobox(window7,textvariable=options2,value=op,state='readonly')
            Van_entry.bind("<<<ComboboxSelect>>>")
            Van_entry.place(x=50,y=150,width=200,height=35)
            Button(window7,text="Search",height="2",width="1",bg ='#00916E',font=("Cascadia Code",10),command= lambda: window7.destroy()).place(x=175,y=200,width=150)


            window7.mainloop()
            no=options2.get()
            s=["All","VAN01(DL1CT 7856)","VAN02(DL1CT 7696)","VAN03(DL1CT 8796)","VAN04(DL2CT 7796)"]
            lst=["All","VAN01","VAN02","VAN03","VAN04"]
            ind=s.index(no)
            van=lst[ind]

            Display_Data("transport",my_ch,van)
            

    window6=Tk()
    window6.title("Report Data")
    window6.geometry("500x300")
    window6.configure(bg='#06283D')


    radio_v=StringVar()
    radio_v.set('x')

    b1=Radiobutton(text='Class', variable=radio_v, width=10,value='0',bg='#06283D',fg="#FF4949",font=("Cascadia Code",20),command=window6.destroy)
    b1.pack()

    b2=Radiobutton(text='Transport', variable=radio_v, width=10,value='1',bg='#06283D',fg="#FF4949",font=("Cascadia Code",20),command=window6.destroy)
    b2.pack()


    window6.mainloop()

    my_ch=radio_v.get()
    if my_ch=='0':
        clas()
    elif my_ch=='1':
        transport()
