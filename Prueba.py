import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario Básico")
ventana.geometry("300x150")

# Etiqueta y campo para el nombre
labelNombre = tk.Label(ventana, text="Nombre:")
labelNombre.pack(pady=5)
entryNombre = tk.Entry(ventana)
entryNombre.pack(pady=5)

# Etiqueta y campo para el correo
labelCorreo = tk.Label(ventana, text="Correo:")
labelCorreo.pack(pady=5)
entryCorreo = tk.Entry(ventana)
entryCorreo.pack(pady=5)

# Ejecutar la ventana
ventana.mainloop()
