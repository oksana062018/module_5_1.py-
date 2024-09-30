House_1 = ('ЖК Эльбрус', 30)

class House:
    def __init__(self,name, number_of_floors ):
        self.name =  name                 # номер этажа
        self.number_of_floors = number_of_floors   #кол-во этажей

    def go_to(self, new_floor):   # на который нужно приехать.

        for i in range(1, new_floor + 1):

            if 1 <= new_floor  <= self.number_of_floors:
                print(i)
            else:
                print("Такого этажа не существует")
                break





h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 30)
h1.go_to(5)
h2.go_to(10)
h3.go_to(14)
print()
h1.go_to(13)
h2.go_to(1)
