import os
def pronuncia (parametro):
    stringa="say "
    os.system(stringa +parametro)
    
def buoncompleanno(nome):
    Frase=["happy bertuddey to you!", "tooohhh" , "ioooouuuuu"]
    pronuncia( Frase[0] )
    pronuncia ( Frase[0] ) 
    pronuncia (Frase[0])   
    pronuncia (nome)  
    pronuncia (Frase[0] )
    pronuncia (Frase[1] )
    pronuncia (Frase[2] )

#pronuncia("birthday")
buoncompleanno("Debora!")
