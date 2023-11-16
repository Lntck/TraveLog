# Импортируем необходимые модули
import sys
import sqlite3
import os
import folium

from PIL import Image
from io import BytesIO
from PyQt5 import QtWidgets, QtCore, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap

from ui_forms.MainWindow import Ui_MainWindow
from ui_forms.Register_form import Register_form
from ui_forms.Login_form import Login_form
from ui_forms.Memory_add_form import Memory_add_form
from ui_forms.Change_memory_form import Memory_change_form
from ui_forms.Delete_memory_form import Memory_del_form
from ui_forms.Memory_form import MemoryForm


# Класс Главного Окна
class MainWindow(QMainWindow):
    def __init__(self, login):
        global images_list
        self.login = login
        self.temp = list()
        self.memory = list()
        images_list = list()

        super().__init__()
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.setWindowTitle("TraveLog: Дневник Путешественника")
        self.window.tabs_icons_text.hide()
        self.window.stackedWidget.setCurrentIndex(0)
        self.window.make_note_btn.clicked.connect(self.add_note)
        self.window.output_note.setSortingEnabled(True)
        self.window.del_note.clicked.connect(self.del_note)

        # Добавляю из БД сохраненные заметки в QListWidget
        connection = sqlite3.connect('database/Users.db')
        cursor = connection.cursor()
        cursor.execute(
            f'SELECT Notes FROM users_memory WHERE login == "{self.login}"')
        notes = cursor.fetchall()
        connection.commit()
        connection.close()
        for i in notes[0][0].split(";"):
            self.window.output_note.addItem(f"{i}")

        self.update_icons_memory()
        self.window.add_mem_btn.clicked.connect(self.open_add_mem_form)
        self.window.change_mem_btn.clicked.connect(self.open_change_mem_form)
        self.window.del_mem_btn.clicked.connect(self.open_del_mem_form)

    # Добавляю из БД сохраненные воспоминания в grid layout в виде иконок-кнопок
    def update_icons_memory(self):
        global images_list

        images_list = list()
        for i in self.memory:
            self.window.memory_grid.removeWidget(i)
            i.deleteLater()
        self.memory = list()

        connection = sqlite3.connect('database/Users.db')
        cursor = connection.cursor()
        cursor.execute(f'SELECT Memories FROM users_memory WHERE Login == "{self.login}"')
        memory = cursor.fetchall()
        connection.commit()
        connection.close()
        self.count = len("" if memory[0][0].split("|")[0] == "" else memory[0][0].split("|"))

        if self.count:
            x, y = 0, 0
            for i in range(self.count):
                name, info, coords, image = memory[0][0].split("|")[i].split(";")
                images_list.append(image)
                # Нужно раскожировать изображение из формата BLOB и закинуть в background-image
                connection = sqlite3.connect('database/Users.db')
                cursor = connection.cursor()
                cursor.execute(f'SELECT {image} FROM users_memory WHERE Login == "{self.login}"')
                images = cursor.fetchall()
                connection.commit()
                connection.close()
                image = Image.open(BytesIO(images[0][0]))
                image.save(f"temp/temp_{str(i)}.jpg")

                mem_btn = QtWidgets.QPushButton(self.window.page_2)
                mem_btn.setText(f"{name}")
                mem_btn.setMinimumSize(QtCore.QSize(130, 130))
                mem_btn.setMaximumSize(QtCore.QSize(130, 130))
                mem_btn.setStyleSheet("QPushButton {\n"
                                      "  background-color: blue;\n"
                                      "  border: none;\n"
                                      "  color: white;;\n"
                                      "  text-align: center;\n"
                                      "  font-size: 16px;\n"
                                      "  display: inline-block;\n"
                                      "  margin: 4px 2px;\n"
                                      "  cursor: pointer;\n"
                                      "  border-radius: 20px;\n"
                                      "  font-family:'Georgia';\n"
                                      "  color:black;\n"
                                      f" background-image: url('temp/temp_{str(i)}.jpg');\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "  border: 3px solid black;\n"
                                      "}")

                # тут добавить кликед коннект на создание окна воспоминания
                mem_btn.clicked.connect(self.open_mem_form)
                self.memory.append(mem_btn)

                if x / 5 >= 1:
                    y += 1
                    x -= 5
                self.window.memory_grid.addWidget(mem_btn, y, x, 1, 1)
                self.temp.append(f'temp/temp_{str(i)}.jpg')
                x += 1
        else:
            connection.close()

    def open_add_mem_form(self):
        self.add_form = MemoryAdd(self.login, self.count, self.update_icons_memory)
        self.add_form.show()

    def open_change_mem_form(self):
        self.change_form = MemoryChange(self.login, self.update_icons_memory)
        self.change_form.show()

    def open_del_mem_form(self):
        self.delete_form = MemoryDel(self.login, self.update_icons_memory)
        self.delete_form.show()

    def open_mem_form(self):
        connection = sqlite3.connect('database/Users.db')
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM users_memory WHERE Login == "{self.login}"')
        info = list(cursor.fetchall())[0]
        memory = info[2].split("|")

        for i in memory:
            if i.find(self.sender().text()) != -1:
                memory = i
                break
        connection.commit()
        connection.close()

        self.memory_form = Memory(self.login, memory)
        self.memory_form.show()

    def del_note(self):
        list_widget = [self.window.output_note.item(i).text() for i in range(self.window.output_note.count())]
        index_del = -1
        # Удаление заметки из QListWidget
        for item in self.window.output_note.selectedItems():
            index_del = self.window.output_note.row(item)
            self.window.output_note.takeItem(self.window.output_note.row(item))

        # Удаление заметки из БД
        connection = sqlite3.connect('database/Users.db')
        cursor = connection.cursor()
        del list_widget[index_del]
        cursor.execute(
            f'UPDATE users_memory SET Notes = "{";".join(list_widget)}" WHERE login == "{self.login}";')
        connection.commit()
        connection.close()

    def add_note(self):
        # Добавление заметки в QListWidget
        item = (self.window.calendarWidget.selectedDate().toString("yyyy-MM-dd"),
                self.window.timeEdit.time().toPyTime(), self.window.input_note.text())
        self.window.output_note.addItem(f"{item[0]} {item[1]} - {item[2]}")

        # Добавление заметки в БД
        connection = sqlite3.connect('database/Users.db')
        cursor = connection.cursor()
        cursor.execute(
            f'UPDATE users_memory SET Notes = "{";".join([self.window.output_note.item(i).text() for i in range(self.window.output_note.count())])}" WHERE login == "{self.login}";')
        connection.commit()
        connection.close()

    def closeEvent(self, event):
        try:
            for i in self.temp:
                os.remove(i)
        except FileNotFoundError:
            pass


