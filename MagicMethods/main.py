from Clases.Mago import Mago

merlin = Mago("Merlin",["Volar","Nadar"])
morgana = Mago("Morgana",["Bolas de fuego","Nadar"])

print(merlin) #devuelve: Mago: Merlin 
print(len(morgana)) # devuelve el len

print(merlin == morgana) # devuelve False porque los nombres y hechizos son diferentes
