from tkinter import *

def main():
    menu = Tk()
    menu.title("Name Painter")
    width_x_heigth = "500x350"
    initial_position = "+200+200"
    menu.geometry(width_x_heigth+initial_position)
    menu.resizable(True, True) # faz com não possamos ou não maximir a janela
    menu.minsize(width=500, height=250)
    menu.maxsize(width=700, height=400)
    maximized_screen = "zoomed" #tela maximizada nas alturar e larguras permitidas
    minimized_screen = "iconic"
    icon_pencil = "images/Designcontest-Outline-Pencil.ico"
    menu.iconbitmap(icon_pencil)
    menu.state(maximized_screen)
    menu.mainloop()


if __name__ == "__main__":
    main()