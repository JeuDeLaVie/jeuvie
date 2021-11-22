import os
from time import sleep
class case(object):
    def __init__(self,x=0,y=0,etat=0,p_etat = 0):
        self.x = x
        self.y = y
        self.etat = etat
        self.p_etat = p_etat
    def etat_n(self,voisins):
        e = self.etat
        self.p_etat = int( (e==1 and voisins== 2) or voisins==3 )
        return self.p_etat
    def __str__(self):
        return "case de coords "+str(self.x)+','+str(self.y)+"; etat "+str(self.etat)
    def disp_etat(self):
        if (self.etat)==1:
            print("\033[4m" + "x" + "\033[0m",end='|')
        else:
            print('\033[4m' + ' ' + '\033[0m',end='|')

def cases_autour(case,taille):
    lst = [(i,j) for i in range(case.x-1,case.x+2) for j in range(case.y-1, 
            case.y+2) if (not (i==case.x and j ==case.y) and i>=0 and j>=0 and i<taille[0] and j<taille[1])]
    
    #print(case.x,case.y,lst)
    return lst
    
def nb_voisins(case,grille,taille):
    voisins = 0
    l = cases_autour(case,taille)
    for i in l:
        st = grille[i].etat
        #print(i,st)
        if st:
            voisins += 1
    #print("coordonnees ",case.x,' ',case.y,' : ',voisins," voisins")
    return voisins

def disp(grille,taille):
    nb_li = taille[0]
    nb_co = taille[1]
    print(' _',end='')
    for i in range(taille[1]):
        print("__",end='')
    print('')
    for i in range(nb_li):
        print('||',end = '')
        for j in range(nb_co):
            grille[ (i,j) ].disp_etat()
        print('|')
    return
def genere(nbre,grille, taille):
    disp(grille,taille)
    print("ETAT INITIAL")
    for f in range(nbre):
        sleep(1.5)
        for i in grille.keys():
            grille[i].etat_n(nb_voisins(grille[i],grille,taille))
        for i in grille.keys():
            grille[i].etat = grille[i].p_etat
        os.system('cls' if os.name == 'nt' else 'clear')
        disp(grille,taille)
        print("itération ",f+1)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("BIENVENUE SUR LE JEU DE LA VIE, FAIT PAR NOUS")
    grille = dict()
    taille = (int(input("hauteur de la grille (en nombre de cases):")), int(input("largeur de la grille :")) )
    for i in range(taille[0]):
        for j in range(taille[1]):
            x = case(i,j)
            grille[ (i,j) ] = x
    #etat = 1-etat
    #fini = False
    #while not Fini

    nbre = int(input("combien de repetitions ? :\t"))
    # grille[(0,1)].etat = 1
    # grille[(1,2)].etat = 1
    # grille[(2,0)].etat = 1
    # grille[(2,1)].etat = 1
    # grille[(2,2)].etat = 1
    genere(nbre,grille,taille)
    print("MERCI D'AVOIR JOUÉ")

if __name__ == "__main__":
        main()