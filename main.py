
f = open("./Input/Letters/starting_letter.txt", "r")
r = open("./Input/Names/invited_names.txt", "r")
texto = f.readlines()
nomes = r.readlines()



for i in range(len(nomes)):
    texto_desejado = nomes[0].replace("[name]", f"{nomes[i]}")
    l = open(f"./Output/letterTo{nomes[0].strip()}", "x")
    l.write(texto_desejado)
    for k in range(1, len(texto)):
       l.write(texto[k])
    l.close()
    



f.close()
r.close()


    