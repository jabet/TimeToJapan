import tkinter as tk
from datetime import datetime, timedelta
from PIL import Image, ImageTk
import random

# Establecer la fecha objetivo
target_date = datetime(2025, 11, 25, 10, 5, 00)

# Crear la ventana principal
root = tk.Tk()
root.title("Days to go to Japan!")

size_x = 200
size_y = 100
particle_size_x = 5
particle_size_y = 5

# Cargar y redimensionar la imagen
image = Image.open("background.jpg")
image = image.resize((size_x, size_y), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Crear una etiqueta para mostrar la imagen
image_label = tk.Label(root, image=photo)
image_label.pack()

# Crear un canvas para las partículas
canvas = tk.Canvas(root, width=size_x, height=size_y)
canvas.place(x=0, y=0)

# Mostrar la imagen en el canvas
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Cargar la imagen de la hoja
leaf_image = Image.open("leaf.png")
leaf_image = leaf_image.resize((5, 5), Image.LANCZOS)
leaf_photo = ImageTk.PhotoImage(leaf_image)

# Crear una etiqueta para mostrar la cuenta regresiva
countdown_label = tk.Label(root, font=("Helvetica", 10))
countdown_label.pack()

# Lista para almacenar las partículas
particles = []

# Función para crear nuevas partículas
def create_particle():
    x = random.randint(0, size_x)
    y = 0
    particle = canvas.create_image(x, y, image=leaf_photo)
    particles.append(particle)
    root.after(500, create_particle)

# Función para actualizar las partículas
def update_particles():
    for particle in particles:
        canvas.move(particle, 0, 1)
        if canvas.coords(particle)[1] > (size_y - particle_size_y+3):
            canvas.delete(particle)
            particles.remove(particle)
    root.after(50, update_particles)

# Función para actualizar la cuenta regresiva
def update_countdown():
    now = datetime.now()
    remaining_time = target_date - now
    days = remaining_time.days
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutos, seconds = divmod(remainder, 60)
    countdown_label.config(text=f"{days} días, {hours} horas,  {minutos} minutos")
    root.after(1000, update_countdown)

# Iniciar la creación y actualización de partículas
update_countdown()
create_particle()
update_particles()

# Posicionar la ventana en la esquina superior izquierda de la pantalla
root.geometry("+0+0")

# Ejecutar la aplicación
root.mainloop()