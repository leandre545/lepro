a=int(input("entrez un nombre: "))
if a==0:
    print("entrez un nombre diferent de zero")
else:    
    b=a*a
    
    print(b)
    c=a*a*a
    print("le curbe de la valeur entre est"+" " +str(c))
    d=1/a
    print("l'inverse de la valeur entrer est"+" " +str(d))
    M=(b+c+d)/3
    print("la moyenne des different resultat est"+" " +str(M))
    delta=c*c-4*b*d
    print("le discriminant est"+" " +str(delta))
    if delta==0:
        x=-(c*c)/(2*b)
        print("il ya une solution unique qui est:"+" "+str(x))
    elif delta>0:
        import math
        y=(-c-math.sqrt(delta))/(2*b)
        z=(-c+math.sqrt(delta))/(2*b)
        print("nous avons deux solution qui son"+" "+str(y)+" "+"et "+str(z))
    else:
        print("IL YA Pas de solution")    
