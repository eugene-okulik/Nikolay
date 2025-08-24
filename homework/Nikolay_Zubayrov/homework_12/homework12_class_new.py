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
    needles = True


class Rose(Flowers):
    needles = True


class Tulip(Flowers):
    needles = False


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flowers(self, flower):
        self.flowers.append(flower)
        return f"{flower.name} добавлен в букет."

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def avg_life_time(self):
        return sum(flower.life_time for flower in self.flowers) / len(self.flowers)

    def max_freshness(self):
        return sorted(max(flower.freshness for flower in self.flowers))

    def min_freshness(self):
        return sorted(flower.freshness for flower in self.flowers)

    def color(self):
        return sorted(flower.color for flower in self.flowers)


cactus = Cactus('кактус', 6, 2, 11, 100, 'зеленый')
rose = Rose('роза', 7, 3, 2, 150, 'красный')
tulip = Tulip('тюльпан', 9, 3, 2, 160, 'желтый')

bouquet = Bouquet()
print(bouquet.add_flowers(cactus))
print(bouquet.add_flowers(rose))
print(bouquet.add_flowers(tulip))
print(f'общая стоимость {bouquet.total_price()} рублей')
print(f'среднее время жизни всех цветов {bouquet.avg_life_time()} часов')
print(bouquet.color())
print(min(bouquet.min_freshness()))
print(max(bouquet.min_freshness()))
