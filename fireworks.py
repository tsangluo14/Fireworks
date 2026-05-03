import turtle
import time
import random
fw1=turtle.Turtle()
fw1.hideturtle()
fw2=turtle.Turtle()
fw2.hideturtle()
fw3=turtle.Turtle()
fw3.hideturtle()
fw4=turtle.Turtle()
fw4.hideturtle()
sc=turtle.Screen()
sc.bgcolor('black')
sc.tracer(0) 

def configFirework(fw,x,y):
    fw.penup()
    fw.goto(x,y)
    fw.pendown()
    
    scale=random.uniform(0.1,1.5)
    nlines=random.randint(6,15)
    color=random.choice(['cyan','purple','pink','teal','green','red','orange','gold'])
    fw.pencolor(color)
    fw.pensize(3)
    total=100*scale
    gap=10*scale
    return nlines,total,gap
    
def fireworkStep(fw, nlines, total, gap):
    for _ in range(nlines):
        fw.pu();fw.fd(gap);fw.pd()
        fw.fd(total-gap)
        fw.pu();fw.bk(total);fw.pd()
        fw.rt(360/nlines)
    fw.rt(180/nlines)
    for _ in range(nlines):
        fw.pu();fw.fd(gap/2);fw.pd()
        fw.fd(total/2-gap/2)
        fw.pu();fw.bk(total/2);fw.pd()
        fw.rt(360/nlines)
    fw.lt(180/nlines)
    
    total*=1.05
    gap*=1.2
    return total,gap


while True:
    x1,x2,x3,x4 = random.sample(range(-300,300), 4)
    y1,y2,y3,y4 = random.sample(range(-300,300), 4)
    
    nlines1, total1, gap1 = configFirework(fw1,x1,y1)
    nlines2, total2, gap2 = configFirework(fw2,x2,y2)
    nlines3, total3, gap3 = configFirework(fw3,x3,y3)
    nlines4, total4, gap4 = configFirework(fw4,x4,y4)
    
    while total1-gap1>0 or total2-gap2>0 or total3-gap3>0 or total4-gap4>0:
        if total1-gap1>0:
            total1, gap1 = fireworkStep(fw1, nlines1, total1, gap1)
        if total2-gap2>0:
            total2, gap2 = fireworkStep(fw2, nlines2, total2, gap2)
        if total3-gap3>0:
            total3, gap3 = fireworkStep(fw3, nlines3, total3, gap3)
        if total4-gap4>0:
            total4, gap4 = fireworkStep(fw4, nlines4, total4, gap4)
            
        sc.update()
        fw1.clear()
        fw2.clear()
        fw3.clear()
        fw4.clear()
        time.sleep(0.01)
        
    fw1.clear()
    fw2.clear()
    fw3.clear()
    fw4.clear()
    time.sleep(0.05)

sc.update()
