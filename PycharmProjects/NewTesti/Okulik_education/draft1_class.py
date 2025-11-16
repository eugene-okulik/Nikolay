class Flower:
    def __init__(self, name, stem_length, life_time, freshness, price, color):
        self.name = name
        self.stem_length = stem_length
        self.life_time = life_time
        self.freshness = freshness
        self.price = price
        self.color = color

    def display_info(self):
        return (f'Название: {self.name}, длина стебля: {self.stem_length} см, '
                f'время жизни: {self.life_time} дн, свежесть: {self.freshness} дн, '
                f'цена: {self.price} руб, цвет: {self.color}')


class Cactus(Flower):
    def __init__(self, name="Кактус", stem_length=6, life_time=30, freshness=15, price=100, color="зеленый"):
        super().__init__(name, stem_length, life_time, freshness, price, color)
        self.needles = True


class Rose(Flower):
    def __init__(self, name="Роза", stem_length=50, life_time=7, freshness=5, price=150, color="красный"):
        super().__init__(name, stem_length, life_time, freshness, price, color)
        self.needles = True


class Tulip(Flower):
    def __init__(self, name="Тюльпан", stem_length=40, life_time=5, freshness=3, price=120, color="желтый"):
        super().__init__(name, stem_length, life_time, freshness, price, color)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        """Добавить цветок в букет"""
        self.flowers.append(flower)
        print(f"✅ Добавлен: {flower.name}")

    def total_price(self):
        """Общая стоимость букета"""
        return sum(flower.price for flower in self.flowers)

    def avg_life_time(self):
        """Среднее время жизни цветов в букете"""
        if not self.flowers:
            return 0
        return sum(flower.life_time for flower in self.flowers) / len(self.flowers)

    # def sort_by_freshness(self):
    #     """Сортировка по свежести (по возрастанию)"""
    #     self.flowers.sort(key=lambda flower: flower.freshness)
    #     return "Букет отсортирован по свежести 🎯"
    def sort_by_freshness(self):
        """Сортировка по свежести (по возрастанию)"""
        self.flowers.sort(key=lambda flower: flower.freshness)

        # Выводим названия отсортированных цветов
        print("Букет отсортирован по свежести 🎯")
        for flower in self.flowers:
            print(f"{flower.name}")

    # Использование:
    bouquet.sort_by_freshness()

    def sort_by_price(self):
        """Сортировка по цене (по возрастанию)"""
        self.flowers.sort(key=lambda flower: flower.price)
        return "Букет отсортирован по цене 💰"

    def sort_by_stem_length(self):
        """Сортировка по длине стебля (по возрастанию)"""
        self.flowers.sort(key=lambda flower: flower.stem_length)
        return "Букет отсортирован по длине стебля 📏"

    def sort_by_color(self):
        """Сортировка по цвету (алфавитный порядок)"""
        self.flowers.sort(key=lambda flower: flower.color)
        return "Букет отсортирован по цвету 🎨"

    def find_by_life_time(self, min_days, max_days):
        """Поиск цветов по диапазону времени жизни"""
        return [flower for flower in self.flowers if min_days <= flower.life_time <= max_days]

    def find_by_price(self, max_price):
        """Поиск цветов по максимальной цене"""
        return [flower for flower in self.flowers if flower.price <= max_price]

    def display_bouquet(self):
        """Показать все цветы в букете"""
        if not self.flowers:
            return "Букет пуст 💐"

        result = ["Цветы в букете:"]
        for i, flower in enumerate(self.flowers, 1):
            result.append(f"{i}. {flower.display_info()}")
        return "\n".join(result)


# Создаем экземпляры цветов
cactus = Cactus()
rose = Rose()
tulip = Tulip()

# Создаем букет и добавляем цветы
bouquet = Bouquet()
bouquet.add_flower(cactus)
bouquet.add_flower(rose)
bouquet.add_flower(tulip)

# print("\n" + "=" * 50)
# print(bouquet.display_bouquet())
# print("=" * 50)

# Тестируем методы
print(f"💰 Общая стоимость: {bouquet.total_price()} руб")
print(f"⏰ Среднее время жизни: {bouquet.avg_life_time():.1f} дней")

# Сортировка
print(bouquet.sort_by_price())
print(bouquet.display_bouquet())

# Поиск
print("\n🔍 Поиск цветов с временем жизни 5-10 дней:")
found_flowers = bouquet.find_by_life_time(5, 10)
for flower in found_flowers:
    print(f" - {flower.name}: {flower.life_time} дней")

print("\n🔍 Поиск цветов до 130 руб:")
found_flowers = bouquet.find_by_price(130)
for flower in found_flowers:
    print(f" - {flower.name}: {flower.price} руб")
