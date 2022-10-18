from PyQt5 import QtWidgets
import sys
import Raschet

Result = "Result.txt"
Sourse = "Sourse.txt"
NewResult = "NewResult.txt"


class MainApp(QtWidgets.QMainWindow, Raschet.Ui_Raschet):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_shifr.clicked.connect(self.Crypt)
        self.pb_rashifr.clicked.connect(self.DeCrypt)

    def Crypt(self):
        A = 5
        B = 1
        M = 16
        Y0 = 7
        gamma_list = []
        for i in range(8):
            y = (A * Y0 + B) % M
            gamma_list.append(y)

        gamma = gamma_list
        line = self.line_vvod.toPlainText()
        with open("Sourse.txt", "w") as file:
            file.write(line)

        res = open("Result.txt", "w", encoding="utf-8")
        with open('Sourse.txt', 'r', encoding="utf-8") as f:
            r_int = ""
            r = ""
            while True:
                temp = f.read(8)
                if temp:
                    for i, item in enumerate(temp):
                        r_int = r_int + " " + str(ord(item) ^ gamma[i])
                        r = r + chr(ord(item) ^ gamma[i])
                        res.write(chr(ord(item) ^ gamma[i]))

                else:
                    break

        self.line_shifr.setText(r)

    def DeCrypt(self):
        A = 5
        B = 1
        M = 16
        Y0 = 7
        gamma_list = []
        for i in range(8):
            y = (A * Y0 + B) % M
            gamma_list.append(y)

        gamma = gamma_list
        line = self.line_shifr.toPlainText()
        with open("Result.txt", "w") as file:
            file.write(line)

        res = open("NewResult.txt", "w", encoding="utf-8")
        with open('Result.txt', 'r', encoding="utf-8") as f:
            r_int = ""
            r = ""
            while True:
                temp = f.read(8)
                if temp:
                    for i, item in enumerate(temp):
                        r_int = r_int + " " + str(ord(item) ^ gamma[i])
                        r = r + chr(ord(item) ^ gamma[i])
                        res.write(chr(ord(item) ^ gamma[i]))
                else:
                    break
        self.line_enter.setText(r)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()