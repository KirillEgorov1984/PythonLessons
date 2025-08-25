def main():
    show_interest(rate=0.01, periods=10, principal=10000.0)

def show_interest(periods, principal, rate):
    interest = periods * principal * rate
    print(f'Простой процентный доход составит ${interest:,.2f}')

main()