class MidPrice:
    name = 'mid price'
    price = 50
    brandManager = 'Maciej Nowak'

    def __str__(self):
        return(f'osoba odpowiedzialna za {self.name} to {self.brandManager} cena to: {self.price}')

class AAAPrice:
    name = 'aaa price'
    price = 250
    brandManager = 'Marianna Srebrna'

    def __str__(self):
        return(f'osoba odpowiedzialna za {self.name} to {self.brandManager} cena to: {self.price}')


class BasePrice:
    name = 'base price'
    price = 10
    brandManager = 'Jan Nowak'

    def __str__(self):
        return(f'osoba odpowiedzialna za {self.name} to {self.brandManager} cena to: {self.price}')


class PriceGameTypeFactory:
    def createGamePriceType(self, typ):
        priceType = None
        if typ == 'baseprice':
            priceType = BasePrice()
        elif typ == 'midprice':
            priceType = MidPrice()
        elif typ == 'aaaprice':
            priceType = AAAPrice()
        
        return priceType
 
def gamesFactor():
    games = []
    gameFactory = PriceGameTypeFactory()
    aaaPrice = gameFactory.createGamePriceType('aaaprice')
    games.append(aaaPrice)

    games.append(gameFactory.createGamePriceType('baseprice'))
    games.append(gameFactory.createGamePriceType('midprice'))

    for i in games:
        print(i)

gamesFactor()


