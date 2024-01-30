from tabulate import tabulate
import sys
from tkinter import *
from tkinter import ttk
from tkinter import Tk, Label, Entry, Button, Frame, messagebox
from tkinter.simpledialog import askfloat
from tkinter.simpledialog import askinteger
from tkinter.simpledialog import askstring

class ATM:
    # Initialize the ATM with an initial balance, current balance, and an empty transaction history.
    def __init__(self):
        self.initial_balance = 100000
        self.balance = self.initial_balance
        self.transaction_history = []

    # Define a method for depositing money into the ATM.
    def deposit(self, amount):
        # Increase the balance by the deposited amount.
        self.balance += amount
        # Create a transaction detail message for the deposit and append it to the transaction history.
        transaction_detail = f'Deposited ${amount}'
        self.transaction_history.append(transaction_detail)
        # Return a message confirming the deposit and showing the new balance.
        return f'Deposited ${amount}. New balance: ${self.balance}'

    # Define a method for withdrawing money from the ATM.
    def withdraw(self, amount):
        # Check if the requested withdrawal amount is less than or equal to the available balance.
        if amount <= self.balance:
            # Reduce the balance by the withdrawn amount.
            self.balance -= amount
            # Create a transaction detail message for the withdrawal and append it to the transaction history.
            self.transaction_history.append(f'Withdrawn ${amount}')
            # Return a message confirming the withdrawal and showing the new balance.
            return f'Withdrawn ${amount}. New balance: ${self.balance}'
        else:
            # Return an "Insufficient funds" message if the withdrawal amount exceeds the available balance.
            return 'Insufficient funds'

    # Define a method for transferring money from the ATM to another recipient.
    def transfer(self, amount, recipient, transfer_type):
        # Check if the requested transfer amount is less than or equal to the available balance.
        if amount <= self.balance:
            # Reduce the balance by the transferred amount based on the transfer type.
            self.balance -= amount
            # Create a transaction detail message for the transfer based on the transfer type.
            if transfer_type == 1:
                transaction_detail = f'Transferred ${amount} to {recipient}'
                self.transaction_history.append(transaction_detail)
            elif transfer_type == 2:
                transaction_detail = f'Transferred ${amount} to {recipient}'
                self.transaction_history.append(transaction_detail)
            elif transfer_type == 3:
                transaction_detail = f'Transferred ${amount} to {recipient}'
                # Append the transaction detail to the transaction history.
                self.transaction_history.append(transaction_detail)
            # Return a message confirming the transfer and showing the new balance.
            return f'Transferred ${amount} to {recipient}. New balance: ${self.balance}'
        else:
            # Return an "Insufficient funds" message if the transfer amount exceeds the available balance.
            return 'Insufficient funds'

    # Define a method to get the current balance.
    def get_balance(self):
        # Return a message displaying the current balance.
        return f'Current balance: ${self.balance}'

    # Define a method to get the transaction history.
    def get_transaction_history(self):
        # Return the list of transaction history.
        return self.transaction_history

#check the login id and password
def login_process(user_id, user_pin):
    # Placeholder for the login process
    # You can replace this with the actual logic to verify user credentials
    if user_id == "123456" and user_pin == "654321":
        messagebox.showinfo("Login Successful", "Welcome to the ATM Interface!")
        # You can call your ATM interface function here or raise another Tkinter frame/page
        login_frame.pack_forget()
        operations_frame.pack()
    else:
        messagebox.showerror("Login Failed", "Invalid User ID or PIN")

# make the login interface
class LoginFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("ATM Application")
        self.master.geometry('700x700')

        label = Label(self, text="Welcome to the ATM Interface!")
        label.pack()

        label_user_id = Label(self, text="User Id", fg='black')
        label_user_pin = Label(self, text="User Pin", fg='black')

        label_user_id.pack(pady=10)
        label_user_pin.pack(pady=10)

        self.user_id_field = Entry(self)
        self.user_pin_field = Entry(self, show='*')  # Use show='*' to hide entered PIN

        self.user_id_field.pack(pady=10)
        self.user_pin_field.pack(pady=10)

        submit_button = Button(self, text="Submit", fg='black', command=self.login_button_clicked)
        submit_button.pack(pady=10)

    def login_button_clicked(self):
        user_id = self.user_id_field.get()
        user_pin = self.user_pin_field.get()
        login_process(user_id, user_pin)

#operations page
# class OperationsFrame(Frame):
#     def __init__(self, master=None, atm_instance=None):
#         super().__init__(master)
#         self.master = master
#         self.master.title("ATM Application")
#         self.master.geometry('700x700')
#
#         label = Label(self, text="Operations to Perform")
#         label.pack()
#
#         #deposit button
#         deposit_button = Button(self, text="Deposit", fg='black', command=self.deposit_button_clicked)
#         deposit_button.pack(pady=10)
#
#     #deposit button when clicked
#     def deposit_button_clicked(self):
#         # Prompt the user to enter the deposit amount using a dialog box
#         amount = askfloat("Deposit", "Enter the deposit amount:")
#         if amount is not None:
#             # Call the deposit method and display the result
#             result = self.atm_instance.deposit(amount)
#             messagebox.showinfo("Deposit Result", result)

