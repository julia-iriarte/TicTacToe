#Cuando el programa comienza a correr, en la pantalla aparece el tablero de TA-TE-TI (de 3x3)
#  y un input que permite al usuario elegir el símbolo “X” o el símbolo “O”. Las “X” empiezan.
#El usuario debe elegir la posición del tablero (esta posición debe ser correcta y no debe estar ocupada) 
# donde poner el símbolo en el tablero y el sistema valida si el juego termina con un ganador o en empate. 
# Si no hay ganador o la partida no terminó todavía en empate, 
# el juego continúa preguntando al otro usuario que seleccione la posición del tablero dónde quiere poner su símbolo
#  y así siguiendo hasta que la partida termine con un ganador o en empate.

#Notas:
#Representar el tablero como una matriz de 3x3.
# El juego termina en empate cuando el tablero está completo y no hay ganadores.
# Ejemplo de dibujo de tablero vacío:
# |_|_|_|
# |_|_|_|
# |_|_|_|

# Ejemplo de dibujo en pantalla tablero completo: 
# |X|X|O|
# |O|O|X|
# |X|X|O|

tablero = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
    ]

#Función que imprime el tablero completo
def imprimir_tablero(tablero):
    for i in tablero:
        print(i)

#Función que determina si alguna ficha ha alcanzado la condición de victoria y devuelve True si es así.
def victoria(tablero, ficha):
    if ((tablero[0][0] == tablero[0][1] == tablero[0][2] == ficha) or
    (tablero[1][0] == tablero[1][1] == tablero[1][2] == ficha) or
    (tablero[2][0] == tablero[2][1] == tablero[2][2] == ficha) or
    (tablero[0][0] == tablero[1][0] == tablero[2][0] == ficha) or
    (tablero[0][1] == tablero[1][1] == tablero[2][1] == ficha) or
    (tablero[0][2] == tablero[1][2] == tablero[2][2] == ficha) or
    (tablero[0][0] == tablero[1][1] == tablero[2][2] == ficha) or
    (tablero[0][2] == tablero[1][1] == tablero[2][0] == ficha)): 
        return True
    else:  
        return False

#Función que evalúa si se han completado las 9 casillas y se situará tras la evaluación de victorias.
def empate(tablero):
    for fila in tablero:
        for elemento in fila:
            if elemento == '_':
                return False        
    return True

print('¡Comienza la partida a Ta-Te-Ti. El tablero está vacío:')
imprimir_tablero(tablero)

#Aquí preguntamos nombres y asignamos turnos en función de la ficha elegida.
name1 = input('¿Cuál es tu nombre?: ').title()
name2 = input('¿Contra quién juegas?: ').title()
ficha_user1 = input(f'\n{name1}, ¿jugarás con las X o con las O? (X/O): ').capitalize()
if ficha_user1 == 'X':
    ficha_user2 = 'O'
    player1 = name1
    player2 = name2
elif ficha_user1 == 'O':
    ficha_user2 = 'X'
    player1 = name2
    player2 = name1
print(f'\nDe acuerdo. Entonces {name2} tomará las {ficha_user2}.')
print('\n¡Comienzan las X!')

# Bucle principal. Jugamos mientras no haya ganado nadie y no haya empate.
while victoria(tablero, 'X') == False and victoria(tablero, 'O') == False and empate(tablero) == False:
    #Turno de player1.
    print(f'\nEs tu turno, {player1}.')
    while True:
        fila_player1 = int(input('Elige número de fila para colocar tu X (1, 2 o 3): '))-1
        columna_player1 = int(input('Ahora elige número de columna para colocar tu X (1, 2 o 3): '))-1
        if ((0<=fila_player1<=2) and (0<=columna_player1<=2) and tablero[fila_player1][columna_player1] == '_'):
            print(f'{player1} coloca su X en el tablero y queda así:')
            tablero[fila_player1][columna_player1] = 'X'
            imprimir_tablero(tablero)
            break
        else:
            print('¡Lo siento! No puedes colocar en esa casilla. Por favor, elige una casilla válida.')

    
    #Evalúa si ahora se ha alcanzado la condición de victoria para las X. Si es así, termina la partida.
    if victoria(tablero, 'X') == True:
        print (f'\n¡Ha ganado {player1}!\n')
        break

    #Evalúa si ahora se ha alcanzado la condición de empate (ocurrirá tras la 9ª ficha). Si es así, termina la partida.
    if empate(tablero) == True:
        print('¡La partida ha terminado en empate!')
        break

    #Turno de player2.
    print(f'\nEs tu turno, {player2}.')
    while True:
        fila_player2 = int(input('Elige número de fila para colocar tu O (1, 2 o 3): '))-1
        columna_player2 = int(input('Ahora elige número de columna para colocar tu O (1, 2 o 3): '))-1
        if ((0<=fila_player2<=2) and (0<=columna_player2<=2) and tablero[fila_player2][columna_player2] == '_'):
            print(f'{player2} coloca su O en el tablero y queda así:')
            tablero[fila_player2][columna_player2] = 'O'
            imprimir_tablero(tablero)
            break
        else:
            print('¡Lo siento! No puedes colocar en esa casilla. Por favor, elige una casilla válida.')

    #Evalúa si ahora se ha alcanzado la condición de victoria para las X. Si es así, termina la partida.
    if victoria(tablero, 'O') == True:
        print (f'\n¡Ha ganado {player2}!\n')
        break
