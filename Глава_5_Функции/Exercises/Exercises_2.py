FEDERAL_TAX = 0.05
LOCAL_TAX = 0.025

def main():
    sum_sale()


def sum_sale():
    client_name = input("Как Вас зовут?: ")
    sale_sum = float(input("Введите стоимость покупки: "))
    print(f"Стоимость Вашей покупки, {client_name}, составляет: {sale_sum:<15,.2f}" + "\n"
          f"Федеральный налог: {sale_sum * FEDERAL_TAX:<15,.2f}" + "\n"
          f"Региональный налог: {sale_sum * LOCAL_TAX:<15,.2f}" + "\n"
          f"Общий налог: {sale_sum * (LOCAL_TAX + FEDERAL_TAX):<15,.2f}" + "\n"
          f"Общая сумма продажи: {sale_sum * (LOCAL_TAX + FEDERAL_TAX) + sale_sum:<15,.2f}")

main()