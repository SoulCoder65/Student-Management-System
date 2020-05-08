from tkinter import *
import tkinter.ttk as ttk

from tkinter.messagebox import showerror,showinfo
import pymysql #FOR DATABASE

class StudentManagement:
    def __init__(self,root):
        self.root=root
        font = ('Khmer OS System', 19, 'bold')
        font_textfield = ('Khmer OS System', 13, 'bold')

        # VARIABLES
        self.Roll_var=StringVar()
        self.Name_var=StringVar()
        self.Email_var=StringVar()
        self.Gender_var=StringVar()
        self.Contact_var=StringVar()
        self.Dob_var=StringVar()
        self.Search_var=StringVar()
        self.Select_var=StringVar()

        self.root.geometry("1300x800")
        self.root.title("Student Management System by Akshay")
        titleFrame=Frame(self.root)
        titleFrame.pack(pady=10,padx=5)
        heading_label=Label(titleFrame,text="Student Management System",bg="Cyan",bd=10,relief=GROOVE,font=('time new roman', 30, 'bold'),width=200)
        heading_label.pack(side=TOP)
        entryFrame=Frame(self.root,bd=5,relief=GROOVE)
        entryFrame.place(x=6, y=85, width=515, height=620)

        # ENTRY FRAME TITLE
        entry_title=Label(entryFrame,text="Student Management",font = ('time new roman', 19, 'bold'),bg="brown",bd=10,width=27)
        entry_title.grid(row=0,columnspan=2,pady=10)

        # image = PhotoImage(file='images/book.png')
        # ImageLabel = Label(titleFrame, image =image)
        # ImageLabel.place(x=5, y=10, width=200, height=70)

        # FIELDS FOR FILLING DATA OF STUDENTS
        Roll_no= Label(entryFrame, text="Roll Number:", font=font,fg='FireBrick')
        Roll_no.grid(row=1, column=0, pady=10,sticky='w',padx=8)

        Roll_no_field=Entry(entryFrame,font=font_textfield,textvariable=self.Roll_var,justify=CENTER,bg='LightYellow')
        Roll_no_field.grid(row=1,column=1,pady=10,sticky="w",padx=0)

        Name= Label(entryFrame, text="Name:", font=font, fg='FireBrick')
        Name.grid(row=2, column=0, pady=10, sticky='w',padx=8)

        Name_field = Entry(entryFrame, font=font_textfield,textvariable=self.Name_var, justify=CENTER, bg='LightYellow')
        Name_field.grid(row=2, column=1, pady=10, sticky="w", padx=0)

        Email = Label(entryFrame, text="E-mail:", font=font, fg='FireBrick')
        Email.grid(row=3, column=0, pady=10, sticky='w', padx=8)

        Email_field = Entry(entryFrame, font=font_textfield,textvariable=self.Email_var, justify=CENTER, bg='LightYellow')
        Email_field.grid(row=3, column=1, pady=10, sticky="w", padx=0)

        contact = Label(entryFrame, text="Contact:", font=font, fg='FireBrick')
        contact.grid(row=4, column=0, pady=10, sticky='w', padx=8)

        contact_field = Entry(entryFrame, font=font_textfield,textvariable=self.Contact_var, justify=CENTER, bg='LightYellow')
        contact_field.grid(row=4, column=1, pady=10, sticky="w",padx=1)

        gender = Label(entryFrame, text="Gender:", font=font, fg='FireBrick')
        gender.grid(row=5, column=0, pady=10, sticky='w', padx=8)

        gender_field = ttk.Combobox(entryFrame, font=font_textfield,textvariable=self.Gender_var, justify=CENTER,state="readonly",width=19)
        gender_field['values']=("Male","Female","Others")
        gender_field.grid(row=5, column=1, pady=10, sticky="w")

        DateBirth = Label(entryFrame, text="D.O.B:", font=font, fg='FireBrick')
        DateBirth.grid(row=6, column=0, pady=10, sticky='w', padx=8)

        DateBirth_field = Entry(entryFrame, font=font_textfield,textvariable=self.Dob_var, justify=CENTER, bg='LightYellow')
        DateBirth_field.grid(row=6, column=1, pady=10, sticky="w", padx=2)

        ButtonFrame=Frame(entryFrame)
        ButtonFrame.place(x=10,y=500,width=450)

        AddButton=Button(ButtonFrame,text="ADD",font=font_textfield,relief='solid',fg='DarkOrange',bg='LightGreen',activebackground='blue',activeforeground='white',command=self.add_stud)
        AddButton.grid(row=0,column=0,padx=10)

        UpdateButton = Button(ButtonFrame, text="UPDATE", font=font_textfield, relief='solid', fg='DarkOrange',bg='LightGreen', activebackground='blue', activeforeground='white',command=self.updateData)
        UpdateButton.grid(row=0, column=1,padx=10)

        DeleteButton = Button(ButtonFrame, text="DELETE", font=font_textfield, relief='solid', fg='DarkOrange',bg='LightGreen', activebackground='blue', activeforeground='white',command=self.deleteData)
        DeleteButton.grid(row=0, column=2,padx=10)

        ClearButton = Button(ButtonFrame, text="CLEAR", font=font_textfield, relief='solid', fg='DarkOrange',bg='LightGreen', activebackground='blue', activeforeground='white',command=self.clear_fun)
        ClearButton.grid(row=0, column=3, padx=10)

        # DISPLAYING DATABASE(TABLES OF ENTERED DETAILS)

        SearchFrame=Frame(self.root)
        SearchFrame.place(x=550,y=90)
        SearchLabel=Label(SearchFrame,text="Search By:",font=font_textfield,fg="FireBrick")
        SearchLabel.grid(row=0,column=0)

        Select_field = ttk.Combobox(SearchFrame, font=font_textfield,textvariable=self.Select_var, justify=CENTER, state="readonly", width=10)
        Select_field['values'] = ("Roll_Number", "Name", "Contact")
        Select_field.grid(row=0, column=1, pady=10, sticky="w",padx=5)

        Search_field = Entry(SearchFrame, font=font_textfield,textvariable=self.Search_var, justify=CENTER,bg='LightYellow')
        Search_field.grid(row=0, column=2, pady=10, sticky="w", padx=2)

        SearchButton = Button(SearchFrame, text="SEARCH", font=font_textfield, relief='solid', fg='DarkOrange',bg='LightGreen', activebackground='blue', activeforeground='white',command=self.searchData)
        SearchButton.grid(row=0, column=3, padx=10)

        ShowButton = Button(SearchFrame, text="SHOW ALL", font=font_textfield, relief='solid', fg='DarkOrange',bg='LightGreen', activebackground='blue', activeforeground='white',command=self.getData)
        ShowButton.grid(row=0, column=4, padx=10)

        # TABLE OF DATA
        TableFrame=Frame(self.root)
        TableFrame.place(x=550,y=150,width=750,height=550)

        scrollX=Scrollbar(TableFrame,orient=HORIZONTAL)
        scrollY=Scrollbar(TableFrame,orient=VERTICAL)
        self.TableDetails=ttk.Treeview(TableFrame,columns=("Roll","Name","Email","Gender","Contact","D.O.B"),xscrollcommand=scrollX,yscrollcommand=scrollY)
        scrollX.pack(side=BOTTOM,fill=X)
        scrollY.pack(side=RIGHT,fill=Y)
        scrollX.config(command=self.TableDetails.xview)
        scrollY.config(command=self.TableDetails.yview)
        self.TableDetails.heading("Roll",text="Roll Number")
        self.TableDetails.heading("Name",text="Name")
        self.TableDetails.heading("Email",text="Email")
        self.TableDetails.heading("Gender",text="Gender")
        self.TableDetails.heading("Contact",text="Contact")
        self.TableDetails.heading("D.O.B",text="D.O.B")
        # SETTING WIDTH OF TABLE
        self.TableDetails.column("Roll",width=125)
        self.TableDetails.column("Name",width=125)
        self.TableDetails.column("Email",width=125)
        self.TableDetails.column("Gender",width=125)
        self.TableDetails.column("Contact",width=125)
        self.TableDetails.column("D.O.B",width=125)
        self.TableDetails['show']='headings'
        self.TableDetails.bind("<ButtonRelease-1>",self.rowFocus)
        self.TableDetails.pack(fill=BOTH,expand=1)
        self.getData()
        # DATABASE CONNECTIVITY FUNCTION

    def add_stud(self):
        try:
            if self.Roll_var.get()=="" or self.Name_var.get()==""or self.Email_var.get()==""or self.Gender_var.get()==""or self.Dob_var.get()=="":
                showerror("Data Required","All Field Are Mandatory")
            else:
                con = pymysql.connect(host="localhost", user="root", password="", database="std")
                cur = con.cursor()
                cur.execute("insert into studentdata values(%s,%s,%s,%s,%s,%s)", (self.Roll_var.get(),
                                                                                  self.Name_var.get(),
                                                                                  self.Email_var.get(),
                                                                                  self.Gender_var.get(),
                                                                                  self.Contact_var.get(),
                                                                                  self.Dob_var.get(),

                                                                                  ))
                con.commit()
                self.getData()
                self.clear_fun()
                con.close()
        except Exception as e:
            showerror("Wrong Info","Roll Number Should Be Unique")

    def clear_fun(self):
        self.Name_var.set("")
        self.Email_var.set("")
        self.Contact_var.set("")
        self.Gender_var.set("")
        self.Roll_var.set("")
        self.Dob_var.set("")

    def getData(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="std")
        cur=con.cursor()
        cur.execute("select * from studentdata")
        detail=cur.fetchall()
        print(cur.fetchone())
        if len(detail)!=0:
            self.TableDetails.delete(*self.TableDetails.get_children())
            for row in detail:
                self.TableDetails.insert('',END,values=row)
            con.commit()
        con.close()
        self.clear_search()
    def clear_search(self):
        self.Select_var.set("")
        self.Search_var.set("")

    def rowFocus(self,hand):
        data=self.TableDetails.focus()
        contents=self.TableDetails.item(data)
        row_data=contents['values']
        self.Roll_var.set(row_data[0])
        self.Name_var.set(row_data[1])
        self.Email_var.set(row_data[2])
        self.Gender_var.set(row_data[3])
        self.Contact_var.set(row_data[4])
        self.Dob_var.set(row_data[5])

    def updateData(self):
        try:
            if self.Roll_var.get()=="" or self.Name_var.get()==""or self.Email_var.get()==""or self.Gender_var.get()==""or self.Dob_var.get()=="":
                showerror("Data Required","All Field Are Mandatory")
            else:
                con=pymysql.connect(host="localhost",user="root",password="",database="std")
                cur=con.cursor()
                cur.execute("update studentdata set Name=%s,Email=%s,Contact=%s,Gender=%s,DOB=%s where Roll_Number=%s",(
                                                                                                                            self.Name_var.get(),
                                                                                                                            self.Email_var.get(),
                                                                                                                            self.Contact_var.get(),
                                                                                                                            self.Gender_var.get(),
                                                                                                                            self.Dob_var.get(),
                                                                                                                            self.Roll_var.get()
                                                                                                                            ))
                con.commit()
                self.getData()
                self.clear_fun()
                con.close()
        except Exception as e:
            showerror("Update Error","Cannot Update these Data!!")

    def deleteData(self):
        try:
            if self.Roll_var.get() == "" or self.Name_var.get() == "" or self.Email_var.get() == "" or self.Gender_var.get() == "" or self.Dob_var.get() == "":
                showerror("Data Required", "All Field Are Mandatory")
            else:
                con=pymysql.connect(host="localhost",user="root",password="",database="std")
                cur=con.cursor()
                cur.execute("delete from studentdata where Roll_Number=%s",self.Roll_var.get())
                con.commit()
                self.getData()
                self.clear_fun()
                con.close()
        except Exception as e:
            showerror("Delete Error","Cannot Delete This data!!")

    def searchData(self):
        try:
            if self.Select_var.get()=="":
                showerror("Empty Field","Please Select one of the parameter from List")
            elif self.Search_var.get()=="":
                showerror("Empty Field","Please Write Name/Contact/Roll no")
            else:
                con = pymysql.connect(host="localhost", user="root", password="", database="std")
                cur = con.cursor()
                if self.Select_var.get()=="Name":
                    cur.execute("select * from studentdata where Name=%s",str(self.Search_var.get()))
                elif self.Select_var.get()=="Roll_Number":
                    cur.execute("select * from studentdata where Roll_Number=%s",str(self.Search_var.get()))
                elif self.Select_var.get()=="Contact":
                    cur.execute("select * from studentdata where Contact=%s",str(self.Search_var.get()))

                detail = cur.fetchall()
                if len(detail) != 0:
                    self.TableDetails.delete(*self.TableDetails.get_children())
                    for row in detail:
                        self.TableDetails.insert('', END, values=row)
                    con.commit()
                con.close()
        except Exception as e:
            showerror("Not Found","Cannot find This data!!")

root=Tk()
std=StudentManagement(root)
root.mainloop()