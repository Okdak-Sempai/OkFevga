from ast import Or
from typing import List
from xml.etree.ElementTree import PI
from colorama import Fore, Back, Style
import random
from datetime import date, datetime
OrdreBlanc=[13,14,15,16,17,18,19,20,21,22,23,24,1,2,3,4,5,6,7,8,9,10,11,12]
Plateau = [['. ','. ','. ','. ','. ','. ','. ','. ','. ','. ','. ','. ','. ','. ','. '] for i in range(24)]
Plateau[12]=['B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ']
Plateau[0]=['N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ']

Jeu=dict(tournum=1,joueurnum=2,stylenum=1) 
def HashDiceThrow():
    '''Retourne un chiffre entre Entre 1 et 6 en int'''
    Hash1 = str(datetime.now())
    Hash1 = Hash1[17:19]
    Hash2 = int(int(Hash1)%10)
    if Hash2 in [0,7,8,9]:
        Hash2 = str(datetime.now())
        Hash2 = int(Hash2[20:21])
    if Hash2 in [0,7,8,9]:
        Hash3 = Hash2%2+1
        return ((Hash3,random.randint(1,6)))
    return ((Hash2,random.randint(1,6)))

def AfficherPlateau():
    '''Affiche le plateau comme il faut.'''
    '''Return->Void'''
    print("24|23|22|21|20|19|18|17|16|15|14|13")
    print("___________________________________")
    PrintablePlateau1 = zip(*reversed(Plateau[12:24]))
    for i in PrintablePlateau1:
        print (*i)
    print("___________________________________")
    aux=Plateau[0:12]
    for i in range(len(aux)):
        aux[i]=reversed(aux[i])
    PrintablePlateau1 = zip(*aux)
    for i in PrintablePlateau1:
        print (*i)
    print("___________________________________")
    print("1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11|12")

