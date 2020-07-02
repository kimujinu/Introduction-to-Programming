import turtle

def olypic_symbol():
    symbol_data = [(0,0,"blue"),(-120,0,"purple"),(60,60,"red"),(-60,60,"yellow"),(-180,60,"green")]

    for data in symbol_data: #data대신에 x,y,color
        t.penup()
        t.goto(data[0], data[1]) #data[0],data[1] 대신에 x,y
        t.pendown()
        t.color(data[2])        #data[2]대신에 color 써도됨
        t.begin_fill()
        t.circle(30)
        t.end_fill()


t = turtle.Turtle()
olypic_symbol()
