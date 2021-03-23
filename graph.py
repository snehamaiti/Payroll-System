from matplotlib import pyplot as plt
import pandas as pd
from tkinter import *

month = pd.read_csv('2019-details.csv')
monthly_df = pd.DataFrame(month)
monthly_df.index = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                    'November', 'December', '2019']
monthly_df = monthly_df[:12]

year = pd.read_csv('Year-details.csv')
yearly_df = pd.DataFrame(year)
yearly_df.index = ['2016', '2017', '2018', '2019']


def g1():
    x = monthly_df.index
    plt.figure(figsize=(12, 6))
    plt.plot(x, monthly_df['Gross Profit'], x, monthly_df['Expenses'])
    plt.xlabel('Months')
    plt.suptitle('Profit and expenses in each month in 2019 (USD Millions)')
    plt.legend(['Gross Profit', 'Expenses'])
    plt.show()


def g2():
    x = monthly_df['Gross Profit'].diff()
    y = monthly_df['Expenses'].diff()
    plt.plot(x, y)
    plt.xlabel('Gross Profit (USD Million)')
    plt.ylabel('Expenses (USD Million)')
    plt.suptitle('Relation between Gross Profit and Expenses')
    plt.show()


def g3():
    x = monthly_df['Net Earnings']
    y = monthly_df['Income tax']
    plt.plot(x, y)
    plt.xlabel('Net Earnings (USD Million)')
    plt.ylabel('Income tax (USD Million)')
    plt.suptitle('Relation between Net Earnings and Income tax')
    plt.show()


def g4():
    x = yearly_df.index
    plt.plot(x, yearly_df['Gross Profit'], x, yearly_df['Expenses'])
    plt.xlabel('Year')
    plt.ylabel('Gross Profit')
    plt.legend(['Gross Profit', 'Expenses'])
    plt.suptitle('Gross Profit and Expenses in years')
    plt.show()


def g5():
    plt.plot(yearly_df['Gross Profit'].diff(), yearly_df['Expenses'].diff())
    plt.xlabel('Gross Profit (USD Million)')
    plt.ylabel('Expenses (USD Million)')
    plt.suptitle('Relation between Gross Profit and Expenses')
    plt.show()


def g6():
    x = yearly_df['Net Earning']
    y = yearly_df['Income Tax']
    plt.plot(x, y)
    plt.xlabel('Net Earnings (USD Million)')
    plt.ylabel('Income tax (USD Million)')
    plt.suptitle('Relation between Net Earning and Income Tax')
    plt.show()


def summary():
    root = Tk()
    root.title('Graph Summary')
    root.iconbitmap('payroll.ico')
    root.geometry('500x300+200+200')
    root.configure(bg='lightblue')
    b1 = Button(root, width=31, bd=2, relief=RAISED,
                font=('Calibri', 15),
                highlightbackground='lightblue', highlightcolor='white', activeforeground='white',
                bg='white', text='Monthly Profit and Expenses', command=g1)
    b1.place(x=95, y=20)

    b2 = Button(root, width=31, bd=2, relief=RAISED,
                font=('Calibri', 15),
                highlightbackground='lightblue', highlightcolor='white', activeforeground='white',
                bg='white', text='Monthly Gross Profit and Expenses', command=g2)
    b2.place(x=95, y=55)

    b3 = Button(root, width=31, bd=2, relief=RAISED,
                font=('Calibri', 15),
                highlightbackground='lightblue', highlightcolor='white', activeforeground='white',
                bg='white', text='Monthly Net Earnings and Income Tax', command=g3)
    b3.place(x=95, y=90)

    b4 = Button(root, width=31, bd=2, relief=RAISED,
                font=('Calibri', 15),
                highlightbackground='lightblue', highlightcolor='white', activeforeground='white',
                bg='white', text='Yearly Profit and Expenses', command=g4)
    b4.place(x=95, y=125)

    b5 = Button(root, width=31, bd=2, relief=RAISED,
                font=('Calibri', 15),
                highlightbackground='lightblue', highlightcolor='white', activeforeground='white',
                bg='white', text='Yearly Gross Profit and Expenses', command=g5)
    b5.place(x=95, y=160)

    b6 = Button(root, width=31, bd=2, relief=RAISED,
                font=('Calibri', 15),
                highlightbackground='lightblue', highlightcolor='white', activeforeground='white',
                bg='white', text='Yearly Net Earning and Expenses', command=g6)
    b6.place(x=95, y=195)

    root.mainloop()
