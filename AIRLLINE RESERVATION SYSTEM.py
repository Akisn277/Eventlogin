from tkinter import *
import mysql.connector

def ins():
    print("WELCOME TO AI AIRLINE RESERVATION SERVICE!")
    print("ENTER 1 FOR BOOKING A TICKET")
    print("ENTER 2 FOR CANCELLING A TICKET")

def detailsF():
    master = Tk()
    master.title("PLS ENTER YOUR REQUIREMENTS")
    Label(master, text='Departure City ', bg="red").grid(row=0)
    Label(master, text='Date of Departure', bg="light cyan").grid(row=1)
    Label(master, text='Arrival City', bg="light green").grid(row=2)
    submit = Button(master, text="Submit", command=master.destroy).grid(row=3)
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)

total_rows = 7
total_columns = 4
lst = [
    ("S_No", "TIME", 'FLIGHT_NAME', 'FLIGHT_ID'),
    (1, '06:00', 'AI Airlines', 'B7#130713'),
    (2, '08:00', 'Avis Airlines', 'A4#103899'),
    (3, '10:00', 'Reise Airlines', 'R3#456839'),
    (4, '14:00', 'Sichere Airlines', 'S4#004445'),
    (5, '18:45', 'Viaje Airlines', 'G3#858999'),
    (6, '22:22', 'Ostatnia Airlines', 'O0#755722')
]

class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='yellow', bg='black', font=('MS Gothic', 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

def flightdis():
    root = Tk()
    t = Table(root)
    root.mainloop()

def detailsP():
    master = Tk()
    master.title("PLS ENTER YOUR DETAILS")
    labels = ['Passport No.', 'Name', 'Gender', 'Phone No.', 'DOB', 'Nationality', 'Residential Address', 'Flight Name', 'Flight ID', 'Departure Time']
    entries = []
    for i, label in enumerate(labels):
        Label(master, text=label).grid(row=i)
        entry = Entry(master)
        entry.grid(row=i, column=1)
        entries.append(entry)
    submit = Button(master, text="Submit", command=master.destroy).grid(row=len(labels))
    return entries

def paymentc():
    master = Tk()
    master.title("PLS ENTER YOUR BANK DETAILS")
    labels = ['Card No.', 'Name', 'Expiry date', 'CVV']
    entries = []
    for i, label in enumerate(labels):
        Label(master, text=label).grid(row=i)
        entry = Entry(master)
        entry.grid(row=i, column=1)
        entries.append(entry)
    submit = Button(master, text="Submit", command=master.destroy).grid(row=len(labels))
    return entries

def seatingarr():
    win = Tk()
    print("Choose the seat of your choice")
    rows = 10
    columns = 9
    selected_seat = StringVar()
    
    def on_seat_click(row, column):
        selected_seat.set(f"R {row + 1}, C {column + 1}")
    
    for x in range(rows):
        for y in range(columns):
            seat_label = Label(win, text=f"R {x + 1}, C {y + 1}", borderwidth=1, relief="solid", width=8, height=2)
            seat_label.grid(row=x + 1, column=y + 1)
            seat_label.bind("<Button-1>", lambda event, row=x, column=y: on_seat_click(row, column))
    
    def on_next_click():
        print("Selected Seat:", selected_seat.get())
        win.destroy()
    
    Button(win, text="NEXT", command=on_next_click).grid(row=rows + 2, columnspan=columns, sticky=SE)
    win.mainloop()

def ticket_cancellation():
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='Akisn@277', database='pps')
    cursor = mycon.cursor()
    mycon.autocommit = True
    passport_no = input("Pls enter your passport no.: ")
    s4 = "DELETE FROM customer_details WHERE Passport_no='{}'".format(passport_no)
    cursor.execute(s4)
    mycon.close()
    print("*********************************************************")
    print("TICKET CANCELLATION SUCCESSFUL!")
    print("*********************************************************")

print("*******************WELCOME TO AI AIRLINES**********************")
ins()
x = int(input("ENTER THE NUMBER: "))

if x == 1:  # booking
    detailsF()
    flightdis()
    detailsP_entries = detailsP()
    seatingarr()
    paymentc()
    print("*********************************************************")
    print("TICKET BOOKING SUCCESSFUL!")
    print("*********************************************************")
elif x == 2:  # cancellation
    ticket_cancellation()
else:
    print("Invalid Entry! Please enter a valid option.")
