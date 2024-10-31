import mysql.connector
from tabulate import tabulate
import time
import requests
import os

# -------------------Configs------------------------------------

#--------------------MySQL--------------------------------------

mydb = mysql.connector.connect(
    host="localhost",
    user="pythonRead",
    password="python",
    database="transistors"
)
cursor = mydb.cursor()

newdatabase = mysql.connector.connect(
    host="localhost",
    user="pythonWrite",
    password="python",
    database="newtransistors"
)
editCurs = newdatabase.cursor()

#--------------------/MySQL---------------------------------------

#--------------------Pastebin-------------------------------------

key='YourAPIKEY'

login_data={
    'api_dev_key':key,
    'api_user_name':'YourUsername',
    'api_user_password':'YourPassword'
    }
#---------------------/Pastebin-----------------------------------

# ----------------------/Configs-----------------------------------


# -------------------------Functions---------------------------------------

def menu():
    print('1 : Find Information About a certain Transistor')
    time.sleep(0.25)
    print('2 : Find Equivalent Transistor')
    time.sleep(0.25)
    print('3 : Add a New Transistor')
    time.sleep(0.25)
    print('4 : Exit')
    print()
    time.sleep(1)
    reply = str(input('Enter Required Option : '))
    if reply == '1':
        print()
        info()
    elif reply == '2':
        print()
        equivalent()
    elif reply == '3':
        print()
        newTrans()
    elif reply == '4':
        pass
    else:
        print()
        print('Sorry, Invalid Input. Please Try again')
        print()
        menu()


def determ(sNo):
    val = '%' + sNo + '%'
    var = (val,)
    command = "select ID, TransID from bjt where TransID like %s"
    cursor.execute(command, var)
    res = cursor.fetchall()
    if len(res) == 0:
        return 0
    elif len(res) == 1:
        return res[0]
    else:
        table = tabulate(res, headers=['ID', 'Serial No.'], tablefmt='orgtbl')
        print(table)
        try:
            opt = int(input('Enter the corresponding ID of Transistor : '))
            return opt
        except:
            print('Incorrect input, please try again')
            determ(sNo)


def final():
    reply = str(input('Would you like to perform any other function? (Yes/No) : '))
    reply = reply.upper()
    if reply == 'YES':
        menu()
    elif reply == 'NO':
        print('Thank You')
        print('Goodbye!')
        exit()
    else:
        print('Incorrect Input, Try again.')
        final()


def info():
    serialNo = str(input('Enter Serial Number of Transistor : '))
    val = (determ(serialNo))
    if val != 0:
        var = (val,)
        command = "select * from bjt where ID = %s"
        cursor.execute(command, var)
        res = cursor.fetchall()
        table = tabulate(res,
                         headers=['ID', 'Serial No.', 'Material', 'Structure', 'Pc', 'Vcb', 'Vec', 'Ic', 'Temp',
                                  'Ft', 'Cc', 'Hfe', 'Package'], tablefmt='orgtbl')
        print()
        print('Information about the', res[0][1], 'Transistor')
        print()
        print(table)
        print()
        txt('info', val, table)
        print()
        final()
    else:
        print('No transistor found.')
        print()
        che = check()
        if che:
            info()
        else:
            final()


