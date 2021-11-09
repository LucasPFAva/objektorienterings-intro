from os import system

class Car():
    '''
    En klass som håller reda på några egenskaper hos en bil.
    '''
    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, brand, color, mileage):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Car har egna värden på dessa.
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        '''
        Skriver ut bilmärket
        '''
        print(self.brand)

    def get_mileage(self):
        '''
        Retunerar miltalet
        '''
        return self.mileage

    def set_brand(self, new_brand):
        '''
        Parameter: new_brand | sträng
        Uppdaterar bilmärket om det existerar. Om det inte existerar
        så tilldelas aktuellt objekt märket enligt parametern.
        '''
        self.brand = new_brand
    
    def set_color(self, new_color):
        '''
        Parameter: new_color | sträng
        Uppdaterar färgen på bilen om det existerar. om det inte existerar
        så tilldelas aktuellt objekt färgen enligt parametern.
        '''
        self.color = new_color

    def set_mileage(self, new_mileage):
        '''
        Parameter: new_mileage | int
        Uppdaterar antal mil på bilen om det existerar. om det inte existerar
        så tilldelas aktuellt objekt miltalet enligt parametern.
        '''
        self.mileage = new_mileage


# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
a_car = Car('Volvo', 'Blå', 1587)
b_car = Car('BMW', 'Röd', 1235)
c_car = Car('Audi', 'Grön', 1689)
d_car = Car('Subaru', 'Svart', 853)

my_cars = [a_car, b_car, c_car, d_car]

def alphabeticalOrder():
    pass

def mileage():
    pass

def year():
    pass

def color():
    pass

OPTION_DICT = {
    'a' : alphabeticalOrder,
    'm' : mileage,
    'y' : year,
    'c' : color
}

opt = ''
while opt.lower() != 'q':
    # ritaSkärm()
    print("Sortera val:\na. bokstavsordning\nm. miltal\ny. årsmodell\nc. färg\nq. Avsluta")
    opt = input("\n\tDitt val -> ")
    if opt.lower() in OPTION_DICT:
        OPTION_DICT[opt.lower()]()
    system("cls || clear")

# 3. Det som händer är att memberfunktionen av klassen Car, get_brand() körs. 
# Detta printar ut member variablen 'brand'. 
# Efter det används funktionen set_brand som simplet sätter member variablen 'brand' till new_brand, 
# vilket är argumentet för member funktionen. 
# Efteråt används get_brand() ingen vilket printar ut den nya värdet som satts som 'brand' i denna instans av klassen Car.

# 4.
# Gjort {b_car = Car('Volvo', 'Röd', 1999)}

# 5. Resultatet är att både objektet a_car och b_car printar ut deras variabel(attribut) brand, detta händer i ordningen i vilket som jag placerade dem, i detta printas först a_car och sedan b_car ut sitt attribut.
# a_car.get_brand()
# b_car.get_brand()

# 6. Gjort
# def set_color(self, new_color):
#     self.color = new_color

# 7. set_color klassmetoden fungerar.
# print(a_car.color)
# a_car.set_color('Grön')
# print(a_car.color)

# 8. set_milage klassmetoden fungerar.
# print(a_car.mileage)
# a_car.set_mileage(1588)
# print(a_car.mileage)

# 9. get_mileage klassmetoden fungerar.
# def get_mileage(self):
#     print(self.mileage)
#
# Här anropar jag metoden:
# theMileage = a_car.get_mileage()
# print(theMileage)

# 10. Gjort
# a_car = Car('Volvo', 'Blå', 1587)
# b_car = Car('BMW', 'Röd', 1235)
# c_car = Car('Audi', 'Grön', 1689)
# d_car = Car('Subaru', 'Svart', 853)

# 11.
# my_cars = [a_car, b_car, c_car, d_car]
# for car in my_cars:
#     car.get_brand()

# 12. 