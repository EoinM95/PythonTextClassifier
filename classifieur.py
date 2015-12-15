#!/usr/bin/ env python
# -*- coding: utf-8 -*-
nom = "Nom Prénom"

class Instance(object):

    def __init__(self, cat, coords) :
        """Constructeur de la classe.
        @param cat: a string
        @param coords: a tuple of floats
        """
        self.cat = cat
        self.coords = coords

def main():
    """Appelez vos fonctions depuis main()"""


"""Cette condition s'assure de n'appeler la fonction main
que lorsque le programme est appelé directement,
et non lorsqu'il est importé."""
if __name__ == "__main__":
    main()