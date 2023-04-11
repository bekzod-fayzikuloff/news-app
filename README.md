Запуск с режиме разработки для просмотра можно осуществить в докер командой
``docker-compose -f docker-compose.dev.yml -f docker-compose.yml up --build``

Изображения с примерами работы приложения находятся в папке `./images`
[Внешний вид запущенного приложения со списком всех новостей](./images/img.png) <br/>
Вначале подгружается только часть новостей и дальнейшая подгрузка по 3 новых новостей
[Подгрузка без перезагрузки дополнительных новостей](./images/img_1.png)<br/>
[Также получение без перезагрузки дополнительных новостей](./images/img_2.png)<br/>
[Просмотр содержания новости](./images/img_3.png)<br/>
[Страница со статистикой новости (Количество просмотров)](./images/img_4.png)<br/>
[Страница со статистикой новости  (Пример изменения количества просмотров при повторном просмотре новости)](./images/img_5.png)<br/>
[Страница со примером фильтрации новостей по тэгам (Также поддерживает бесконечный скрол)](./images/img_6.png)<br/>
[Документация API](./images/img_8.png)<br/>
[Внешний вид кнопок `like` и `dislike`](./images/img_9.png)<br/>
[Сохранения состояния после перезагруки страницы](./images/img_10.png)<br/>
[Пример с кнопкой дизлайк](./images/img_11.png)<br/>
