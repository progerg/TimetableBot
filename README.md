# Бот для напоминания расписания

Этот бот был создан ленивым студентом ФКН для других ленивых студентов ФКН
Открываешь короче бота, пишешь курс, группу, подгруппу и получаешь всё, что тебе надо. 
Больше никаких ужасных расписаний, где предстоит разобраться с числителем и знаменателем

## Что умеет бот?
- Отправлять расписание студентам 1 курса (в дальнейшем добавим и остальные)
- Скоро будут и другие функции после предложений

## Что по технической части?
- Язык программирования (как уже подсказал github) - python или как ещё называют питон или питухон
- В качестве прослойки юзал vkbottle, так как один из самых лучший
- БД - postgresql (в целом если чуть-чуть постараться, то можете поменять пару строчек для остальных)
- Ну и ORM-очку не забыл - sqlalchemy

## А как "адаптировать" код-то?
Всё просто
```sh
mkdir communism
cd communism
git clone https://github.com/progerg/TimetableBot
cd TimetableBot/bot
```

Потом предстоит там файлик .env создать со следующим содержанием, где заполняешь свои данные
```
token = {}

db_login = {}
db_password = {}
db_name = {}
db_host = {}
db_port = {}
```

После этого просто делаешь
```sh
cd ../
docker compose up --build -d
```

Готово, поздравляю, ты скоммуниздил код

## В каких случаях так делать не стоит?

- Если тебе надо именно добавить свое расписание, то можешь предложить это мне в issue
- Если тебе надо внести новые функции, то меняй их тут и предложи изменения, так мы сможем допилить до идеала

Ну в целом, если надо именно для другого ВУЗа, то возможно прикольнее будет своего поднять, но скоро я планирую добавить и поддержку ВУЗов, поэтому если хочешь помочь, то буду рад)