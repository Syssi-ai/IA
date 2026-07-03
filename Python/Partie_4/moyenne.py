from ast import Break
def resultat(moyenne) :
  if moyenne >18 and moyenne <20 :
   return "Mention très bien avec félicitations du jury"
  elif moyenne >16 and moyenne <18 :
   return "Mention très bien"
  elif moyenne >14 and moyenne <16 : 
   return "Mention bien"
  elif moyenne >12 and moyenne <14 :
   return "Mention assez bien"
  elif moyenne >10 and moyenne <12 :
   return "Mention passable"
  else :
   return "Refusé"   


def calcul_moyenne (notes) :
  x = 0
  for i in notes :
   x = x + i
  return x/len(notes)

notes_balkis = []
while True :
  A = input("Donnez moi votre note (ou Fini)")
  if A == "Fini" :
     break
  else :
     notes_balkis.append(int(A))

print("Les notes sont:", notes_balkis)
y = calcul_moyenne(notes_balkis) 
print("La moyenne est:", y)
print("Tu as eu la", resultat(y))