Django Async REST API
Ushbu loyiha Django 4.2+ va Asynchronous Django REST Framework (ADRF) yordamida qurilgan asinxron API namunasi hisoblanadi. Loyiha yuqori unumdorlik va asinxron ma'lumotlar bazasi so'rovlarini qo'llab-quvvatlaydi.

🚀 Texnologiyalar
Python 3.10+

Django 5.x (Async support)

ADRF (Async Django REST Framework)

Uvicorn (ASGI Server)

drf-spectacular (OpenAPI 3.0 / Swagger UI)

🛠 O'rnatish
Virtual muhitni yarating va faollashtiring:

Bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
Zarur kutubxonalarni o'rnating:

Bash
pip install django adrf uvicorn drf-spectacular
Statik fayllarni yig'ing (Swagger uchun):

Bash
python manage.py collectstatic
Migratsiyalarni amalga oshiring:

Bash
python manage.py migrate
⚙️ Sozlamalar (ASGI Configuration)
Loyihaning asinxron ishlashi uchun settings.py da quyidagilar sozlangan:

Python
# settings.py
INSTALLED_APPS = [
    ...
    'adrf',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    ...
]

# ASGI server sozlamasi
ASGI_APPLICATION = 'conf.asgi.application'

# REST Framework sxemasi
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
📖 API Hujjatlari (Swagger)
Loyiha ishga tushgandan so'ng, API hujjatlarini quyidagi manzillarda ko'rishingiz mumkin:

Swagger UI: http://127.0.0.1:8000/api/schema/swagger-ui/

Redoc: http://127.0.0.1:8000/api/schema/redoc/

Schema (YAML): http://127.0.0.1:8000/api/schema/

💻 Loyihani ishga tushirish
Asinxron rejimda ishlash uchun loyihani Uvicorn orqali ishga tushiring:

Bash
uvicorn conf.asgi:application --reload