def Coupspossibles(Vdice,joueur):
    '''Retourne le tuple des cases avec coups possible EN ARRIVE'''
    if (Plateau[23]==['N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N '] or Plateau[11]==['B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ']):
        return ()
    OrdreBlanc=[13,14,15,16,17,18,19,20,21,22,23,24,1,2,3,4,5,6,7,8,9,10,11,12]
    CoupElig=[]
    LesCoups=list(range(24))
    if (len(Vdice))==2:
        NVdice=(sum(Vdice),Vdice[0],Vdice[1])
    else:
        NVdice=Vdice
    #Debut de game
    Oui=1
    NombreDepart=0
    if joueur==1 and Plateau[0][-1]!='N ':
        for i in range(12,24):
            if Plateau[i][0]=='N ':
                Oui=0
        if (Oui==1 and Plateau[0]==['N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','. ']):
            for i in range(1,24):
                if Plateau[i][0]=='N ':
                    NombreDepart=i
            for d in NVdice:
                if NombreDepart+d in OrdreBlanc:
                    CoupElig.append(NombreDepart+d)
            for i in CoupElig:
                if Plateau[i][0]=='B ':
                    CoupElig=set(CoupElig)
                    CoupElig.discard(i)
                    CoupElig=list(CoupElig)
            return(tuple(set(CoupElig)))
    
    if joueur!=1 and Plateau[12][-1]!='B ':
        for i in range(12):
            if Plateau[i][0]=='B ':
                Oui=0
        if (Oui==1 and Plateau[12]==['B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','. ']):
            for i in [13,14,15,16,17,18,19,20,21,22,23,1,2,3,4,5,6,7,8,9,10,11]:
                if Plateau[i][0]=='B ':
                    NombreDepart=i
            OrdreBlanc=[12,13,14,15,16,17,18,19,20,21,22,23,0,1,2,3,4,5,6,7,8,9,10,11]
            for d in NVdice:
                for o in range(len(OrdreBlanc)):
                    if OrdreBlanc[o]==NombreDepart:
                        if (o+d) in OrdreBlanc:
                            CoupElig.append(OrdreBlanc[o+d])
            for i in CoupElig:
                if Plateau[i][0]=='N ':
                    CoupElig=set(CoupElig)
                    CoupElig.discard(i)
                    CoupElig=list(CoupElig)
            return(tuple(set(CoupElig)))
    #Debut de game
    
    if joueur==1: #J!
        pions="N "###
        LesCoups=set(LesCoups)
        LesCoups.discard(0)
        LesCoups=list(LesCoups)
        for i in range(24):
            if (("B " in Plateau[i][0]) or Plateau[i][-1]=="N "):
                LesCoups=set(LesCoups)
                LesCoups.discard(i)
                LesCoups=list(LesCoups)

        for i in range(24):
            if ("N " in Plateau[i][0]):
                NVdice=Vdice
                (NVdice)=[x+i for x in NVdice]
                NVdice=tuple(NVdice) #produit cartesien de tout les coups apres l'addition du de dans une case
                for n in NVdice:
                    if n in LesCoups:
                        CoupElig.append(n)

        #Limitations on primes #On ne peut pas placer de pions si 1 a 6 casi rempli
        CounterIlleg=0
        for i in range(6):
            if Plateau[i][0]=='N ':
                CounterIlleg+=1
        if CounterIlleg==5:
            for i in range(6):
                if Plateau[i][0]=='. ':
                    CoupElig=set(CoupElig)
                    CoupElig.discard(i)
                    CoupElig=list(CoupElig)

        return tuple(set(CoupElig))
        
    else: #J2
        pions="B "
        OrdreBlanc=[13,14,15,16,17,18,19,20,21,22,23,24,1,2,3,4,5,6,7,8,9,10,11,12]
        LesCoups=set(OrdreBlanc)
        LesCoups.discard(12)
        LesCoups=list(LesCoups)
        for i in OrdreBlanc:
            if (("N " in Plateau[i-1][0]) or Plateau[i-1][-1]=="B "):
                LesCoups=set(LesCoups)
                LesCoups.discard(i)
                LesCoups=list(LesCoups)

        for i in range(len(OrdreBlanc)):
            if ('B ' in Plateau[OrdreBlanc[i]-1][0]): #cherche case avec pion pour les cases apres le de
                NVdice2=Vdice
                NVdice=[]
                for x in NVdice2:
                    if i+x in range(24):
                        NVdice.append(OrdreBlanc[i+x])
                NVdice=tuple(NVdice) #produit cartesien de tout les coups apres l'addition du de dans une case
                for n in NVdice:
                    if n in LesCoups:
                        CoupElig.append(n-1)

        #Limitations on primes #On ne peut pas placer de pions si 1 a 6 casi rempli
        CounterIlleg=0
        for i in [12,13,14,15,16,17]:
            if Plateau[i][0]=='B ':
                CounterIlleg+=1
        if CounterIlleg==5:
            for i in [12,13,14,15,16,17]:
                if Plateau[i][0]=='. ':
                    CoupElig=set(CoupElig)
                    CoupElig.discard(i)
                    CoupElig=list(CoupElig)
        return tuple(set(CoupElig))

def SCoupsSingle(Vdice,case,joueur):
    '''Retourne les coups possible a partir de la dite case'''
    EligF=[]
    SVdice=Vdice
    if (len(SVdice))>1:
        SVdice=(sum(SVdice),SVdice[0],SVdice[1])
    if Jeu['joueurnum']==1:
        for i in SVdice:
            if case+i<24:
                EligF.append(case+i)
        for a in EligF:
            if Plateau[a-1][0]=='B ':
                EligF=set(EligF)
                EligF.discard(a)
                EligF=list(EligF)
        EligF2=[]
        for i in EligF:
            EligF2.append(i)
    else:
        x=int()
        OrdreBlanc=[13,14,15,16,17,18,19,20,21,22,23,24,1,2,3,4,5,6,7,8,9,10,11,12]
        for reel in range(len(OrdreBlanc)):
            if OrdreBlanc[reel]==case:
                x=reel
        for i in SVdice:
            if x+i<23:
                EligF.append(OrdreBlanc[x+i])
        for b in EligF:
            if Plateau[b-1][0]=='N ':
                EligF=set(EligF)
                EligF.discard(b)
                EligF=list(EligF)
        EligF2=[]
        for i in EligF:
            EligF2.append(i)
    EligF2=set(EligF2)
    return tuple(EligF2)

