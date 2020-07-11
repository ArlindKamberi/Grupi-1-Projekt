import time
from datetime import datetime, timedelta
from database import Database 
from bills import monthlyBills,yearlyBills

try:
    import getch
    def getpass(prompt):
        """Replacement for getpass.getpass() which prints asterisks for each character typed"""
        print(prompt, end='', flush=True)
        buf = ''
        while True:
            ch = getch.getch()
            if ch == '\n':
                print('')
                break
            else:
                buf += ch
                print('*', end='', flush=True)
        return buf
except ImportError:
    from getpass import getpass




db = Database(dbname="database")
db.createtableifnotexists("monthlyBills",monthlyBills,monthlyBills.fromline)
db.createtableifnotexists("yearlyBills",yearlyBills,yearlyBills.fromline)

# All accounts
users = {
    "root": {
        "password": "gucci-mane",
        "group": "admin",
        "mail": []
    }
}

# Form validation
def validate(form):
    if len(form) > 0:
        return False
    return True

# Login authorization
def loginauth(db, username, password):
    users = db.getObjectsFrom("users")
    for user in users:
      if user.username==username and user.password==password:
        return session(username)

# Login
def login(db):
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = getpass("Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break

    if loginauth(db, username, password):
        return session(username)
    #else:
      #  print("Invalid username or password")

# Register
def register(db:Database):
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        else:
            break
    while True:
        password = getpass("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    print("Creating account...")
    user = User(username,password)
    db.appendObjectInto("users",user)
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"
    users[username]["mail"] = []
    time.sleep(1)
    print("Account has been created")

def change_password(db):
  print(" ")
  username = input("Enter account's username: ")
  usrs = db.getObjectsFrom("users", lambda x: x.username == username)
  if len(usrs) == 1:
    password = input("Please confirm by entering current password: ")
    if usrs[0].password == password:
      new_password = input("Please enter your new password: ")
      all_users = db.getObjectsFrom("users", lambda x:x.username != username)
      all_users.append(User(username, new_password))
      db.overwriteObjectsInto("users", all_users)
    else:
      print("Password entered doesn't match your current one")


def change_username(db):
  print(" ")
  username = input("Enter current username: ")
  usrs = db.getObjectsFrom("users", lambda x: x.username == username)
  if len(usrs) == 1:
    password = input("Please confirm by entering current password: ")
    if usrs[0].password == password:
      new_username = input("Please enter your new username: ")
      all_users = db.getObjectsFrom("users", lambda x:x.username != username)
      all_users.append(User(new_username, password))
      db.overwriteObjectsInto("users", all_users)
    else:
      print("Password entered doesn't match your current one")


# User session
def session(username):
  print("Welcome to your account " + username)
  '''if users[username]["group"] == "admin":
    print("") '''
  while True:
    print(" ")
    print("      ****** Main Menu ******      ")
    print(" ")
    print( "Monthly Bills |  Yearly Bills  |  Personal Budget Calculator | Manage Account | Logout")
    print(" ")
    choice= input("Which one would you like to check >  ")
    choice.lower()
    if choice=="monthly bills":
      print(" ")
      print( "Water bills | House tax |  Electricity bills | Mobile services | Other ")
      print(" ")
      monthbill= input("Which one would you like to check >  ")
      print(" ")
      monthbill.lower()
      if monthbill=="water bills":
        Water_bill(db,username)
      elif monthbill=="house tax":
        House_tax(db,username)
      elif monthbill=="electricity bills":
        Electricity_bill(db,username)
      elif monthbill=="mobile services":
        Mobile_services(db,username)
      elif monthbill=="other":
        Monthly_other(db,username)
      else:
        #monthbill.capitalise()
        print(monthbill, "is not an option")


    elif choice=="yearly bills":
      print( "Insurance bills | Holiday bills |  Education bills | Car testing bills | Other ")
      yearbill= input("Which one would you like to check: ")
      print(" ")
      yearbill.lower()
      if yearbill=="insurance bills":
        insurance_bills(db,username)
      elif yearbill=="holiday bills":
        holiday_bills(db,username)
      elif yearbill=="education bills":
        education_bills(db,username)
      elif yearbill=="car testing bills":
        car_testing_bills(db,username)
      elif yearbill=="other":
        yearly_other(db,username)
      else:
        print(yearbill, "is not an option")



    elif choice == "personal budget calculator":
      print(" ")
      personal_budget_calculator()
      
    elif choice =="manage account":
      print("Change Password | Change Username ")
      uchoice = input("> ")
      uchoice.lower()
      if uchoice == "change password":
        change_password(db)
      elif uchoice == "change username":
        change_username(db)
      else:
        print(uchoice, "is not an option")
    
    elif choice == "logout":
      print("Logging out...")
      break


    else:
      print("Invalid choice.")

def Water_bill(db,username):
  print("press 1 to create new water bill ")
  print("press 2 to see all bills ")
  print(" press anything else to exit")
  choice = input(">")
  if choice =="1":
    print("creating water bill")
    
    monthlyBills.createBill(db,"waterbill")
    reminder_input=input("Do you want to add a reminder: ")
    reminder_input.lower
    if reminder_input== "yes":
      monthlyBills.reminder(db, "pay_date_str")
    elif reminder_input == "no":
      print ("You won't be reminded for the paydate of this bill")
    
  elif choice=="2":
    bills = db.getObjectsFrom("monthlyBills",lambda x:x.btype=="waterbill" and x.name==username)
    for bill in bills:
      print(bill.toString())
      
def House_tax(db,username):
  print("press 1 to create new housetax bill ")
  print("press 2 to see all bills ")
  print(" press anything else to exit")
  choice = input(">")
  if choice =="1":
    print("creating housetax bill")
    monthlyBills.createBill(db,"housetaxbill")
    reminder_input=input("Do you want to add a reminder: ")
    reminder_input.lower
    if reminder_input== "yes":
      monthlyBills.reminder(db, "pay_date_str")
    elif reminder_input == "no":
      print ("You won't be reminded for the paydate of this bill")
    
  elif choice=="2":
    bills = db.getObjectsFrom("monthlyBills",lambda x:x.btype=="housetaxbill" and x.name==username )
    for bill in bills:
      print(bill.toString())

def Electricity_bill(db,username):
  print("press 1 to create new electricity bill ")
  print("press 2 to see all bills ")
  print(" press anything else to exit")
  choice = input(">")
  if choice =="1":
    print("creating electricity bill")
    monthlyBills.createBill(db,"electricitybill")
    reminder_input=input("Do you want to add a reminder: ")
    reminder_input.lower
    if reminder_input== "yes":
      monthlyBills.reminder(db, "pay_date_str")
    elif reminder_input == "no":
      print ("You won't be reminded for the paydate of this bill")
    
  elif choice=="2":
    bills = db.getObjectsFrom("monthlyBills",lambda x:x.btype=="electricitybill" and x.name==username)
    for bill in bills:
      print(bill.toString())

def Mobile_services(db,username):
  print(" ")
  print( "Telephone Bills | Internet Bills")
  mobile_choice= input("> ")
  mobile_choice.lower()
  if mobile_choice=="telephone bills":
    print("press 1 to create new telephone bill ")
    print("press 2 to see all bills ")
    print(" press anything else to exit")
  choice = input(">")
  if choice =="1":
    print("creating telephone bill")
    monthlyBills.createBill(db,"telephonebill")
    reminder_input=input("Do you want to add a reminder: ")
    reminder_input.lower
    if reminder_input== "yes":
      monthlyBills.reminder(db, "pay_date_str")
    elif reminder_input == "no":
      print ("You won't be reminded for the paydate of this bill")
  elif choice=="2":
    bills = db.getObjectsFrom("monthlyBills",lambda x:x.btype=="telephonebill" and x.name==username)
    for bill in bills:
      print(bill.toString())
  elif mobile_choice=="internet bills":
    print("press 1 to create new internet bill ")
    print("press 2 to see all bills ")
    print(" press anything else to exit")
  choice = input(">")
  if choice =="1":
    print("creating internet bill")
    monthlyBills.createBill(db,"internetbill")
    reminder_input=input("Do you want to add a reminder: ")
    reminder_input.lower
    if reminder_input== "yes":
      monthlyBills.reminder(db, "pay_date_str")
    elif reminder_input == "no":
      print ("You won't be reminded for the paydate of this bill")
    
  elif choice=="2":
    bills = db.getObjectsFrom("monthlyBills",lambda x:x.btype=="internetbill" and x.name==username)
    for bill in bills:
      print(bill.toString())

def Monthly_other(db,username):
  print("press 1 to create new other bill ")
  print("press 2 to see all bills ")
  print(" press anything else to exit")
  choice = input(">")
  if choice =="1":
    print("creating other bill")
    monthlyBills.createBill(db,"otherbill")
    reminder_input=input("Do you want to add a reminder: ")
    reminder_input.lower
    if reminder_input== "yes":
      monthlyBills.reminder(db, "pay_date_str")
    elif reminder_input == "no":
      print ("You won't be reminded for the paydate of this bill")
    
  elif choice=="2":
    bills = db.getObjectsFrom("monthlyBills",lambda x:x.btype=="otherbill" and x.name==username)
    for bill in bills:
      print(bill.toString())

def insurance_bills(db,username):
  print("press 1 to create new insurance bill ")
  print("press 2 to see all bills ")
  print(" press anything else to exit")
  choice = input(">")
  if choice =="1":
    print("creating insurance bill")
    yearlyBills.createBill(db,"insurancebill")
    reminder_input=input("Do you want to add a reminder: ")
    reminder_input.lower
    if reminder_input== "yes":
      monthlyBills.reminder(db, "pay_date_str")
    elif reminder_input == "no":
      print ("You won't be reminded for the paydate of this bill")
  elif choice=="2":
    bills = db.getObjectsFrom("yearlyBills",lambda x:x.btype=="insurancebill" and x.name==username)
    for bill in bills:
      print(bill.toString())
      
def holiday_bills(db,username):
  print("Acomodation | Transportation")
  holiday_choice= input("> ")
  holiday_choice.lower()
  if holiday_choice=="acomodation":
    def akomodim():
      print("press 1 to create new insurance bill ")
      print("press 2 to see all bills ")
      print(" press anything else to exit")
  choice = input(">")
  if choice =="1":
    print("creating accomodation bill")
    yearlyBills.createBill(db,"accomodationbill")
  elif choice=="2":
    bills = db.getObjectsFrom("yearlyBills",lambda x:x.btype=="accomodationbill" and x.name==username)
    for bill in bills:
      print(bill.toString())
  elif holiday_choice=="transportation":
    print("press 1 to create new transportation bill ")
    print("press 2 to see all bills ")
    print(" press anything else to exit")
  choice = input(">")
  if choice =="1":
    print("creating  transportation bill")
    yearlyBills.createBill(db,"transportationbill")
  elif choice=="2":
    bills = db.getObjectsFrom("yearlyBills",lambda x:x.btype=="transportationbill"and x.name==username)
    for bill in bills:
      print(bill.toString())

def education_bills(db,username):
  print("School | Courses")
  education_choice= input("> ")
  education_choice.lower()
  if education_choice=="school":
    print("press 1 to create new school bill ")
    print("press 2 to see all bills ")
    print(" press anything else to exit")
  choice = input(">")
  if choice =="1":
    print("creating school bill")
    yearlyBills.createBill(db,"schoolbill")
    print("press 2 to see all bills ")
    print(" press anything else to exit")
  choice = input(">")
  if choice =="1":
    print("creating courses bill")
    yearlyBills.createBill(db,"coursesbill")
    reminder_input=input("Do you want to add a reminder: ")
    reminder_input.lower
    if reminder_input== "yes":
      monthlyBills.reminder(db, "pay_date_str")
    elif reminder_input == "no":
      print ("You won't be reminded for the paydate of this bill")
    elif choice=="2":
      bills = db.getObjectsFrom("yearlyBills",lambda x:x.btype=="coursesbill" and x.name==username)
    for bill in bills:
      print(bill.toString())

def car_testing_bills(db,username):
  print("press 1 to create new other bill ")
  print("press 2 to see all bills ")
  print(" press anything else to exit")
  choice = input(">")
  if choice =="1":
    print("creating other bill")
    yearlyBills.createBill(db,"cartestingbill")
    reminder_input=input("Do you want to add a reminder: ")
    reminder_input.lower
    if reminder_input== "yes":
      monthlyBills.reminder(db, "pay_date_str")
    elif reminder_input == "no":
      print ("You won't be reminded for the paydate of this bill")
    
  elif choice=="2":
    bills = db.getObjectsFrom("yearlyBills",lambda x:x.btype=="cartestingbill" and x.name==username)
    for bill in bills:
      print(bill.toString())

def yearly_other(db,username):
  print("press 1 to create new other bill ")
  print("press 2 to see all bills ")
  print(" press anything else to exit")
  choice = input(">")
  if choice =="1":
    print("creating other bill")
    yearlyBills.createBill(db,"otherbill")
    reminder_input=input("Do you want to add a reminder: ")
    reminder_input.lower
    if reminder_input== "yes":
      monthlyBills.reminder(db, "pay_date_str")
    elif reminder_input == "no":
      print ("You won't be reminded for the paydate of this bill")
    
  elif choice=="2":
    bills = db.getObjectsFrom("yearlyBills",lambda x:x.btype=="otherbill" and x.name==username)
    for bill in bills:
      print(bill.toString())

def personal_budget_calculator():
  print(" Personal  Budget  Calculator ")
  print(" ")
  print("Fill in the required information below to calculate your savings. Note: this information won\'t be saved and is recommanded to be done in the end of each month. ")
  print(" ")
  print("Incomes: ")
  salary = int(input("Salary:  "))
  partenrs_salary = int(input("Partner\'s Salary:  "))
  public_assistance = int(input("Public Assistance: "))
  other = int(input("Other: "))
  total_income = salary+partenrs_salary+public_assistance+other
  print(" ")
  print(" ")
  print("Expenses: ")
  print(" ")
  print("Living/Housing: ")
  rent = int(input("Rent/Mortage: "))
  electricity = int(input("Electricity: "))
  water = int(input("Water: "))
  gas = int(input("Gas/Heating: "))
  telephone = int(input("Telephone: "))
  cable_TV = int(input("Cable TV: "))
  household_repairs = int(input("Household Repairs: "))
  food = int(input("Food: "))
  internet = int(input("Internet: "))
  other1 = int(input("Other: "))
  print(" ")
  print("Transportation: ")
  auto_expenses = int(input("Gas/Auto Expenses: "))
  vehicles  = int(input("Bus/Taxi/Plane etc: "))
  parking = int(input("Parking: "))
  other2 = int(input("Other: "))
  print(" ")
  print("Miscellaneous: ")
  gifts_charity = int(input("Gifts/Charity: "))
  education = int(input("Education: "))
  other3 = int(input("Other: "))
  total_expenses = rent+ electricity + water+ gas + telephone + cable_TV + household_repairs + food + internet + other1 + auto_expenses + vehicles + parking + other2 + gifts_charity + education + other3
  savings = total_income - total_expenses
  print(" ")
  print("Total Income: ", total_income, "Lekë")
  print("Total Expenses: ", total_expenses, "Lekë")
  print("Total savings:", savings, "Lekë")
  print(" ") 



# On start
print("Welcome to this bill organiser. Please register or login.")
print(" ")
print("Options: register | login | exit")

class User:
  def __init__(self,username,password):
    self.username = username
    self.password = password
  def toString(self):
    return str(self.username)+","+str(self.password)
  
  @classmethod
  def fromline(cls,line):
    tokens = line.split(",")
    return cls(tokens[0],tokens[1])

db.createtableifnotexists("users",User,User.fromline)
usrs = db.getObjectsFrom("users")
if len(usrs)==0:
  register(db)
while True:
    option = input("> ")
    if option == "login":
      login(db)
    elif option == "register":
      register(db)
    elif option == "exit":
      break
    else:
      print(option + " is not an option")



