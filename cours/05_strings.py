ma_phrase = "J'ai mon masque"
ma_phrase = 'J\'ai mon masque'
ma_phrase  = """
J'ai mon masque 
et je suis content
"""
ma_phrase= "J'ai mon masque \n et je suis content"
print(ma_phrase, type(ma_phrase))
print(ma_phrase)

prenom = "Pierre"
nom = "Nédélec"

# écrire la phrase suivante :
# Je m'apelle Pierre Nédélec.
ma_phrase = "Je m'apelle" +  " " + prenom + " " +nom + '.'


# version python 2
ma_phrase = "Je m'apelle %s %s." % (prenom,nom)
print(ma_phrase)

# version python3 ( dutch )
ma_phrase = "Je m'apelle {0} {1}.".format(prenom, nom)
print(ma_phrase)

# version pythonique
ma_phrase = f"Je m'apelle {prenom} {nom}."
print(ma_phrase)


