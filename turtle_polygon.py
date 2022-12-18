"""
Írj egy Python programot, amely a teknőcgrafika és eseményvezérlés segítségével
billentyűnyomás hatására egy szabályos poligont rajzol ki! A 3-as karakter esetén
háromszöget, a 4-es hatására négyszöget, és így tovább egészen a szabályos kilencszögig.
Mindegyik sokszög legyen más színű!
"""


import turtle

teknöc = turtle.Turtle()
ablak = turtle.Screen()
ablak.bgcolor("green")

def haromszog():
    for i in range(3):
        teknöc.forward(90)
        teknöc.left(120)
        teknöc.color("yellow")
    

def negyszog():
    for i in range(4):
        teknöc.forward(90)
        teknöc.left(90)
        teknöc.color("white")
    


def otszog():
    for i in range(5):
        teknöc.forward(90)
        teknöc.left(72)
        teknöc.color("blue")

def hatszog():
    for i in range(6):
        teknöc.forward(90)
        teknöc.left(60)
        teknöc.color("black")

def hetszog():
    for i in range(7):
        teknöc.forward(90)
        teknöc.left(51.43)
        teknöc.color("pink")

def nyolcszog():
    for i in range(8):
        teknöc.forward(90)
        teknöc.left(45)
        teknöc.color("purple")

def kilencszog():
    for i in range(9):
        teknöc.forward(90)
        teknöc.left(40)
        teknöc.color("grey")
    

ablak.onkey(haromszog, "3") 
ablak.onkey(negyszog, "4")   
ablak.onkey(otszog, "5")
ablak.onkey(hatszog, "6")  
ablak.onkey(hetszog, "7")     
ablak.onkey(nyolcszog, "8")  
ablak.onkey(kilencszog, "9")  



ablak.listen()
ablak.mainloop()
