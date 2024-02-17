total_price = int(input('Введите общую стоимость часов: '))
price_silver = 48
price_gold = price_silver / 16
total_silver_price = 96 * price_silver
total_gold_price = total_price - total_silver_price
num_gold = total_gold_price / price_gold
print(int(num_gold))