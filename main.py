﻿import os, sys
import hashlib
import subprocess
import openpyxl

import PyQt5
import requests #это нужно, хватит удалять!!!
from datetime import datetime
import random

from mysql.connector import connect, Error
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QDoubleValidator, QCursor, QPixmap
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt


# pyinstaller -F -w main.py создание ярлыка
# pyuic5 -x LimboQT.ui -o test.py

def write_to_folder(directory='', ):
    pass


print(os.path.realpath(__file__))
dirname, filename = os.path.split(os.path.realpath(__file__))
print(dirname)
Form, Window = uic.loadUiType((dirname + "\\Construct.ui"))
# Form2, Window2 = uic.loadUiType((dirname + "\\licence_input.ui"))
Form3, Window3 = uic.loadUiType((dirname + "\\supreme_access.ui"))
Form4, Window4 = uic.loadUiType((dirname + "\\supreme_window.ui"))
Form5, Window5 = uic.loadUiType((dirname + "\\username_change_window.ui"))
Form6, Window6 = uic.loadUiType((dirname + "\\update.ui"))
Form7, Window7 = uic.loadUiType((dirname + "\\InfoWindow.ui"))

app = QApplication([])
window = Window()
# window2 = Window2()
window3 = Window3()
window4 = Window4()
window5 = Window5()
window6 = Window6()
window7 = Window7()

form = Form()
# form2 = Form2()
form3 = Form3()
form4 = Form4()
form5 = Form5()
form6 = Form6()
form7 = Form7()
form.setupUi(window)
# form2.setupUi(window2)
form3.setupUi(window3)
form4.setupUi(window4)
form5.setupUi(window5)
form6.setupUi(window6)
form7.setupUi(window7)

window.show()
#mydir = ""
# -------------------------------------------
current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
# current_machine_id = "1111-2222-0000-4444"
encodedProfile = ""
encodedWeight = float()

lengthRecord = []
profileRecord = []
amountRecord = []
weightRecord = []
mainWeightRecord = []

def uname_change():
    name = form5.textEdit.toPlainText()
    req = "UPDATE users_table SET name=" + "\"" + name + "\"" + "WHERE unique_id=" + "\"" + current_machine_id + "\""
    queryToDb(req)
    show_username()
    window5.close()


def show_uname_change():
    window5.show()


def info():
    window7.show() #Window "О программе"


def getAccess():
    window3.show()


def showSupreme():
    window4.show()


#def on_click_select_folder():
#    global mydir
#    dialog = QFileDialog()
#    mydir = dialog.getExistingDirectory(window, 'Select directory')
#    print(mydir)
#    form.label_4.setText(mydir)


def queryToDb(my_query):
    res = "lol"
    try:
        with connect(
                host="niklowkick.beget.tech",
                user="niklowkick_users",
                password="2AXx5&ej",
                database="niklowkick_users",
                buffered=True
        ) as connection:
            query = my_query
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
                res = cursor.fetchall()
    except Error as e:
        print(e)
    res = str(res)
    return (res)


def insert_query(request, data):
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
                cursor.executemany(query, data)
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
    # ----------------------------------------------------------------------
    if is_user_exits != "None":
        print("user is avaliable")
        show_username()
    else:
        print("user is not avaliable")
        form.user_name.setText("Hello, stranger..")
        secret_key = hashlib.md5(current_machine_id.encode())
        secret_key = secret_key.hexdigest()
        print(secret_key)
        req_non_exist = """
        INSERT INTO users_table
        (unique_id, is_main_access, is_sub_access, license_key, name)
        VALUES( %s, %s, %s, %s, %s )
        """
        user_records = [
            (current_machine_id, "1", "0", secret_key, "user"),
        ]
        insert_query(req_non_exist, user_records)
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
                is_active = ""
                is_active = cursor.fetchall()
    except Error as e:
        print(e)
    # ----------------------------------------------------
    is_active_str = str(is_active)
    is_active_str = is_active_str[2:-3]
    print(is_active_str)
    # ---------------------------------------------------------------
    if is_active_str == '1':
        form.way_to_supreme_btn.setEnabled(True)
        form.label_is_premium.setText("PREMIUM")
    elif is_active_str == '0':
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
    return (result)


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
                query_update = 'UPDATE users_table SET is_sub_access = "1" WHERE unique_id =' + "\"" + str(
                    current_machine_id) + "\""
                with connection.cursor() as cursor:
                    cursor.execute(query_update)
                    connection.commit()
        except Error as e:
            print(e)


