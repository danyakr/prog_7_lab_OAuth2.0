from requests_oauthlib import OAuth2Session
import os
import sys


CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = "https://localhost:8000/callback"

if not CLIENT_ID or not CLIENT_SECRET:
    print("Ошибка: CLIENT_ID или CLIENT_SECRET не установлены как переменные окружения.")
    sys.exit(1)

AUTHORIZATION_BASE_URL = "https://github.com/login/oauth/authorize"
TOKEN_URL = "https://github.com/login/oauth/access_token"
RESOURCE_URL = "https://api.github.com/user"
SCOPE = ["read:user"]  # Запрашиваемые права доступа

print("--- Шаг 1: Получение кода авторизации ---")
oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=SCOPE)

authorization_url, state = oauth.authorization_url(AUTHORIZATION_BASE_URL)

print(f"Сгенерированное состояние (state): {state}")
print("Перейдите по этой ссылке в браузере для авторизации:")
print(authorization_url)

print("\n--- Шаг 2: Обмен кода на Access Token ---")
redirect_response = input("Вставьте полный URL перенаправления из браузера (включая 'code' и 'state'): ")

try:
    token = oauth.fetch_token(
        TOKEN_URL,
        authorization_response=redirect_response,
        client_secret=CLIENT_SECRET
    )

    print("\nУспешно получен Access Token и другие токены:")
    print(token)

except Exception as e:
    print(f"\nОшибка при обмене кода на токен: {e}")
    sys.exit(1)

print("\n--- Шаг 3: Доступ к защищенному ресурсу ---")

try:
    r = oauth.get(RESOURCE_URL)

    print(f"Статус ответа Resource Server: {r.status_code}")

    if r.status_code == 200:
        print("Ваши данные пользователя GitHub (первые 5 ключей):")
        data = r.json()
        for key in list(data.keys())[:5]:
            print(f"- {key}: {data[key]}")
    else:
        print(f"Ошибка при доступе к ресурсу. Ответ сервера: {r.text}")

except Exception as e:
    print(f"Произошла ошибка при запросе к ресурсу: {e}")