# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с программой в контейнер
COPY task_docker.py /app/task_docker.py

# Команда для запуска программы
CMD ["python", "task_docker.py"]