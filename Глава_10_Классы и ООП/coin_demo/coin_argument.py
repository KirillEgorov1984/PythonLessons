import coin

def main():
    my_coin = coin.Coin()

    print(my_coin.get_sidup())

    flip(my_coin)

    print(my_coin.get_sidup())

def flip(coin_obj):
    coin_obj.toss()

if __name__ == '__main__':
    main()