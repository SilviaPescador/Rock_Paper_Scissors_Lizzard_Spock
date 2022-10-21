from random import choice
from play import Paper, Scissors, Rock, Lizard, Spock, Result


def run_game():
    """
    Arranca el juego
    """
    display_game()
    while True:
        # una nueva partida
        user_play = get_user_play()
        comp_play = random_play()
        display_match(user_play, comp_play)
        # Averigua quien gana y me devuelve 
        # una de las dos jugadas(jugador, compu o None)
        winner = get_winner(user_play, comp_play)
        # primera opcion: no hay vencedor
        if winner == None: 
            # muestra empate
            display_tie(user_play, comp_play)
        else:
            # gana o jugador o compu 
            display_victory(winner)
        # pregunto al usuario y si quiere salir  salgo con un break.
        resp = another_match()
        if resp == False:
            break 
         
def display_match(play1, play2):
    """
    Imprime la lucha entre las dos jugadas 
    """
    print(f'{play1.description()} vs {play2.description()} ➢ ➢ ➢ ➢ FIGHT!!!\n')

def display_game():
    """
    Muestra el nombre del juego
    """
    print('\n\n\t\t~ Rock Paper Scissors Lizard Spock  ~\n\n')

def get_user_play():
    """
    Le pregunta al usuario qué quiere jugar y lo devuelve
    """
    res = get_user_response()
    if res == 1:
        return Rock()
    if res == 2:
        return Paper()
    if res == 3:
        return Scissors()
    if res == 4:
        return Lizard()
    else:
        return Spock()

def get_user_response():
    """
    Presenta un menu de  opciones y pide que seleccione
    una. Devuelve una cadena que indica lo que ha elegido.
    """
    response = None
    while True:
        print("Chose your play:")
        print("1. Rock 💎")
        print("2. Paper 🧻")
        print("3. Scissors ✂")
        print("4. Lizard 🦎")
        print("5. Spock  🖖")

        raw = input("Enter 1, 2, 3, 4 or 5\n")
        # validar raw (fila)
        raw = raw.strip()
        if raw == "1":
            response = 1
            break
        elif raw == "2":
            response = 2
            break
        elif raw == "3":
            response = 3
            break
        elif raw == "4":
            response = 4
            break
        elif raw == "5":
            response = 5
            break
        else:
            continue 

    return response

def random_play():
    """
    Selecciona una jugada al azar para competir con el usuario
    """
    return choice([Paper(), Rock(), Scissors(), Lizard(), Spock()])

def get_winner(play1, play2):
    """
    Obtiene el vencedor o None si hay empate
    """
    winner = ""
    result = play1.compare(play2)
    if result == Result.WINS:
        winner = play1
    elif result == Result.EQUAL:
        winner = None
    else: 
        winner = play2
    return winner

def display_tie(play1, play2):
    """
    Imprime que ha habido un empate
    """
    print(f'Tie between {play1.description()} & {play2.description()}')

def display_victory(winner):
    """
    Muestra qué winner ha ganado
    """
    print(f'The fucking winner is ¡¡¡{winner.description()}!!!')
    print("__________________________________________________")

def another_match():
    """
    Pregunta al user si quiere jugar otra vez.
    """
    while True:
        rematch = input("\nDo you want to keep playing?  Y/N:\n >> ")
        if rematch.lower() == "y":
            return True
        elif rematch.lower() == "n":
            bye = ["\t\t\tOh, I'm sorry U'r a coward, go home.", 
            "\t\t\tSee you next time baby...🤸‍♀️", 
            "\t\t\tDon't worry, sometimes we win, sometimes we learn."]
            print(choice(bye))
            return False
        else:
            print("You must enter a correct character. Try again.")
            continue
        

if __name__ == '__main__':
    run_game()


