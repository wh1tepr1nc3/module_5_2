class House:
    def __init__(self, name, number_of_floors):
        self.number_of_floors = number_of_floors
        self.name = name

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        print(self.number_of_floors)

    def __str__(self):
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')


h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Домовенок', 8)
# h1.go_to(5)
# h2.go_to(9)

#__str__
h1.__str__()
h2.__str__()

#__len__
h1.__len__()
h2.__len__()
