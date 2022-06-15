# lib. used ************************************************************
import mysql.connector as mysql # used to communicate with mysql
import os # used to perform system functions
import time # used to give some delay in the program
import random as r # used to generate random numbers 
import csv # used to store data in a .csv file
# Functions 1 *************************************************************#
def OTP(): #----------> OTP generator 
 while True: 
  file=open('otp.txt','w') #-----------------------------------> opening a text file in write mode 
  otp=r.randint(100000,999999) #----------------------------------> genatating a 6 digit OTP using random 
  file.write('\nYour OTP sent by SBI bankserver is '+str(otp)) #---> writing the data and the OTP to the file opened
  file.write('\ndo not share the OTP') #------------------------> writing mode data 
  os.startfile('otp.txt') #-----------------------------------> opening the file that has been created using os module 
  file.close() #-----------------------------------------------> closing the text file opened 
  ask=input('give the OTP :- ') #----------------------------------> asking the OTP for validation 
  if ask==str(otp): #----------------------------------------------> checking if the OTP given is correct or not
    print('***** correct OTP ***** ') #--------------------------> printing the OTP is correct
    break #--------------------------------------------------> comming out of the loop
  else: 
    print('Wrong OTP...\n Try again...') #-----------------------> printing wrong OTP
    continue 
 
#
#
#
# Functions 2 *************************************************************#
def all_acc_no(): #---------> list off all acc no.
 list_acc_no=[] #-------------------------------------> creating empty list to store all account no.
 cursor.execute('select acc_no from account') #-----------> selecting all acc_no from the SQL server

 for i in cursor: #--------------> loop to extract data provided by SQL
  for j in i: #-------------------------> organising data to a variable
    list_acc_no.append(j) #--------------------> and adding it to the list created
 
  return list_acc_no #-----------------------------------> returning the list that contains all account number
 
#
#
#
# Functions 3 *************************************************************#
def create_acc(): #--------------> creating account
 while True:
  time.sleep(1) #-------------------> creating delay of 1 sec 
  print("\n\n\t CREATE ACCOUNT") #-------------------> printing create account 
  print(" -------------------------")
  print('\nGive the following details to create a new account :- \n') #-------> printing message to give the below details
 # taking some inputs from the user

  name=input("ENTER YOUR NAME :- ") #-----------------> asking name of the account holder 
  DOB=input("ENTER YOUR DATE OF BIRTH (YYYY/MM/DD) :- ") #----------> asking date of birth of user
  password=input("ENTER PASSWORD :- ") #---------------------> creating a new password for the account 
  confirm_pass=input("ENTER YOUR PASSWORD AGAIN :- ") #--------------> confirming the new password
 
  if confirm_pass==password: #------------------------------> checking if the password and confirm password are same
    list_acc_no=all_acc_no() #------------------- getting list of all account number in the data base
    while True:
      acc_no=str(r.randint(1000000000,1000000000000)) # generating acc no. using random module
      if acc_no in list_acc_no: #--------------------> if the generated accno is in the data base 
        continue #--------------------> then generating another accno untill it is unique
      else:
        break #----------------------->if the acc no is unique then exiting the loop
  else:

    print("RETRY!! \nPASSWORD and CONFIRM PASSWORD DON\'T MATCH ") #---->if password and conferm password dont match
    time.sleep(1) #----> creating a second delay
    continue #----------------------> and going back to top of create_acc function to retake correct data
 
  capital_amount=input("ENTER THE INITIAL AMOUNT IN ACCOUNT :- ") #------->asking the initial amount the account will open with
  email=input("ENTER YOUR EMAIL ADDRESS :- ") #--------------> asking email of the user
  phone=input("ENTER YOUR PHONE NUMBER :- ") #---------------> asking phone number of the user
  gender=input("ENTER YOUR GENDER(MALE/FEMALE) :- ") #----------------> asking gender of the user
  address=input("ENTER YOUR CURRENT ADDRESS :- ") #----------------> taking the address of the user to create an acc
  city=input("ENTER THE NAME OF YOUR CITY :- ") #--------------------> asking the city of the account holder
  state=input("ENTER NAME OF YOUR STATE :- ") #---------------------> asking the state in which the user live
  pin=input("ENTER PIN CODE OF YOUR AREA :- ") #------------------> asking pin code of the area
  acc_type=input("ENTER THE TYPE OF ACCOUNT(CURRENT OR SAVING) :- ") #----> initialising the account type
  id_proof=input('GIVE AADHAR NUMBER :- ') #---------------------> taking the id proof to finish creating account
 
 #converting all input to SQL commands
 
