from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Easy Ticket")
root.geometry("600x600")
frame = Frame(root)
root.config(bg="#0d8f73")

# define variable set in class
variable = StringVar()
# class
class ClsTicketSales:
    myresult = StringVar()
    variable.set("Select")

# defining clear button
    def clear(self):
        self.txt_cell.delete(0, END)
        self.spn_no_tics.delete(0, END)

    def __init__(self, window):
        # number info
        self.cell = Label(window, text="Cell Number", bg="#0d8f73")
        self.cell.pack()
        self.txt_cell = Entry(window)
        self.txt_cell.pack()
        # ticket options
        self.options = Label(window, text="Category", bg="#0d8f73")
        self.options.pack()
        self.tic_options = OptionMenu(window, variable, 'soccer', 'movie', 'theater')
        self.tic_options.pack()
        # number of tickets bought
        self.no_tics = Label(window, text="Number Of Tickets", bg="#0d8f73")
        self.no_tics.pack()
        self.spn_no_tics = Spinbox(window, from_=0, to=20)
        self.spn_no_tics.pack()
        # calculate button
        self.cal = Button(window, text="Calculate Price", command=self.calc_prepayment)
        self.cal.pack()
        # clear button
        self.clear = Button(window, text="Clear Entries", command=self.clear)
        self.clear.pack()
        self.CalcPrepayment = Entry(window)
        self.exit = Button(window, text="X", command="exit")
        self.exit.place(x=565, y=0)
        self.frame = Frame(window, width="100", height="100", relief="groove", borderwidth=2)
        self.frame.place(relx=0.7, rely=0.8)
        self.calc_prepayment = Label(self.frame, text="", bg="blue")
        self.calc_prepayment.place(x=500, y=200,)
        self.reserve = Label(window, text="")


    def calc_prepayment(self):
        ticket_no = int(self.spn_no_tics.get())
        vat = 0.14
        try:
            int(self.txt_cell.get())
            if len(self.txt_cell.get()) < 10 or len(self.txt_cell.get()) > 10:
                raise ValueError

            elif variable.get() == "Select Ticket":
                raise ValueError

            elif int(self.spn_no_tics.get()) == 0:
                raise ValueError


            # Soccer
            elif variable.get() == "Soccer":
                price = 40  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.calc_prepayment.config(text=text)


            # Movie
            elif variable.get() == "Movie":
                price = 75  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.calc_prepayment.config(text=text)

            # Theater
            elif variable.get() == "Theater":
                price = 100  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.calc_prepayment.config(text=text)

            # Reservation
                reserve_text = "Reservation for {} for : {} ".format(self.tic_options.get(), ticket_no)
                cell_text = "Reservation Made By: {}".format(self.txt_cell_entry.get())
                self.reserve.config(text=reserve_text)
                self.cell.config(text=cell_text)

        except ValueError:   # Error Message
         messagebox.showerror(message="INVALID - Please Try Again")


obj_Ticketsales=ClsTicketSales(root)
root.mainloop()