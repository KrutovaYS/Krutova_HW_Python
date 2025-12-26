from smartphone import Smartphone

catalog = [
    Smartphone('IPhone', 'XR', '+79123123123'),
    Smartphone('Samsung', 'A30', '+79111111111'),
    Smartphone('ZTE', 'HP233', '+79222222222'),
    Smartphone('Xiaomi', 'Redmi', '+79333333333'),
    Smartphone('Huawei', 'Nova 13', '+79444444444')
]

for Smartphone in catalog:
    print(f"{Smartphone.name} - {Smartphone.model}. {Smartphone.number}")