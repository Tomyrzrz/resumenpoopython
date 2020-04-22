#Repaso de ventanas en Python
from tkinter import *
from tkinter import messagebox

#----------------------Ventana Raiz--------------------------
raiz = Tk()
raiz.title("Promedio CESOM")
raiz.config(bg="#999999")
raiz.resizable(0,0)

#----------------------FUNCIONES-----------------------------
def calcularPromedio():
	valor_1 = calificacion_t1.get()
	valor_2 = calificacion_t2.get()
	valor_3 = calificacion_t3.get()
	valor_4 = calificacion_t4.get()

	try:
		promedio_final = (float(valor_1) + float(valor_2) + float(valor_3) + float(valor_4))/4
		promedio_result.set(promedio_final)
	
	except Exception as error:
		messagebox.showerror("Error", "Debes colocar calificaciones solo en numeros enteros y decimales\n" + str(error))

def borrarCajas():
	calificacion_t1.set("")
	calificacion_t2.set("")
	calificacion_t3.set("")
	calificacion_t4.set("")
	promedio_result.set("")

def salir():
	raiz.destroy()


#---------------------DISEÑO DE VENTANA----------------------
frame = Frame(raiz, width=600, height=500)
frame.config(bg="#AAAAAA", bd=1, relief="groove")
frame.pack()

trimestre1 = Label(frame, text="1 Trimestre", font=("Arial",13), bg="#AAAAAA")
trimestre1.grid(row=0, column=0, padx=10, pady=14)

calificacion_t1 = StringVar()
calificacion_trime1 = Entry(frame, textvariable=calificacion_t1, bg="#AAAAAA", font=("Arial",12), bd=2)
calificacion_trime1.grid(row=0, column=1, padx=20, pady=14)

trimestre2 = Label(frame, text="2 Trimestre", font=("Arial",13), bg="#AAAAAA")
trimestre2.grid(row=1, column=0, padx=10, pady=8)

calificacion_t2 = StringVar()
calificacion_trime2 = Entry(frame, textvariable=calificacion_t2, bg="#AAAAAA", font=("Arial",12), bd=2)
calificacion_trime2.grid(row=1, column=1, padx=20, pady=8)

trimestre3 = Label(frame, text="3 Trimestre", font=("Arial",13), bg="#AAAAAA")
trimestre3.grid(row=2, column=0, padx=10, pady=8)

calificacion_t3 = StringVar()
calificacion_trime3 = Entry(frame, textvariable=calificacion_t3, bg="#AAAAAA", font=("Arial",12), bd=2)
calificacion_trime3.grid(row=2, column=1, padx=20, pady=8)

trimestre4 = Label(frame, text="4 Trimestre", font=("Arial",13), bg="#AAAAAA")
trimestre4.grid(row=3, column=0, padx=10, pady=8)

calificacion_t4 = StringVar()
calificacion_trime4 = Entry(frame, textvariable=calificacion_t4, bg="#AAAAAA", font=("Arial",12), bd=2)
calificacion_trime4.grid(row=3, column=1, padx=20, pady=8)

promedio = Label(frame, text="Promedio", font=("Arial",13), bg="#AAAAAA")
promedio.grid(row=4, column=0, padx=10, pady=15)

promedio_result = StringVar()
promedio_val = Entry(frame, textvariable=promedio_result, bg="#AAAAAA", font=("Arial",12), bd=2)
promedio_val.grid(row=4, column=1, padx=20, pady=15)

btn_calcular = Button(frame, text="Calcular Promedio", bg="#222222", font=("Arial",13), bd=2, fg="white", command=lambda:calcularPromedio())
btn_calcular.grid(row=5, column=0, padx=25, pady=25, ipadx=3, ipady=3)

btn_borrar = Button(frame, text="Borrar", bg="#222222", font=("Arial",14), bd=2, fg="white", command=lambda:borrarCajas())
btn_borrar.grid(row=5, column=1, padx=25, pady=25, ipadx=16, ipady=3)

btn_salir = Button(frame, text="Salir", bg="#FF0000", font=("Arial",14), bd=2, command=lambda:salir())
btn_salir.grid(row=5, column=2, padx=25, pady=25, ipadx=16, ipady=3)

raiz.mainloop()
