from tkinter import *
from tkinter import ttk
import tkinter.messagebox


class School:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='gainsboro')

        # ================================Frame=============================================
        MainFrame = Frame(self.root, bd=10, width=1350, height=800, relief=RIDGE)
        MainFrame.grid()

        OuterFrame = Frame(MainFrame, bd=10, width=1340, height=600, relief=RIDGE)
        OuterFrame.grid(row=0, column=0)

        InnerMostFrame = Frame(OuterFrame, bd=5, width=600, height=500, bg='cadet blue', relief=RIDGE)
        InnerMostFrame.grid(row=0, column=0)

        InnerFrame = Frame(OuterFrame, bd=5, width=700, height=500, bg='cadet blue', relief=RIDGE)
        InnerFrame.grid(row=0, column=1)

        BottomInnerFrame = Frame(MainFrame, bd=7, width=1340, height=300, bg='cadet blue', relief=RIDGE)
        BottomInnerFrame.grid(row=2, column=0)

        Records_Frame = Frame(InnerFrame, bd=4, width=800, height=600, relief=RIDGE)
        Records_Frame.grid()

        DisplayFrame = Frame(InnerMostFrame, bd=4, width=400, height=100, relief=RIDGE)
        DisplayFrame.grid()

        Button_Frame = Frame(BottomInnerFrame, bd=4, width=1340, height=100, bg="cadet blue", relief=RIDGE)
        Button_Frame.grid(row=0, column=0)
        # ========================================Variables================================================
        self.StudentID = StringVar()
        self.Firstname = StringVar()
        self.Surname = StringVar()
        self.NINumber = StringVar()
        self.Address = StringVar()
        self.Gender = StringVar()
        self.DOB = StringVar()
        self.Mobile = StringVar()
        self.Email = StringVar()

        # ====================================Student Details======================================

        self.lblStudentID = Label(DisplayFrame, font=('arial', 12, 'bold'), text="Student ID", bd=12)
        self.lblStudentID.grid(row=0, column=0, sticky=W, padx=5, pady=3)
        self.txtStudentID = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=3, width=29, textvariable=self.StudentID)
        self.txtStudentID.grid(row=0, column=1)

        self.lblFirstname = Label(DisplayFrame, font=('arial', 12, 'bold'), text="Firstname", bd=10)
        self.lblFirstname.grid(row=1, column=0, sticky=W, padx=5, pady=3)
        self.txtFirstname = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=3, width=29, textvariable=self.Firstname)
        self.txtFirstname.grid(row=1, column=1)

        self.lblSurname = Label(DisplayFrame, font=('arial', 12, 'bold'), text="Surname", bd=10)
        self.lblSurname.grid(row=2, column=0, sticky=W, padx=5, pady=3)
        self.txtSurname = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=3, width=29, textvariable=self.Surname)
        self.txtSurname.grid(row=2, column=1)

        self.lblNINumber = Label(DisplayFrame, font=('arial', 12, 'bold'), text="NI Number", bd=10)
        self.lblNINumber.grid(row=3, column=0, sticky=W, padx=5, pady=3)
        self.txtNINumber = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=3, width=29, textvariable=self.NINumber)
        self.txtNINumber.grid(row=3, column=1)

        self.lblAddress = Label(DisplayFrame, font=('arial', 12, 'bold'), text="Address", bd=10)
        self.lblAddress.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtAddress = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=3, width=29, textvariable=self.Address)
        self.txtAddress.grid(row=4, column=1)

        self.lblGender = Label(DisplayFrame, font=('arial', 12, 'bold'), text="Gender", bd=12)
        self.lblGender.grid(row=5, column=0, sticky=W, padx=5, pady=3)
        self.cboGender = ttk.Combobox(DisplayFrame, width=27, font=('arial', 12, 'bold'), state='readonly',
                                      textvariable=self.Gender)
        self.cboGender['values'] = ('', 'Female', 'Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=5, column=1)

        self.lblDOB = Label(DisplayFrame, font=('arial', 12, 'bold'), text="DOB", bd=12)
        self.lblDOB.grid(row=6, column=0, sticky=W, padx=5, pady=3)
        self.txtDOB = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=3, width=29, textvariable=self.DOB)
        self.txtDOB.grid(row=6, column=1)

        self.lblMobile = Label(DisplayFrame, font=('arial', 12, 'bold'), text="Mobile", bd=12)
        self.lblMobile.grid(row=7, column=0, sticky=W, padx=5, pady=3)
        self.txtMobile = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=5, width=29, textvariable=self.Mobile)
        self.txtMobile.grid(row=7, column=1)

        self.lblEmail = Label(DisplayFrame, font=('arial', 12, 'bold'), text="Email", bd=12, justify=LEFT)
        self.lblEmail.grid(row=8, column=0, sticky=W, padx=5, pady=3)
        self.txtEmail = Entry(DisplayFrame, font=('arial', 12, 'bold'), bd=5, width=29, justify='left',
                              textvariable=self.Email)
        self.txtEmail.grid(row=8, column=1)

        # =====================================Student Record========================================
        scroll_x = Scrollbar(Records_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Records_Frame, orient=VERTICAL)

        self.student_records = ttk.Treeview(Records_Frame, height=20, columns=("stdid", "firstname", "surname",\
        "ninumber", "address", "gender", "dob","mobile", "email"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_records.heading("stdid", text="Student ID")
        self.student_records.heading("firstname", text="Firstname")
        self.student_records.heading("surname", text="Surname")
        self.student_records.heading("ninumber", text="NINumber")
        self.student_records.heading("address", text="Address")
        self.student_records.heading("gender", text="Gender")
        self.student_records.heading("dob", text="DOB")
        self.student_records.heading("mobile", text="Mobile")
        self.student_records.heading("email", text="Email")

        self.student_records['show'] = 'headings'
        self.student_records.column("stdid", width=70)
        self.student_records.column("firstname", width=100)
        self.student_records.column("surname", width=100)
        self.student_records.column("ninumber", width=70)
        self.student_records.column("address", width=150)
        self.student_records.column("gender", width=70)
        self.student_records.column("dob", width=70)
        self.student_records.column("mobile", width=100)
        self.student_records.column("email", width=150)

        self.student_records.pack(fill=BOTH, expand=1)

        # =========================================Buttons=====================================
        self.btnAddNew = Button(Button_Frame, pady=1, padx=24, bd=6, font=('arial', 10, 'bold'), width=9,
                                text="Add New")
        self.btnAddNew.grid(row=1, column=0)

        self.btnUpdate = Button(Button_Frame, pady=1, padx=24, bd=6, font=('arial', 10, 'bold'), width=9, text="Update")
        self.btnUpdate.grid(row=1, column=1)

        self.btnDelete = Button(Button_Frame, pady=1, padx=24, bd=6, font=('arial', 10, 'bold'), width=9, text="Delete")
        self.btnDelete.grid(row=1, column=2)

        self.btnReset = Button(Button_Frame, pady=1, padx=24, bd=6, font=('arial', 10, 'bold'), width=9, text="Reset",command=self.Reset)
        self.btnReset.grid(row=1, column=3)

        self.btnExit = Button(Button_Frame, pady=1, padx=24, bd=6, font=('arial', 10, 'bold'), width=9, text="Exit",command=self.iExit)
        self.btnExit.grid(row=1, column=4)

           # =====================================Functions============================================#

    def Reset(self):
        self.StudentID.set("")
        self.Firstname.set("")
        self.Surname.set("")
        self.NINumber.set("")
        self.Address.set("")
        self.Gender.set("")
        self.DOB.set("")
        self.Mobile.set("")
        self.Email.set("")


    def iExit(self):
        iExit = tkinter.messagebox.askyesno("School Management System", "Confirm if you want to exit")
        if iExit > 0:
            self.root.destroy()
            return





if __name__ == '__main__':
    root = Tk()
    application = School(root)
    root.mainloop()
