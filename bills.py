import time
from datetime import datetime, timedelta

class monthlyBills():
  def __init__(self,billID,payvalue, name, company, address,btype):
    self._ID = billID
    #self._paydate = int(input("Add date: "))
    self._payvalue = payvalue
    self.name= name
    self.company= company
    #self.paymentstatus= paymentstat
    #self.reminder=reminder
    self.address=address

    self.btype = btype# water  electricity tax #
  @staticmethod
  def createBill(db,btype):
    print("Enter bill ID, payvalue, name, company, address ")
    class_input = str(input())
    class1 = class_input.split(",")
    #list
    class2 = monthlyBills(class1[0],class1[1], class1[2],class1[3], class1[4],btype)
    db.appendObjectInto("monthlyBills",class2)



  def toString(self):
    return str(self._ID)+","+str(self._payvalue)+","+str(self.name)+","+str(self.company)+","+ str(self.address)+","+str(self.btype)
  @classmethod
  def fromline(cls,line):
    tokens = line.split(",") 
    return cls(tokens[0],tokens[1], tokens[2], tokens[3], tokens[4],tokens[5])
  
  def reminder(self, pay_date_str):
    now = datetime.now()
    print(now)

    pay_date_str=str(input("Enter due date:"))
    self.pay_date_str= pay_date_str
    pay_date_obj = datetime.fromisoformat(pay_date_str)
    #print(pay_date_obj)


    delta = now-pay_date_obj
    days = delta.days
    seconds = delta.seconds

    #print(days)
    #print(seconds)
    time.sleep(seconds)
    print("You need to pay this bill by ", pay_date_str, ".")
    



class telephoneBills(monthlyBills):
  pass
class waterBills(monthlyBills):
  pass
class electricityBills(monthlyBills):
  pass
class medicalCheckups(monthlyBills):
  pass
class houseTax(monthlyBills):
  pass
class monthlyOthers(monthlyBills):
  pass


class yearlyBills():
  def __init__(self,billID,payvalue, name, company, address,btype):
    self._ID = billID
    #self._paydate = int(input("Add date: "))
    self._payvalue = payvalue
    self.name= name
    self.company= company
    #self.paymentstatus= paymentstat
    #self.reminder=reminder
    self.address=address

    self.btype = btype# water  electricity tax #
  @staticmethod
  def createBill(db,btype):
    print("Enter bill ID, payvalue, name, company, address ")
    class_input = str(input())
    class1 = class_input.split(",")
    #list
    class2 = yearlyBills(class1[0],class1[1], class1[2],class1[3], class1[4],btype)
    db.appendObjectInto("yearlyBills",class2)



  def toString(self):
    return str(self._ID)+","+str(self._payvalue)+","+str(self.name)+","+str(self.company)+","+ str(self.address)+","+str(self.btype)
  @classmethod
  def fromline(cls,line):
    tokens = line.split(",") 
    return cls(tokens[0],tokens[1], tokens[2], tokens[3], tokens[4],tokens[5])
    
  def reminder(self, pay_date_str):
    now = datetime.now()
    print(now)

    pay_date_str=str(input("Enter due date:"))
    self.pay_date_str= pay_date_str
    pay_date_obj = datetime.fromisoformat(pay_date_str)
    #print(pay_date_obj)


    delta = now-pay_date_obj
    days = delta.days
    seconds = delta.seconds

    #print(days)
    #print(seconds)
    time.sleep(seconds)
    print("You need to pay this bill by ", pay_date_str, ".")
     

class schoolfeeBills(yearlyBills):
  pass
class coursesBills(yearlyBills):
  pass
class insuranceBills(yearlyBills):
  pass
class planeBills(yearlyBills):
  pass
class accommodation(yearlyBills):
  pass
class transportation(yearlyBills):
  pass
class carTesting(yearlyBills):
  pass
class yearlyOthers(yearlyBills):
  pass




