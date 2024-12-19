import json
from openexchangerate import OpenExchangeRates

# Инициализация клиента с вашим API ключом
client = OpenExchangeRates(api_key="6b6660a0973740c2a59b1e4c02255560")

# Получение данных о текущих обменных курсах
exchange_rates = client.latest()

# Запись данных в JSON файл
with open('database.json', 'w') as json_file:
    json.dump(exchange_rates, json_file, indent=4)

print("Данные успешно записаны в файл database.json")

from openexchangerate import OpenExchangeRates

client = OpenExchangeRates(api_key="bc1qra7aw9jlr4xvlh70aak2fgu9jfnjjal684ak8n")
print(client.latest())
