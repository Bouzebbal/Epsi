# Fonction several_zeros
def several_zeros():
    return [0] * 10

# Fonction several_zeros_custom
def several_zeros_custom(nb_zeros=10):
    return [0] * nb_zeros

# Fonction Matrix
def matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

# Objet Matrix

class Matrix:
    def __init__(self, rows, cols):
        # Création d'une matrice rows x cols initialisée à 0
        self._matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def get_value(self, row, col):
        # Retourne la valeur à la position (row, col)
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self._matrix[row][col]
        else:
            raise IndexError("Indices hors de la portée de la matrice.")
        
    def __eq__(self, other):
        # Vérifie si deux matrices sont égales
        if not isinstance(other, Matrix):
            return False
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self._matrix[i][j] != other._matrix[i][j]:
                    return False
        return True
    
# Fonction sort
def my_sort(my_list: [int]) -> [int]:
    sorted_list = my_list.copy()
    
    # Parcourir la liste autant de fois qu'il y a d'éléments
    for i in range(len(sorted_list)):
        # Pour chaque élément, comparer les éléments adjacents
        for j in range(0, len(sorted_list) - i - 1):
            # Si l'élément actuel est plus grand que le suivant, les échanger
            if sorted_list[j] > sorted_list[j + 1]:
                # Échange des deux éléments
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    
    # Retourner la liste triée
    return sorted_list

if __name__ == '__main__':
    print(several_zeros())
    print(several_zeros_custom(2))
    result = matrix(2, 3)
    print(result[1][2])
    m1 = Matrix(2, 3)
    m2 = Matrix(2, 3)
    print(m1 == m2) 
    print(my_sort([1])) 