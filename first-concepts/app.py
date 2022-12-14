from tkinter import *
import sys

def main():
    menu = Tk()
    menu.title("Name Painter")
    width_x_heigth = "500x350"
    initial_position = "+200+200"
    menu.geometry(width_x_heigth+initial_position)
    menu.resizable(True, True) # faz com não possamos ou não maximir a janela
    menu.minsize(width=500, height=250)
    menu.maxsize(width=700, height=400)
    menu['bg'] = "#4A4A4A"
    maximized_screen = "zoomed"
    menu.state(maximized_screen)
    # minimized_screen = "iconic"
    icon_pencil = sys.path[0]+"\\images\\pencil.ico"
    print(sys.path[0])
    menu.iconbitmap(icon_pencil)

    ##botão
    button = Button(menu, text="Run", command=  lambda:click_Run(), bg="blue", fg="yellow", font="Arial 20 bold", bd=2)
    button.pack()

    ## Label
    label_first_name = Label(
        menu, text="First Name", bd=2, relief="solid"
        ).pack()

    label_last_name = Label(menu, text="Last Name").pack()
    ## pack que define a ordem dos elementos



    menu.mainloop()

def click_Run():
    print("Botão clicado")

if __name__ == "__main__":
    main()