def profileShow(self):
    global encodedProfile
    global encodedWeight
    encodedProfile = str('SA-152-15-U-OUT')
    if self == 'PN-152-1,5':
        form.photo.setPixmap(QtGui.QPixmap('profile_images/PN-152-1,5.png'))
        encodedProfile = str('SA-152-15-U-OUT')
        form.ProfileLabel.setText(str(self))
        encodedWeight = float(3.13)
    elif self == 'TPN-152-1,5':
        form.photo.setPixmap(QtGui.QPixmap('profile_images/TPN-152-1,5.png'))
        encodedProfile = str('SA-152-15-TU-OUT')
        form.ProfileLabel.setText(str(self))
        encodedWeight = float(2.92)
    elif self == 'PS-152-1,5':
        form.photo.setPixmap(QtGui.QPixmap('profile_images/PS-152-1,5.png'))
        encodedProfile = str('SA-152-15-C-IN')
        form.ProfileLabel.setText(str(self))
        encodedWeight = float(3.13)
    elif self == 'TPS-152-1,5':
        form.photo.setPixmap(QtGui.QPixmap('profile_images/TPS-152-1,5.png'))
        encodedProfile = str('SA-152-15-TC-IN')
        form.ProfileLabel.setText(str(self))
        encodedWeight = float(2.92)

def click_run():
    encrypt()
    profileRecording()


