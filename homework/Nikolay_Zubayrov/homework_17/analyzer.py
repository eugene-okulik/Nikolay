import os
import argparse
import sys  # Добавлено для диагностики
from datetime import datetime


def main():
    print("Скрипт запущен! Аргументы:", sys.argv)  # Добавлено для диагностики

    parser = argparse.ArgumentParser(description="Анализ логов.")
    parser.add_argument('path', nargs='?', help='Путь к папке')  # Сделал опциональным для обработки
    parser.add_argument('--date', help='Дата YYYY-MM-DD')
    parser.add_argument('--text', help='Текст для поиска')

    try:
        args = parser.parse_args()
    except SystemExit:
        print("Ошибка: укажите путь к папке и хотя бы --date или --text.")
        return

    if not args.path:
        print("Ошибка: укажите путь к папке.")
        return

    if not args.date and not args.text:
        print("Укажите --date или --text.")
        return

    search_date = None
    if args.date:
        try:
            search_date = datetime.strptime(args.date, "%Y-%m-%d").date()
        except ValueError:
            print("Неправильная дата. Используйте YYYY-MM-DD.")
            return

    if not os.path.isdir(args.path):
        print("Не папка или папка не существует.")
        return

    files = [f for f in os.listdir(args.path) if os.path.isfile(os.path.join(args.path, f))]
    found = False

    for file in files:
        file_path = os.path.join(args.path, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Ошибка чтения файла {file}: {e}")
            continue

        blocks = {}
        current_dt = None
        current_lines = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                dt = datetime.strptime(line[:19], "%Y-%m-%d %H:%M:%S")
                if current_dt:
                    blocks[current_dt] = current_lines
                current_dt = dt
                current_lines = [line]
            except ValueError:
                if current_dt:
                    current_lines.append(line)
        if current_dt:
            blocks[current_dt] = current_lines

        for dt, lines in blocks.items():
            if search_date and dt.date() != search_date:
                continue
            if args.text:
                for line_num, line in enumerate(lines, 1):
                    if args.text in line:
                        # Исправленный сниппет: правильно берёт слова вокруг текста
                        words = line.split()
                        text_words = args.text.split()
                        # Найдём индекс первого слова текста
                        start_idx = None
                        for i in range(len(words) - len(text_words) + 1):
                            if words[i:i + len(text_words)] == text_words:
                                start_idx = i
                                break
                        if start_idx is not None:
                            start = max(0, start_idx - 5)
                            end = min(len(words), start_idx + len(text_words) + 5)
                            snippet = ' '.join(words[start:end])
                        else:
                            snippet = line  # Если не найдено, весь line
                        found = True
                        print(f"Файл: {file}")
                        print(f"Дата: {dt}")
                        print(f"Строка: {line_num}")
                        print(f"Сниппет: {snippet}")
                        print("-" * 40)

    if not found:
        print("Ничего не найдено.")
