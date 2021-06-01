# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
pygame.init()


#from tkinter import *

def main():

    pygame.display.set_caption("RARENE")
    pygame.display.set_mode((800,600))

    running=True

    while running:
        print("Hello")
        running=False
"""
    #Création fenêtre:
    window = Tk()

    #Parametrage fenêtre:
    window.title("Rarene")
    windows_size_x = 800
    windows_size_z = 600
    #windows_size_x = input("Dimension de la fenetre en x? :")
    #windows_size_z = input("Dimension de la fenetre en z? :")
    window.geometry(str(windows_size_x) + "x" + str(windows_size_z))
    window.minsize(str(windows_size_x) , str(windows_size_z))
    window.maxsize(str(windows_size_x) , str(windows_size_z))
    window.config(background='#4065A4')

    #Affichage de la fenêtre:
    window.mainloop()
"""

if __name__ == '__main__':
    main()

