import sys
import re
import json

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")

try:
    with open("raw.txt", "r", encoding="utf-8") as file:
        text = file.read()
except UnicodeDecodeError:
    with open("raw.txt", "r", encoding="cp1251") as file:
        text = file.read()

# 1. Извлечение цен товаров
prices = re.findall(r'(\d[\d ]*,\d{2})\nСтоимость', text)
prices = [float(price.replace(" ", "").replace(",", ".")) for price in prices]

# 2. Извлечение названий товаров
products = re.findall(
    r'\d+\.\n(.*?)\n\d+,\d+\s*x',
    text,
    re.DOTALL
)

products = [product.replace("\n", " ").strip() for product in products]

# 3. Общая сумма
total_match = re.search(r'ИТОГО:\s*\n([\d ]+,\d{2})', text)
total = total_match.group(1) if total_match else "Not found"

# 4. Дата и время
datetime_match = re.search(
    r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})',
    text
)

date = datetime_match.group(1) if datetime_match else "Not found"
time = datetime_match.group(2) if datetime_match else "Not found"

# 5. Способ оплаты
payment_match = re.search(r'(Банковская карта|Наличные)', text)
payment_method = payment_match.group(1) if payment_match else "Not found"

# 6. JSON вывод
result = {
    "date": date,
    "time": time,
    "payment_method": payment_method,
    "total_amount": total,
    "products": products,
    "prices": prices
}

print(json.dumps(result, indent=4, ensure_ascii=False))