import tkinter

ventana = tkinter.Tk()
ventana.title("CALCULADORA DE CALCULO DIFERENCIAL")
ventana.geometry("+480+180")




label_titulo = tkinter.Label(ventana, text = "Calculadora de limites de funciones" , font="20")


label_numerador = tkinter.Label(ventana, text = "INGRESE EL VALOR DEL NUMERADOR", font="10" )
label_denominador = tkinter.Label(ventana, text = "INGRESE EL VALOR DEL DENOMINADOR ", font="10" )
label_x = tkinter.Label(ventana, text = "INGRESE EL VALOR DE X ", font="10" )

e_valor1 = tkinter.Entry(ventana, font = "20")
e_valor2 = tkinter.Entry(ventana, font = "20")
e_valor3 = tkinter.Entry(ventana, font = "20")
#numeros de 1 al 10
button_cal = tkinter.Button(ventana, text = "CALCULAR", bg="orange")
boton1 = tkinter.Button(ventana, text = "1", font="40", width = 10)
boton2 = tkinter.Button(ventana, text = "2", font="40", width = 10)
boton3 = tkinter.Button(ventana, text = "3", font="40", width = 10)
boton4 = tkinter.Button(ventana, text = "4", font="40", width = 10)
boton5 = tkinter.Button(ventana, text = "5", font="40", width = 10)
boton6 = tkinter.Button(ventana, text = "6", font="40", width = 10)
boton7 = tkinter.Button(ventana, text = "7", font="40", width = 10)
boton8 = tkinter.Button(ventana, text = "8", font="40", width = 10)
boton9 = tkinter.Button(ventana, text = "9", font="40", width = 10)
boton0 = tkinter.Button(ventana, text = "0", font="40", width = 25)


boton_borrar = tkinter.Button(ventana, text = "AC", font="40", width = 10)
boton_parentesis1 = tkinter.Button(ventana, text = "(", font="40", width = 10)
boton_parentesis2 = tkinter.Button(ventana, text = ")", font="40", width = 10)
boton_punto = tkinter.Button(ventana, text = ".", font="40", width = 10)

boton_div = tkinter.Button(ventana, text = "/", font="40", width = 10)
boton_multi = tkinter.Button(ventana, text = "x", font="40", width = 10)
boton_sum = tkinter.Button(ventana, text = "+", font="40", width = 10)
boton_resta = tkinter.Button(ventana, text = "-", font="40", width = 10)
boton_igual = tkinter.Button(ventana, text = "=", font="40", width = 10)



label_titulo.grid(row= 0, column= 0, columnspan=2)

label_numerador.grid(row= 1, column= 0)
label_denominador.grid(row= 2, column= 0)
label_x.grid(row= 3, column= 0)

e_valor1.grid(row= 1, column= 1)
e_valor2.grid(row= 2, column= 1)
e_valor3.grid(row= 3, column= 1)

button_cal.grid(row=4, column=1)

#BOTONES DEL 1 AL 10
#
boton_borrar.grid(row = 5 ,column = 0, padx = 10, pady = 10)
boton_parentesis1.grid(row = 5 ,column = 1, padx = 10, pady = 10)
boton_parentesis2.grid(row = 5,column = 2, padx = 10, pady = 10)
boton_div.grid(row = 5,column = 3, padx = 10, pady = 10)


boton7.grid(row = 6,column = 0, padx = 5, pady = 5)
boton8.grid(row = 6,column = 1, padx = 5, pady = 5)
boton9.grid(row = 6,column = 2, padx = 5, pady = 5)
boton_multi.grid(row = 6,column = 3, padx = 5, pady = 5)

boton4.grid(row = 7,column = 0, padx = 5, pady = 5)
boton5.grid(row = 7,column = 1, padx = 5, pady = 5)
boton6.grid(row = 7,column = 2, padx = 5, pady = 5)
boton_sum.grid(row = 7,column = 3, padx = 5, pady = 5)

boton1.grid(row = 8,column = 0, padx = 5, pady = 5)
boton2.grid(row = 8,column = 1, padx = 5, pady = 5)
boton3.grid(row = 8,column = 2, padx = 5, pady = 5)
boton_resta.grid(row = 8,column = 3, padx = 5, pady = 5)

boton0.grid(row = 9,column = 1,  padx = 5, pady = 5)
boton_punto.grid(row = 9,column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 9,column = 3, padx = 5, pady = 5)


label_resultado = tkinter.Label(ventana)
ventana.mainloop()
