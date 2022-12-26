# entityProperies 

TEST create/list M2M

## instalation

```bash
git clone https://github.com/DenisDolmatov2020/entityProperies.git

cd entityProperties

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## URLS

### localhost:8000/api/item/


# Задание

## Вопросы
### 1. Как правильно сохранять modified_by?
Пояснение: при создании записи в запросе приходит только value, но в БД нужно записать не только value, но и того пользователя, который сделал POST-запрос.
Подсказка: Модели и сериализатор остаются неизменными

### 2. Для создания Entity на вход POST API подаётся json вида

```{"data[value]": 10}```

Как исправить сериализатор так, чтобы он мог принять поле "data[value]" и сохранить его в поле value?
Пояснение: Python не позволит написать в сериализаторе 
```data[value] = IntegerField(...)```, но есть другое решение 

Подсказка: Модели остаются неизменными

### 3. Как вывести propertiesв формате {key:value, ...}, если мы заранее не знаем сколько и каких key может быть?
Пояснение: Иногда нужно вывести данные, когда имена полей заранее неизвестны. См. пример ниже. Не обращайте внимания на то, что value - строка, это всего лишь пример, как может выглядеть properties.


```json

[ 
  {
    "value": "circle",
    "properties": {
      "center": "100, 100",
      "radius": "50"
    }
  },
  {
    "value": "line",
    "properties": {
      "start": "150, 50",
      "end": "50, 150"
    }
  },
  {
    "value": "Медведь",
    "properties": {
      "класс": "Млекопитающие"
    }
  },
  {
    "value": "rectangle",
    "properties": {
      "corner_1": "50, 50",
      "corner_2": "150, 150"
    }
  }
]

```
