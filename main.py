import os,sys
import hashlib
import subprocess

from mysql.connector import connect, Error
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog



# pyinstaller -F -w main.py создание ярлыка

def write_to_folder(directory='', ):
    pass



print(os.path.realpath(__file__))
dirname, filename = os.path.split(os.path.realpath(__file__))
print(dirname)
Form, Window = uic.loadUiType((dirname + "\\LimboQT.ui"))
# Form2, Window2 = uic.loadUiType((dirname + "\\licence_input.ui"))
Form3, Window3 = uic.loadUiType((dirname + "\\supreme_access.ui"))
Form4, Window4 = uic.loadUiType((dirname + "\\supreme_window.ui"))
Form5, Window5 = uic.loadUiType((dirname + "\\username_change_window.ui"))

app = QApplication([])
window = Window()
# window2 = Window2()
window3=Window3()
window4=Window4()
window5=Window5()

form = Form()
# form2 = Form2()
form3=Form3()
form4=Form4()
form5=Form5()
form.setupUi(window)
# form2.setupUi(window2)
form3.setupUi(window3)
form4.setupUi(window4)
form5.setupUi(window5)
window.show()
mydir = ""
#-------------------------------------------
current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
# current_machine_id = "1111-2222-0000-4444"

def uname_change():
    name = form5.textEdit.toPlainText()
    req = "UPDATE users_table SET name=" + "\"" + name + "\"" + "WHERE unique_id=" + "\"" + current_machine_id + "\""
    queryToDb(req)
    show_username()
    window5.close()

def show_uname_change():
    window5.show()

def getAccess():
    window3.show()

def showSupreme():
    window4.show()

def on_click_select_folder():
    global mydir
    dialog = QFileDialog()
    mydir = dialog.getExistingDirectory(window, 'Select directory')
    print(mydir)
    form.label_4.setText(mydir)

def click_run():
    pass

def queryToDb(my_query):
    res="lol"
    try:
        with connect(
                host="niklowkick.beget.tech",
                user="niklowkick_users",
                password="2AXx5&ej",
                database="niklowkick_users",
                buffered=True
        ) as connection:
            query =  my_query
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                res = cursor.fetchall()
    except Error as e:
        print(e)
    res=str(res)
    return(res)

def insert_query(request,data):
    res = "lol"
    try:
        with connect(
                host="niklowkick.beget.tech",
                user="niklowkick_users",
                password="2AXx5&ej",
                database="niklowkick_users",
                buffered=True
        ) as connection:
            query = request
            with connection.cursor() as cursor:
                cursor.executemany(query,data)
                connection.commit()
                res = cursor.fetchall()
    except Error as e:
        print(e)
    res = str(res)
    return (res)

def show_username():
    req = "SElECT name FROM users_table WHERE unique_id=" + "\"" + str(current_machine_id) + "\""
    username = queryToDb(req)
    resp = username[3:-4]
    form.user_name.setText("Hello, " + resp + "!")

def at_start_license():
#----------------------------------------------------------------------
    if is_user_exits!="None":
        print("user is avaliable")
        show_username()
    else:
        print("user is not avaliable")
        form.user_name.setText("Hello, stranger..")
        secret_key=hashlib.md5(current_machine_id.encode())
        secret_key=secret_key.hexdigest()
        print(secret_key)
        req_non_exist="""
        INSERT INTO users_table
        (unique_id, is_main_access, is_sub_access, license_key, name)
        VALUES( %s, %s, %s, %s, %s )
        """
        user_records = [
            (current_machine_id, "1", "0", secret_key, "user"),
        ]
        insert_query(req_non_exist,user_records)
        show_username()

    try:
        with connect(
                host="niklowkick.beget.tech",
                user="niklowkick_users",
                password="2AXx5&ej",
                database="niklowkick_users",
                buffered=True
        ) as connection:
            query_is_sub = "SELECT is_sub_access FROM users_table WHERE unique_id=" + "\"" + str(
                current_machine_id) + "\""
            with connection.cursor() as cursor:
                cursor.execute(query_is_sub)
                connection.commit()
                is_active=""
                is_active = cursor.fetchall()
    except Error as e:
        print(e)
#----------------------------------------------------
    is_active_str = str(is_active)
    is_active_str = is_active_str[2:-3]
    print(is_active_str)
#---------------------------------------------------------------
    if is_active_str=='1':
        form.way_to_supreme_btn.setEnabled(True)
        form.label_is_premium.setText("PREMIUM")
    elif is_active_str=='0':
        form.way_to_supreme_btn.setEnabled(False)
        form.label_is_premium.setText("DEMO")

