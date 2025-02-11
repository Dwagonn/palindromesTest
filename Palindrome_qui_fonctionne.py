import sys

class CelluleP:
    """une cellule d'une liste chaînée"""
    def __init__(self, v, s):
        self.valeur = v # valeur de l'élément
        self.suivante = s # adresse de l'élément suivant

class CelluleF:
    """une cellule d'une liste chaînée"""
    def __init__(self, v, s = None):
        self.valeur = v
        self.suivante = s
        
class Pile:
    """structure de pile"""
    def __init__(self):
        self.contenu = None
    
    def est_vide(self):
        return self.contenu is None

    def empiler(self, v):
        self.contenu = CelluleP(v, self.contenu)

    def depiler(self):
        if self.est_vide():
            raise IndexError("depiler sur une pile vide")
        v = self.contenu.valeur
        self.contenu = self.contenu.suivante
        return v

    def consulter(self):
        if self.est_vide():
            raise IndexError("consulter sur une pile vide")
        return self.contenu.valeur

class File:
    """structure de file"""
    def __init__(self):
        self._first = None
        self._last = None

    def est_vide(self):
        return self._first is None

    def enfile(self, value):
        new_node = CelluleF(value)
        if self._last is None:
            self._first = new_node
            self._last = new_node
        else:
            self._last.suivante = new_node
            self._last = new_node

    def defile(self):
        if self._first is None:
            raise RuntimeError("File vide")
            value = self._first.valeur
            self._first = self._first.suivante
        if self._first is None:
            self._last = None
        return value

def est_palindrome(mot):
    """Vérifie si un mot est un palindrome en utilisant une pile et une file"""
    # Créer les structures
    f = File()
    p = Pile()
    
    # Remplir la pile et la file avec les lettres du mot
    for lettre in mot:
        f.enfile(lettre)
        p.empiler(lettre)
    
    # Comparer les lettres
    while not f.est_vide() and not p.est_vide():
        lettref = f.defile()
        lettrep = p.depiler()
        if lettref != lettrep:
            return False
    
    return True

def main():
    while True:
        mot = input("Entrez un mot (ou appuyez sur Entrée pour quitter) : ")
        if mot == "":
            print("Au revoir !")
            break
            
        if est_palindrome(mot):
            print(f"'{mot}' est un palindrome")
        else:
            print(f"'{mot}' n'est pas un palindrome")

if __name__ == "__main__":
    main()