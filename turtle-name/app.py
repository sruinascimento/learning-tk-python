from tkinter import *
import sys

from turtle import Turtle, fillcolor, pen, pencolor, position

def main():
    app = Tk()
    app.title("Name Painter")
    width_x_heigth = "500x350"
    initial_position = "+200+200"
    app.geometry(width_x_heigth+initial_position)
    app.resizable(True, True) # faz com não possamos ou não maximir a janela
    app.minsize(width=500, height=250)
    app.maxsize(width=700, height=400)
    app['bg'] = "#4A4A4A"
    maximized_screen = "zoomed"
    app.state(maximized_screen)
    icon_pencil = sys.path[0]+"\\images\\pencil.ico"
    app.iconbitmap(icon_pencil)


    ##Menu criando uma instância do menu
    menu_bar = Menu(app)
    ##Adicionando opções
    file_menu = Menu(menu_bar)
    file_menu.add_command(label="First Name", command= lambda: draw_name("First Name"))
    file_menu.add_command(label="Last Name", command= lambda: draw_name("Last Name"))
    file_menu.add_command(label="Middle Name", command= lambda: draw_name("Middle Name"))
    
    ##passando as opções para o menu
    menu_bar.add_cascade(label="File", menu=file_menu)
    #configurando o app para ter o menu
    app.config(menu=menu_bar)

    app.mainloop()

def draw_name(name):
    pencil = Turtle()
    pencil.pen(fillcolor="black", pensize=10, pencolor="blue")
    pencil.pensize(10)
    if name == "First Name":
        draw_first_name(pencil)

    if name == "Last Name":
        draw_last_name(pencil)


def draw_first_name(pencil:Turtle) -> None:
    initial_position(pencil)
    # R
    pencil.lt(90)
    pencil.fd(100)
    pencil.rt(90)
    pencil.circle(-30, 180)
    pencil.rt(225)
    pencil.fd(55.82)

    pencil.penup()
    pencil.setpos(pencil.position()[0] + 30, pencil.position()[1])
    # pencil.settiltangle(45)
    pencil.lt(135)
    pencil.pendown()
    #U
    pencil.fd(90)
    pencil.fd(-90)
    pencil.rt(90)
    pencil.fd(39.47)
    pencil.lt(90)
    pencil.fd(90)

    # Pingo do I
    pencil.penup()
    pencil.setpos(pencil.position()[0] + 40, pencil.position()[1] + 20)
    pencil.pendown()
    pencil.circle(1, 360)
    #I
    pencil.penup()
    pencil.setpos(pencil.position()[0], pencil.position()[1] - 20)
    pencil.rt(180)
    pencil.pendown()
    pencil.fd(90)
    pencil.hideturtle()

def draw_last_name(pencil:Turtle) -> None:
    initial_position(pencil)
    #N
    pencil.left(90)
    pencil.fd(100)
    pencil.rt(150)
    pencil.fd(115)
    pencil.lt(150)
    pencil.fd(100)
    print(pencil.position())

    #A
    pencil.penup()
    pencil.setpos(pencil.position()[0] + 30, pencil.position()[1])
    pencil.pendown()
    pencil.lt(180)
    pencil.fd(100)
    pencil.fd(-100)
    pencil.lt(90)
    pencil.fd(50)
    pencil.rt(90)
    pencil.fd(100)
    pencil.fd(-40)
    pencil.rt(90)
    pencil.fd(50)

    pencil.penup()
    pencil.hideturtle()
    pencil.setpos(pencil.position()[0] + 80, pencil.position()[1] - 20)
    pencil.showturtle()
    pencil.pendown()
    #S
    pencil.lt(90)
    pencil.fd(20)
    pencil.lt(90)
    pencil.fd(50)
    pencil.lt(90)
    pencil.fd(50)
    pencil.lt(90)
    pencil.fd(50)
    pencil.rt(90)
    pencil.fd(50)
    pencil.rt(90)
    pencil.fd(50)
    pencil.rt(90)
    pencil.fd(20)


def initial_position(pencil:Turtle) -> None:
    pencil.penup()
    pencil.setpos(-200, 0)
    pencil.pendown()

if __name__ == "__main__":
    main()