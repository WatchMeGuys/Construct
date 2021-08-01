import os, sys
import hashlib
import subprocess
# import requests
from datetime import datetime
import random

from mysql.connector import connect, Error
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QDoubleValidator

global encodedProfile
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
Form6, Window6 = uic.loadUiType((dirname + "\\update.ui"))

app = QApplication([])
window = Window()
# window2 = Window2()
window3 = Window3()
window4 = Window4()
window5 = Window5()
window6 = Window6()

form = Form()
# form2 = Form2()
form3 = Form3()
form4 = Form4()
form5 = Form5()
form6 = Form6()
form.setupUi(window)
# form2.setupUi(window2)
form3.setupUi(window3)
form4.setupUi(window4)
form5.setupUi(window5)
form6.setupUi(window6)

window.show()
mydir = ""
# -------------------------------------------
current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
# current_machine_id = "1111-2222-0000-4444"
lol = "lol"


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


# for auto-update
def updater():
    window6.show()
    with open("version.txt", "r") as f:
        vers = f.read()
    form6.label.setText("Your Construct version is " + vers)
    vers = vers.replace(".", "")
    print("Your Construct version is " + vers)


def download_updater():
    download_folder = 'D:'
    if form6.pushButton_2.clicked == True:
        download_folder = select_download_folder()
    f = open(download_folder + '\construct_setup.exe', 'wb')
    url = "http://ggfhhrtrh.niklowkick.beget.tech/construct_setup.exe"
    response = requests.get(url, stream=True)  # делаем запрос
    f.write(response.content)
    f.close()


# total_size_in_bytes = int(response.headers.get('content-length', 0))
# block_size = 1024  # 1 Kibibyte
# progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
#
# with open(download_folder + '\construct_setup.exe', 'wb') as file:
#     for data in response.iter_content(block_size):
#         progress_bar.update(len(data))
# file.write(data)
# progress_bar.close()
# if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
#     print("ERROR, something went wrong")
# form6.label_2.setText("Downloaded! Please close and reinstall the app.")
# form6.progressBar.setValue(int(str(progress_bar)[:3]))

def select_download_folder():
    dialog = QFileDialog()
    download_folder = dialog.getExistingDirectory(window, 'Select directory')
    form6.label_2.setText(download_folder)
    return (str(download_folder))


def profileShow(self):
    if self == 'PN-152-1,5':
        form.photo.setPixmap(QtGui.QPixmap('profile_images/PN-152-1,5.png'))
        encodedProfile = str('SA-152-15-U-OUT')
        form.ProfileLabel.setText(str(self))
    elif self == 'TPN-152-1,5':
        form.photo.setPixmap(QtGui.QPixmap('profile_images/TPN-152-1,5.png'))
        encodedProfile = str('SA-152-15-TU-OUT')
        form.ProfileLabel.setText(str(self))
    elif self == 'PS-152-1,5':
        form.photo.setPixmap(QtGui.QPixmap('profile_images/PS-152-1,5.png'))
        encodedProfile = str('SA-152-15-C-IN')
        form.ProfileLabel.setText(str(self))
    elif self == 'TPS-152-1,5':
        form.photo.setPixmap(QtGui.QPixmap('profile_images/TPS-152-1,5.png'))
        encodedProfile = str('SA-152-15-TC-IN')
        form.ProfileLabel.setText(str(self))

def click_run():
    encrypt()


# --------------------- encrypt ---------------------
def encrypt():
    current_time = datetime.now()
    project_name = str(form.Project_name.text())
    element_name = str(form.Element_name.text())
    material = str('C375')  #### material could change, constant value
    lenght = str(form.Length.text())
    detail_id = int(1)
    detailBeam_id = int(1)
    fileName = str(form.Project_name.text() + ' - ' + form.Element_name.text())
    # encodedProfile = str('')

    f = open(mydir + '/' + fileName + '.xml', 'w')
    f.write('<?xml version="1.0" encoding="utf-8"?>')
    f.write("\n\n")
    f.write('<BatchDataSet>')
    f.write("\n")
    f.write('<Meta>')
    f.write("\n")
    f.write('  <ModificationTime>')
    f.write(str(current_time))
    f.write('</ModificationTime>')
    f.write("\n")
    f.write('  <CreatedBy />')
    f.write("\n")
    f.write('  <ModificationTime>')
    f.write(str(current_time))
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
    f.write(str(mydir))
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
    f.write(
        str(encodedProfile))  # beam name is the name of profile that we use to encide (ТС-152-1,5 == SA-152-15-C-IN)
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
    f.write(str(lenght))
    f.write('</BeamXEnd>')
    f.write("\n")
    f.write('  <BeamYEnd>0</BeamYEnd>')
    f.write("\n")
    f.write('  <BeamZEnd>0</BeamZEnd>')
    f.write("\n")

    f.write('  <BeamLength>')
    f.write(str(lenght))
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


def runCheck():
    if len(form.Length.text()) > 0 and len(form.Project_name.text()) > 0 and len(form.Element_name.text()) > 0:
        form.pushButton_2.setDisabled(False)
    else:
        form.pushButton_2.setDisabled(True)


def lengthCheck():
    form.sizeLength.setText(str(form.Length.text()))


# --------------------------------------------------
#form.comboBox.indexChanged.connect(profileBoxCkeck)
form.pushButton.clicked.connect(on_click_select_folder)
form.pushButton_2.clicked.connect(click_run)
form.pushButton_2.setDisabled(True)
form.Amount.setDisabled(True)
form.check_access_button.clicked.connect(getAccess)
form.way_to_supreme_btn.clicked.connect(showSupreme)
form.actionChange_username.triggered.connect(show_uname_change)
form.actionUpdate_App.triggered.connect(updater)
form.comboBox.currentTextChanged.connect(profileShow)
form.Length.textChanged.connect(runCheck)
form.Length.textChanged.connect(lengthCheck)
form.Project_name.textChanged.connect(runCheck)
form.Element_name.textChanged.connect(lengthCheck)
form.Length.setValidator(QDoubleValidator(0, 2000, 2))
form3.pushButton.clicked.connect(checkSupremeAccess)
form5.pushButton.clicked.connect(uname_change)
form6.pushButton.clicked.connect(download_updater)
# form6.pushButton_2.clicked.connect(select_download_folder)
# ---------------------------------------------------
print(current_machine_id)

is_user_exits = str(is_user_exist())  # FIRSTLY need to know is user exists
at_start_license()

# result from mysql to str
true_license_key = str(get_license_key())
true_license_key = true_license_key[3:-4]
print(true_license_key)

app.exec_()
