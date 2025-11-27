FROM python:3.12.0

WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Копируем скрипт ожидания БД
COPY wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh

EXPOSE 8000

# Запускаем скрипт ожидания, который потом стартует Gunicorn
CMD ["/wait-for-db.sh"]
