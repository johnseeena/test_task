# 1. Функция для поиска уникальных элементов в списке
def unique_elements(input_list):
    return list(set(input_list))

# 2. Функция для нахождения простых чисел в заданном диапазоне
def prime_numbers_in_range(min_num, max_num):
    prime_numbers = []
    for num in range(min_num, max_num + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    return prime_numbers

# 3. Класс Point для работы с точками
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

    def get_coordinates(self):
        return (self.x, self.y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

# 4. Программа для сортировки списка строк по длине
def sort_strings(input_list):
    return sorted(input_list, key=lambda x: (len(x), x))

if __name__ == "__main__":
    input_list = [1, 2, 2, 3, 4, 4, 5]
    print("Уникальные элементы в списке:", unique_elements(input_list))

    min_num = 10
    max_num = 30
    print("Простые числа в диапазоне от", min_num, "до", max_num, ":", prime_numbers_in_range(min_num, max_num))

    point1 = Point(1, 1)
    point2 = Point(4, 5)
    print("Расстояние между точками point1 и point2:", point1.distance_to(point2))

    strings_list = ["hello", "world", "python", "is", "great"]
    print("Список строк после сортировки по длине:", sort_strings(strings_list))
