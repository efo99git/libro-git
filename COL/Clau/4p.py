cursos=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas=[]
for a in cursos:
    nota=(input("¿Qué nota has sacado en "+a+"? :"))
    notas.append(nota)
for i in range(len(cursos)):
    print("Yo en " + cursos[i] +" he sacado " +notas[i])
    