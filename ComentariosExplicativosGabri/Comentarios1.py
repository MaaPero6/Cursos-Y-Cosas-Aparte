class Coordinate(object): # Definicion del objeto
    def __init__(self, x, y): # Definicion del constructor
        self.x = x # Definicion del atributo x
        self.y = y # Definicion del atributo y

    def distance(self, other): # Definicion de la funcion distance para calcular la distancia entre dos puntos(se usa Pitagoras)
        x_diff_sq = (self.x - other.x) ** 2 # Define la variable x_diff_sq
        y_diff_sq = (self.y - other.y) ** 2 # Define la variable y_diff_sq
        return (x_diff_sq + y_diff_sq) ** 0.5 # Retorna el valor de la operación

    def getX(self): # Getter del atributo x
        return self.x 

    def getY(self): # Getter del atributo y
        return self.y

    #Aqui se define como queremos que se muestre el objeto por pantalla cuando lo imprimamos, ya que por definicion, cuando imprimes un objeto 
    #con print(objeto) te sale su direccion de memoria.
    def __str__(self): 
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>' #Retorna esta cadena de caracteres, quedaria < cordx, cordy >

    # Aqui definimos la igualación entre dos objetos, ya que por defecto, si haces obj1 == obj2, lo que se va a comparar es sus posiciones
    # en memoria. Con esta funcion le decimos que lo que queremos comparar es sus atributos x e y.
    def __eq__(self, other):
        #Si la comparacion de los atributos x e y es True, es decir, que la x y la y de ambos objetos coinciden
        if self.getX() == other.getX() and self.getY() == other.getY(): 
            return True #retorna True
        else:
            return False #si no, retorna False

    # Aqui hacemos una obrecarga del operador '+', ya que por defecto, da error al sumar objetos.
    # Hacemos que cuando usemos '+' entre dos objetos, se sumen las X y las Y, y retorne un nuevo objeto Coordinate con el resultado.
    def __add__(self, other):
        return Coordinate(self.getX() + other.getX(), self.getY() + other.getY())

    # Funciona igual que el __add__, pero en este caso, en vez de sumar, restamos.
    def __sub__(self, other):
        return Coordinate(self.getX() - other.getX(), self.getY() - other.getY()) 