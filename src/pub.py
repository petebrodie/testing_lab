class Pub:
    def __init__(self, name, drinks, till):
        self.name = name
        self.drinks = drinks
        self.till = till

    def drink_count(self):
        return len(self.drinks)    
 
    def increase_till(self, amount):
        self.till += amount    

    def find_drink_by_name(self, drink_to_find):
        result_drink = None

        for drink in self.drinks:
            if drink.name == drink_to_find.name:
                result_drink = drink

        return result_drink       

    def sell_drink(self, drink, customer):
        drink = self.find_drink_by_name(drink)
        if drink.price > customer.wallet:
            return
        customer.reduce_money(drink.price)
        self.increase_till(drink.price)
        customer.add_drink(drink)

