MONEY_CAPITAL = 20000  # Подушка безопасности
SALARY = 5000  # Ежемесячная зарплата
SPEND = 6000  # Траты за первый месяц
INCREASE = 0.05  # Ежемесячный рост цен
BUDEGT = SALARY + MONEY_CAPITAL
expenses = SPEND
month_counter = 0

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while expenses < BUDEGT :
    month_counter+= 1
    expenses  = (month_counter*INCREASE*expenses + expenses)

print("Количество месяцев, которое можно протянуть без долгов:",month_counter)
