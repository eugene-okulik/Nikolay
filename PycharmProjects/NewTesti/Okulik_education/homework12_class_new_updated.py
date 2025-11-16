class Flowers:
    def __init__(self, name, stem_length, life_time, freshness, price, color):
        self.name = name
        self.stem_length = stem_length
        self.life_time = life_time
        self.freshness = freshness
        self.price = price
        self.color = color

    def display_info(self):
        return (f'название: {self.name}, длина стебля: {self.stem_length} см, время жизни: {self.life_time} дн,'
                f'свежесть: {self.freshness} дн, цена: {self.price} руб,  цвет: {self.color}')


class Cactus(Flowers):
    def __init__(self, name, stem_length, life_time, freshness, price, color):
        super().__init__(name, stem_length, life_time, freshness, price, color)


class Rose(Flowers):
    def __init__(self, name, stem_length, life_time, freshness, price, color):
        super().__init__(name, stem_length, life_time, freshness, price, color)


class Tulip(Flowers):
    def __init__(self, name, stem_length, life_time, freshness, price, color):
        super().__init__(name, stem_length, life_time, freshness, price, color)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flowers(self, flower):
        self.flowers.append(flower)
        return f"{flower.name} добавлен в букет."

    def total_price(self):  # общая стоимость
        return sum(flower.price for flower in self.flowers)

    def avg_life_time(self):  # среднее время жизни
        if not self.flowers:
            return 0
        return sum(flower.life_time for flower in self.flowers) / len(self.flowers)

    def sort_by_freshness(self):  # сортировка по свежести
        self.flowers.sort(key=lambda flower: flower.freshness)
        return [flower.name for flower in self.flowers]

    def sort_by_color(self):  # сортировка цветов по цвету
        self.flowers.sort(key=lambda flower: flower.color)
        return [(flower.name, flower.color) for flower in self.flowers]

    def sort_by_stem_length(self):  # сортировка по длине стебля
        self.flowers.sort(key=lambda flower: flower.stem_length)
        return [(flower.name, flower.stem_length) for flower in self.flowers]

    def find_by_lifetime(self, min_lifetime=2, max_lifetime=5):  # Поиск цветов по среднему времени жизни
        result = []
        for flower in self.flowers:
            if min_lifetime <= flower.life_time <= max_lifetime:
                result.append(flower)
        return result


# Тестирование
cactus = Cactus('кактус', 6, 2, 11, 100, 'зеленый')
rose = Rose('роза', 7, 5, 2, 150, 'красный')
tulip = Tulip('тюльпан', 9, 3, 2, 160, 'желтый')
bouquet = Bouquet()

print(bouquet.add_flowers(cactus))
print(bouquet.add_flowers(rose))
print(bouquet.add_flowers(tulip))
print()
print(f'общая стоимость {bouquet.total_price()} рублей')
print(f'среднее время жизни всех цветов {bouquet.avg_life_time()} дней')

# Сортировка по свежести
print("Цветы в букете, отсортированные по свежести:")
print(bouquet.sort_by_freshness())
print()

# Сортировка по цвету
print("Цветы в букете, отсортированные по цвету:")
for name, color in bouquet.sort_by_color():
    print(f"{name} {color}")
print()

# Сортировка по длине стебля
print("Цветы в букете, отсортированные по длине стебля:")
for name, length in bouquet.sort_by_stem_length():
    print(f"{name} - {length} см")

# Поиск по времени жизни
print("\nЦветы с временем жизни от 2 до 5 дней:")
found_flowers = bouquet.find_by_lifetime(2, 5)
for flower in found_flowers:
    print(f"{flower.name} - {flower.life_time} дней")

    # def sort_by(self, key):
    #     self.flowers.sort(key=lambda flow: getattr(flow, key)) альтернатива