def equivalent():
    serialNo = str(input('Enter Serial Number of Transistor : '))
    serialNo.upper()
    val = determ(serialNo)
    var = (val,)
    command = "select * from bjt where ID = %s"
    cursor.execute(command, var)
    tempRes = cursor.fetchall()
    ID, SerialNo, Material, Structure, Pc, Vcb, Vec, Ic, Temp, Ft, Cc, Hfe, Package = tempRes[0][0], tempRes[0][1], tempRes[0][2], tempRes[0][3], tempRes[0][4], tempRes[0][5], tempRes[0][6], tempRes[0][7], tempRes[0][8], tempRes[0][9], tempRes[0][10], tempRes[0][11], tempRes[0][12]
    command = "select * from bjt where Material = %s and Structure = %s and Pc >= %s and Vcb >= %s and Vce >= %s and Ic >= %s and Temp >= %s and Ft >= %s and Cc <= %s and Hfe >= %s"
    items = (Material, Structure, Pc, Vcb, Vec, Ic, Temp, Ft, Cc, Hfe)
    cursor.execute(command, items)
    res = cursor.fetchall()
    if len(res) != 0:
        table = tabulate(res,headers=['ID', 'Serial No.', 'Material', 'Structure', 'Pc', 'Vcb', 'Vec', 'Ic', 'Temp','Ft', 'Cc', 'Hfe', 'Package'], tablefmt='orgtbl')
        print('Equivalent Transistors and their Information')
        print()
        print(table)
        print()
        txt('equ', val, table)
        print()
        final()
    else:
        print('Sorry, No Equivalent transistors in the Database')
        print()
        che = check()
        if che:
            equivalent()
        else:
            final()


# -------------Input Functions-------------
def transID():
    a = str(input('Enter Serial No. of transistor: '))
    if len(a) > 14:
        print('Serial No of transistor is too long, Please try again')
        transID()
    else:
        return a


def material():
    a = str(input('Enter Material of transistor (Si/Ge) : '))
    if len(a) > 3:
        print('Material of transistor is too long, Please try again')
        material()
    else:
        return a


def structure():
    a = str(input('Enter Structure of transistor (PNP/NPN) : '))
    if len(a) > 3:
        print('Structure of transistor is too long, Please try again')
        structure()
    else:
        return a


def pc():
    a = str(input('Enter Maximum Power Capacity of transistor (Numeric) : '))
    try:
        float(a)
        b = float(a)
        return b
    except:
        print('Input was not a numeric value, Please try again')
        pc()


def vcb():
    a = str(input('Enter Maximum collector-base voltage of transistor (Integer) : '))
    try:
        int(a)
        b = int(a)
        return b
    except:
        print('Input was not a Integer value, Please try again')
        vcb()


def vce():
    a = str(input('Enter Maximum collector-emitter voltage of transistor (Integer) : '))
    try:
        int(a)
        b = int(a)
        return b
    except:
        print('Input was not a Integer value, Please try again')
        vce()


def ic():
    a = str(input('Enter Maximum collector current of transistor (Numeric) : '))
    try:
        float(a)
        b = float(a)
        return b
    except:
        print('Input was not a numeric value, Please try again')
        ic()


def temp():
    a = str(input('Enter Maximum Temperature of transistor (Integer) : '))
    try:
        int(a)
        b = int(a)
        return b
    except:
        print('Input was not a integer value, Please try again')
        temp()


def ft():
    a = str(input('Enter Frequency of the current transfer coefficient of transistor (Numeric) : '))
    try:
        float(a)
        b = float(a)
        return b
    except:
        print('Input was not a numeric value, Please try again')
        ft()


def cc():
    a = str(input('Enter Collector junction capacity of transistor (Numeric) : '))
    try:
        float(a)
        b = float(a)
        return b
    except:
        print('Input was not a numeric value, Please try again')
        cc()


def hfe():
    a = str(input('Enter Static current transfer coefficient of transistor (Numeric) : '))
    try:
        float(a)
        b = float(a)
        return b
    except:
        print('Input was not a numeric value, Please try again')
        hfe()


def package():
    a = str(input('Enter Package Name of transistor: '))
    if len(a) > 29:
        print('Package Name of transistor is too long, Please try again')
        package()
    else:
        return a


# ------------/Input Functions--------------

