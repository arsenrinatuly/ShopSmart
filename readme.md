🛒 ShopSmart

ShopSmart — это приложение для ведения совместного списка покупок в реальном времени. Пользователи могут делиться ссылкой на список и редактировать его одновременно — все изменения синхронизируются через WebSocket.
📌 О проекте

    ShopSmart — учебный проект, реализованный на Django с использованием WebSocket.
    Пользователь может создавать список покупок, делиться им по ссылке и редактировать его вместе с другими в реальном времени.

    🧠 Backend реализован самостоятельно на Django.

    🌐 WebSocket-связь через Daphne и Django Channels.

    ⚡ JavaScript-фронт написан с помощью ИИ (ChatGPT).

    🖥️ Интерфейс — простой HTML/CSS + JS

⚙️ Стек технологий

    Backend: Django, Django Channels, Daphne

    Frontend: HTML / CSS / JavaScript (генерировался с помощью ИИ)

    Веб-сокеты: WebSocket API + Channels

    База данных: PostgreSQL

    Хостинг: Render (планируется)

🚀 Запуск проекта (локально)

# 1. Клонировать репозиторий
git clone https://github.com/your-username/shopsmart.git
cd shopsmart

# 2. Создать и активировать виртуальное окружение
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Настроить переменные окружения
cp .env.example .env

# 5. Применить миграции
python manage.py migrate

# 6. Собрать статические файлы
python manage.py collectstatic

# 7. Запустить сервер через Daphne
daphne -b 0.0.0.0 -p 8000 shopsmart.asgi:application

🌐 WebSocket

    WebSocket работает через Django Channels.

    Протокол подключается на фронте через чистый JavaScript.

    Все изменения в списке синхронизируются мгновенно между участниками.

💻 Интерфейс

    Минималистичный UI на HTML/CSS.

    Весь JavaScript-фронтенд написан с помощью ИИ.

    Интерфейс адаптирован под мобильные устройства.

    В будущем возможна реализация iOS-приложения.

🙌 Заключение

    Этот проект — моя попытка создать простой, но полезный продукт, который может пригодиться в повседневной жизни.

📬 Контакты

    Автор: Arsen Rinatuly


    Email: suttibaevrinat@gmail.com
