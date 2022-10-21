# Piedra Papel Tijera Lagarto Spock 
# (Rock Paper Scissors Lizard Spock)

Esquema del juego:

1. Se le pide al usuario que elija de entre unas opciones (piedra, papel, tijera, lagarto, y Spock).
2. Creamos una jugada a partir de lo que haya elegido el usuario.
3. Creamos otra jugada al azar para competir con la del usuario.
4. Las comparamos y determinamos quién ha ganado.
5. Si el usuario así lo desea, jugamos otra partida.


## Claves

El juego es un bucle, del que no se sale hasta que el usuario así lo pide.

Hay que modelar las jugadas y su comparación. Usaremos clases para ello.


## Comparación

* Tijeras cortan a Papel
* Papel envuelve a Piedra
* Piedra aplasta a Lagarto
* Lagarto envenena a Spock
* Spock rompe a Tijeras
* Tijeras decapitan a Lagarto
* Lagarto devora a Papel
* Papel desautoriza a Spock
* Spock vaporiza a Piedra
* Piedra aplasta a Tijeras


## Mejoras

1. Hacer que get_user_response NO devuelva una cadena, sino una enum.
2. Para la implementación de compare no usar el type de un objeto. Python ya sabe comparar objetos para ver si uno es mayor que otro __lt__, __gt__, __eq__ Reimplementar con dunders y simplifcar get_winner.

3. Ampliarlo a Rock, paper, scissors, lizard, spock.

![](http://geekandsundry.com/wp-content/uploads/2015/05/Rock-Paper-Scissors-Lizard-Spock.jpg)
