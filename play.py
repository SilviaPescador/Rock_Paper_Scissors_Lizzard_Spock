from enum import Enum

class Result(Enum):
    EQUAL = 0
    WINS = 1
    LOSES = 2

class Play(object):
    """
    Representa una jugada
    """
    def beats(self):
        pass
    def description(self):
        pass
    
    def compare(self, otherPlay):
        """
        Se compara con la otra jugada y devuelve un resultado de la comparación.
        """
        if self == otherPlay:
            return Result.EQUAL
        elif otherPlay in self.beats():
            return Result.WINS
        else:
            return Result.LOSES

    # Dunders
    def __eq__(self, other):
        ''' 
        devuelve True si self y Other son equivalentes
        '''
        if isinstance(self, other.__class__):
            #tal vez seamos iguales, vamos a comparar propiedades
            return self.description() == other.description()
        else:
            # ni de coña podemos ser iguales
            return False

    def __hash__(self):
        '''
        devuelve un hash que represente al atributo de self que lo diferencia de otros. 
        en este caso lo que usamos para diferenciarlo y compararlo con los otros es la descripción,
        por ello calculamos el hash de description.
        '''
        return hash(self.description())

    
class Paper(Play):

    def beats (self):
        return {Rock(), Spock()}

    def description(self):
        return "Paper"


class Scissors(Play):

    def beats (self):
        return {Paper(), Lizard()}

    def description(self):
        return "Scissors"
    # en esta usamos otra alternativa igualmente valida para definir esta clase
    
class Rock(Play):
    def beats (self):
        return {Scissors(), Lizard()}

    def description(self):
        return "Rock"


class Lizard(Play):
    def beats (self):
        return {Spock(), Paper()}

    def description(self):
        return "Lizard"


class Spock(Play):
    def beats (self):
        return {Scissors(), Rock()}

    def description(self):
        return "Spock"

   