# Класс Окна Авиторизации
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login = Login_form()
        self.login.setupUi(self)
        self.login.ToRegister_btn.clicked.connect(self.register_open)
        self.login.Auth_btn.clicked.connect(self.auth)

    def auth(self):
        connection = sqlite3.connect('database/Users.db')
        cursor = connection.cursor()
        cursor.execute('select * from Lgn_Psw')
        info = dict(cursor.fetchall())
        connection.commit()
        connection.close()

        if info.get(self.login.Auth_lgn.text(), False) is not False:
            if self.login.Auth_psw.text() == info[self.login.Auth_lgn.text()]:
                print("Вход прошел успешно!")
                self.MainWind = MainWindow(self.login.Auth_lgn.text())
                self.MainWind.show()
                self.close()
            else:
                ErrorShow()
                print("Неверно введен пароль!")
        else:
            ErrorShow()
            print("Аккаунта с таким логином не существует!")

    def register_open(self):
        self.new_window = Register()
        self.new_window.show()


# Класс Окна ошибок
class ErrorShow(QMessageBox):
    def __init__(self, title="Login or Password error!", text="Логин или пароль введены неверно! Попробуйте, еще раз!"):
        super().__init__()
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(text)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()


# Класс Окна Регистрации
class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        self.register = Register_form()
        self.register.setupUi(self)
        self.register.Register_btn.clicked.connect(self.login_open)

    def login_open(self):
        connection = sqlite3.connect('database/Users.db')
        cursor = connection.cursor()
        # реализовать проверку если тип с таким логином в системе
        cursor.execute('select Login from Lgn_Psw')
        logins = list(map(lambda x: x[0], list(cursor.fetchall())))
        if self.register.Register_lgn.text() in logins:
            ErrorShow(title="Such a user is already in the system!",
                      text="Пользователь с таким логином уже есть в системе!\nизмените логин и попробуйте еще раз!")
        else:
            cursor.execute(
                f'insert into Lgn_Psw values("{self.register.Register_lgn.text()}", "{self.register.Register_psw.text()}")')
            img_blob = open("img/london.jpg", 'rb').read()
            cursor.execute(
                f'insert into users_memory(Login, Notes, Memories, Image_1) values("{self.register.Register_lgn.text()}", "{"Твои заметки тут"}","{"London 2021;Я побывал в Лондоне и посетил Биг Бен. Это было моё первое путешествие, и я был очень рад. Биг-Бен поразил меня своим величием и красотой. Внутри башни я почувствовал прохладу и спокойствие. Со смотровой площадки мне открылся вид на весь Лондон. Даже после долгой прогулки, я не забыл свои впечатления от Биг-Бена. Это путешествие стало одним из самых запоминающихся в моей жизни.;51.500712 -0.124600;Image_1"}", ?)',
                [img_blob])
        connection.commit()
        connection.close()
        self.hide()


