from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("nokia", "3310", "+79110567785"))
catalog.append(Smartphone("sumsung", "A53", "+79115567785"))
catalog.append(Smartphone("nubia", "S300", "+73330567785"))
catalog.append(Smartphone("sony", "F51", "+79110567555"))
catalog.append(Smartphone("nokia", "T34", "+79119379992"))

for phone in catalog:
    print(phone)
