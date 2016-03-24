# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:50:17 2016

@author: daphnehb
"""

from error_tools import FinProgException

DICO_PATH = "/media/daphnehb/Lexar/RP/data/Dicos/"

DICT_FNAME = "850-mots-us.txt"

################# LECTURE D'UN FICHIER DICTIONNAIRE ##########

# le dictionnaire de mots utilisé pour lancer l'algo
# de la forme {length : {set de mots de cette length}}
DICTIONNAIRE = dict()

"""
    Lit le fichier filename
    et rempli le dico DICTIONNAIRE contenant tous les mots
"""
def recupDictionnaire(liste_fname=None):
    # on vide le dictionnaire courant
    clearDico()
    # si le fichier à charger est le fichier par defaut
    if liste_fname is None or liste_fname==[]:
        remplirDico()
    # sinon on remplit le dico avec tous les nom de fichier de la liste
    else:
        global DICT_FNAME
        for name in liste_fname:
            DICT_FNAME = name
            try:
                remplirDico()
            except FinProgException:
                print "Le fichier {} n'a pu être chargé...".format(name)
        #end for
        # si aucun fichier n'était valide, le dico reste vide
        if DICTIONNAIRE=={}:
            raise FinProgException("Aucun fichier ne correspondait à un dictionnaire.")
        # end if
    # end if
    
def remplirDico():
    # on récuère le dictionnaire global
    global DICTIONNAIRE
    
    monfile = None
    
    filename = DICO_PATH+DICT_FNAME
    try :
        monfile = open(filename,"r")
    except IOError:
        print "Fichier inexistant"
        raise FinProgException('Fichier {} inexitant!'.format(DICO_PATH+DICT_FNAME))
    
    print "Récupération du dictionnaire contenu dans",DICO_PATH+DICT_FNAME
    line = "\n"
    # tant que ce n'est pas la fin du fichier
    while line!="":
        # getting the next word
        line = monfile.readline()
        # tant que ce sont des lignes vides
        while line=="\n":
            line =monfile.readline()
        # si la dernière ligne non vide est la fin du fichier
        if line=="":
            break;
        # removing the last \n
        line = line.rstrip().upper()
        # sinon on recupere la taille du mot
        taille = len(line)
        # on l'ajoute à la liste du dictionnaire correspondante
        if not DICTIONNAIRE.has_key(taille):
            DICTIONNAIRE[taille] = {line}
        else:
            DICTIONNAIRE[taille].add(line)
        # end if
    # end while
    monfile.close()
    # en fonction
        
def clearDico():
    global DICTIONNAIRE
    DICTIONNAIRE = dict()    
    
def afficheDico(outStream):
    global DICTIONNAIRE
    
    for t in sorted(DICTIONNAIRE.keys()):
        outStream.write("Mots de taille {} : \n\t{}\n".format(t,DICTIONNAIRE[t]))
    # end for
    # end