class OperationsFrame(Frame):
    def __init__(self, master=None, atm_instance=None):
        super().__init__(master)
        self.master = master
        self.master.title("ATM Application")
        self.master.geometry('700x700')

        self.atm_instance = atm_instance  # Store the ATM instance as an attribute

        label = Label(self, text="Operations to Perform")
        label.pack()

        # deposit button
        deposit_button = Button(self, text="Deposit", fg='black', command=self.deposit_button_clicked)
        deposit_button.pack(pady=10)

        # withdraw function
        withdraw_button = Button(self, text="Withdraw", fg='black', command=self.withdraw_button_clicked)
        withdraw_button.pack(pady=10)

        # transfer button
        transfer_button = Button(self, text="Transfer", fg='black', command=self.transfer_button_clicked)
        transfer_button.pack(pady=10)

        #get balance
        balance_button = Button(self, text="Balance", fg='black', command=self.balance_button_clicked)
        balance_button.pack(pady=10)

        # transaction_history_button
        transaction_history_button = Button(self, text="Transaction History", fg='black',
                                            command=self.transaction_history_button_clicked)
        transaction_history_button.pack(pady=10)

        #quit button
        quit_button = Button(self, text="Quit", fg='black', command=self.quit_button_clicked)
        quit_button.pack(pady=10)


    # deposit button when clicked
    def deposit_button_clicked(self):
        # Prompt the user to enter the deposit amount using a dialog box
        amount = askfloat("Deposit", "Enter the deposit amount:")
        if amount is not None:
            # Call the deposit method and display the result
            result = self.atm_instance.deposit(amount)
            messagebox.showinfo("Deposit Result", result)

    # withdraw button when clicked
    def withdraw_button_clicked(self):
        # Prompt the user to enter the deposit amount using a dialog box
        amount = askfloat("Withdraw", "Enter the withdrawing amount:")
        result = self.atm_instance.withdraw(amount)
        messagebox.showinfo("Deposit Result", result)

    # transfer button when clicked
    def transfer_button_clicked(self):
        # Prompt the user to choose a transfer type
        transfer_type = askinteger("Transfer Type", "Choose Transfer Type (1/2/3):", minvalue=1, maxvalue=3)
        if transfer_type is not None:
            # Prompt the user to enter the transfer amount using a dialog box
            amount = askfloat("Transfer", "Enter the Transferring amount:")
            if amount is not None:
                # Prompt the user to enter the recipient's name using a dialog box
                recipient = askstring("Recipient", "Enter the Recipient's Name:")
                if recipient is not None:
                    # Call the ATM instance's transfer method based on the transfer type
                    result = self.atm_instance.transfer(amount, recipient, transfer_type)
                    # Display the result using a messagebox
                    messagebox.showinfo("Transfer Result", result)

    # balance display
    def balance_button_clicked(self):
        result = self.atm_instance.get_balance()
        messagebox.showinfo("Balance Result", result)

    # transaction history
    def transaction_history_button_clicked(self):
        history = self.atm_instance.get_transaction_history()

        if len(history) > 0:
            # Initialize an empty list to store the transaction table.
            table = []
            # Initialize the available_balance with the initial_balance of the ATM.
            available_balance = self.atm_instance.initial_balance
            # Loop through each transaction in the history.
            for i, transaction in enumerate(history, start=1):
                # Split the transaction string by the dollar sign and take the last part
                transaction_parts = transaction.split('$')
                if len(transaction_parts) > 1:
                    # Extract the transaction amount from the split transaction string.
                    transaction_amount = float(transaction_parts[-1].split()[0])

                    # Update available_balance based on the type of transaction.
                    if "Deposited" in transaction:
                        available_balance += transaction_amount
                    elif "Withdrawn" in transaction or "Transferred" in transaction:
                        available_balance -= transaction_amount

                # Create a row for the table with the transaction number, details, and available balance.
                table.append([i, transaction, f"${available_balance:.2f}"])
            # Display the transaction history table using tabulate.
            messagebox.showinfo("Transaction History",
                                tabulate(table, headers=["#", "Transaction", "Available Balance"],
                                         tablefmt="grid"))
        else:
            # If the transaction history is empty, show a message.
            messagebox.showinfo("Transaction History", "Transaction history is empty.")

    # quit functionality
    def quit_button_clicked(self):
        # Hide the current frame (OperationsFrame)
        self.pack_forget()
        # Show the login frame
        login_frame.pack()



if __name__ == "__main__":
    # Call the "atm_interface" function to start the ATM application.
    # atm_interface()
    # Define a class named "ATM" to represent the ATM functionality.
    root = Tk()
    atm = ATM()
    login_frame = LoginFrame(root)
    operations_frame = OperationsFrame(root, atm_instance=atm)
    login_frame.pack()
    root.mainloop()


    # Adding a label to window



