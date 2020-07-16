# Libreria usada 
from tkinter import *
#  Registro de datos en documento externo 
def send_data():
  paciente_info = paciente.get()
  pregunta_info = pregunta.get()
  especialidad_info = especialidad.get()
  DNI_info = str(DNI.get())
  correo_info = str(correo.get())
  print(paciente_info,"\t", pregunta_info,"\t", especialidad_info,"\t", DNI_info,"\t", correo_info)
 
 # Condicional

  if pregunta_info == "si":
    pregunta_info = "Paciente de riesgo"
  else:
    pregunta_info = "Paciente general"


#  Recopilacion de datos e impresion en consola
  file = open("registro.txt", "a")
  file.write(paciente_info)
  file.write("\t")
  file.write(pregunta_info)
  file.write("\t")
  file.write(especialidad_info)
  file.write("\t")
  file.write(DNI_info)
  file.write("\t\n")
  file.write(correo_info)
  file.write("\t\n")
  file.close()
  print(" New user registered. paciente: {} | especialidad: {}   ".format(paciente_info, especialidad_info))
 
#  Agilizacion de registro
  paciente_entry.delete(0, END)
  pregunta_entry.delete(0, END)
  especialidad_entry.delete(0, END)
  DNI_entry.delete(0, END)
  correo_entry.delete(0, END)

#  Lista de especialidades (En proceso)

especialidades = ["Neumologia","Traumatologia","Cardiologia","Endocrinologia"]

#  Interfaz general de la ventana

ventana = Tk()
ventana.geometry("700x500")
ventana.title("Registration Form - Python + Tkinter")
ventana.resizable(False,False)
ventana.config(background = "#0c343d")
main_title = Label(text = "Agendamiento de citas", font = ("Microsoft YaHei UI Light", 20), bg = "#EEEEEE", fg = "black", width = "500", height = "2")
main_title.pack()

# Parte grafica de las variables

paciente_label = Label(text = "Paciente", font = ("BIZ UDGothic", 15), bg = "#EEEEEE")
paciente_label.place(x = 20, y = 80)
pregunta_label = Label(text = "¿Usted padece de covid?", font = ("BIZ UDGothic", 12), bg = "#EEEEEE")
pregunta_label.place(x = 10, y = 150)
especialidad_label = Label(text = "Especialidad", font = ("BIZ UDGothic", 15), bg = "#EEEEEE")
especialidad_label.place(x = 20, y = 220)
DNI_label = Label(text = "DNI", font = ("BIZ UDGothic", 15), bg = "#EEEEEE")
DNI_label.place(x = 20, y = 290)
correo_label = Label(text = "Correo", font = ("BIZ UDGothic", 15), bg = "#EEEEEE")
correo_label.place(x = 20, y = 360)
 
# Definicion de las variables (Data) 

paciente = StringVar()
pregunta = StringVar()
especialidad = StringVar(ventana)
especialidad.set(especialidades[0])
especialidad_label = OptionMenu(ventana, especialidad, *especialidades)
especialidad_label.pack()
especialidad_label.place(x = 295, y = 190)
DNI = StringVar()
correo = StringVar()

# Recuadros de ingreso de datos

paciente_entry = Entry(textvariable = paciente, width = "40")
pregunta_entry = Entry(textvariable = pregunta, width = "40")
especialidad_entry = Entry(textvariable = especialidad, width = "40")
DNI_entry = Entry(textvariable = DNI, width = "40", show = "*")
correo_entry = Entry(textvariable = correo, width = "40")

paciente_entry.place(x = 225, y =85)
pregunta_entry.place(x = 225, y = 155)
especialidad_entry.place(x = 225, y = 225)
DNI_entry.place(x = 225, y = 295)
correo_entry.place(x = 225, y = 365)

# Boton "Guardar"

submit_btn = Button(ventana,text = "Guardar", width = "30", height = "2", command = send_data, bg = "#EEEEEE")
submit_btn.place(x = 240, y = 420)


def vent2():
    ventana2=Toplevel()
    ventana2.geometry("700x500")
    ventana2.title("Asignar Fecha")
    ventana2.configure(background = "black")
    e3 = Label(ventana2, text = "Verificacion", font = ("Microsoft YaHei UI Light", 20), bg = "#FFFFFF", fg = "black", width = "500", height = "2")
    e3.pack()

 
    validacion_label = Label(ventana2, text = "Validacion", font = ("BIZ UDGothic", 15), bg = "#FFFFFF")
    validacion_label.place(x = 20, y = 220)
    validacion = (ventana2,StringVar())
    validacion_entry = Entry(ventana2,textvariable = validacion, width = "40")
    validacion_entry.place(x = 225, y = 225)

    def cerrar():
      ventana2.quit()

    def vent3():
      ventana3=Toplevel()
      ventana3.geometry("400x400")
      ventana3.title("Asignar")
   

    def validar():
      if validacion_entry.get() == "hola123":
        cerrar()
      else: 
        vent3()

    boton= Button(ventana2,text = "verificar", width = "30", height = "2")

    

     

boton_1=Button(ventana,text="Asignar Fecha", command=vent2)
boton_1.place(x = 490, y = 435)


ventana.mainloop()

