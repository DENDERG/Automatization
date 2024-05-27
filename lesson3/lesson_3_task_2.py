from smartphone import Smartphone

catalog = []

my_smartphone_1 = Smartphone("Iphone", "15 pro max", "+79639187390")
my_smartphone_2 = Smartphone("Nokia", "3310", "+79277785754")
my_smartphone_3 = Smartphone("Xiaomi", "Mi 12X", "+79270208375")
my_smartphone_4 = Smartphone("Samsung", "S23", "+79278918277")
my_smartphone_5 = Smartphone("Honor", "10X", "+7901860111")

catalog.append(my_smartphone_1)
catalog.append(my_smartphone_2)
catalog.append(my_smartphone_3)
catalog.append(my_smartphone_4)
catalog.append(my_smartphone_5)

for phone in catalog:
    print(phone.brand + " - " + phone.model + ". " + phone.phone_number)