command='\''+acc_no+'\',\''+name+'\',\''+DOB+'\',\''+gender+'\',\''+phone+'\',\''+email+'\',\''+city+'\',\''+state+'\',\''+address+'\','+pin+',\''+password+'\',\''+acc_type+'\',\''+id_proof+'\','+capital_amount+',\'Beneficiary not enabled\''
 try: #------------------------------------> trying to execute some SQL Query
  cursor.execute('insert into account values('+command+')') #----> inserting the account details that have been created to data base
  time.sleep(1)
  print('\naccount created.....\n your account number is :-',acc_no,'\nThank you for creating account in our bank...') #--->printing account created and printing account number of the new account
  time.sleep(1)
 except: #---------------------------------------> if there is any error in data or while communicate with SQL
  print('***********************************************************')
  print('\nerror while creating account...\nTRY AGAIN \n') # printing error message
  ask=input('Do you want to try again?(Y/N) [default no] :- ')
  if ask =='y' or ask=='Y': #--------------------> asking choice to continue or exit the loop
    continue
  else:
    break
 
  break #-----------------------------> breaking theloop if the account is created 
 
#
#
#
# Functions 4 *************************************************************#
def deposit(): #--------------------> deposit money
 while True:
  time.sleep(1) 
  print("\n\n\t DEPOSIT MONEY") #----> printing deposit money 
  print(" -------------------------")
  print('\nGive the following details :- \n')
  # asking some details from the user
  acc_no=input('GIVE YOUR ACCOUNT NUMBER :- ') #--> asking account number to deposit money
  password=input("ENTER PASSWORD :- ") #---------> asking password to veryfy the user 
  amount=input('ENTER THE AMOUNT YOU WANT TO DEPOSIT :- ') 
  # taking the amount to be deposited

  list_acc_no=all_acc_no() #------------------- getting list of all account number in the data base
 if acc_no in list_acc_no: #------------>checking if the account existes 