# --------------------- encrypt ---------------------
def encrypt():
    check_dir = os.path.exists("C:/ConstructFiles/")
    current_time = datetime.now()
    project_name = str(form.Project_name.text())
    element_name = str(form.Element_name.text())
    material = str('C375')  #### material could change, constant value
    profileLength = str(form.Length.text())
    detail_id = int(1)
    detailBeam_id = int(1)
    fileName = str(form.Project_name.text() + ' - ' + form.Element_name.text() + ' - ' + str(form.Length.text())+ 'mm')
    #text = "\:"
    #encodedProfile = str('')
    year = '{:02d}'.format(current_time.year)
    month = '{:02d}'.format(current_time.month)
    day = '{:02d}'.format(current_time.day)
    ymd = '{}-{}-{}'.format(year, month, day)
    hour = '{:02d}'.format(current_time.hour)
    minute = '{:02d}'.format(current_time.minute)
    second = '{:02d}'.format(current_time.second)
    hms = '{}:{}:{}'.format(hour, minute, second)
    if check_dir==False:
        os.mkdir("C:/ConstructFiles/")

    f = open('C:/ConstructFiles/' + fileName+'.xml', 'w')
    f.write('<?xml version="1.0" encoding="utf-8"?>')
    f.write("\n\n")
    f.write('<BatchDataSet>')
    f.write("\n")
    f.write('<Meta>')
    f.write("\n")
    f.write('  <ModificationTime>')
    f.write(str(ymd))
    f.write('T'+str(hms)+'.'+str(current_time.microsecond)+'+03:00')
    f.write('</ModificationTime>')
    f.write("\n")
    f.write('  <CreatedBy />')
    f.write("\n")
    f.write('  <ModificationTime>')
    f.write(str(ymd))
    f.write('T' + str(hms) + '.' + str(current_time.microsecond) + '+03:00')
    f.write('</ModificationTime>')
    f.write("\n")
    f.write('  <ModificatedBy>not modified</ModificatedBy>')
    f.write("\n")
    f.write('  <Version>1.0</Version>')
    f.write("\n")
    f.write('  <CadVersion>20.0 Service Release 5</CadVersion>')
    f.write("\n")
    f.write('  </Meta>')
    f.write("\n\n")

    f.write('<Project>')
    f.write("\n")
    f.write('  <ProjectID>1</ProjectID>')
    f.write("\n")
    f.write('  <ProjectName>')
    f.write(str(project_name))
    f.write('</ProjectName>')
    f.write("\n")
    f.write('  </Project>')
    f.write("\n\n")

    f.write('<Element>')
    f.write("\n")
    f.write('  <ElementID>1</ElementID>')
    f.write("\n")
    f.write('  <ElementName>')
    f.write(str(element_name))
    f.write('</ElementName>')
    f.write("\n")
    f.write('  <ElementTypeStr>wall</ElementTypeStr>')
    f.write("\n")
    f.write('  <ElementFilePath>')
    f.write(str('C:\ConstructFiles'))
    f.write('</ElementFilePath>')
    f.write("\n")
    f.write('  <ElementCount>1</ElementCount>')
    f.write("\n")
    f.write('</Element>')
    f.write("\n\n")

    f.write('<Beam>')
    f.write("\n")
    f.write('  <BeamID>1</BeamID>')
    f.write("\n")
    f.write('  <BeamElementID>1</BeamElementID>')
    f.write("\n")
    f.write('  <BeamSerial>')
    f.write(str(int(random.uniform(1, 1000000))))
    f.write('</BeamSerial>')
    f.write("\n")
    f.write('  <BeamName>')
    subEncodeProfile = str('SA-152-15-U-OUT')
    if not encodedProfile:
        f.write(str(subEncodeProfile))
    else:
        f.write(str(encodeProfile))
    #f.write(str(encodedProfile))  # beam name is the name of profile that we use to encode (ТС-152-1,5 == SA-152-15-C-IN)
    f.write('</BeamName>')
    f.write("\n")
    f.write('  <BeamMaterialGrade>')
    f.write(str(material))
    f.write('</BeamMaterialGrade>')
    f.write("\n")
    f.write('  <BeamRotation>90</BeamRotation>')
    f.write("\n")

    f.write('  <BeamXStart>0</BeamXStart>')
    f.write("\n")
    f.write('  <BeamYStart>0</BeamYStart>')
    f.write("\n")
    f.write('  <BeamZStart>0</BeamZStart>')
    f.write("\n")

    f.write('  <BeamXEnd>')
    f.write(str(profileLength))
    f.write('</BeamXEnd>')
    f.write("\n")
    f.write('  <BeamYEnd>0</BeamYEnd>')
    f.write("\n")
    f.write('  <BeamZEnd>0</BeamZEnd>')
    f.write("\n")

    f.write('  <BeamLength>')
    f.write(str(profileLength))
    f.write('</BeamLength>')
    f.write("\n")
    f.write('</Beam>')
    f.write("\n\n")

    f.write('<Detail>')
    f.write("\n")
    f.write('  <DetailID>')
    f.write(str(detail_id))
    detail_id = detail_id + 1
    f.write('</DetailID>')
    f.write("\n")
    f.write('  <DetailBeamID>')
    f.write(str(detailBeam_id))
    f.write('</DetailBeamID>')
    f.write("\n")
    f.write('  <DetailType>Front</DetailType>')
    f.write("\n")
    f.write('  <DetailName>Straight</DetailName>')
    f.write("\n")
    f.write('  <DetailXPos>0</DetailXPos>')
    f.write("\n")
    f.write('  <DetailYPos>0</DetailYPos>')
    f.write("\n")
    f.write('  <DetailProfileFace>Web</DetailProfileFace>')
    f.write("\n")
    f.write('  </Detail>')
    f.write("\n\n")

    f.write('<Detail>')
    f.write("\n")
    f.write('  <DetailID>')
    f.write(str(detail_id))
    detail_id = detail_id + 1
    f.write('</DetailID>')
    f.write("\n")
    f.write('  <DetailBeamID>')
    f.write(str(detailBeam_id))
    f.write('</DetailBeamID>')
    f.write("\n")
    f.write('  <DetailType>End</DetailType>')
    f.write("\n")
    f.write('  <DetailName>Straight</DetailName>')
    f.write("\n")
    f.write('  <DetailXPos>0</DetailXPos>')
    f.write("\n")
    f.write('  <DetailYPos>0</DetailYPos>')
    f.write("\n")
    f.write('  <DetailProfileFace>Web</DetailProfileFace>')
    f.write("\n")
    f.write('  </Detail>')
    f.write("\n\n")

    f.write('</BatchDataSet>')
    f.close()


def profileRecording():
    subProfile = str('SA-152-15-U-OUT')
    if not encodedProfile:
        profileRecord.append(subProfile)
    else:
        profileRecord.append(encodedProfile)
    lengthRecord.append(form.Length.text())
    amountRecord.append(form.Amount.text())
    subWeight = float(3.13)
    if not encodedWeight:
        weightRecord.append(subWeight)
    else:
        weightRecord.append(encodedWeight)
    if not encodedWeight:
        mainWeight = float((int(form.Length.text()) * subWeight) / 1000)
        mainWeightRecord.append(mainWeight)
    else:
        mainWeight = float((int(form.Length.text()) * encodedWeight) / 1000)
        mainWeightRecord.append(mainWeight)



