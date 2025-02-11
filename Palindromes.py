import sys

class CelluleP:
    """une cellule d'une liste chaînée"""
    def __init__(self, v, s):
        self.valeur = v # valeur de l’élément
        self.suivante = s # adresse de l’élément suivant

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
            raise IndexError ("depiler sur une pile vide")
        v = self.contenu.valeur
        self.contenu = self.contenu.suivante
        return v

    def consulter(self):
        return self.contenu.valeur

    def vider(self):
        return CelluleEmpty(self.contenu)

    def tailleR(self):
        return CelluleCount(self.contenu)

    def tailleI(self):
        Pile = self.contenu
        taille = 0
        while Pile is not None:
            Pile = Pile.suivante
            taille += 1
        return taille

def CelluleCount(cellule):
    taille = 0
    if cellule == None:
        return taille + 0

    else:
        taille = 1 + CelluleCount(cellule.suivante)
    return taille

def CelluleEmpty(cellule):

    while cellule is not None:
        cellule = cellule.suivante

    return "Pile vidée avec succès !" + f"La pile est donc égale à :{cellule}"

class Fifo:
    """structure de file"""
    def __init__( self ):
        self._first = None
        self._last = None

    def is_empty( self ):
        return self._first is None

    def enfile(self, value):
        new_node = CelluleF(value)
        if self._last is None :
            self._first = new_node
        else :
            self._last.suivante = new_node
            self._last = new_node

    def defile( self ):
        if self._first is None :
            raise RuntimeError( "Empty Queue" )
            value = self._first.valeur
            self._first = self._first.suivante
        if self._first is None :
            self._last = None
        return value


def main():
    f = Fifo()
    p = Pile()
    mot = input("un mot svp :")
    while mot != "":
        lettre = mot[0]
        f.enfile(lettre)
        p.empiler(lettre)
        mot = mot[1:]
        print(mot)

    while Pile != None :
        lettref = f.defile()
        lettrep = p.depiler()
        if lettref == lettrep :
            return True
        
        elif lettref != lettrep :
            return "n'est pas un palindrome"
            exit_program()



main()