from tkinter import *
from  tkinter import ttk
import mysql.connector as ms


mydb = ms.connect(host="localhost",user="root",passwd="Devansh#03",database="world")


def Display_Data(a,x,y):
    Table_Window=Tk()
    Table_Window.title('Data Report')
    Table_Window.geometry('1820x900')
    Table_Window.configure(bg='#094163')

    Table_Frame = Frame(Table_Window)
    Table_Frame.pack()

    My_Table = ttk.Treeview(Table_Frame)

    My_Table['columns'] = ('Admission_Number', 'Student_Name', 'Class', 'Parent_Name', 'Parent_Number','Transport')

    My_Table.column("#0", width=0,  stretch=NO)
    My_Table.column("Admission_Number",anchor=CENTER, width=120)
    My_Table.column("Student_Name",anchor=CENTER,width=120)
    My_Table.column("Class",anchor=CENTER,width=80)
    My_Table.column("Parent_Name",anchor=CENTER,width=120)
    My_Table.column("Parent_Number",anchor=CENTER,width=120)
    My_Table.column("Transport",anchor=CENTER,width=90)


    My_Table.heading("#0",text="",anchor=CENTER)
    My_Table.heading("Admission_Number",text="Admission_Number",anchor=CENTER)
    My_Table.heading("Student_Name",text="Student_Name",anchor=CENTER)
    My_Table.heading("Class",text="Class",anchor=CENTER)
    My_Table.heading("Parent_Name",text="Parent_Name",anchor=CENTER)
    My_Table.heading("Parent_Number",text="Parent_Number",anchor=CENTER)
    My_Table.heading("Transport",text="Transport",anchor=CENTER)


    My_Table1 = ttk.Treeview(Table_Frame)
    My_Table1['columns'] = ('Admission_Number', 'Student_Name', 'Class', 'Parent_Name', 'Parent_Number','Transport',"Van_No","Driver_Name","Driver_Contact","Van_Reg_No")


    My_Table1.column("#0", width=0,  stretch=NO)
    My_Table1.column("Admission_Number",anchor=CENTER, width=120)
    My_Table1.column("Student_Name",anchor=CENTER,width=120)
    My_Table1.column("Class",anchor=CENTER,width=80)
    My_Table1.column("Parent_Name",anchor=CENTER,width=120)
    My_Table1.column("Parent_Number",anchor=CENTER,width=120)
    My_Table1.column("Transport",anchor=CENTER,width=90)
    My_Table1.column("Van_No",anchor=CENTER,width=120)
    My_Table1.column("Driver_Name",anchor=CENTER,width=120)
    My_Table1.column("Driver_Contact",anchor=CENTER,width=120)
    My_Table1.column("Van_Reg_No",anchor=CENTER,width=120)


    My_Table1.heading("#0",text="",anchor=CENTER)
    My_Table1.heading("Admission_Number",text="Admission_Number",anchor=CENTER)
    My_Table1.heading("Student_Name",text="Student_Name",anchor=CENTER)
    My_Table1.heading("Class",text="Class",anchor=CENTER)
    My_Table1.heading("Parent_Name",text="Parent_Name",anchor=CENTER)
    My_Table1.heading("Parent_Number",text="Parent_Number",anchor=CENTER)
    My_Table1.heading("Transport",text="Transport",anchor=CENTER)
    My_Table1.heading("Van_No",text="Van_No",anchor=CENTER)
    My_Table1.heading("Driver_Name",text="Driver_Name",anchor=CENTER)
    My_Table1.heading("Driver_Contact",text="Driver_Contact",anchor=CENTER)
    My_Table1.heading("Van_Reg_No",text="Van_Reg_No",anchor=CENTER)


    if a=="class":
        st=("select st.Admno, st.Name,st.Class, st.P_name, st.P_number, st.Transport , van.Van_No, van.Drv_Name, van.Drv_Contact, van.Van_Reg_No from student_details st left outer join van_details van on st.Van_No= van.Van_No where Class = '" + x + "' order by st.Transport;")
    else:
        if x=="Self":
            st=("SELECT Admno, Name, Class, P_name, P_number, Transport from student_details where Transport = '" + x + "' order by Class ;")
        elif y != "All":
            st=("select st.Admno, st.Name,st.Class, st.P_name, st.P_number, st.Transport , van.Van_No, van.Drv_Name, van.Drv_Contact, van.Van_Reg_No from student_details st, van_details van where st.Van_No= van.Van_No and st.Van_No = '" + y + "'  order by st.Class ;")
        else:
            x="Van"   
            st=("select st.Admno, st.Name,st.Class, st.P_name, st.P_number, st.Transport , van.Van_No, van.Drv_Name, van.Drv_Contact, van.Van_Reg_No from student_details st, van_details van where st.Van_No= van.Van_No order by van.Van_No ;")
    cursor = mydb.cursor()
    cursor.execute(st)
    row = cursor.fetchall()

    n=0
    if a=="class" or x=="Van":
        for i in row:
            My_Table1.insert(parent='',index='end',iid=n,text='',values=(row[n]))
            n+=1
        My_Table1.pack()
    else:
        for i in row:
            My_Table.insert(parent='',index='end',iid=n,text='',values=(row[n]))
            n+=1
        My_Table.pack()   


    Table_Window.mainloop()
