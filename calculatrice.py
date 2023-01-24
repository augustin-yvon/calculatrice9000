from tkinter import *
import csv

interface = Tk()
interface.title('Calculatrice')

text_resultat = Text(interface,height = 1, width = 14, font='lucida 24 bold', fg='black', bg='#ddd', borderwidth=10)
text_resultat.grid(row = 1, column = 1,columnspan = 5)

calcul = ""

historique = Tk()
historique.title('Historique')
historique.geometry('200x400')

text = Text(historique, font='lucida 24 bold', fg='black', bg='#ddd')
text.grid(row = 0, column = 0)

def ajout_calcul(symbol):
    global calcul
    historique = ""
    calcul += str(symbol)
    for i in calcul:
        if i == '√':
            historique = str(calcul) + " = " + str(float(calcul.strip('√'))**(1/2)) + "\n"
            calcul = calcul.strip('√')
            f = open("historique.csv", "a", encoding='utf-8')
            f.write(historique)
            f.close()
            try:
                text_resultat.delete(1.0,"end")
                text_resultat.insert(1.0, pow(float(calcul), 1/2))
            except:
                effacer()
                text_resultat.insert(1.0,"Erreur")
        elif i == '²':
            calcul = calcul.strip('²')
            historique = calcul + "²" + " = " + str(pow(float(calcul), 2)) + "\n"
            f = open("Historique.csv","a", encoding='utf-8')
            f.write(historique)
            f.close()
            try:
                text_resultat.delete(1.0,"end")
                text_resultat.insert(1.0, pow(float(calcul), 2))
            except:
                effacer()
                text_resultat.insert(1.0,"Erreur")
        elif i == '%':
            hist_calc = calcul
            calcul = calcul.strip('%')
            historique = hist_calc + " = " + str(float(calcul) / 100) + "\n"
            f = open("Historique.csv","a", encoding='utf-8')
            f.write(historique)
            f.close()
            try:
                text_resultat.delete(1.0,"end")
                text_resultat.insert(1.0, float(calcul) / 100)
            except:
                effacer()
                text_resultat.insert(1.0,"Erreur")
        elif i == 'e':
            hist_calc = calcul
            calcul = calcul.strip('e')
            historique = hist_calc + " = " + str(pow(float(2.718281828459045235360287471352662497757247093699959574966967), float(calcul))) + "\n"
            f = open("Historique.csv","a", encoding='utf-8')
            f.write(historique)
            f.close()
            try:
                text_resultat.delete(1.0,"end")
                text_resultat.insert(1.0, pow(float(2.718281828459045235360287471352662497757247093699959574966967), float(calcul)))
            except:
                effacer()
                text_resultat.insert(1.0,"Erreur")
        else:
            text_resultat.delete(1.0,"end")
            text_resultat.insert(1.0, calcul)

def eval_calul():
    global calcul
    try:
        hist_calc = calcul
        calcul = str(eval(calcul))
        text_resultat.delete(1.0,"end")
        text_resultat.insert(1.0, calcul)
        historique = hist_calc + " = " + calcul + "\n"
        f = open("Historique.csv","a", encoding='utf-8')
        f.write(historique)
        f.close()
    except:
        effacer()
        text_resultat.insert(1.0,"Erreur")

def effacer():
    global calcul
    calcul = ""
    text_resultat.delete(1.0,"end")

def afficher_historique():
    global text
    global historique
    file = open('Historique.csv', "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        text.insert(1.0, line.strip()+"\n")
    historique.mainloop()

def suprrimer_historique():
    f = open("Historique.csv", "w+")
    f.close()
    historique.mainloop()




#Bouton de 0 à 9
btn_0 = Button(interface, text = '0', command = lambda:ajout_calcul(0), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_0.grid(row = 7, column = 2)

btn_1 = Button(interface, text = '1', command = lambda:ajout_calcul(1), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_1.grid(row = 6, column = 1)

btn_2 = Button(interface, text = '2', command = lambda:ajout_calcul(2), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_2.grid(row = 6, column = 2)

btn_3 = Button(interface, text = '3', command = lambda:ajout_calcul(3), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_3.grid(row = 6, column = 3)

btn_4 = Button(interface, text = '4', command = lambda:ajout_calcul(4), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_4.grid(row = 5, column = 1)

btn_5 = Button(interface, text = '5', command = lambda:ajout_calcul(5), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_5.grid(row = 5, column = 2)

btn_6 = Button(interface, text = '6', command = lambda:ajout_calcul(6), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_6.grid(row = 5, column = 3)

btn_7 = Button(interface, text = '7', command = lambda:ajout_calcul(7), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_7.grid(row = 4, column = 1)

btn_8 = Button(interface, text = '8', command = lambda:ajout_calcul(8), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_8.grid(row = 4, column = 2)

btn_9 = Button(interface, text = '9', command = lambda:ajout_calcul(9), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_9.grid(row = 4, column = 3)


#Bouton parenthèse
btn_open = Button(interface, text = '(', command = lambda:ajout_calcul('('), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_open.grid(row = 3, column = 2)

btn_close = Button(interface, text = ')', command = lambda:ajout_calcul(')'), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_close.grid(row = 3, column = 3)


#Bouton opérateur
btn_somme = Button(interface, text = '+', command = lambda:ajout_calcul('+'), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_somme.grid(row = 3, column = 4)

btn_soustraction = Button(interface, text = '-', command = lambda:ajout_calcul('-'), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_soustraction.grid(row = 4, column = 4)

btn_produit = Button(interface, text = 'x', command = lambda:ajout_calcul('*'), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_produit.grid(row = 5, column = 4)

btn_division = Button(interface, text = '/', command = lambda:ajout_calcul('/'), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_division.grid(row = 6, column = 4)


#Bouton opérateur scientifique
btn_carré = Button(interface, text = 'x²', command = lambda:ajout_calcul('²'), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_carré.grid(row = 2, column = 1)

btn_racine = Button(interface, text = '√x', command = lambda:ajout_calcul('√'), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_racine.grid(row = 2, column = 2)

btn_pourcentage = Button(interface, text = '%', command = lambda:ajout_calcul('%'), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_pourcentage.grid(row = 2, column = 3)

btn_exponentielle = Button(interface, text = 'exp', command = lambda:ajout_calcul('e'), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_exponentielle.grid(row = 2, column = 4)


#Bouton égal et clear
btn_egal = Button(interface, text = '=', command = eval_calul, width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_egal.grid(row = 7, column = 4)

btn_clear = Button(interface, text = 'C', command = effacer, width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_clear.grid(row = 3, column = 1)


#Bouton virgule et moins
btn_virgule = Button(interface, text = ',', command = lambda:ajout_calcul('.'), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_virgule.grid(row = 7, column = 3)

btn_negatif = Button(interface, text = '+/-', command = lambda:ajout_calcul('-'), width = 5, font = ('Arial', 14), borderwidth=3, fg='black', bg='grey')
btn_negatif.grid(row = 7, column = 1)

#Bouton historique
btn_suppr_hist = Button(interface, text = 'Suppr historique', command = suprrimer_historique, font = 'Arial 13', bd = 3, fg='black', bg='grey')
btn_suppr_hist.grid(row = 8, column = 1, columnspan = 2)
btn_suppr_hist = Button(interface, text = 'Historique', command = afficher_historique, font = 'Arial 13', bd = 3, fg='black', bg='grey')
btn_suppr_hist.grid(row = 8, column = 3, columnspan = 2)

interface.mainloop()