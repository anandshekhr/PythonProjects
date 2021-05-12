from tkinter import *
from tkinter import ttk
import pymysql

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Students Database")
        self.root.geometry("1350x700+0+0")

        Frame_title=Label(self.root, text = "Student Database", font = ("times new roman",20,"bold"))
        Frame_title.pack(side= TOP)
        #=====Variables Definition===
        self.Roll_no_var= StringVar()
        self.name_var =StringVar()
        self.gender_var = StringVar()
        self.age_var = StringVar()
        self.search_by=StringVar()
        self.search_text =StringVar()
        #=====Manage frame=========
        Manage_Frame = Frame(self.root,bd= 4,relief =RIDGE)
        Manage_Frame.place(x=20,y=70,width=500,height=560)

        m_title = Label(Manage_Frame,text = "Manage Students",font = ("times new roman",20,"bold"),bg = "crimson", fg = "white")
        m_title.grid(row=0,columnspan=2,pady=20,)

        roll_number_lbl = Label(Manage_Frame,text = "Roll Number",font = ("times new roman",20,"bold"),bg = "crimson", fg = "white")
        roll_number_lbl.grid(row=1, column=0, pady=10,padx=20,sticky='w')

        txt_roll = Entry(Manage_Frame, textvariable = self.Roll_no_var,font=("times new roman",15,"bold"),bd=6,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky ="w")

        students_name_lbl = Label(Manage_Frame, text="Name of Students", font=("times new roman", 20, "bold"), bg="crimson",
                                fg="white")
        students_name_lbl.grid(row=2, column=0, pady=10, padx=20, sticky='w')

        txt_Student_name = Entry(Manage_Frame, textvariable = self.name_var,font=("times new roman", 15, "bold"), bd=6, relief=GROOVE)
        txt_Student_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        Student_age_lbl = Label(Manage_Frame, text="Age", font=("times new roman", 20, "bold"), bg="crimson",
                                fg="white")
        Student_age_lbl.grid(row=3, column=0, pady=10, padx=20, sticky='w')

        txt_age = Entry(Manage_Frame,textvariable = self.age_var ,font=("times new roman", 15, "bold"), bd=6, relief=GROOVE)
        txt_age.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        Gender_lbl = Label(Manage_Frame, text="Gender", font=("times new roman", 20, "bold"), bg="crimson",
                                fg="white")
        Gender_lbl.grid(row=4, column=0, pady=10, padx=20, sticky='w')

        combo_gender = ttk.Combobox(Manage_Frame,textvariable = self.gender_var,font =("times new roman",12,"bold"),state = 'readonly')
        combo_gender["values"]=("male","female","transgender")
        combo_gender.grid(row=4, column = 1, pady=10, padx=20, sticky ="w")
        #txt_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        #==========Button Frame==========
        btn_Frame = Frame(self.root, bd=4, relief=RIDGE)
        btn_Frame.place(x=30, y=500, width=480)

        addbutton = Button(btn_Frame,text = "Insert",command =self.insert_students(), width = 10 ).grid(row=0,column=0,padx=10,pady=10)
        update_button = Button(btn_Frame, text="Update", width=10,command=self.upate_data()).grid(row=0, column=1, padx=10, pady=10)
        delete_button = Button(btn_Frame,text = "Delete", width = 10,command = self.delete_data()).grid(row=0,column=2,padx=10,pady=10)
        clear_button = Button(btn_Frame,text = "Clear", width = 10,command=self.clear() ).grid(row=0,column=3,padx=10,pady=10)

        #==========Details Frame=============
        Details_Frame = Frame(self.root, bd=4, relief=RIDGE)
        Details_Frame.place(x=520, y=70, width=800,height = 560)


        search_label = Label(Details_Frame,text = "Search by",font = ("times new roman",20,"bold"))
        search_label.grid(row=0,column=0,pady=10,padx=20,sticky='w')

        combo_search_by = ttk.Combobox(Details_Frame, textvariable=self.search_by,font=("times new roman", 12, "bold"), state='readonly')
        combo_search_by["values"] = ("Roll Number", "Name of Students", "Age")
        combo_search_by.grid(row=0, column=1, pady=20, padx=10)

        txt_search = Entry(Details_Frame, font = ("times new roman",12,"bold"),bd=5, relief = GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky='w')

        searchbutton = Button(Details_Frame, textvariable=self.search_text,text="Search", width=10,command = self.searching_data()).grid(row=0, column=3, padx=10, pady=10)
        showallbutton = Button(Details_Frame, text="Show All", width=10).grid(row=0, column=4, padx=10, pady=10)

        #=======Table Frame=========
        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE)
        Table_Frame.place(x=10, y=70, width=760, height=480)

        scroll_x = Scrollbar(Table_Frame,orient = HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","gender","age"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name", text="Name of Students")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("age", text="Student's Age")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=50)
        self.Student_table.column("name", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("age", width=100)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.fetching_data()

    def insert_students(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s)",(self.Roll_no_var.get(),self.name_var.get(),self.gender_var.get(),self.age_var.get()))
        con.commit()
        self.fetching_data()
        con.close()

    def fetching_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows =cur.fetchall()
        #if len(rows)!=0:
            #self.Student_table.delete(*self.Student_table.get_children())
         #   for row in rows:

        #      self.Student_table.insert("",END,values=rows)
        con.commit()
        con.close()
                    #(self.Roll_no_var.get(), self.name_var.get(), self.gender_var.get(), self.age_var.get()))
    def clear(self):
        self.Roll_no_var.set("")
        self.name_var.set("")
        self.gender_var.set("")
        self.age_var.set("")

    def upate_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update students set Name_students =%s,gender =%s, age =%s where Roll_Number = %s",
                    (self.name_var.get(), self.gender_var.get(), self.age_var.get(),self.Roll_no_var.get()))
        con.commit()
        self.fetching_data()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete from students where Roll_Number=%s",self.Roll_no_var.get())
        con.commit()
        con.close()

    def searching_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students where" +str(self.search_by.get())+"LIKE"+str(self.search_text.get()))
        rows =cur.fetchall()
        #if len(rows)!=0:
            #self.Student_table.delete(*self.Student_table.get_children())
         #   for row in rows:

        #      self.Student_table.insert("",END,values=rows)
        con.commit()
        con.close()


root = Tk()
ob = Student(root)
root.mainloop()