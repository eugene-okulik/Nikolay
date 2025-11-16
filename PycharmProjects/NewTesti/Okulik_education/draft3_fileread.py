import os

# Папка, где лежит скрипт (работает на любом ПК)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Путь к data.txt относительно скрипта
file_path = os.path.join(script_dir, 'data.txt')

# Для отладки: выведем пути
print("Папка скрипта:", script_dir)
print("Путь к data.txt:", file_path)
print("Файл существует?", os.path.exists(file_path))

# Открываем файл
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        print("Файл прочитан! Содержимое:", data[:100])  # Показываем первые 100 символов
except FileNotFoundError as e:
    print(f"Ошибка: файл не найден. Проверьте, добавлен ли он в репозиторий: {e}")
except Exception as e:
    print(f"Другая ошибка: {e}")