or not
 cursor.execute('select password from account where 
acc_no='+acc_no) #exetuting sql commant to get the password of the 
account
 for i in cursor: #---------------> extracting the password
 for j in i: 
 p=j #------------> organising the password to a variable 
 if p == password: # ----------------> checking if the given password 
matches the account password
 command='update account set amount=amount+'+amount+' 
where acc_no='+acc_no #----->creating command to be executed in SQL 
to update the amount 
 try: # trying to execute the command
 cursor.execute(command) #-------------> executing the 
command in the SQL
 time.sleep(1)
 print('\nAmount deposited ....') #------------> printing amount 
deposited if it is sucessfull
 time.sleep(1)
 break
 except: # -----------------> if any error while updating the amount 

 print('error :- failed to deposit .....\ntry again.....') # printing error 
and asking to try again
 time.sleep(2)
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue
 else:
 break
 
 else:
 print('wrong password...\n try again \n') # ----------> if the 
password is wrong printing wronge password
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue
 else:
 break
 else:
 print('this account does not exist... \ntry again...\n\n') #-------> 
printing acc dont exist if the account number is not found 
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to continue 
or exit the loop

 continue
 else:
 break
 
#
#
#
# Functions 5 *************************************************************#
def withdraw(): #---------------------> withdraw money
 while True:
 time.sleep(1) 
 print("\n\n\t WITHDRAW MONEY") #----------> printing withdraw 
money 
 print(" -------------------------")
 print('\nGive the following details :- \n')
 # asking some details from the user
 acc_no=input('GIVE YOUR ACCOUNT NUMBER :- ') #--> asking 
account number to deposit money
 password=input("ENTER PASSWORD :- ") #---------> asking 
password to veryfy the user 
 amount=input('ENTER THE AMOUNT YOU WANT TO WITHDRAW :-
') # taking the amount to be withdrawed
 list_acc_no=all_acc_no() #------------------- getting list of all account 
number in the data base

 if acc_no in list_acc_no: #------------>checking if the account existes 
or not
 cursor.execute('select password from account where 
acc_no='+acc_no) #exetuting sql commant to get the password of the 
account
 for i in cursor: #---------------> extracting the password
 for j in i: 
 p=j #------------> organising the password to a variable 
 if p == password: # ----------------> checking if the given password 
matches the account password
 command='update account set amount=amount-'+amount+' 
where acc_no='+acc_no #----->creating command to be executed in SQL 
to update the amount 
 try: # trying to execute the command
 cursor.execute(command) #-------------> executing the 
command in the SQL
 time.sleep(1)
 print('\nAmount withdrawed ....') #------------> printing amount 
withdrawed if it is sucessfull
 time.sleep(1)
 break
 except: # -----------------> if any error while updating the amount 
 print('error :- failed to withdraw .....\ntry again.....') # printing 
error and asking to try again
 time.sleep(2)

 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue
 else:
 break
 else:
 print('wrong password...\n try again \n') # ----------> if the 
password is wrong printing wronge password
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue
 else:
 break
 else:
 print('this account does not exist... \ntry again...\n\n') #-------> 
printing acc dont exist if the account number is not found 
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to continue 
or exit the loop
 continue
 else:
 break
 

#
#
#
# Functions 6 *************************************************************#
def change_passwd(): #------------ change password
 while True:
 time.sleep(1) 
 print("\n\n\t CHANGE PASSWORD") #---------->printing change 
password 
 print(" -------------------------")
 print('\nGive the following details to change the password :- \n')
 # asking some details from the user
 acc_no=input('ENTER THE ACCOUNT NUMBER :- ') #-------------> 
asking account number 
 old_pass=input("ENTER THE OLD PASSWORD :- ") #-------------> 
asking old password
 new_pass=input("ENTER NEW PASSWORD :- ") #-------------> 
asking to create new password
 confirm_pass=input("CONFIRM NEW PASSWORD :- ") #-------------> 
asking to confirm new password
 list_acc_no=all_acc_no() #------------------- getting list of all account 
number in the data base
 if acc_no in list_acc_no: #------------>checking if the account existes 
or not

 cursor.execute('select password from account where 
acc_no='+acc_no) #exetuting sql commant to get the password of the 
account
 for i in cursor: #---------------> extracting the password
 for j in i: 
 p=j #------------> organising the password to a variable 
 if p == old_pass: # checking if the given old password is correct or 
not
 if new_pass==confirm_pass: # checking if the new password 
and its conformation match or not
 OTP() #--------------------> calling OTP function to 
verify otp 
 command='update account set password='+new_pass+' where 
acc_no='+acc_no #------> creating command to the old password of the 
account to the new password
 try: # trying to execute the command
 cursor.execute(command) #-------------> executing the 
command in the SQL
 time.sleep(1)
 print('\nPassword changed ....') #------> printing password 
changed if it is sucessfull
 time.sleep(1)
 break
 except: # -----------------> if any error while updating the 
password

 print('error :- failed to change password .....\nTRY 
AGAIN.....') # printing failed to change password
 time.sleep(2)
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue
 else:
 break 
 else: # if new password and confirm password do not match
 print("new password and confirm password do not match ...\n 
TRY AGAIN") #printing new password and confirm password do not match
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue
 else:
 break
 else: #-----------------------> if entered wrong password 
 print('ACCESS DENIED !!! \nYou entered wrong password...\n 
TRY AGAIN') #--------> printing ACCESS DENIED
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue

 else:
 break
 else:
 print('The account number you entered does not exist...\n TRY 
AGAIN')#-------> printing acc dont exist if the account number is not found 
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue
 else:
 break
 
#
#
#
# Functions 7 *************************************************************#
def fund_trans(): #------------------- fund transfer
 while True:
 time.sleep(1) 
 print("\n\n\t FUND TRANSFER") #----- printing fund 
transfer 
 print(" -------------------------")
 print('\nGive the following details to send money :- \n')
 # asking some details from the user

 f_acc_no=input('ENTER SENDER\'S ACCOUNT NUMBER :- ') #------
asking senders acc no
 password=input("ENTER PASSWORD :- ") #------------ asking 
password of the account
 t_acc_no=input('ENTER RECIVER\'S ACCOUNT NUMBER :- ') #------
asking recivers acc no
 amount=input('ENTER THE AMOUNT YOU WANT TO TRANSFER :-
') #---- asking amount to be transfer
 list_acc_no=all_acc_no() #------------------- getting list of all account 
number in the data base
 if f_acc_no in list_acc_no: #----------------- checking if the senders 
account existes or not
 cursor.execute('select password from account where 
acc_no='+f_acc_no) ##exetuting sql commant to get the password of the 
account
 for i in cursor: #---------------> extracting the password
 for j in i: 
 p=j #------------> organising the password to a variable 
 if p == password: # ------checking if the given password is correct 
or not
 if t_acc_no in list_acc_no: #----------------- checking if the recivers
account existes or not
 OTP() #--------------------> calling OTP function to 
verify otp 
 #creating commands to execute in SQL for fund transfer

 fcommand='update account set amount=amount-'+amount+' 
where acc_no='+f_acc_no
 tcommand='update account set amount=amount+'+amount+' 
where acc_no='+t_acc_no
 try: # trying to execute the command
 cursor.execute(fcommand) # executing command to the 
SQL
 cursor.execute(tcommand)
 time.sleep(1)
 print('\nTRANSFER COMPLETE !!! ....') # printing transfer 
complete if sucessfull
 time.sleep(1)
 break
 except: # if any error occure while transfering
 print('error :- failed to transfer money .....\nTRY AGAIN.....') 
# printing failed to transfer money
 time.sleep(2)
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue
 else:
 break 
 
 break

 else: #-----------------if the recivers account do not existes
 print('The recivers account number does not exist !!\n TRY 
AGAIN') #printing recivers account number does not exist
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue
 else:
 break 
 else: # if the given password is not correct
 print('wrong password...\n try again \n') # printing wrong 
password 
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue
 else:
 break 
 else: #----------------- if the senders account do not existes
 print('Senders account does not exist... \ntry again...\n\n') # 
printing Senders account does not exist
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to continue 
or exit the loop
 continue

 else:
 break 
#
#
#
# Functions 8 *************************************************************#
def create_Virtual_acc(): # ----------------- create Virtual account
 while True:
 time.sleep(1) 
 print("\n\n\t CREATE VIRTUAL ACCOUNT") # printing CREATE 
VIRTUAL ACCOUNT 
 print(" ---------------------------------")
 print('\nGive the following details to create virtual account :- \n')
 # asking some details from the user
 acc_no=input('GIVE YOUR ACCOUNT NUMBER :- ') #--> asking 
account number to create virtual account
 password=input("ENTER PASSWORD :- ") #---------> asking 
password to veryfy the user 
 user_name=input('GIVE A USER NAME FOR YOUR VIRTUAL 
ACCOUNT :- ') #-------> asking to create a user name for the virtual 
account
 passwd=input('ENTER PASSWORD FOR YOUR VIRTUAL 
ACCOUNT :- ') #-------> asking to create a password for the virtual 
account

 confirm_pass=input('CONFIRM PASSWORD FOR YOUR VIRTUAL 
ACCOUNT :- ') #-------> asking to confirm the password for the virtual 
account
 
 list_acc_no=all_acc_no() #------------------- getting list of all account 
number in the data base
 if acc_no in list_acc_no: #------------>checking if the account existes 
or not
 cursor.execute('select password from account where 
acc_no='+acc_no) #exetuting sql commant to get the password of the 
account
 for i in cursor: #---------------> extracting the password
 for j in i: 
 p=j #------------> organising the password to a variable 
 if p == password: # ----------------> checking if the given password 
matches the account password
 if passwd==confirm_pass: # ----------------> checking if the given 
virtual account password matches the confirm password
 OTP() #--------------------> calling OTP function to verify 
otp 
 # creating a command to insert the data to the virtual table
 command='insert into virtual_account 
values(\''+acc_no+'\',\''+user_name+'\',\''+passwd+'\')'
 try: # trying to execute the command

 cursor.execute(command) #executing the command in the 
SQL
 time.sleep(1)
 print('\nVIRTUAL ACCOUNT CREATED ....') #--------> 
printing virtual account created on sucess
 time.sleep(1)
 break
 except: # if any error while adding virtual account
 print('error :- failed to create virtual account .....\nTRY 
DIFFERENT USER NAME\nTRY AGAIN.....')
 time.sleep(2)
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue
 else:
 break 
 else: # if user password and confirm password do not match
 print("user password and confirm password do not match ...\n 
TRY AGAIN") # printing user password and confirm password do not match
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue
 else:

 break 
 else: # if if the given password do not match the account password
 print('ACCESS DENIED !!! \nYou entered wrong password...\n 
TRY AGAIN') # printing access denied
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue
 else:
 break 
 else: #if the account do not existes
 print('this account does not exist... \ntry again...\n\n') # printing 
account does not exist
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to continue 
or exit the loop
 continue
 else:
 break 
 
#
#
#
# Functions 9 *************************************************************#

def login_Virtual_acc(): #------------------ login Virtual account
 while True:
 time.sleep(1) 
 print("\n\n\t LOGIN TO VIRTUAL ACCOUNT") # printing LOGIN TO 
VIRTUAL ACCOUNT 
 print(" ---------------------------------")
 print('\nGive the following details to login to virtual account :- \n')
 # asking some details from the user
 user_name=input('GIVE USER NAME :- ') # asking the user name of 
the virtual account
 password=input("ENTER PASSWORD OF VIRTUAL ACCOUNT :- ") 
# asking the password of the virtual account
 list_user_name=[] # -----------------------> creating an empty list to store 
all user name
 cursor.execute('select user_name from virtual_account') # executing 
SQL command to get all user name from virtual account
 for i in cursor: #--------------> loop to extract data 
provided by SQL
 for j in i: #-------------------------> organising data to a 
variable
 list_user_name.append(j) #--------------------> and adding it 
to the list created
 if user_name in list_user_name: #------------>checking if the user 
existes or not

 cursor.execute('select password from virtual_account where 
user_name=\''+user_name+'\'') #exetuting sql commant to get the 
password of the user
 for i in cursor: #---------------> extracting the password
 for j in i: 
 p=j #------------> organising the password to a variable 
 if p == password: # ----------------> checking if the given password 
matches the account password
 print('LOGIN SUCESSFULL .....\n') # printing login sucessfull
 print('Below are some details of your account :-\n')
 cursor.execute('select acc_no from virtual_account where 
user_name=\''+user_name+'\'') # getting account number of the user who 
loged in
 for i in cursor: #--------------> loop to extract data provided 
by SQL
 for j in i: #-------------------------> organising data to a 
variabl
 acc_no=j #------------------- getting the needed data
 
 # getting some information of the account linked to the user
 cursor.execute('select 
acc_no,name,DOB,gender,phone,email,city,state,address,pin_code,acc_ty
pe,beneficiary,amount from account where acc_no='+acc_no)
 # creating heder to display on screen

 heder=['ACCOUNT NUMBER','NAME ','DOB 
','GENDER ','PHONE NUMBER ','EMAIL ','CITY ','STATE 
','ADDRESS ','PIN CODE ','ACCOUNT TYPE ','BENEFICIARY 
','AMOUNT ']
 data=cursor.fetchone() # fetching data one by one
 temp=0 # creating a temperary variable
 for i in data: # loop to print data in a organised way
 print(heder[temp],' :- ',i) # printing data with the heder
 temp+=1 # changing the temperary variable
 time.sleep(2)
 break
 else: #if the given password do not matches the account password
 print('ACCESS DENIED !!! \nYou entered wrong password...\n 
TRY AGAIN') # printing ACCESS DENIED
 ask=input('Do you want to try again?(Y/N) [default no] :- ')
 if ask =='y' or ask=='Y': #--------------------> asking choice to 
continue or exit the loop
 continue
 else:
 break 
 else: # if the user do not existes
 print('this user does not exist... \ntry again...\n\n') # printing user 
does not exist
 ask=input('Do you want to try again?(Y/N) [default no] :- ')

 if ask =='y' or ask=='Y': #--------------------> asking choice to continue 
or exit the loop
 continue
 else:
 break 
 
 
#
#
#
# Functions 10 ************************************************************#
def super_user(): #--------------------- all details of all accounts
 time.sleep(1) 
 print("\n\n\t ALL DETAILS OF ALL ACCOUNT (SUPER USER)") # ----
printing ALL DETAILS OF ALL ACCOUNT 
 print(" --------------------------------------------------")
 print('\nGive the following details :- \n')
 # asking some details from the user
 password=input('GIVE SUPER USER PASSWORD :- ') # asking the 
super user password
 if password != supass: # if the entered password is wrong
 print('\nACCESS DENIED !!! \nYou entered wrong password...\n') 
#printing ACCESS DENIED
 time.sleep(2)

 else: # if the entered password is correct
 print('PERMITION GRANTED ......') # printing PERMITION GRANTED
 time.sleep(2)
 # printing all data for super user
 print('\nloading all the details of all the accounts in the bank servr 
database :- \n\n LOADING .....')
 
 #saving all data in csv file
 csvfile=open('all data.csv','w') # opening a CSV file in write mode to 
write data
 # creating header for the csv file
 header=['ACCOUNT 
NUMBER','NAME','DOB','GENDER','PHONE','EMAIL','CITY','STATE','ADD
RESS','PIN CODE','PASSWORD','ACCOUNT TYPE','AADHAR 
NUMBER','AMOUNT','BENEFICIARY']
 W=csv.writer(csvfile,delimiter=',') #---------------> creating a writer to 
write all data to the CSV file opened
 W.writerow(header) # ----------------- writing the header to the csv file
 record=[] # ------------------ creating an empty list to store all records
 cursor.execute('select * from account') #-----------> getting all data 
from the bankserver for the super user
 data = cursor.fetchall() # ------> fetching all data from the cursor
 for i in data: #------> loop to extract data
 for j in i: #----------> organising data to a variable
 record.append(' '+str(j)+' ') # adding data to the list created

 W.writerow(record) # --------> writing the data to the CSV file 
opened
 record=[] # making the list empty to store next set of data
 csvfile.close() #------------> closing the opened CSV file 
 os.startfile('all data.csv') #---------------------------------> using os module 
to start the CSV file that was created
 
#
#
#
# Functions 11 ************************************************************#
def beneficiary(): #--------------------- adding beneficiary
 time.sleep(1) 
 print("\n\n\t ADD OR REMOVE BENEFICIARY TO YOUR ACCOUNT") 
#---------------> printing ADD OR REMOVE BENEFICIARY 
 print(" ---------------------------------------------------")
 print('\nGive the following details to add beneficiary to your account :-
\n')
 # asking some details from the user
 acc_no=input('GIVE YOUR ACCOUNT NUMBER :- ') #--> asking 
account number to add beneficiary
 password=input("ENTER PASSWORD :- ") #--------------> confirming the 
account by asking password

 list_acc_no=all_acc_no() #------------------- getting list of all account 
number in the data base
 if acc_no in list_acc_no: #------------>checking if the account existes or 
not
 cursor.execute('select password from account where 
acc_no='+acc_no) #exetuting sql commant to get the password of the 
account
 for i in cursor: #---------------> extracting the password
 for j in i: 
 p=j #------------> organising the password to a variable 
 if p == password: # ----------------> checking if the given password 
matches the account password
 cursor.execute('select beneficiary from account where 
acc_no='+acc_no) # -------> geting beneficiary details of this account from 
the database
 for i in cursor: #-------------- loop to get beneficiary details
 for j in i:
 q=j #-------------> storing the retrived details in a 
variable
 if q =='Beneficiary not enabled': #--------->checking is beneficiary is 
enabled or nor
 ask=input('Do you want to enable beneficiary ? (y/n) :- ') #-----> 
asking choice to enable 
 if ask =='y' or ask=='Y':

 trust=input('GIVE THE NAME OF THE PERSON ,TO WHOM 
YOU \nWANT THIS ACCOUNT TO GO AFTER YOUR DEATH ? :- ') #---
--> asking name of the person in trust of beneficiary 
 command='update account set beneficiary=\'IN TRUST OF 
'+trust+'\''+' where acc_no='+acc_no # ---------> command to add 
beneficiary in trust of the provided name
 cursor.execute(command) # executing the command in the 
SQL
 print('\nBeneficiary added in name of ',trust,' !! .....') #-----> 
printing beneficiary added after adding
 time.sleep(2)
 else: # canceling the process if the user dont want to add 
beneficiary
 print('\nCANCELING REQUEST ....')
 time.sleep(2)
 else: #--------> if the beneficiary is already enabled 
 print('\n\nBENEFICIARF is',q)
 ask=input('Do you want to Remove beneficiary ? (y/n) :- ') # 
asking choice to remove beneficiary
 if ask =='y' or ask=='Y':
 command='update account set beneficiary=\'Beneficiary not 
enabled\' where acc_no='+acc_no # command to remove the beneficiary 
from this account
 cursor.execute(command) #--------> executing the command 
in the SQL

 print('Beneficiary REMOVED !! ......') #--------> printing 
beneficiary removed after removing
 time.sleep(2)
 else: # canceling the process if the user dont want to remove 
beneficiary
 print('\nCANCELING REQUEST ....')
 time.sleep(2)
 
 else: # if the given password dont match the account password
 print('\nwrong password...\n') # printing wrong password
 time.sleep(2)
 else: # if the account do not existes
 print('\nthis account does not exist... \n') # printing account does not 
exist
 time.sleep(2)
# body *****************************************************************
# connecting to SQL
while True:
 print('Give the below details to connect to SQL server')
 # asking the below details to connect to the SQL server
 host=input('give host name of SQL server :- ') #----------------------> 
asking host name of the SQL server

 user=input('which user :- ') #--------------------------------------> asking user 
of the hostr of the SQL server
 passwd=input('what is the password :- ') #------------------------> asking 
the password of the SQL to login to SQL server
 try: # trying to connect with SQL server with the given details
 mydb=mysql.connect(host=host,user=user,passwd=passwd) # 
connecting with the MySQL
 print('\n...... SQL connected ......\n') #------ printing connected if 
sucessfully connected
 time.sleep(1)
 break
 except: # if error while connection with SQL server
 print('***********************************************************')
 print('\nerror while communicating with SQL server...\nTRY AGAIN \n') 
#---- printing error while communicating 
cursor=mydb.cursor() #creating cursor to execute SQL query
#checking and using bankserver
try: 
 cursor.execute('use bankserver') # selecting bankserver as the data 
base
 print('database changed to bankserver') # printing database changed 
# creating bankserver ,if bankserver not available
except:

 print('bankserver database not found...') #-----------> printing bankserver 
not found 
 time.sleep(1)
 print('creating database.......') 
 cursor.execute('create database bankserver') # -----------------> creating 
bankserver database for the program 
 cursor.execute('use bankserver') # ---------------> using bankserver after 
creating 
 # creating account table to store all the account details of all accounts
 cursor.execute('create table account (acc_no varchar(12) primary key 
not null,name varchar(50) not null,DOB date not null,gender 
varchar(10),phone varchar(10) not null,email varchar(50),city varchar(30) 
not null,state varchar(30) not null,address varchar(100) not null,pin_code 
int(10) not null,password varchar(50) not null,acc_type 
varchar(10),ID_proof varchar(20) not null,amount int(50) not 
null,beneficiary varchar(50) default \'Beneficiary not enabled\');')
 # creating virtual account to store the details of some account applied for 
virtual account
 cursor.execute('create table virtual_account (acc_no varchar(12) not 
null,user_name varchar(50) primary key not null,password varchar(50) not 
null);')
 time.sleep(1)
 print('bankserver database created') # printing bankserver database 
created after creating

# ***************** WELCOME *****************
print('\n\n********** WELCOME TO SBI **********')
time.sleep(2)
# asking which task to perform
while True:
 print('which task do you want to perform ?')
 # creating menu for the user to chose from
 # it contains all option available to the user
 print('''
+------------------------------------+ 
| 1) Create account | 
| 2) Change Password |
| 3) Withdraw Money | Select any One
| 4) Deposit Money | option
| 5) Fund Transfer | that you want 
| 6) Create Virtual Account | to perform
| 7) Login to Virtual Account |
| 8) Manage Beneficiary |
| 9) All details of ALL Account |
|10) Quit |
+------------------------------------+ 
 ''')
 opp=['1','2','3','4','5','6','7','8','9','10'] # creating a list to validate the option 
number
 supass='full_acc_su_password' # creating a super user password

 choice=input('give option number :- ') # asking the user for a option from 
the menu
 if choice not in opp:
 print('give vallid option number') #---------> printing invalid option 
number for any invalid option entered
 continue
 if choice=='1': # for the option 1 
 create_acc() # calling create_acc function to perform the task
 
 elif choice=='2': # for the option 2
 change_passwd() # calling change_passwd function to perform the 
task
 elif choice=='3': # for the option 3
 withdraw() # calling withdraw function to perform the task
 
 elif choice=='4': # for the option 4
 deposit() # calling deposit function to perform the task # calling 
create_acc function to perform the task
 
 elif choice=='5': # for the option 5
 fund_trans() # calling fund_trans function to perform the task
 
 elif choice=='6': # for the option 6

 create_Virtual_acc() # calling create_Virtual_acc function to perform 
the task
 
 elif choice=='7': # for the option 7
 login_Virtual_acc() # calling login_Virtual_acc function to perform the 
task
 
 elif choice=='8': # for the option 8
 beneficiary() # calling beneficiary function to perform the task
 
 elif choice=='9': # for the option 9
 super_user() # calling super_user function to perform the task
 
 elif choice=='10': # for the option 10
 print('\n*********** Thank You ***********')
 mydb.commit() # saving all changes made to the database 
 break
 mydb.commit() # saving all changes made to the database 
 print('\n***********************************************************\n')
