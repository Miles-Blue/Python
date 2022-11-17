import coin

def main():
    coin_obj = coin.Coin()
    
    print(f"Your coin is currently showing: {coin_obj.get_sideup()}")
    
    flip(coin_obj)

def flip(coin_obj):
    
    coin_obj.toss()
    print("\nTossing your coin...\n")
    
    print(f"Your coin is now showing: {coin_obj.get_sideup()}")