# Класс окна добавления воспоминания
class MemoryAdd(QMainWindow):
    def __init__(self, login, count, function):
        super().__init__()

        self.function = function
        self.add_window = Memory_add_form()
        self.add_window.setupUi(self)
        self.login = login
        self.count = count
        self.add_window.add_pic_btn.clicked.connect(self.add_pic)
        self.add_window.add_memory_btn.clicked.connect(self.add_memory)

    def add_pic(self):
        # Открываем диалоговое окно выбора файла
        PicDialog = QFileDialog(self)
        PicDialog.setNameFilter("Images (*.jpg)")
        if PicDialog.exec_():
            filename = PicDialog.selectedFiles()[0]
        # преобразовываем картинку в формат binary
        self.blob_img = open(filename, 'rb').read()

    def add_memory(self):
        global images_list
        # Добавление воспоминания в БД
        try:
            self.count += 1
            image = f"Image_{str(self.count)}"
            c = 1
            while image in images_list:
                image = f"Image_{str(c)}"
                if c > 20:
                    self.close()
                c += 1
            connection = sqlite3.connect('database/Users.db')
            cursor = connection.cursor()
            cursor.execute(f'SELECT Memories, {image} FROM users_memory WHERE Login == "{self.login}"')
            mem_img = cursor.fetchall()[0]
            memory = f"{self.add_window.memory_name.text()};{self.add_window.memory_info.toPlainText()};{self.add_window.memory_coords.text()};{image}"
            if mem_img[0] == "":
                cursor.execute(
                    f'UPDATE users_memory SET Memories = "{f"{memory}"}", {image} = ? WHERE Login == "{self.login}"',
                    [self.blob_img])
            else:
                cursor.execute(
                    f'UPDATE users_memory SET Memories = "{f"{mem_img[0]}|{memory}"}", {image} = ? WHERE Login == "{self.login}"',
                    [self.blob_img])
            connection.commit()
            connection.close()
            images_list.append(image)
        except Exception as er:
            print(er.__class__.__name__)
        finally:
            self.function()
            self.close()


# Класс окна редактирования воспоминания
class MemoryChange(QMainWindow):
    def __init__(self, login, function):
        super().__init__()

        self.change_window = Memory_change_form()
        self.change_window.setupUi(self)
        self.function = function
        self.login = login
        self.change_window.change_pic_btn.clicked.connect(self.change_pic)
        self.change_window.change_memory_btn.clicked.connect(self.change_memory)
        self.blob_img = None

    def change_pic(self):
        # Открываем диалоговое окно выбора файла
        PicDialog = QFileDialog(self)
        PicDialog.setNameFilter("Images (*.jpg)")
        if PicDialog.exec_():
            filename = PicDialog.selectedFiles()[0]
            self.blob_img = open(filename, 'rb').read()

    def change_memory(self):
        # Редактирование воспоминания в БД
        try:
            connection = sqlite3.connect('database/Users.db')
            cursor = connection.cursor()
            cursor.execute(f'SELECT Memories FROM users_memory WHERE Login == "{self.login}"')
            mem = cursor.fetchall()[0][0].split("|")
            index = -1
            for i in range(len(mem)):
                if mem[i].find(self.change_window.memory_name_old.text()) != -1:
                    index = i
                    break
            if index != -1:
                img = mem[index].split(";")[-1]
                memory = f"{self.change_window.memory_name.text()};{self.change_window.memory_info.toPlainText()};{self.change_window.memory_coords.text()};{img}"
                mem[index] = memory
                if self.blob_img is not None:
                    cursor.execute(
                        f'UPDATE users_memory SET Memories = "{"|".join(mem)}", {img} = ? WHERE Login == "{self.login}"',
                        [self.blob_img])
                else:
                    cursor.execute(
                        f'UPDATE users_memory SET Memories = "{"|".join(mem)}" WHERE Login == "{self.login}"')
            connection.commit()
            connection.close()
        except Exception as er:
            print(er.__class__.__name__)
        finally:
            self.function()
            self.close()


