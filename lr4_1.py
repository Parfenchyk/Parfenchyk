import datetime


class House:
    def_area = 55
    def_room = 2

    def __init__(self, id_N, apartment_number, area, floor, room, street, building_type, year_of_building, lifetime):
        self.__id_N = id_N
        self.__apartment_number = apartment_number
        self.__area = area
        self.__floor = floor
        self.__room = room
        self.__street = street
        self.__build_type = building_type
        self.__lifetime = lifetime
        self.__year_of_building = year_of_building

    def get_id_N(self):
        return self.__id_N

    def get_apartment_number(self):
        return self.__apartment_number

    def set_apartment_number(self, new_apartment_number):
        if new_apartment_number > 0:
            self.__apartment_number
        else:
            raise ValueError("apartment_number must be more then zero")

    def get_area(self):
        return self.__area

    def get_floor(self):
        return self.__floor

    def get_room(self):
        return self.__room

    def get_street(self):
        return self.__street

    def set_street(self, new_street):
        if isinstance(new_street, int):
            self.__street
        else:
            raise ValueError("Street should be a string")

    def get_building_type(self):
        return self.__build_type

    def get_lifetime(self):
        return self.__lifetime

    def get_year_of_building(self):
        return self.__year_of_building

    # проверка возраста здания для сноса (EXTERMINATE)
    @staticmethod
    def get_house_demolition(house):
        current_year = datetime.datetime.now().year  # текущий год
        if (current_year - house.get_year_of_building()) < house.get_lifetime():
            return print("not yet time")
        return print("EXTERMINATE this building!!!")

    @classmethod
    def house_without_address(cls):
        house_without_address = cls(11, 190, 56.2, 11, 3, None, "residential", 1990, 22)
        return house_without_address

    def __str__(self):
        return f"Номер квартиры: {self.__apartment_number}, этаж {self.__floor}, улица: {self.__street}," \
               f"год постройки: {self.__year_of_building}"


houses = [
    House(1, 19, 56.2, 2, 2, "Ponomareva", "residential", 1890, 50),
    House(2, 38, 56.2, 3, 3, "Sadovaya", "non-residential", 1900, 33),
    House(3, 57, 56.2, 4, 2, "Belyaeva", "residential", 1910, 44),
    House(4, 76, 56.2, 5, 3, "Heroes of 120th division", "residential", 1920, 55),
    House(5, 95, 56.2, 6, 4, "Vodolazhskogo", "residential", 1930, 66),
    House(6, 114, 56.2, 7, 3, "Pochtovaya", "residential", 1940, 77),
    House(7, 133, 56.2, 8, 3, "50th years of Victory", "non-residential", 1950, 88),
    House(8, 152, 56.2, 9, 2, "Rogachevskaya", "residential", 1960, 99),
    House(9, 171, 56.2, 10, 2, "Osnovatelei", "residential", 1970, 11),
    House(10, 190, 56.2, 11, 3, "Gvishiani", "residential", 1980, 22)

]

# вывод списка квартир, имеющих заданное число комнат;
apartment_number_room_2 = [house for house in houses if house.get_room() == 2]
print("Список квартир, имеющих заданное число комнат:")
for house in apartment_number_room_2:
    print(house)
    house.get_house_demolition(house)
print(' ', end="\n")
# вывод списка квартир, имеющих заданное число комнат и
# расположенных на этаже, который находится в заданном промежутке;

apartment_number_room_2_floor = [house for house in houses if house.get_room() == 2 and (2 < house.get_floor() <= 9)]
print("Список квартир, имеющих заданное число комнат и расположенных на этаже, \n"
      "который находится в заданном промежутке:")
for house in apartment_number_room_2_floor:
    print(house)
print(' ', end="\n")
# вывод квартиры методом класса
print(House.house_without_address())