# Money-Tracker
This a small software have created for my friend in order automate all the payment is receiving from his teaching classes. for GUI have used tkinter library and i'm using excel as my DB of storing data using pandas library.
Its also provides a history of transactions and maintains  a record in an Excel file. Below is a brief explanation of the main features and functionality of the Money Tracker application

# Overview

1 GUI interface

![image](https://github.com/kada2004/Money-Tracker/assets/117305234/139760f4-28ff-4669-a2b8-a717dc6e0a7a)


2 Password window

![image](https://github.com/kada2004/Money-Tracker/assets/117305234/d59cf9b1-0604-49cc-9fe8-00920ca77248)

![image](https://github.com/kada2004/Money-Tracker/assets/117305234/768b71ba-ac2b-4170-a495-dc1d77c070a6)

3 Read data history from Excel sheet

![image](https://github.com/kada2004/Money-Tracker/assets/117305234/1977a12d-9428-4e5e-bbce-735a448e62a9)

4 Excel sheet View where entry data is stored

![image](https://github.com/kada2004/Money-Tracker/assets/117305234/bc6f614b-072b-42b6-93b9-077ffaf4361a)

## Features
1. Add Money
.You can add money to your balance by entering an amount and clicking "Save" button.
.Before saying, you need to enter a password(default password: "123") to ensure security.
2. Revision Class
.This button allows you to deduct a specified amount from your balance for revision classes.
 . A window password will open, enter the password, and the amount will be subtracted from your balance
3. New Class
. Similar to the Revision Class feature, this button lets you deduct a specied amount for new classes.
. You need to enter the password to make this deduction.
4. Read Data
. You can view the history of your transactions by clicking the " Read Data" button.
. This opens a new window displaying a table of all your saved data.
5. Remainning Money
. This label displays the remaining balance after each transaction.

 6. Data and Time
. This label shows the current date and time, which updates every second.
## Usage
1. Run the application
2. Add money to you balance the" Add Money" button
3. Deduct money for revision or new classes by cliking the respective buttons.
4. Click the" Read data" button to view your transaction history.
5. The application will automatically update the remaining balance and display the current date and time.
## Security
.To ensure the security of your financial data, a password is required before making any transactions or deductions.
. The default password is "123" which you can change or customise in the code

## Data Storage
. The application stores all transaction in an Excel file
## Note
. Before running the application, make sure to change the  file path for the Excell sheet to your preferred location

## Dependencies
. tkinter for the GUI
. pandas for handling data and Excel file operations
## Run the Applicatiom
. Simply run the script in a Python environment with tkinter and pandas installed

Enjoy tracking your expenses with the Money Tracker application ! :)

Dan Kalenga






