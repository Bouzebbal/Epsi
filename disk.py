class Disk:
    def __init__(self, total: int, used: int):
        self.total = total  
        self.used = used    

    @property
    def free(self):
        return self.total - self.used

    @property
    def used_perc(self):
        return self.used / self.total

    def __str__(self):
        # Permet l'affichage de l'objet sous forme lisible.
        return f"Disk[total: {self.total} Gb, used: {self.used} Gb]"

    def __lt__(self, other):
        # Permet de comparer deux disques en fonction du ratio d'espace utilisé.
        return self.used_perc < other.used_perc


# Exemple d'utilisation
disk1 = Disk(total=10, used=2)
disk2 = Disk(total=20, used=5)

if __name__ == '__main__':
    print(disk1.free)
