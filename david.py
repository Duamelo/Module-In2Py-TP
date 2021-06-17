david = {'python':[17,18,19], 'electro': [14,15,16], 'langage C': [16, 18, 19]}
moyPy = (david['python'][0]+ david['python'][1]+ david['python'][2])/3
moyElec = (david['electro'][0]+ david['electro'][1]+ david['electro'][2])/3
moylangC = (david['langage C'][0]+ david['langage C'][1]+ david['langage C'][2])/3
moyenne = (moyPy + moyElec + moylangC)/3
print(moyenne)



E0

L = list([1,2,3,4,5,6,7,8,9,10])

L[0] += 11
L[1] += 11
L[2] += 11
L[3] += 11
L[4] += 11
L[5] += 11
L[6] += 11
L[7] += 11
L[8] += 11
L[9] += 11

L.append(22)

L.extend([23,24])

L1 = L[1::2]
print("Liste des nombres pairs de la liste L :")
print(L1)
print("Liste des nombres impairs de la liste L :")
L2 = L[::2]
print(L2)

L.pop(3)

print("Voici la  liste L")
print(list(L))


E1

d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age':30}
d['prenom'] = 'Jacques'
print(d.keys())
print(d.values())
print(d)
print(d['prenom'] , d['nom'] + " a" +  d['age'] + " ans")
