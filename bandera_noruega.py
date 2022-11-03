from tkinter import*

ventana_principal=Tk()
ventana_principal.title("Bandera de noruega")

ventana_principal.geometry("700x400")

ventana_principal.resizable(0,0)
ventana_principal.config(bg= "red")



frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg= "white", width=100, height=400)
frame_entrada.place(x=200,y=0)


frame_operciones=Frame(ventana_principal)
frame_operciones.config(bg= "white", width=700, height=100)
frame_operciones.place(x=0,y=150)


frame_operciones=Frame(ventana_principal)
frame_operciones.config(bg= "blue4", width=700, height=50)
frame_operciones.place(x=0,y=175)

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg= "blue4", width=50, height=400)
frame_entrada.place(x=225 , y=0)



ventana_principal.mainloop()