from UI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
import decimal
import sys
import json

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('ConvertPlus')

        # Загружаем валюты из JSON файла
        self.load_currencies()

        # Устанавливаем валидатор для ввода только чисел с плавающей точкой и двумя знаками после запятой
        regex = QRegExp("^[0-9]*\.?[0-9]{0,2}$")
        validator = QRegExpValidator(regex)
        self.Sum1.setValidator(validator)
        self.Sum2.setValidator(validator)

        # Подключаем сигналы для автоматической конвертации
        self.Sum1.editingFinished.connect(self.converter_from_sum1)  # При завершении редактирования текста в Sum1
        self.Sum1BOX.currentIndexChanged.connect(self.converter_from_sum1)  # При изменении валюты в Sum1BOX
        self.Sum2BOX.currentIndexChanged.connect(self.converter_from_sum1)  # При изменении валюты в Sum2BOX

        self.Sum2.editingFinished.connect(self.converter_from_sum2)  # При завершении редактирования текста в Sum2

        # Кнопка обмена значениями
        self.ButtonSWAP.clicked.connect(self.swap_values)

    def load_currencies(self):
        try:
            with open('database.json', 'r') as file:
                data = json.load(file)
                self.currencies = data[0]
                currencies = list(self.currencies.keys())
                self.Sum1BOX.addItems(currencies)
                self.Sum2BOX.addItems(currencies)
        except Exception as e:
            print(f"Ошибка при загрузке валют: {str(e)}")

    def converter_from_sum1(self):
        try:
            amount = decimal.Decimal(self.Sum1.text()) if self.Sum1.text() else decimal.Decimal(0)
            from_currency = self.Sum1BOX.currentText()  # Выбранная валюта
            to_currency = self.Sum2BOX.currentText()  # Выбранная валюта

            if from_currency in self.currencies and to_currency in self.currencies:
                from_rate = decimal.Decimal(self.currencies[from_currency])
                to_rate = decimal.Decimal(self.currencies[to_currency])
                converted_amount = (amount / from_rate) * to_rate

                # Округляем до двух знаков после десятичной точки
                converted_amount = converted_amount.quantize(decimal.Decimal('1.00'))

                # Удаляем ненужные нули после десятичной точки
                converted_amount = converted_amount.normalize()

                self.Sum2.setText(f"{converted_amount}")
            else:
                self.Sum2.setText("Ошибка: валюта не найдена")
        except ValueError:
            self.Sum2.setText("Ошибка: неверный ввод")
        except Exception as e:
            self.Sum2.setText(f"Ошибка: {str(e)}")

    def converter_from_sum2(self):
        try:
            amount = decimal.Decimal(self.Sum2.text()) if self.Sum2.text() else decimal.Decimal(0)
            from_currency = self.Sum2BOX.currentText()  # Выбранная валюта
            to_currency = self.Sum1BOX.currentText()  # Выбранная валюта

            if from_currency in self.currencies and to_currency in self.currencies:
                from_rate = decimal.Decimal(self.currencies[from_currency])
                to_rate = decimal.Decimal(self.currencies[to_currency])
                converted_amount = (amount / from_rate) * to_rate

                # Округляем до двух знаков после десятичной точки
                converted_amount = converted_amount.quantize(decimal.Decimal('1.00'))

                # Удаляем ненужные нули после десятичной точки
                converted_amount = converted_amount.normalize()

                self.Sum1.setText(f"{converted_amount}")
            else:
                self.Sum1.setText("Ошибка: валюта не найдена")
        except ValueError:
            self.Sum1.setText("Ошибка: неверный ввод")
        except Exception as e:
            self.Sum1.setText(f"Ошибка: {str(e)}")

    def swap_values(self):
        sum1box_value = self.Sum1BOX.currentText()
        sum2box_value = self.Sum2BOX.currentText()

        self.Sum1BOX.setCurrentText(sum2box_value)
        self.Sum2BOX.setCurrentText(sum1box_value)

        self.Sum1.setText("0")
        self.Sum2.setText("0")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
