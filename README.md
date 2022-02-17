# NearestCashiersBot

### Ejercicio 1

Geohash: https://en.wikipedia.org/wiki/Geohash

Para poder encontrar a los cajeros dentro de un rango de 500m obtuve el geohash de cada cajero 
y almacene estos geohashes en un diccionario de la forma {clave_geohash : lista_de_bancos} en memoria. 
Luego, una vez recibida la consulta use una funcion de terceros que me permite obtener una serie de
geohashes que cubren circularmente el punto solicitado, con el rango pedido(500m).
Por cada geohash que estaba dentro del rango de los 500m del punto usado en la consulta,
me fije si existian bancos en ese geohash. Si era el caso, agregaba el o los bancos
de ese geohash a los resultados.


En conclusion, la consulta tiene una complejidad de O(K=3) ≈ O(1)
siendo k la cantidad de cajeros que se recorren para obtener los 3 cajeros resultantes. Ahora bien, las operaciones que se hacen despues
de responder la consulta al usuario no son de orden constante, ya que, hay que actualizar
la base de datos y realizar otras operaciones. Igualmente, esto ultimo tambien
se podria optimizar pero no estaba en los requerimientos del enunciado.

### Ejercicio 3

Para que el sistema sea resistente a reinicios y caidas, persisti
la cantidad de extracciones disponibles restantes de los cajeros
en una base de datos PostgreSQL.
Esta cantidad de extracciones disponibles es una estimacion, ya que, no se sabe
con certeza sobre que cajero se hara la extraccion luego de cada consulta al bot.  

Para el reabastecimiento de los cajeros, deje disponible un metodo en el modelo
(load_cashiers) que cambiara el estado de todos los cajeros(reiniciando la cantidad de
extracciones disponibles) tanto en la tabla como en memoria.

##Requerimientos:

python3.76+ version

##Librerias:

pip install python-telegram-bot

pip install geolib


