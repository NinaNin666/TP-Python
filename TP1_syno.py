
# librairie graphique Python
#from tkinter import *

from synonymes import synonymo


print("Bonjour, vous recherchez un synonyme ?")
print("Tapez donc votre mot ci-dessous : ")
synoRecherche = input()


print("Résultat de votre recherche : " + synoRecherche)

nbreLettresMot = len(synoRecherche)
#print(nbreLettresMot)

if nbreLettresMot < 2 or nbreLettresMot >= 26:
	print("Votre mot doit comporter entre 2 et 25 caractères")

else:
	#print(synonymo(synoRecherche))
	# On met le retour dans une variable
	list_syno = synonymo(synoRecherche)
	#print(list_syno) #affiche en liste []

	if len(list_syno) == 0:

		print("Aucun synonyme")

	else:
		# J'utilise ta méthode C ci-dessous
		for synoTrouve in list_syno:
			print("-" + " " + synoTrouve)





"""
	#si tableau vide, on affiche : il n ya pas de de syno pour votre mot

!!!! Dans presque toutes mes tentatives j'ai un message d'erreur pour 'elif' et je ne trouve 
pas laquelle, ou lesquelle

if nbreLettresMot < 2 or nbreLettresMot >= 26:
	print("Votre mot doit comporter entre 1 et 25 caractères")
elif (synoRecherche == ([])) :
	print("Aucun synonyme trouvé, ou mot non reconnu")
else:
	print(synonymo(synoRecherche))	


ou encore :

if nbreLettresMot = []:
	print("Aucun synonyme trouvé, ou mot non reconnu")
elif 
	print("Votre mot doit comporter entre 2 et 25 caractères")
else:
	print(synonymo(synoRecherche))




ou :

synoRecherche = []
if not synoRecherche:
	print('Aucun synonyme trouvé, ou mot non reconnu')
elif
	print("Votre mot doit comporter entre 2 et 25 caractères")
else:
	print(synonymo(synoRecherche))



ou bien :

if nbreLettresMot < 2 or nbreLettresMot >= 26:
	print("Votre mot doit comporter entre 2 et 25 caractères")
elif
	print(synonymo(synoRecherche))
else:
	return synoRecherche or Aucun synonyme trouvé, ou mot non reconnu




ou alors

if nbreLettresMot <= 2 or nbreLettresMot >= 26:
	print("Votre mot doit comporter entre 1 et 25 caractères")
elif
	print(synonymo(synoRecherche))
else:
 	return synoRecherche if len(synoRecherche) > 0 else Aucun synonyme trouvé, ou mot non reconnu



ou peut-être
 return synoRecherche if len(synoRecherche) >= 2 else Aucun synonyme trouvé, ou mot non reconnu
 ça me parait possible, puisque la fonction len() renvoie le nombre des éléments dans un objet... ?

ou j'ai pensé a :


if nbreLettresMot < 2 or nbreLettresMot >= 26:
	print("Votre mot doit comporter entre 2 et 25 caractères")
elseif:
	print(len([]))
	print ("Aucun synonyme trouvé, ou mot non reconnu")
else
	print(synonymo(synoRecherche))



ou rajouter
elementSupprime = maListe.pop([]) oui tiré par les cheveux mais je les tire souvent...



et encore :

if nbreLettresMot < 2 or nbreLettresMot >= 26:
	print("Votre mot doit comporter entre 2 et 25 caractères")
else:
	print(synonymo(synoRecherche))
elif synoRecherche == ([]):
print ("Aucun synonyme trouvé, ou mot non reconnu")


NB : J'ai aussi trouvé l'objet SET, comme len(set), s.discard('d') ? qui me semblerait vraiment convenir,
je crois, puisqu'on peut l'utiliser entre autre pour remplacer des éléments par d'autres (add et remove).
Et qu'il n'y a pas d'ordre stricto senso à respecter pour afficher les liste, même si c'est mieux qu'elle
soit affichée alphabétiquement bien sûr et si j'ai  capté correctement je crois que l'utilisation
de cet objet boulverse l'ordre d'affichage.
Par contre je ne comprend pas du tout comment l'utiliser.

Ou encore :

liste = []
liste
[]
liste.append(1)
liste
[1]
liste.append("Aucun synonyme trouvé, ou mot non reconnu")
liste
[1, 'Aucun synonyme trouvé, ou mot non reconnu']

"""




