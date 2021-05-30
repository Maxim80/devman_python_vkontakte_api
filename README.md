# Публикация комиксов

Скрипт скачивает случайный комикс с ресурса [xkcd.com] (https://xkcd.com/)  и публикует его в группе, в социальной сети [ВКонтакте](https://vk.com/).

### Как установить
Клонируйте репозиторий на локальный компьютер:
```
$ git clone https://github.com/Maxim80/devman_python_vkontakte_api.git
```

Создайте и активируйте виртуальное окружение (рекомендовано). Пример:
```
$ virtualenv -p python3.9 venv
$ source venv/bin/activate
```

Установите зависимости:
```
pip install requirements.txt
```

Получите ключ доступа пользователя, процедура [Implicit Flow](https://vk.com/dev/implicit_flow_user). Он нужен для того, чтобы ваше приложение имело доступ к вашему аккаунту и могло публиковать сообщения в группах. Потребуются следующие права: "photos", "groups",  "wall" и "offline".

Создайте и заполните файл `.env`:
```
VK_API_ACCESS_TOKEN=<ваш access token ВКонтакте>
VK_GROUP_ID=<ID группы ВКонтакте, в которой будут публиковаться комиксы>
```

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
Clone the repository to your local computer:
```
$ git clone https://github.com/Maxim80/devman_python_vkontakte_api.git
```

Create a virtual and activate environment (recommended). Example:
```
$ virtualenv -p python3.9 venv
$ source venv/bin/activate
```

Install dependencies:
```
pip install requirements.txt
```

Get the user's access token, procedure [Implicit Flow](https://vk.com/dev/implicit_flow_user). It is needed so that your application has access to your account and can post messages to groups. The following rights are required: "photos", "groups", "wall" and "offline".

Create and populate a `.env` file:
```
VK_API_ACCESS_TOKEN=<your VK access token>
VK_GROUP_ID=<ID of the VKontakte group in which the comics will be published>
```

Run script:
```
python main.py
```

### Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