def is_user_exist():
    try:
        with connect(
                host="niklowkick.beget.tech",
                user="niklowkick_users",
                password="2AXx5&ej",
                database="niklowkick_users",
                buffered=True,
        ) as connection:
            query_registration = "SELECT id FROM users_table WHERE unique_id=" + "\"" + str(current_machine_id) + "\""
            with connection.cursor() as cursor:
                cursor.execute(query_registration)
                result = cursor.fetchone()
    except Error as e:
        print(e)
    return(result)

def get_license_key():
    try:
        with connect(
                host="niklowkick.beget.tech",
                user="niklowkick_users",
                password="2AXx5&ej",
                database="niklowkick_users",
                buffered=True,
        ) as connection:
            query_compare_key = "SElECT license_key FROM users_table WHERE unique_id=" + "\"" + str(
                current_machine_id) + "\""
            with connection.cursor() as cursor:
                cursor.execute(query_compare_key)
                connection.commit()
                result = cursor.fetchall()
    except Error as e:
        print(e)
    return (result)

def checkSupremeAccess():
    license_key = form3.textEdit.toPlainText()
    print(license_key)
    print(license_key == true_license_key)
    if license_key == true_license_key:
        window3.close()
        form.label_is_premium.setText("PREMIUM")
        form.way_to_supreme_btn.setEnabled(True)
        try:
            with connect(
                    host="niklowkick.beget.tech",
                    user="niklowkick_users",
                    password="2AXx5&ej",
                    database="niklowkick_users",
                    buffered=True
            ) as connection:
                query_update = 'UPDATE users_table SET is_sub_access = "1" WHERE unique_id =' +"\"" + str(
                    current_machine_id)+ "\""
                with connection.cursor() as cursor:
                    cursor.execute(query_update)
                    connection.commit()
        except Error as e:
            print(e)

#--------------------------------------------------
form.pushButton.clicked.connect(on_click_select_folder)
form.pushButton_2.clicked.connect(click_run)
form.check_access_button.clicked.connect(getAccess)
form.way_to_supreme_btn.clicked.connect(showSupreme)
form.actionChange_username.triggered.connect(show_uname_change)
form3.pushButton.clicked.connect(checkSupremeAccess)
form5.pushButton.clicked.connect(uname_change)
#---------------------------------------------------
print(current_machine_id)
# hash MD5

# try:
#     with connect(
#             host="localhost",
#             #user=input("Введите имя пользователя: "),   # root
#             # password = input('Enter Password:'),  #vipmost2007
#             user="root",
#             password="vipmost2007",
#             database="users",
#             buffered=True,  #for cursor
#     ) as connection:
#         # query = """
#         # INSERT INTO users_table
#         # (unique_id, is_main_access, is_sub_access, license_key)
#         # VALUES( %s, %s, %s, %s )
#         # """
#         # users_records = [
#         #     ("01DE20FA-6BB8-41C3-AC4E-003D24CAE5A4", "1", "1", "66d33a07105a3f9b5a23345177468ad7"),
#         #     ("01DE50FA-6GB8-41C3-AC4E-009D24CDE5A4", "1", "0", "f9e47499d4b82c9ab3d475bdf964b53a"),
#         # ]
#         # query_update="""
#         # UPDATE
#         #     users_table
#         # SET
#         #     is_sub_access = "1"
#         # WHERE
#         #     unique_id = "01DE20FA-6BB8-41C3-AC4E-003D24CAE5A4"
#         # """
#         # query_show_table="SELECT * FROM users_table"
#         # get string from table with current user uuid to compare true lic key and key, provided by user
#         query_compare_key="SElECT license_key FROM users_table WHERE unique_id=" + "\"" + str(current_machine_id)+ "\""
#         query_registration = "SELECT id FROM users_table WHERE unique_id="+ "\"" + str(current_machine_id)+ "\""
#         with connection.cursor() as cursor:
#             # cursor.executemany(query, users_records)
#             cursor.execute(query_compare_key)
#             connection.commit()
#             result = cursor.fetchall()   # Получить строки из последнего выполненного запроса
#             cursor.execute(query_registration)
#             result2=cursor.fetchone()
# except Error as e:
#     print(e)




is_user_exits = str(is_user_exist()) #FIRSTLY need to know is user exists
at_start_license()

#result from mysql to str
true_license_key = str(get_license_key())
true_license_key = true_license_key[3:-4]
print(true_license_key)

app.exec_()
