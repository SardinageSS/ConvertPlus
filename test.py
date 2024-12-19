from UI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
import decimal
import requests
import sys
from openexchangerate import OpenExchangeRates

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('ConvertPlus')

        # Подключаем сигналы для автоматической конвертации
        self.Sum1.textChanged.connect(self.converter_from_sum1)  # При изменении текста в Sum1
        self.Sum1BOX.currentIndexChanged.connect(self.converter_from_sum1)  # При изменении валюты в Sum1BOX
        self.Sum2BOX.currentIndexChanged.connect(self.converter_from_sum1)  # При изменении валюты в Sum2BOX

        self.Sum2.textChanged.connect(self.converter_from_sum2)  # При изменении текста в Sum2

        # Кнопка обмена значениями
        self.ButtonSWAP.clicked.connect(self.swap_values)

    def converter_from_sum1(self):
        try:
            amount = decimal.Decimal(self.Sum1.text()) if self.Sum1.text() else decimal.Decimal(0)
            from_currency = self.Sum1BOX.currentText()  # Выбранная валюта
            to_currency = self.Sum2BOX.currentText()  # Выбранная валюта

            # Получаем курсы валют с помощью API Open Exchange Rates
            api_key = '6b6660a0973740c2a59b1e4c02255560'  # API ключ
            response = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={api_key}')
            response.raise_for_status()  # Проверка на успешность запроса
            data = response.json()

            if from_currency in data['rates'] and to_currency in data['rates']:
                from_rate = decimal.Decimal(data['rates'][from_currency])
                to_rate = decimal.Decimal(data['rates'][to_currency])
                converted_amount = (amount / from_rate) * to_rate

                self.Sum2.setText(f"{converted_amount:.2f}")
            else:
                self.Sum2.setText("Ошибка: валюта не найдена")
        except ValueError:
            self.Sum2.setText("Ошибка: неверный ввод")
        except requests.RequestException as e:
            self.Sum2.setText(f"Ошибка API: {str(e)}")
        except Exception as e:
            self.Sum2.setText(f"Ошибка: {str(e)}")

    def converter_from_sum2(self):
        try:
            amount = decimal.Decimal(self.Sum2.text()) if self.Sum2.text() else decimal.Decimal(0)
            from_currency = self.Sum2BOX.currentText()  # Выбранная валюта
            to_currency = self.Sum1BOX.currentText()  # Выбранная валюта

            # Получаем курсы валют с помощью API Open Exchange Rates
            api_key = '19bdf38d63854d1e8529f68b2dfc8399'  # Ваш API ключ
            response = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={api_key}')
            response.raise_for_status()  # Проверка на успешность запроса
            data = response.json()

            if from_currency in data['rates'] and to_currency in data['rates']:
                from_rate = decimal.Decimal(data['rates'][from_currency])
                to_rate = decimal.Decimal(data['rates'][to_currency])
                converted_amount = (amount / from_rate) * to_rate

                self.Sum1.setText(f"{converted_amount:.2f}")
            else:
                self.Sum1.setText("Ошибка: валюта не найдена")
        except ValueError:
            self.Sum1.setText("Ошибка: неверный ввод")
        except requests.RequestException as e:
            self.Sum1.setText(f"Ошибка API: {str(e)}")
        except Exception as e:
            self.Sum1.setText(f"Ошибка: {str(e)}")

    def swap_values(self):
        sum1_value = self.Sum1.text()
        sum2_value = self.Sum2.text()

        sum1box_value = self.Sum1BOX.currentText()
        sum2box_value = self.Sum2BOX.currentText()

        self.Sum1.setText(sum2_value)
        self.Sum2.setText(sum1_value)

        self.Sum1BOX.setCurrentText(sum2box_value)
        self.Sum2BOX.setCurrentText(sum1box_value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())