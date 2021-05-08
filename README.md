# Публикация комиксов

Скрипт скачивает случайный комикс с ресурса [xkcd.com](https://xkcd.com/) и публикует его в группе, в социальной сети [ВКонтакте](https://vk.com/).

### Как установить
Клонировать репозиторий на локальный компьютер.
Установить зависимости:
```
pip install requirements.txt
```

Для работы скрипта необходимо установить две переменные окружения:
VK_API_ACCESS_TOKEN - токен для авторизации, процедура [Implicit Flow](https://vk.com/dev/implicit_flow_user).
VK_GROUP_ID - ID группы ВКонтакте, в которой будут публиковаться комиксы. Узнать group_id для вашей группы можно [здесь](https://regvk.com/id/).

Запустить скрипт:
```
python main.py
```

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).


***

# Comics publisher

The script downloads a random comic from the resource [xkcd.com] (https://xkcd.com/) and publishes it in a group on a social network [VK](https://vk.com/).

### How to install
Clone the repository to your local computer.
Install dependencies:
```
pip install requirements.txt
```

For the script to work, set two environment variables:
VK_API_ACCESS_TOKEN - authorization token, procedure [Implicit Flow](https://vk.com/dev/implicit_flow_user).
VK_GROUP_ID - ID of the VKontakte group in which the comics will be published. You can find out the group_id for your group [here](https://regvk.com/id/).

Run script:
```
python main.py
```

### Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