def DeplacerPions(pionsC,dice,caseDepart,caseArrive):
    '''Deplace le pion et Retourne la valeur du de apres deplacement'''
    OrdreBlanc=[13,14,15,16,17,18,19,20,21,22,23,24,1,2,3,4,5,6,7,8,9,10,11,12]
    caseArrive-=1
    caseDepart-=1
    #1 a 24
    Vald=None
    dice=sum(dice)
    #remove
    for i in range(len(Plateau[caseDepart])):
        if Plateau[caseDepart][i]==pionsC:
            Vald=i
    Plateau[caseDepart][Vald]=". "
    #add
    Vald=None
    for i in reversed(range(len(Plateau[caseArrive]))):
        if Plateau[caseArrive][i]==". ":
            Vald=i

    Plateau[caseArrive][Vald]=pionsC
    
    if pionsC=="N ":
        dice=dice-(caseArrive-caseDepart)
    if pionsC=="B ":
        for i in range(len(OrdreBlanc)):
            for n in range(len(OrdreBlanc)):
                if OrdreBlanc[i]==caseDepart+1:
                    if OrdreBlanc[n]==caseArrive+1:
                        dice=dice-(n-i)  
    #modifier le dice
    return (dice,)

def turn(tournum,joueurnum,stylenum):
    '''prend Jeu en argument -> retourne 1 si victoire/fin sinon 0'''
    Jeu['joueurnum']=joueurnum
    print("Tour ",Jeu['tournum'],"\tJoueur",Jeu['joueurnum'])
    AfficherPlateau()
    if Jeu['joueurnum']==2 and Jeu['stylenum']==1:
        input("Press Enter to make the IA play")
    else:
        input("Press Enter to roll dice\t")
    Action=HashDiceThrow()
    SuperDice=()
    if len(Action)==2:
        if Action[0]==Action[1]:
            SuperDice=Action
            print(Fore.RED+"Vous avez un fait un coup double,Vous avez un Super De en reserve,",SuperDice)
            print(" Utilisez votre De et vous aurez acces a celui ci.")
            print(Style.RESET_ALL)

    if Jeu['joueurnum']==1:
        pions="N "
    else:
        pions="B "

    while sum(Action)>0:
        print(Fore.LIGHTBLUE_EX+"\nDE=[",Action,"]")
        print(Style.RESET_ALL)
        Coup=Coupspossibles(Action,Jeu['joueurnum'])
        Coup2=Coup
        Coup2=[x+1 for x in Coup2]
        Coup2=tuple(Coup2)
        Coup3=()
        if Jeu['joueurnum']!=1: #J2
            Coup3=set(Coup2)
            Coup3.discard(13)
            Coup3.discard(12)
            Coup3=tuple(Coup3)
        if Jeu['joueurnum']==1: #J1
            Coup3=set(Coup2)
            Coup3.discard(24)
            Coup3.discard(1)
            Coup3=tuple(Coup3)
        Coup2=Coup3
        ###FIN DU JEU
        EndGame=0
        if Jeu['joueurnum']==1: #J1
            for i in range(0,18):
                if Plateau[i][0]=='N ':
                    EndGame+=1
            if EndGame==0:
                if Plateau[23][0]!='B ':
                    print(Fore.YELLOW+"PHASE FINALE!")
                    print(Style.RESET_ALL)
                    PionsFinaux=[]
                    Action3=Action
                    for i in Action3:
                        if i==6 and Plateau[18][0]=='N ':
                            PionsFinaux.append(19) #Valeur affiche
                        elif i==5 and Plateau[19][0]=='N ':
                            PionsFinaux.append(20)
                        elif i==4 and Plateau[20][0]=='N ':
                            PionsFinaux.append(21)
                        elif i==3 and Plateau[21][0]=='N ':
                            PionsFinaux.append(22)
                        elif i==2 and Plateau[22][0]=='N ':
                            PionsFinaux.append(23)
                        else: #i==1:
                            a=0
                            for i in [18,19,20,21,22]:
                                if Plateau[i][0]=='N ':
                                    a=i
                            PionsFinaux.append(a+1)
                    PionsFinaux=tuple(PionsFinaux)
                    print(Fore.CYAN+"Les cases qui peuvent finir sont:",PionsFinaux)
                    print(Style.RESET_ALL)
                    choix=42
                    while choix not in Action:
                        if Jeu['stylenum']==1 and Jeu['joueurnum']!=1:
                            choix=random.choice(Action)
                        else:
                            choix=int(input("Choix du de a utiliser:"))
                    print("De choisi:",Fore.BLUE+"",choix)
                    Action3=sum(Action)-choix
                    Action3=(Action3,)
                    print(Style.RESET_ALL)
                    #choix= le de / choixPF= la case a bouger
                    choixPF=0
                    for i in PionsFinaux:
                        if i==6 and Plateau[18][0]=='N ':
                            choixPF=19
                        elif i==5 and Plateau[19][0]=='N ':
                            choixPF=20
                        elif i==4 and Plateau[20][0]=='N ':
                            choixPF=21
                        elif i==3 and Plateau[21][0]=='N ':
                            choixPF=22
                        elif i==2 and Plateau[22][0]=='N ':
                            choixPF=23
                        else:
                            a=0
                            for i in [18,19,20,21,22]:
                                if Plateau[i][0]=='N ':
                                    a=i
                            choixPF=a+1

                    #bouger et suprimmer le pion
                    sup=0 #suprime de case
                    for i in range(len(Plateau[choixPF-1])):
                        if Plateau[choixPF-1][i]=='N ':
                            sup=i
                    Plateau[choixPF-1][sup]='. '
                    #ajoute a la fin
                    for i in reversed(range(len(Plateau[23]))):
                        if Plateau[23][i]=='. ':
                            sup=i
                    Plateau[23][sup]='N '
                    #Retourner le bon de

                    Action=Action3
                    Coup2=()
                    AfficherPlateau()
                else:
                    Action=()
                    print("Aucun coup jouable,c'est au tour du prochain Joueur.\n")
        if Jeu['joueurnum']!=1: #2
            OrdreBlanc2=[12,13,14,15,16,17,18,19,20,21,22,23,0,1,2,3,4,5]
            for i in OrdreBlanc2:
                if Plateau[i][0]=='B ':
                    EndGame+=1
            if EndGame==0:
                if Plateau[11][0]!='N ':
                    print(Fore.YELLOW+"PHASE FINALE!")
                    print(Style.RESET_ALL)
                    PionsFinaux=[]
                    Action3=Action
                    for i in Action3:
                        if i==6 and Plateau[6][0]=='B ':
                            PionsFinaux.append(7) #Valeur affiche
                        elif i==5 and Plateau[7][0]=='B ':
                            PionsFinaux.append(8)
                        elif i==4 and Plateau[8][0]=='B ':
                            PionsFinaux.append(9)
                        elif i==3 and Plateau[9][0]=='B ':
                            PionsFinaux.append(10)
                        elif i==2 and Plateau[10][0]=='B ':
                            PionsFinaux.append(11)
                        else: #i==1:
                            a=0
                            for i in [6,7,8,9,10]:
                                if Plateau[i][0]=='B ':
                                    a=i
                            PionsFinaux.append(a+1)
                    PionsFinaux=tuple(PionsFinaux)
                    print(Fore.CYAN+"Les cases qui peuvent finir sont:",PionsFinaux)
                    print(Style.RESET_ALL)
                    choix=42
                    while choix not in Action:
                        if Jeu['stylenum']==1 and Jeu['joueurnum']!=1:
                            choix=random.choice(Action)
                        else:
                            choix=int(input("Choix du de a utiliser:"))
                    print("De choisi:",Fore.BLUE+"",choix)
                    Action3=sum(Action)-choix
                    Action3=(Action3,)
                    print(Style.RESET_ALL)
                    #choix= le de / choixPF= la case a bouger
                    choixPF=0
                    for i in PionsFinaux:
                        if i==6 and Plateau[6][0]=='B ':
                            choixPF=6
                        elif i==5 and Plateau[7][0]=='B ':
                            choixPF=7
                        elif i==4 and Plateau[8][0]=='B ':
                            choixPF=8
                        elif i==3 and Plateau[9][0]=='B ':
                            choixPF=9
                        elif i==2 and Plateau[10][0]=='B ':
                            choixPF=10
                        else:
                            a=0
                            for i in [6,7,8,9,10]:
                                if Plateau[i][0]=='B ':
                                    a=i
                            choixPF=a+1

                    #bouger et suprimmer le pion
                    sup=0 #suprime de case
                    for i in range(len(Plateau[choixPF-1])):
                        if Plateau[choixPF-1][i]=='B ':
                            sup=i
                    Plateau[choixPF-1][sup]='. '
                    #ajoute a la fin
                    for i in reversed(range(len(Plateau[11]))):
                        if Plateau[11][i]=='. ':
                            sup=i
                    Plateau[11][sup]='B '
                    #Retourner le bon de

                    Action=Action3
                    Coup2=()
                    AfficherPlateau()
                else:
                    Action=()
                    print("Aucun coup jouable,c'est au tour du prochain Joueur.\n")

        ###FIN DU JEU
        print("Les cases des disponibles pour placer un pion sont ",Fore.CYAN+"",Coup2)
        print(Style.RESET_ALL)
        if Coup2!=():
            CasepionD=42
            CasepionA=42
            OrdreBlanc=[13,14,15,16,17,18,19,20,21,22,23,24,1,2,3,4,5,6,7,8,9,10,11,12]
            casesDeplacables=[]
            iter=0
            if pions=="N ":
                for i in Plateau:
                    if pions in i[0]:
                        casesDeplacables.append(iter+1)
                    iter+=1
                casesDeplacables=tuple(casesDeplacables)
            else:
                for i in range(len(Plateau)):
                    if pions in Plateau[i][0]:
                        casesDeplacables.append(iter+1)
                    iter+=1

            casesDeplacables2=[]
            casesDeplacables3=[]
            Action2=()
            if len(Action)!=1:
                Action2=(Action[0],Action[1],sum(Action))
            else:
                Action2=Action
            casesDeplacables3=casesDeplacables2
            for x in casesDeplacables2:
                compteur=0
                for y in Action2:
                    listeretir=0
                    if len(Action2)==1:
                        if Jeu['joueurnum']==1:
                            if x+y<24:
                                if Plateau[x+y][0]=='B ':
                                    listeretir=x
                                    compteur+=1
                        else:
                            for w in range(24):
                                if OrdreBlanc[w]==x:
                                    if w+y<24:
                                        OBV=OrdreBlanc[w+y]
                                        if Plateau[OBV+1][0]=='N ':
                                            listeretir=x
                                            compteur+=1
                if len(Action2)==compteur:
                    casesDeplacables3=set(casesDeplacables3)
                    casesDeplacables3.discard(listeretir)
                    casesDeplacables3=tuple(casesDeplacables3)
                casesDeplacables4=[]
                casesDeplacables5=[]
                casesDeplacables6=[]

                for i in Coup2:
                    for j in Action:
                        if Jeu['joueurnum']==1:   
                            casesDeplacables4.append(i-j)
                        else:
                            for i in range(24):
                                if OrdreBlanc[i]==Coup2:
                                    if i-j in OrdreBlanc:
                                        casesDeplacables4.append(OrdreBlanc[i-j])
                for i in casesDeplacables4:
                    if i in range(24):
                        casesDeplacables5.append(i)
                if Jeu['joueurnum']!=1: #J2
                    for i in casesDeplacables5:
                        if (Plateau[i-1][0]!='N ' and Plateau[i-1][0]!='. '):
                            casesDeplacables6.append(i)
                else: #J1
                    for i in casesDeplacables5:
                        if (Plateau[i-1][0]!='B ' and Plateau[i-1][0]!='. '):
                            casesDeplacables6.append(i)
                casesDeplacables3=tuple(set(casesDeplacables6))

            #Debut nouveau
            casesDeplacablesX=[]
            casesDeplacablesZX=[]
            if Jeu['joueurnum']==1: #J1 donc N
                for i in range(24):
                    if Plateau[i][0]=='N ':
                        casesDeplacablesX.append(i+1) #VAL PLAT
                for A in Action2:
                    for Ca in casesDeplacablesX:
                        F=Ca+A
                        if F in Coup2:
                            casesDeplacablesZX.append(Ca)
            else: #J2 donc B OrdreBlanc=[13,14,15,16,17,18,19,20,21,22,23,24,1,2,3,4,5,6,7,8,9,10,11,12]
                for i in range(24):
                    if Plateau[i][0]=='B ':
                        casesDeplacablesX.append(i+1) #VAL PLAT
                for A in Action2:
                    for Ca in casesDeplacablesX:
                        for OB in range(24):
                            if OrdreBlanc[OB]==Ca:
                                F=OB+A
                                if F<24:
                                    F2=OrdreBlanc[F]
                                    if F2 in Coup2:
                                        casesDeplacablesZX.append(Ca)

            #Fin nouveau
            Oui=1
            if Jeu['joueurnum']==1:
                for i in range(12,24):
                    if Plateau[i][0]=='N ':
                        Oui=0
                if (Oui==1 and Plateau[0]==['N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','. ']):
                    if len(casesDeplacablesZX)!=1:
                        casesDeplacablesZX=set(casesDeplacablesZX)
                        casesDeplacablesZX.discard(1)
                        casesDeplacablesZX=tuple(casesDeplacablesZX)
            if Jeu['joueurnum']!=1:
                for i in range(12):
                    if Plateau[i][0]=='B ':
                        Oui=0
                if (Oui==1 and Plateau[12]==['B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','. ']):
                    if len(casesDeplacablesZX)!=1:
                        casesDeplacablesZX=set(casesDeplacablesZX)
                        casesDeplacablesZX.discard(13)
                        casesDeplacablesZX=tuple(casesDeplacablesZX)
            casesDeplacables3=tuple(set(casesDeplacablesZX))
            print("Voici les cases avec des pions deplacables")
            print(Fore.CYAN+"",casesDeplacables3) #debug
            print(Style.RESET_ALL) 
         
            while(CasepionD not in list(casesDeplacables3)):
                '''
                if Jeu['stylenum']=1:
                    if Jeu['joueurnum']==1:
                        CasepionD=int(input("Entrer la case du pion a deplacer:\t"))
                    else:
                        CasepionD=random.choice(casesDeplacables2)
                else:
                    CasepionD=int(input("Entrer la case du pion a deplacer:\t"))

                '''
                CasepionD=random.choice(casesDeplacables3) #debug a supr
                print("CHOIX ORDI",CasepionD) #debug a suprimmer
            if Jeu['joueurnum']==1:
                SOL=[CasepionD+i for i in Action]+[CasepionD + sum(Action)]
            else:
                SOL=[]
                for i in range(len(OrdreBlanc)):
                    for n in Action:
                        if OrdreBlanc[i]==CasepionD:
                            SOL.append(CasepionD+n)
                for i in range(len(OrdreBlanc)):
                    if OrdreBlanc[i]==CasepionD:
                        SOL.append(OrdreBlanc[i]+sum(Action))
            SOL2=set(Coup2).intersection(set(SOL))
            SOL2=tuple(SOL2)
            SOL3=[]
            OrdreBlanc=[13,14,15,16,17,18,19,20,21,22,23,24,1,2,3,4,5,6,7,8,9,10,11,12]
            Action2=()
            if len(Action)!=1:
                Action2=(Action[0],Action[1],sum(Action))
            else:
                Action2=Action
            for h in range(len(OrdreBlanc)): #h parseur de OrdreBlanc
                if OrdreBlanc[h] in casesDeplacables3: #k if h in CaseDeplacables
                    for l in Action2:
                        met=h+l
                        if met<23:
                            if OrdreBlanc[met] in Coup2:
                                SOL3.append(OrdreBlanc[met])
            SOL3=tuple(set(SOL3))
            SOLN=SOL3
            SAC=[]
            for q in range(len(OrdreBlanc)):
                if OrdreBlanc[q]==CasepionD:
                    SAC=OrdreBlanc[q:]
            SAC2=[x+1 for x in SAC]
            if Jeu['joueurnum']!=1:
                SAC2.append(24)
            for i in SOL3:
                if i not in SAC2:
                    SOL3=set(SOL3)
                    SOL3.discard(i)
                    SOL3=tuple(SOL3)
            if Jeu['joueurnum']!=1:
                SOL4=[]
                for p in range(len(OrdreBlanc)):
                    if OrdreBlanc[p]==CasepionD:
                        for o in Action2:
                            a=OrdreBlanc[p]+o 
                            SOL4.append(a)
                SOL4=tuple(set(SOL4))
                SOL3=set(Coup2).intersection(set(SOL3))
                SOL3=tuple(SOL3)
                if 24 in Coup2:
                    SOL3=list(SOL3)
                    SOL3.append(24)
                    SOL3=tuple(SOL3)
                SOLF=[]
                for i in SOL4:
                    for n in range(len(OrdreBlanc)):
                        if OrdreBlanc[n]==CasepionD:
                            if i in OrdreBlanc[n:]:
                                SOLF.append(i)
                SOLF=tuple(SOLF)
                SOL3=SOLF

            if Jeu['joueurnum']==1:
                SOL3=tuple(set(SOL3).union(set(SOL2)))
                SOL4=SOL3
                ListN=range(24)
                for i in ListN:
                    if ListN[i]==CasepionD:
                        for g in Action:
                            if i+g<24:
                                for z in SOL3:
                                    if z not in ListN[i:]:
                                        SOL4=set(SOL4)
                                        SOL4.discard(z)
                                        SOL4=tuple(SOL4)
                SOL3=SOL4
                for o in range(24):
                    if 'B ' == Plateau[o][0]:
                        SOL3=set(SOL3)
                        SOL3.discard(o+1)
                        SOL3=tuple(SOL3)

            else:
                SOL3=tuple((set(SOL3).union(set(SOL2))))
                SOL4=SOL3
                for i in range(len(OrdreBlanc)):
                    if OrdreBlanc[i]==CasepionD:
                        for g in Action:
                            if i+g<24:
                                for z in SOL3:
                                    if z not in OrdreBlanc[i:]:
                                        SOL4=set(SOL4)
                                        SOL4.discard(z)
                                        SOL4=tuple(SOL4)
                SOL3=SOL4
                #debug pour empecher empilage
                for o in range(24):
                    if 'N ' == Plateau[o][0]:
                        SOL3=set(SOL3)
                        SOL3.discard(o+1)
                        SOL3=tuple(SOL3)
            
            if Jeu['joueurnum']!=1 and SOL2!=():
                SOL3=set(SOL3).intersection(set(SOL2))
                SOL3=tuple(SOL3)

            SOL3=SCoupsSingle(Action,CasepionD,Jeu['joueurnum'])

            print("Cases de destinations possibles avec ce pion:",Fore.CYAN+"",SOL3)
            print(Style.RESET_ALL)
            while (CasepionA not in SOL3):
                '''
                if Jeu['stylenum']=1:
                    if Jeu['joueurnum']==1:
                        CasepionA=int(input("Entrer la case du pion a deplacer:\t"))
                    else:
                        CasepionA=random.choice(casesDeplacables2)
                else:
                    CasepionA=int(input("Entrer la case du pion a deplacer:\t"))
                '''
                CasepionA=random.choice(SOL3)
                print("CHOIX ORDI",CasepionA)   
            Action=DeplacerPions(pions,Action,CasepionD,CasepionA)
        else:
            if EndGame!=0:
                print("Aucun coup jouable,c'est au tour du prochain Joueur.\n")
                Action=()
        if (Action==(0,) and SuperDice!=()):
            print(Fore.RED+"Vous avez acces a vos coups Bonus.",SuperDice)
            print(Style.RESET_ALL)
            Action=SuperDice
            SuperDice=()

    if Jeu['joueurnum']==1:
        Jeu['joueurnum']=2
    else:
        Jeu['joueurnum']=1


    if ((Coupspossibles(Action,Jeu['joueurnum'])==()) and (Plateau[23]==['N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N ','N '] or Plateau[11]==['B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B ','B '] )):
        return 1
    else:
        Jeu['tournum']+=1
        return 0

