import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from data import search_row, add_row, check
from graph import summary


class Application():

    def __init__(self, master=None):
        self.master = master
        self.createWidgets()
        self.master.title('Payroll')
        self.master.iconbitmap('payroll.ico')

    def graph(self, event=None):
        summary()

    def set_male(self):
        self.new_gender.set('male')

    def set_female(self):
        self.new_gender.set('female')

    def add_data(self, event=None):

        # To not throw an error in console if one or two inputs are empty
        try:
            name = self.add_name_entry.get()
            eid = int(self.add_eid_entry.get())
            gender = self.new_gender.get()
            salary = int(self.add_salary_entry.get())
            new_row = [eid, name, gender, salary]
            b = check(eid)
            if not b:
                return
            add_row(new_row)

        except ValueError:
            # To check if all inputs are being given
            if (not self.add_name_entry.get()):
                mb.showwarning(title='Invalid Input', message='Please Enter all values to proceed.')
            elif (not self.new_gender.get()):
                mb.showwarning(title='Invalid Input', message='Please Enter all values to proceed.')
            elif (not self.add_eid_entry.get()):
                mb.showwarning(title='Invalid Input', message='Please Enter all values to proceed.')
            elif (not self.add_salary_entry.get()):
                mb.showwarning(title='Invalid Input', message='Please Enter all values to proceed.')

        self.add_eid_entry.delete(0, 'end')
        self.add_name_entry.delete(0, 'end')
        self.add_salary_entry.delete(0, 'end')
        self.add_eid_entry.delete(0, 'end')

    def searchEmp(self, event=None):
        try:
            self.eid = int(self.eid_entry.get())
            self.name = self.name_entry.get()
            self.dat = search_row(self.eid)
        except KeyError:
            mb.showerror(title='Error!', message='The Instance doesn\'t exist in database.')
            return
        except ValueError:
            mb.showerror(title='Error!', message='Enter a Valid ID.')
            return

        root = Tk()
        root.title('Search')
        root.iconbitmap('payroll.ico')
        root.geometry('1000x650+35+100')
        self.days = IntVar()
        self.leave = IntVar()
        self.GST = DoubleVar()
        self.Gross = DoubleVar()

        f1 = Frame(root, bg='lightblue', relief=GROOVE, borderwidth=5)
        f1.place(x=20, y=10, width=500, height=600)

        self.txtPaySlip = Text(root, font=('arial', 12, 'bold'), bg='white')
        self.txtPaySlip.place(anchor='e', x=980, y=200, width=370)

        # Employee ID Label widget
        self.eid_label = Label(root, text='Employee ID', font=('Calibri', 19, 'bold'), width=13, bd=2, bg='skyblue3',
                               activebackground='blue', relief=RIDGE,
                               activeforeground='white')
        self.eid_label.place(x=35, y=30)

        # Employee Name Label widget
        self.name_label = Label(root, text='Name', font=('Calibri', 19, 'bold'), width=13, bd=2, bg='skyblue3',
                                activebackground='blue', relief=RIDGE,
                                activeforeground='white')
        self.name_label.place(x=35, y=70)

        # Employee Gender Label Widget
        self.gender_label = Label(root, text='Gender', font=('Calibri', 19, 'bold'), width=13, bd=2, bg='skyblue3',
                                  activebackground='blue', relief=RIDGE,
                                  activeforeground='white')
        self.gender_label.place(x=35, y=110)

        # Employee Salary Label Widget
        self.salary_label = Label(root, text='Salary', font=('Calibri', 19, 'bold'), width=13, bd=2, bg='skyblue3',
                                  activebackground='blue', relief=RIDGE,
                                  activeforeground='white')
        self.salary_label.place(x=35, y=150)

        # Employee Working days Widget
        self.days_label = Label(root, text='Working days', font=('Calibri', 19, 'bold'), width=13, bd=2, bg='skyblue3',
                                activebackground='blue', relief=RIDGE,
                                activeforeground='white')
        self.days_label.place(x=35, y=190)

        # Employee wage per day Widget
        self.wage_label = Label(root, text='Wage per day', font=('Calibri', 19, 'bold'), width=13, bd=2, bg='skyblue3',
                                activebackground='blue', relief=RIDGE,
                                activeforeground='white')
        self.wage_label.place(x=35, y=240)

        # Employee Leave Widget
        self.leave_label = Label(root, text='Leave', font=('Calibri', 19, 'bold'), width=13, bd=2, bg='skyblue3',
                                 activebackground='blue', relief=RIDGE,
                                 activeforeground='white')
        self.leave_label.place(x=35, y=280)

        # Tax Widget
        self.taxes_label = Label(root, text='GST', font=('Calibri', 19, 'bold'), width=13, bd=2, bg='skyblue3',
                                 activebackground='blue', relief=RIDGE,
                                 activeforeground='white')
        self.taxes_label.place(x=35, y=320)

        # Gross Salary
        self.Gross_label = Label(root, text='Gross Salary', font=('Calibri', 19, 'bold'), width=13, bd=2, bg='skyblue3',
                                 activebackground='blue', relief=RIDGE,
                                 activeforeground='white')
        self.Gross_label.place(x=35, y=360)

        # Employee ID text widget
        self.eid_text = Text(root, height=1, width=20, font=('Calibri', 15))
        self.eid_text.place(x=230, y=33)
        self.eid_text.insert(END, str(self.dat[0]))

        # Employee Name text Widget
        self.name_text = Text(root, height=1, width=20, font=('Calibri', 15))
        self.name_text.place(x=230, y=73)
        self.name_text.insert(END, str(self.dat[1]))

        # Employee Gender Text Widget
        self.gender_text = Text(root, height=1, width=20, font=('Calibri', 15))
        self.gender_text.place(x=230, y=113)
        self.gender_text.insert(END, str(self.dat[2]))

        # Employee Salary Text Widget
        self.salary_text = Text(root, height=1, width=20, font=('Calibri', 15))
        self.salary_text.place(x=230, y=153)
        self.salary_text.insert(END, str(self.dat[3]))

        # Employee working days
        self.days_entry = tk.Scale(root, from_=0, to=31, orient=HORIZONTAL, variable=self.days)
        self.days_entry.place(x=230, y=193)

        # Employee wage per days

        self.wage = self.dat[3] / 30
        self.wage_text = Text(root, height=1, width=20, font=('Calibri', 15))
        self.wage_text.place(x=230, y=243)
        self.wage_text.insert(END, str(self.wage))

        # Employee leave
        self.leave_entry = Entry(root, width=22, highlightbackground='lightblue', textvariable=self.leave)
        self.leave_entry.place(x=230, y=283)

        # Taxes
        self.taxes_entry = Entry(root, width=22, highlightbackground='lightblue', textvariable=self.GST)
        self.taxes_entry.place(x=230, y=323)

        # Gross salary
        self.Gross_entry = Entry(root, width=22, highlightbackground='lightblue', textvariable=self.Gross)
        self.Gross_entry.place(x=230, y=363)

        # Compute button
        self.add_new_button = Button(root, width=31, bd=2, relief=RAISED,
                                     font=('Calibri', 15),
                                     highlightbackground='lightblue', highlightcolor='white', activeforeground='white',
                                     bg='white', text='Compute', command=self.EnterInfo)
        self.add_new_button.place(x=100, y=413)

    def EnterInfo(self):
        self.txtPaySlip.delete("1.0", END)
        self.txtPaySlip.insert(END, "\t\tPay Slip\n\n")
        self.txtPaySlip.insert(END, 'Employer ID:\t\t' + str(self.dat[0]) + "\n\n")
        self.txtPaySlip.insert(END, 'Name:\t\t' + str(self.dat[1]) + "\n\n")
        self.txtPaySlip.insert(END, 'Gender:\t\t' + str(self.dat[2]) + "\n\n")
        self.txtPaySlip.insert(END, 'Gross Salary :\t\t' + str(self.dat[3]) + "\n\n")
        self.txtPaySlip.insert(END, 'Working days of company:\t\t' + str(self.days_entry.get()) + "\n\n")
        self.txtPaySlip.insert(END, 'Leave:\t\t' + str(self.leave_entry.get()) + "\n\n")
        self.txtPaySlip.insert(END, 'Wages Per day:\t\t' + str(self.wage) + "\n\n")
        self.txtPaySlip.insert(END, 'GST is:\t\t' + str(self.taxes_entry.get()) + "%" + "\n\n")
        self.payableTax = (int(self.taxes_entry.get()) / 100) * int(self.dat[3])

        self.txtPaySlip.insert(END, 'Tax payable:\t\t' + str(self.payableTax) + "\n\n")
        self.netSalary = float(int(self.days_entry.get()) - int(self.leave_entry.get())) * (self.wage)
        self.txtPaySlip.insert(END, 'Net salary:\t\t{}'.format(self.netSalary))

    def addEmp(self, event=None):
        root = Tk()
        root.title('Add New Employee')
        root.iconbitmap('payroll.ico')
        root.geometry("520x620+990+100")
        self.new_eid = StringVar()
        self.new_name = StringVar()
        self.new_salary = StringVar()
        self.new_gender = StringVar()

        f2 = Frame(root, bg='lightblue', relief=GROOVE, borderwidth=5)
        f2.place(x=10, y=10, width=500, height=600)

        frontlabel = Label(f2, text='Enter Details', width=30,
                           font=('Calibri', 20, 'italic bold'), bg='white')
        frontlabel.place(x=35, y=100)

        # Employee ID Label Widget
        self.add_eid_label = Label(f2, text='Employee ID', font=('Calibri', 19, 'bold'), width=13, bd=2, bg='skyblue3',
                                   activebackground='blue', relief=RIDGE,
                                   activeforeground='white')
        self.add_eid_label.place(x=56, y=191)

        # Employee Name Lable Widget
        self.add_name_label = Label(root, text='Employee Name', font=('Calibri', 19, 'bold'), width=13, bd=2,
                                    bg='skyblue3',
                                    activebackground='blue', relief=RIDGE,
                                    activeforeground='white')
        self.add_name_label.place(x=70, y=250)

        # Employee Gender Label Widget
        self.add_gender_label = Label(root, text='Gender', font=('Calibri', 19, 'bold'), width=13, bd=2, bg='skyblue3',
                                      activebackground='blue', relief=RIDGE,
                                      activeforeground='white')
        self.add_gender_label.place(x=70, y=300)

        # Employee Salary Label Widget
        self.add_salary_label = Label(root, text='Salary', font=('Calibri', 19, 'bold'), width=13, bd=2, bg='skyblue3',
                                      activebackground='blue', relief=RIDGE,
                                      activeforeground='white')
        self.add_salary_label.place(x=70, y=350)

        # Employee ID entry Widget
        self.add_eid_entry = Entry(root, width=20, bd=2, textvariable=self.new_eid)
        self.add_eid_entry.place(x=270, y=208)

        # Employee Name Entry Widget
        self.add_name_entry = Entry(root, width=20, textvariable=self.new_name)
        self.add_name_entry.place(x=270, y=250)

        # Employee Gender Radio Widget
        self.add_gender_radio_m = Radiobutton(root, text='Male', value='male', variable=self.new_gender,
                                              bg='lightblue',
                                              command=self.set_male)
        self.add_gender_radio_m.place(x=270, y=304)

        self.add_gender_radio_f = Radiobutton(root, text='Female', value='female', variable=self.new_gender,
                                              bg='lightblue',
                                              command=self.set_female)
        self.add_gender_radio_f.place(x=350, y=304)

        # Employee Salary Entry Widget
        self.add_salary_entry = Entry(root, width=20, textvariable=self.new_salary)
        self.add_salary_entry.place(x=270, y=350)

        # ADD new button
        self.add_new_button = Button(root, text='Add to Database', width=31, bd=2, relief=FLAT, font=('Calibri', 15),
                                     activeforeground='white', highlightbackground='lightblue', highlightcolor='white',
                                     bg='white', command=self.add_data)
        self.add_new_button.place(x=100, y=420)

        # Enter key functionality on Add to database button
        self.add_new_button.bind('<Return>', self.add_data)

    def createWidgets(self):

        self.empId = StringVar()
        self.name = StringVar()

        # Frame Inside Master
        f2 = Frame(self.master, bg='lightblue', relief=GROOVE, borderwidth=5)
        f2.place(x=10, y=10, width=500, height=600)

        # Top Label
        frontlabel = Label(f2, text='Payroll Management System', width=30,
                           font=('Calibri', 20, 'italic bold'), bg='white')
        frontlabel.place(x=35, y=100)

        # Employee ID Label widget
        self.eid_label = Label(f2, text='Employee ID', font=('Calibri', 19, 'bold'), width=10, bd=2, bg='skyblue3',
                               activebackground='blue', relief=RIDGE,
                               activeforeground='white')
        self.eid_label.place(x=55, y=260)

        # Employee Name Label widget
        self.name_label = Label(f2, text='Name', font=('Calibri', 19, 'bold'), width=10, bd=2, bg='skyblue3',
                                activebackground='blue', relief=RIDGE,
                                activeforeground='white')
        self.name_label.place(x=55, y=300)

        # Employee ID Entry Widget
        self.eid_entry = Entry(f2, width=20, font=('roman', 15, 'bold'), bd=2, textvariable=self.empId)
        self.eid_entry.place(x=200, y=260)

        # Employee Name Entry Widget
        self.name_entry = Entry(f2, width=20, font=('roman', 15, 'bold'), bd=2, textvariable=self.name)
        self.name_entry.place(x=200, y=300)

        # Search Button
        self.search_button = Button(f2, text='Search', width=31, bd=2, relief=RIDGE, font=('Calibri', 15),
                                    activeforeground='white', highlightbackground='lightblue', highlightcolor='white',
                                    bg='white', command=self.searchEmp)
        self.search_button.place(x=90, y=370)

        # Add new Employee Button
        self.add_button = Button(f2, text='Add New Employee', width=31, bd=2, relief=RIDGE, activeforeground='white',
                                 highlightbackground='lightblue', font=('Calibri', 15),
                                 highlightcolor='white', command=self.addEmp)
        self.add_button.place(x=90, y=400)

        self.summaryButton = Button(self.master, text='Graph Summary', width=31, bd=2, relief=RIDGE,
                                    font=('Calibri', 15),
                                    highlightbackground='lightblue', highlightcolor='white', activeforeground='white',
                                    bg='white', command=self.graph)
        self.summaryButton.place(x=105, y=450)

        # Enter key functionality for buttons
        self.search_button.bind("<Return>", self.searchEmp)
        self.add_button.bind("<Return>", self.addEmp)
        self.summaryButton.bind('<Return>', self.graph)


root = Tk()
root.geometry('520x620+470+100')
root.resizable(FALSE, FALSE)
app = Application(master=root)
root.mainloop()
