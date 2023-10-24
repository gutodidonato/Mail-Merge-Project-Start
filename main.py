#TODO: Create a letter using starting_letter.txt 
f = open("./Input/Letters/starting_letter.txt", "r")
r = open("./Input/Names/invited_names.txt", "r")
texto = f.readlines()
nomes = r.readlines()
for i in range(len(nomes)):
    nome_padrao = nomes[i] - "\n"
    l = open(f"./Output/ReadyToSend/para{nome_padrao}", "x")
    l.write(f"Dear {nomes[i]}")
    l.write(texto[1])
    l.write(texto[2])
    l.write(texto[3])
    l.close()
    



f.close()
r.close()


        
        
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp