#!/usr/bin/python3.2
import tkinter
from tkinter import *
import random
window = tkinter.Tk()
window.geometry("400x70")
window.title("Adivina el numero")
Texto = tkinter.Label(window, text = "Adivina el numero", font = "Monospace, 15")
Texto.pack(fill = "both")
Texto.grid(row = 1, column = 1)
NumberImput = tkinter.Entry(window, width="15")
NumberImput.grid(row = 1, column = 2)
NumeroBot = random.randint(1, 9999)
NumeroBot = NumeroBot
NumeroPersona = NumberImput.get()
Indicador = ""
def Form():
	global NumberImput
	global window
	global Indicador
	global NumeroBot
#	NumeroOfPersona = int(NumberImput.get())		
	print(NumeroPersona) 
	NumeroOfPersona = int(NumberImput.get())	
	if NumeroOfPersona == NumeroBot:
		print("Lo lograste")
		Indicador = " Lo Lograste"
	if NumeroOfPersona > NumeroBot:
		print("Un numero mas bajo porfavor")
		Indicador = "Un Numero Mas Bajo Porfavor"
	if NumeroOfPersona < NumeroBot:
		print("Un Numero Mas alto porfavor")
		Indicador = "Un Numero mas alto Porfavor"
	Pistero = tkinter.Label(window,text= Indicador)
	Pistero.grid(row = 2, column = 1)
#Texto.pack()
botonGet = tkinter.Button(text = "Aplastame",bg = "orange", command = Form)
botonGet.pack(fill = "both")
botonGet.grid(row = 1, column = 3)
window.mainloop()