def reportVE():
    book = openpyxl.Workbook()

    sheet = book.active
    dims = {}
    sheet['A1'] = 'Профиль'
    sheet['B1'] = 'Длина, мм'
    sheet['C1'] = 'Количество'
    sheet['D1'] = 'Масса, кг на пм'
    sheet['E1'] = 'Общаяя масса'

    column = int(2)
    for profile in profileRecord:
        sheet[column][0].value = str(profile)
        column = int(column + 1)

    column = int(2)
    for length in lengthRecord:
        sheet[column][1].value = str(length)
        column = int(column + 1)

    column = int(2)
    for amount in amountRecord:
        sheet[column][2].value = str(amount)
        column = int(column + 1)

    column = int(2)
    for weight in weightRecord:
        sheet[column][3].value = str(weight)
        column = int(column + 1)

    column = int(2)
    for main in mainWeightRecord:
        sheet[column][4].value = str(main)
        column = int(column + 1)

    for row in sheet.rows:
        for cell in row:
            if cell.value:
                dims[cell.column_letter] = max((dims.get(cell.column_letter, 0), (len(str(cell.value)) + 2)))
    for col, value in dims.items():
        sheet.column_dimensions[col].width = value

    book.save("C:/ConstructFiles/Ведомость элементов.xlsx")
    book.close()

def runCheck():
    if len(form.Length.text()) > 0 and len(form.Project_name.text()) > 0 and len(form.Element_name.text()) > 0:
        form.pushButton_2.setDisabled(False)
    else:
        form.pushButton_2.setDisabled(True)


class Updater:
    dFolder="D:"

    def select_download_folder(self):
        window6.hide()
        dialog = QFileDialog()
        download_folder = dialog.getExistingDirectory(window, 'Select directory')
        form6.label_2.setText(download_folder)
        Updater.dFolder = download_folder
        window6.show() # to prevent hiding behind main window, after calling qfile dialog

    def updater(self):
        window6.show()
        with open("TextFiles/version.txt", "r") as f:
            vers = f.read()
        form6.label.setText("Your Construct version is " + vers)
        vers = vers.replace(".", "")
        print("Your Construct version is " + vers)

    def download_updater(self):
        f = open(Updater.dFolder + '\construct_setup.exe', 'wb')
        url = "http://ggfhhrtrh.niklowkick.beget.tech/construct_setup.exe"
        response = requests.get(url, stream=True)  # делаем запрос
        f.write(response.content)
        f.close()


def lengthCheck():
    form.sizeLength.setText(str(form.Length.text()))

#def graphics_view():
    #painter = QPainter()
    #painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
    #painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
    #painter.drawRect(100, 15, 400, 200)
    #rect = scene.addRect(-100, -100, 200, 200, blackPen, redBrush)
# --------------------------------------------------
#form.comboBox.indexChanged.connect(profileBoxCkeck)
#form.pushButton.clicked.connect(on_click_select_folder)
form.pushButton_2.clicked.connect(click_run)
form.pushButton_2.setDisabled(True)
form.Amount.setDisabled(True)
form.check_access_button.clicked.connect(getAccess)
form.way_to_supreme_btn.clicked.connect(showSupreme)
form.actionChange_username.triggered.connect(show_uname_change)
form.ConstructAction.triggered.connect(info)
form.actionElementBill.triggered.connect(reportVE)
form.actionUpdate_App.triggered.connect(Updater.updater)
form.comboBox.currentTextChanged.connect(profileShow)
form.Length.textChanged.connect(runCheck)
form.Length.textChanged.connect(lengthCheck)
form.Project_name.textChanged.connect(runCheck)
form.Element_name.textChanged.connect(runCheck)
form.Length.setValidator(QDoubleValidator(0, 2000, 2))
form3.pushButton.clicked.connect(checkSupremeAccess)
form5.pushButton.clicked.connect(uname_change)
form6.pushButton.clicked.connect(Updater.download_updater)
form6.pushButton_2.clicked.connect(Updater.select_download_folder)
#form.GV.clicked.connect(graphics_view)
#Cursor = QCursor(QPixmap('profile_images/classic_grey.png'), 0, 0)
#form.dashboard.setCursor(Cursor)
# ---------------------------------------------------
print(current_machine_id)

is_user_exits = str(is_user_exist())  # FIRSTLY need to know is user exists
at_start_license()

# result from mysql to str
true_license_key = str(get_license_key())
true_license_key = true_license_key[3:-4]
print(true_license_key)

app.exec_()
