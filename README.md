# Djnago Datins Site
This web app has been developed using the popular Django framework and Bootstrap for the frontend. My motivation to build this project is so that I can learn about Django and tighten up my skills. This mini-app can be easily integrated into a bigger system project that needs to have a registration and login system.

### Basic Features of The App
*/register - Регистрация пользователя <br>
*/login - Авторизация пользователя <br>
*/profile - Редактирование профиля(при добавлении картинки ставиться водяной знак), также можно поменять пароль<br>
*/profiles/int:profile_id - Можно зайти на профиль к зарегистрированному человеку(в расстоянии показывается кол-во км от вас до человека)
*/logout - Выйти из системы
Для того, чтобы отправлялись сообщения на почты во views.pofiles нужно вписать майл и пароль, откда будут отпраляться письма
При нажатии кнопки "Like" в профиле создается таблица в бд, и если лайк взаимный, то на почту приходит уведомление c username
### Quick Start
Чтобы запустить проект на локальном сервере следйте этим шагам:
1.Пропишите эти команды в такой же последовательности
    * pip install -r requirements.txt
    * python manage.py makemigrations
    * python manage.py migrate
    * python manage.py createsuperuser
    * python manage.py runserver
   
2.Откройте браузер и перейдите на  http://localhost:8000/