def newTrans():
    print()
    print('Welcome to the Transistor appending Function')
    print('Any Transistor that is added will be added to the Database only after confirmation of inputted Properties')
    print('If any information is unknown skip the parameter during input')
    editCurs.execute("SELECT ID FROM newbjt ORDER BY ID DESC LIMIT 1")
    results = editCurs.fetchone()
    Id = results[0]
    ID = Id + 1
    TransID = transID()
    Material = material()
    Structure = structure()
    Pc = pc()
    Vcb = vcb()
    Vce = vce()
    Ic = ic()
    Temp = temp()
    Ft = ft()
    Cc = cc()
    Hfe = hfe()
    Package = package()
    editCurs.execute("Select TransID from newbjt")
    tup = editCurs.fetchall()
    if TransID in tup:
        print('Transistor already recommended for addition.')
        che = check()
        if che:
            newTrans()
        else:
            final()
    else:
        val = (ID, TransID, Material, Structure, Pc, Vcb, Vce, Ic, Temp, Ft, Cc, Hfe, Package)
        res = [val, ]
        table = tabulate(res,
                         headers=['ID', 'Serial No.', 'Material', 'Structure', 'Pc', 'Vcb', 'Vec', 'Ic', 'Temp',
                                  'Ft', 'Cc', 'Hfe', 'Package'], tablefmt='orgtbl')
        print(table)
        print('Please confirm all details entered')
        while True:
            conf = str(input('Confirm and add to database? Yes/No : '))
            con = conf.upper()
            if con == 'YES':
                command = "INSERT INTO newbjt(ID, TransID, Material, Structure, Pc, Vcb, Vce, Ic, Temp, Ft, Cc, Hfe, Package) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                editCurs.execute(command, val)
                newdatabase.commit()
                print('Transistor Successfully added for review')
                break
            elif con == 'NO':
                break
            else:
                print('Incorrect Input, please try again')
        che = check()
        if che:
            newTrans()
        else:
            final()


def check():
    che = input('Would you like to try again? Yes/No : ')
    che = che.upper()
    if che == 'YES':
        return True
    elif che == 'NO':
        return False
    else:
        print('Incorrect Input, please enter again')
        check()

def txt(type,ref,out):
    q=input('Would you like a text document of the output for future reference? (Yes/No) : ')
    q=q.upper()
    var=(ref,)
    command = 'select TransID from bjt where ID = %s'
    cursor.execute(command,var)
    res=cursor.fetchall()
    if q=='YES' or q=='Y':
        if type=='info':
            file=open('text.txt','w')
            file.write('Information about '+str(res[0][0])+' Transistor\n')
            file.write('\n')
            file.write(out)
            file.close()
            fr=open('text.txt')
            cont=fr.read()
            fr.close()
            data={
                'api_option': 'paste',
                'api_dev_key': key,
                'api_paste_code': cont,
                'api_paste_name': res,
                'api_paste_expire_date': '1H',
                }
            login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
            data['api_user_key'] = login.text

            r = requests.post("https://pastebin.com/api/api_post.php", data=data)
            print()
            print('Use the following link to Download the Text File, The file is valid for 1 Hour')
            print("Paste URL: ", r.text)
            os.remove('text.txt')

        else:
            file = open('text.txt', 'w')
            file.write('Equivalent of ' + str(res[0][0]) + ' Transistor\n')
            file.write('\n')
            file.write(out)
            file.close()
            fr = open('text.txt')
            cont = fr.read()
            fr.close()
            data = {
                'api_option': 'paste',
                'api_dev_key': key,
                'api_paste_code': cont,
                'api_paste_name': res,
                'api_paste_expire_date': '1H',
            }
            login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
            data['api_user_key'] = login.text

            r = requests.post("https://pastebin.com/api/api_post.php", data=data)
            print()
            print('Use the following link to Download the Text File, The file is valid for 1 Hour')
            print("Paste URL: ", r.text)
            os.remove('text.txt')

# ----------------------/Functions------------------------------------------

print('Welcome to the Transistor Database')
time.sleep(0.5)
print()
print('How may I help You?')
time.sleep(0.5)
print()
time.sleep(0.25)

menu()