def main():
    print("Welcome to The Fevga,\nPress:\n1 Pour un ordi\n2 Pour du PVP")
    Jeu['stylenum']=int(input("Choix:"))
    while (Jeu['stylenum'] not in [1,2]):
        Jeu['stylenum']=int(input("Choix:"))
        print(Jeu['stylenum'])
    print("\nLe joueur 1 a les pions Noirs\nLe joueur 2 a les pions Blancs.")
    print("\n")
    print("Joueur 1")
    input("Press Enter to roll dice\t")
    Action=HashDiceThrow()

    
    if (Action[0]==Action[1]):
        while (Action[0]==Action[1]):
            Action=HashDiceThrow()

    print("Le Joueur 1 a fait[",Action[0],"]\n")

    if Jeu['stylenum']==2:
        print("Joueur 2")
        input("Press Enter to roll dice\t")
        print("Le Joueur 2 a fait[",Action[1],"]\n")
    else:
        print("L'IA a fait[",Action[1],"]\n")
    if (int(Action[0])>int(Action[1])):
        print("Le joueur 1 commence.")
        Jeu['joueurnum']=1
    else:
            if Jeu['stylenum']==2:
                print("Le joueur 2 commence.")
                Jeu['joueurnum']=2
            else:
                print("L'IA commence.")
    input("Press Enter to Start the game.\t")
    print("\n")


    while (turn(**Jeu)!=1):
        pass
    winner=Jeu['joueurnum']
    if (Jeu['stylenum']==1 and winner==1):
        winner="L'IA"
    else:
        if Jeu['joueurnum']==1:
            winner="Joueur 2"
        else:
            winner="Joueur 1"


    print("\t  Fin du jeu!\n\t",winner,"a gagne !")

main()