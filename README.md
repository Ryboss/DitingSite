# Djnago Datins Site
### Basic Features of The App
*/register - Регистрация пользователя <br>
*/login - Авторизация пользователя <br>
*/profile - Редактирование профиля(при добавлении картинки ставиться водяной знак), также можно поменять пароль<br>
*/profiles/int:profile_id - Можно зайти на профиль к зарегистрированному человеку(в расстоянии показывается кол-во км от вас до человека)<br>
*/logout - Выйти из системы<br>
Для того, чтобы отправлялись сообщения на почты во views.pofiles нужно вписать майл и пароль, откда будут отпраляться письма<br>
При нажатии кнопки "Like" в профиле создается таблица в бд, и если лайк взаимный, то на почту приходит уведомление c username<br>
### Quick Start
Чтобы запустить проект на локальном сервере следйте этим шагам:
1.Пропишите эти команды в такой же последовательности
    * pip install -r requirements.txt<br>
    * python manage.py makemigrations<br>
    * python manage.py migrate<br>
    * python manage.py createsuperuser<br>
    * python manage.py runserver
   
2.Откройте браузер и перейдите на  http://localhost:8000/