# Класс окна Удаления воспоминания
class MemoryDel(QMainWindow):
    def __init__(self, login, function):
        super().__init__()

        self.del_window = Memory_del_form()
        self.del_window.setupUi(self)
        self.login = login
        self.function = function
        self.del_window.del_memory_btn.clicked.connect(self.del_memory)

    def del_memory(self):
        global images_list
        # Удаление воспоминания из БД
        try:
            connection = sqlite3.connect('database/Users.db')
            cursor = connection.cursor()
            cursor.execute(f'SELECT Memories FROM users_memory WHERE Login == "{self.login}"')
            mem = cursor.fetchall()[0][0].split("|")
            index = -1

            for i in range(len(mem)):
                if mem[i].find(self.del_window.memory_name.text()) != -1:
                    index = i
                    break

            if index != -1:
                img = mem[index].split(";")[-1]
                del mem[index]
                cursor.execute(
                    f'UPDATE users_memory SET Memories = "{"|".join(mem)}", {img} = NULL WHERE Login == "{self.login}"')
                if img in images_list:
                    del images_list[images_list.index(img)]
            connection.commit()
            connection.close()
        except Exception as er:
            print(er.__class__.__name__)
        finally:
            self.function()
            self.close()


# Класс окна Показа воспоминания
class Memory(QMainWindow):
    def __init__(self, login, memory):
        super().__init__()

        self.memory_window = MemoryForm()
        self.memory_window.setupUi(self)

        self.login = login
        self.memory = memory.split(";")
        self.memory_window.open_map_btn.clicked.connect(self.open_map)
        self.memory_window.memory_info.setPlainText(self.memory[1])
        self.memory_window.memory_name.setText(self.memory[0])
        self.memory_window.save_mem_btn.clicked.connect(self.save_memory_txt)

        connection = sqlite3.connect('database/Users.db')
        cursor = connection.cursor()
        cursor.execute(f'SELECT {self.memory[-1]} FROM users_memory WHERE Login == "{self.login}"')
        img = cursor.fetchall()[0][0]
        image = Image.open(BytesIO(img))
        image.save(f"temp/temp_{self.memory[-1][-1]}.jpg")
        self.pixmap = QPixmap.fromImage(QImage(f"temp/temp_{self.memory[-1][-1]}.jpg"))
        self.memory_window.image_label.setPixmap(self.pixmap)
        self.memory_window.image_label.setText("")
        connection.commit()
        connection.close()

    def save_memory_txt(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", self.memory_window.memory_name.text(),
                                                   "Text Files(*.txt)",
                                                   options=options)
        if file_name:
            f = open(file_name, 'w')
            text = self.memory_window.memory_info.toPlainText()
            f.write(f"{self.memory_window.memory_name.text()}\n\n{text}")
            f.close()

    def open_map(self):
        self.map_window = Map(self.memory[-2])

    def closeEvent(self, event):
        os.remove(f"temp/temp_{self.memory[-1][-1]}.jpg")


# Класс карты
class Map(QMainWindow):
    def __init__(self, coords):
        super().__init__()

        if len(coords):
            self.coords = list(map(float, coords.split()))
            popup = "<i>Потрясающее место!</i>"
            tooltip = "Вы были здесь!"
        else:
            self.coords = [55.755115, 37.617649]
            popup = "<i>Вы не указали местоположение!</i>"
            tooltip = "Автоматически установлена Москва!"

        m = folium.Map(location=[self.coords[0], self.coords[1]], tiles='openstreetmap', zoom_start=13)
        folium.Marker(location=[self.coords[0], self.coords[1]], popup=popup, tooltip=tooltip).add_to(m)
        data = BytesIO()
        m.save(data, close_file=False)

        self.map_win = QtWebEngineWidgets.QWebEngineView()
        self.map_win.setHtml(data.getvalue().decode())
        self.map_win.resize(640, 480)
        self.map_win.setWindowTitle("Карта")
        self.map_win.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
