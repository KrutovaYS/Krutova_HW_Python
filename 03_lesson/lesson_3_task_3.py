from address import Address
from mailing import Mailing

address_to = Address("123456", "Тольятти", "Ворошилова", "10", "25")
address_from = Address("654321", "Сочи", "Виноградная", "5", "12")

my_mailing = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=2500.50,
    track="RB123456789RU"
)

print(
    f"Отправление {my_mailing.track} из "
    f"{my_mailing.from_address.index}, {my_mailing.from_address.city}, "
    f"{my_mailing.from_address.street}, {my_mailing.from_address.house} - "
    f"{my_mailing.from_address.apartment} в "
    f"{my_mailing.to_address.index}, {my_mailing.to_address.city}, "
    f"{my_mailing.to_address.street}, {my_mailing.to_address.house} - "
    f"{my_mailing.to_address.apartment}. "
    f"Стоимость {my_mailing.cost} рублей."
)