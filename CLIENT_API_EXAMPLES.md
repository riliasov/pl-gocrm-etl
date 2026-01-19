# Примеры данных Client API (Демо)

Ниже приведены структуры данных, которые мы получим после авторизации с `APP_TOKEN`.

### 1. Профиль родителя (`GET /profile`)
```json
{
  "status": "success",
  "data": {
    "id": 123,
    "fio": "Иванов Иван Иванович",
    "phone": "+79100019301",
    "email": "ivanov@example.com",
    "birthday": "1985-05-20"
  }
}
```

### 2. Список детей (`GET /clients`)
*Здесь мы видим всех детей, привязанных к этому родителю.*
```json
{
  "status": "success",
  "data": [
    {
      "id": 456,
      "fio": "Иванов Петр Иванович",
      "phone": "+79100019302",
      "birthday": "2018-10-12"
    }
  ]
}
```

### 3. Абонементы и Баланс (`GET /client-season-tickets`)
*Ответ на вопрос: Можно ли считать остаток? Да, поле `balance` показывает остаток занятий.*
```json
{
  "status": "success",
  "data": [
    {
      "id": 789,
      "clientId": 456,
      "seasonTicketName": "Плавание груп. 8 занятий",
      "price": 3000.0,
      "numberExercise": 8,
      "balance": 3,
      "validityDate": "2024-05-24",
      "blockTypeName": "Активный"
    }
  ]
}
```
> **Вывод**: В этом примере клиент купил 8 занятий, осталось 3.

### 4. Посещения и Пропуски (`GET /client-hours`)
```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "visited": "visited",
      "missed": "",
      "hour": {
        "datetime": "2024-01-07 12:00:00",
        "duration": 60,
        "comment": "Хорошо занимался"
      }
    }
  ]
}
```

### 5. Долги (`GET /debts`)
```json
{
  "status": "success",
  "data": [
    {
      "centerId": 1,
      "address": "ул. Давлеткильдеева 16",
      "money": 500.0,
      "currency": "руб."
    }
  ]
}
```
