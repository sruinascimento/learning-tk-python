from tkinter import *
import sys

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
    file_menu.add_command(label="Full Name", command= lambda: draw_name("Full Name"))
    
    ##passando as opções para o menu
    menu_bar.add_cascade(label="File", menu=file_menu)
    #configurando o app para ter o menu
    app.config(menu=menu_bar)

    app.mainloop()

def draw_name(name):
    print(name)

if __name__ == "__main__":
    main()