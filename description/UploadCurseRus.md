#Пример для текстового формата
*format:txt,size:1,font:fat *Something about sea teacher *

**Атрибуты для текстового формата**

* цвет (*format:txt,color:blue *)
* размер: от одного до трех, от малого к большему (*format:txt,size:1 *)
* шрифт (*format:txt,font:fat *)

Если вы пишите то не забудьте о закрываюшем «*» 

*format:txt * Some text * 

#Пример для фото формата

*format:photo,size:2,source:2.jpg *

**Атрибуты для фото формата**

* Цвет (*format:txt,color:blue *) это цвет рамки для фото
* размер: от одного до трех, от малого к большему (*format:txt,size:1 *)
* source (*format:photo,source:1.jpg *) в этом атрибуте хранится путь к файлу

Для загрузки фото вам необходимо поместить его в static/images/curse

#Пример для видео формата

*format:video,size:2,source:1.mp4 *

**Атрибуты для видео формата**

* цвет (*format:txt,color:blue *) это цвет рамки для видео
* размер: от одного до трех, от малого к большему (*format:txt,size:1 *)
* source (*format:video,source:1.mp4 *) в этом атрибуте хранится путь к файлу

Для загрузки видео вам необходимо поместить его в static/video/curse