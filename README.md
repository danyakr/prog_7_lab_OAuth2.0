# Лабораторная работа: практика OAuth 2.0 в Python

## Цель работы

Изучение концепций OAuth 2.0 и реализация потоков Authorization Code Flow и Refresh Token с использованием Python.


### Authorization Code Flow

Последовательность действий:
1. Пользователь перенаправляется на сервер авторизации
2. Пользователь предоставляет разрешение
3. Сервер возвращает авторизационный код
4. Клиент обменивает код на access token
5. Клиент использует токен для доступа к ресурсам

## Подготовка окружения

### Установка зависимостей

```bash
python -m venv venv
.venv\Scripts\activate    # для Windows

pip install requests requests-oauthlib google-api-python-client google-auth-oauthlib
```

---

## Задание 1: Authorization Code Flow (GitHub)

### Этап А: Настройка приложения в GitHub

1. Создано OAuth приложение в GitHub Developer Settings
2. Получены учетные данные:
   - **Client ID**: `Ov...iWZM`
   - **Client Secret**: `<скрыт>`
   - **Redirect URI**: `https://localhost:8000/callback`

![Настройка OAuth приложения в GitHub](https://github.com/user-attachments/assets/3f90810c-cb08-4d7d-808e-99698c37d26f)

### Этап Б: Установка переменных окружения

В PowerShell:
```powershell
$env:CLIENT_ID="<Client_ID>"
$env:CLIENT_SECRET="<Client_Secret>"
```

### Этап В: Реализация кода

Файл `oauth_client.py` содержит реализацию Authorization Code Flow.

### Этап Г: Выполнение программы

```bash
python oauth_client.py
```

![Выполнение программы](https://github.com/user-attachments/assets/063b1360-2955-4c71-9d40-b97a5fa39f81)

### Результаты выполнения

```
(.venv) PS C:\Users\d\PycharmProjects\oauth> python oauth_client.py
--- Шаг 1: Получение кода авторизации ---
Сгенерированное состояние (state): qzL0p6CwJd7aKEHyS1WJNjHhIMzJC6
Перейдите по этой ссылке в браузере для авторизации:
https://github.com/login/oauth/authorize?response_type=code&client_id=Ov...iWZM&redirect_uri=https%3A%2F%2Flocalhost%3A8000%2Fcallback&scope=read%3Auser&state=qzL0p6CwJd7aKEHyS1WJNjHhIMzJC6

--- Шаг 2: Обмен кода на Access Token ---
Вставьте полный URL перенаправления из браузера (включая 'code' и 'state'): 
https://localhost:8000/callback?code=540406846fdd4efd2e5a&state=qzL0p6CwJd7aKEHyS1WJNjHhIMzJC6

Успешно получен Access Token и другие токены:
{'access_token': 'gho_s1...Mg', 'token_type': 'bearer', 'scope': ['read:user']}

--- Шаг 3: Доступ к защищенному ресурсу ---
Статус ответа Resource Server: 200
Ваши данные пользователя GitHub (первые 5 ключей):
- login: danyakr
- id: 75899583
- node_id: MDQ6VXNlcjc1ODk5NTgz
- avatar_url: https://avatars.githubusercontent.com/u/75899583?v=4
- gravatar_id:
```

### Результат Задания 1

✅ **Успешно выполнено:**
- Сгенерирован URL авторизации с параметрами `response_type=code`, `client_id`, `redirect_uri`, `scope` и `state`
- Параметр `state` используется для защиты от CSRF-атак
- Получен авторизационный код через редирект
- Код успешно обменян на access token
- Access token использован для запроса защищенного ресурса (информация о пользователе GitHub)
- Получен ответ со статусом 200 и данными пользователя

---

## Задание 2: Refresh Token (Google APIs)

### Этап А: Настройка в Google Cloud Console

1. Создан проект в Google Cloud Console
2. Настроены OAuth 2.0 учетные данные
3. Загружен файл `client_secret.json`

### Этап Б: Реализация кода

Файл `google_refresh_token.py` содержит реализацию получения Refresh Token.

### Этап В: Выполнение программы

```bash
python google_refresh_token.py
```

### Результаты выполнения

```
(.venv) PS C:\Users\d\PycharmProjects\oauth> python google_refresh_token.py
--- Шаг 1: Запрос кода авторизации ---
1. Перейдите по этой ссылке, чтобы авторизовать доступ:
https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=745511312737-orh8j9fsq9dfufa0luf6el3mrdtsra83.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Flocalhost%3A8080%2Fauth%2Fgoogle%2Fcallback&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fphotoslibrary.readonly&state=pcROH0XNisSc4QINj6JX6hjwGI0Uge&access_type=offline&include_granted_scopes=true

--- Шаг 2: Ввод кода ---
2. Вставьте полный URL перенаправления из браузера (с параметрами code и state): 
https://localhost:8080/auth/google/callback?state=pcROH0XNisSc4QINj6JX6hjwGI0Uge&code=4/0Ab32j92-syiq0Kg99-vhQfHl6eGoTsAnSIPAHnlQACY4MqiLPn_NW6AW6m_aiWw7O91ZVw&scope=https://www.googleapis.com/auth/photoslibrary.readonly

Успешно получены токены:
{
  "token": "ya29.a0ATi6K2tXdsUbYN...",
  "refresh_token": "1//0cKa...OJhhaI",
  "token_uri": "https://oauth2.googleapis.com/token",
  "client_id": "74551131273...ra83.apps.googleusercontent.com",
  "client_secret": "GO...DJ",
  "scopes": [
    "https://www.googleapis.com/auth/photoslibrary.readonly"
  ],
  "universe_domain": "googleapis.com",
  "account": "",
  "expiry": "2025-10-25T17:41:45Z"
}

Refresh Token успешно получен и готов к использованию для обновления Access Token.
```

### Результат Задания 2

- Сформирован URL авторизации с параметром `access_type=offline` для получения refresh token
- Получен авторизационный код
- Успешно получены access token и refresh token
- Refresh token сохранен и может использоваться для обновления access token после истечения срока действия
- Указано время истечения токена: `2025-10-25T17:41:45Z`

---

## Контрольные вопросы

### 1. Основные роли в протоколе OAuth 2.0

- **Resource Owner (Владелец ресурса)** — пользователь, владеющий защищенными данными и предоставляющий доступ к ним
- **Client (Клиент)** — приложение, запрашивающее доступ к ресурсам от имени пользователя
- **Authorization Server (Сервер авторизации)** — выдает токены доступа после успешной аутентификации и авторизации
- **Resource Server (Сервер ресурсов)** — хранит защищенные ресурсы и обслуживает запросы с валидным access token

### 2. Что такое Authorization Code?

**Authorization Code** — временный код, выдаваемый Authorization Server после того, как пользователь предоставляет разрешение. Этот код обменивается на access token. 

**Назначение:**
- Разделение процесса авторизации на два этапа для повышения безопасности
- Предотвращение утечки access token через браузер пользователя
- Позволяет аутентифицировать клиентское приложение через client_secret

### 3. Зачем нужен параметр state?

Параметр `state` используется для **защиты от CSRF-атак (Cross-Site Request Forgery)**:
- Клиент генерирует случайное значение и отправляет его в запросе авторизации
- Authorization Server возвращает это значение вместе с кодом
- Клиент проверяет совпадение значений
- Если значения не совпадают, запрос отклоняется как потенциально вредоносный

### 4. Отличия Authorization Code Flow от Client Credentials Flow

| Характеристика | Authorization Code Flow | Client Credentials Flow |
|---|---|---|
| **Участие пользователя** | Требуется авторизация пользователя | Не требуется |
| **Применение** | Доступ к ресурсам пользователя | Доступ к ресурсам приложения |
| **Токены** | Access token, опционально refresh token | Только access token |
| **Сценарии** | Веб/мобильные приложения от имени пользователя | Серверное взаимодействие между приложениями |
| **Безопасность** | Пользователь не передает пароль клиенту | Требуется надежное хранение client_secret |

### 5. Когда используется refresh token?

**Refresh token** используется в следующих случаях:

- **Обновление access token** — когда срок действия access token истекает, refresh token позволяет получить новый без повторной авторизации пользователя
- **Долгосрочный доступ** — для приложений, требующих постоянного доступа к ресурсам пользователя
- **Улучшение безопасности** — access token имеет короткий срок жизни (минуты/часы), refresh token — длительный (дни/месяцы)
- **Снижение нагрузки** — пользователю не нужно заново проходить процесс авторизации

**Важно:** Refresh token должен храниться безопасно, так как его компрометация дает долгосрочный доступ к ресурсам.

---



# prog_7_lab_OAuth2.0

pip install requests requests-oauthlib google-api-python-client google-auth-oauthlib

Задание 1: Authorization Code Flow (GitHub)
Этап А: Настройка Приложения (GitHub)
<img width="974" height="1040" alt="image" src="https://github.com/user-attachments/assets/3f90810c-cb08-4d7d-808e-99698c37d26f" />

Установите переменные окружения: В PowerShell установите полученные секреты

$env:CLIENT_ID="<Client_ID>"
$env:CLIENT_SECRET="<Client_Secret>"

файл oauth_client.py

python oauth_client.py
<img width="989" height="833" alt="image" src="https://github.com/user-attachments/assets/063b1360-2955-4c71-9d40-b97a5fa39f81" />

```
(.venv) PS C:\Users\d\PycharmProjects\oauth> python oauth_client.py
--- Шаг 1: Получение кода авторизации ---
Сгенерированное состояние (state): qzL0p6CwJd7aKEHyS1WJNjHhIMzJC6
Перейдите по этой ссылке в браузере для авторизации:
https://github.com/login/oauth/authorize?response_type=code&client_id=Ov...iWZM&redirect_uri=https%3A%2F%2Flocalhost%3A8000%2Fcallback&scope=read%3Auser&state=qzL0p6CwJd7aKEHyS1WJNjHhIMzJC6

--- Шаг 2: Обмен кода на Access Token ---
Вставьте полный URL перенаправления из браузера (включая 'code' и 'state'): https://localhost:8000/callback?code=540406846fdd4efd2e5a&state=qzL0p6CwJd7aKEHyS1WJNjHhIMzJC6

Успешно получен Access Token и другие токены:
{'access_token': 'gho_s1...Mg', 'token_type': 'bearer', 'scope': ['read:user']}

--- Шаг 3: Доступ к защищенному ресурсу ---
Статус ответа Resource Server: 200
Ваши данные пользователя GitHub (первые 5 ключей):
- login: danyakr
- id: 75899583
- node_id: MDQ6VXNlcjc1ODk5NTgz
- avatar_url: https://avatars.githubusercontent.com/u/75899583?v=4
- gravatar_id:

```

Задание 2: Refresh Token (Google APIs)

Google Cloud Console
файл client_secret.json и сохраните его в папке проекта

файл google_refresh_token.py

python google_refresh_token.py

```
(.venv) PS C:\Users\d\PycharmProjects\oauth> python google_refresh_token.py
--- Шаг 1: Запрос кода авторизации ---
1. Перейдите по этой ссылке, чтобы авторизовать доступ:
https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=745511312737-orh8j9fsq9dfufa0luf6el3mrdtsra83.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Flocalhost%3A8080%2Fauth%2Fgoogle%2Fcallback&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fphotoslibrary.readonly&state=pcROH0XNisSc4QINj6JX6hjwGI0Uge&access_type=offline&include_granted_scopes=true

--- Шаг 2: Ввод кода ---
2. Вставьте полный URL перенаправления из браузера (с параметрами code и state): https://localhost:8080/auth/google/callback?state=pcROH0XNisSc4QINj6JX6hjwGI0Uge&code=4/0Ab32j92-syiq0Kg99-vhQfHl6eGoTsAnSIPAHnlQACY4MqiLPn_NW6AW6m_aiWw7O91ZVw&scope=https://www.googleapis.com/auth/photoslibrary.readonly

Успешно получены токены:
{
  "token": "ya29.a0ATi6K2tXdsUbYN...",
  "refresh_token": "1//0cKa...OJhhaI",
  "token_uri": "https://oauth2.googleapis.com/token",
  "client_id": "74551131273...ra83.apps.googleusercontent.com",
  "client_secret": "GO...DJ",
  "scopes": [
    "https://www.googleapis.com/auth/photoslibrary.readonly"
  ],
  "universe_domain": "googleapis.com",
  "account": "",
  "expiry": "2025-10-25T17:41:45Z"
}

Refresh Token успешно получен и готов к использованию для обновления Access Token.

```





