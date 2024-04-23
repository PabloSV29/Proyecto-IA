# Proyecto-IA
Desarrollo de proyecto de IA del juego conecta-4 
Descripcion del juego: El juego es de a 2 jugadores en el que consiste en formar una linea de 4 fichas que se van ingresando al tablero, en el cual cada jugador escoge su mejor jugada en el que trata de impedir que el otro gane. 
Solucion: Para este caso de implementará una IA que permita jugar con una personal real y que permita realizar jugadas estrategicas para oponerse al jugador, en el cual a medida que juege aprenda de las jugadas pasadas para implementar mejores jugadas en juegos futuros.
Descricion del ambiente:
Es observable porque en todo momento tiene de vista el tablero que tiene de frente en el que las jugaddas son visibles para ambas partes.
Determinista debido a que la jugada de alguno de los 2 jugadores, no va a cambiar una vez que cambie de turno.
Episodico dado que no hay dependencia de los movimientos anteriores con algun movimiento actual.
Estatico: Debido a que no hay movimientos del otro jugador una vez su turno ha acabado, es decir, el agente podria estar pensando en donde colocar una ficha y el tablero en toda esa instancia no cambia.
Discreto: Ya que los agentes tienen una cnatidad de movimeinetos finitos y limitados
Agente singular / multiagente, hay que decirdir

Representacion concreta del estado del juego: 
Se tendra una matriz en el que en cada coordenada sera una casilla posible en el que el jugador podra colocar una "X" o bien un "O" donde represetan la ficha correspondiente a cada jugador.

Descripcion de las acciones que puede tomar el agente: 
Como se habia mencionado anteriormente el ambiente en el que se trata es discreto, por lo que sus movimientos son dados el poder agregar una ficha al tablero y en cualquier posicion valida que este dentro del tablero, y que a medida que avanza el juego van apareciendo las restricciones en ciertos puntos del juego en el que por ejemplo una ficha no puede ser colocada si no hay una sobre el. Su dominio es: 

Represntacion concreta de las acciones:
Propuesta: En este caso se podria almacenar las coordenas del tablero en que colocar una ficha dentro de matriz y tener otra variable me permita distingir la ficha correspondiente. (Puede que asigne desde un principio la ficha).







