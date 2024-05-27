from address import Address
from mailing import Mailing

to_address = Address("445057", "Тольятти", "Спортивная", "18", "172")
from_address = Address("115280", "Москва", "Автозаводская", "30", "54")
mailing = Mailing(to_address, from_address, 500, "ABC123")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartament} в "
      f"{mailing.to_addres.index}, {mailing.to_addres.city},"
      f" {mailing.to_addres.street}, {mailing.to_addres.house}"
      f" - {mailing.to_addres.apartament}."
      f" Стоимость {mailing.cost} рублей")
