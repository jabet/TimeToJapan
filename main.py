import tkinter as tk
from datetime import datetime, timedelta
from PIL import Image, ImageTk
import random

# Establecer la fecha objetivo
target_date = datetime(2025, 11, 25, 10, 5, 00)

# Crear la ventana principal
root = tk.Tk()
root.title("Days to go to Japan!")

# Eliminar los bordes de la ventana
root.overrideredirect(True)


size_x = 200
size_y = 120
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

text = [
    "¡おはよう Japón!", 
    "Ya queda menos", 
    "¿Tienes todo listo?",
    "No te olvides de la maleta",
    "¿Tienes listo el pasaporte?"
]



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
        if canvas.coords(particle)[1] > size_y - particle_size_y // 2:
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

def update_text():
    canvas.delete("text")
    selected_text = random.choice(text)
    x = size_x // 2
    y = size_y // 2
    halo_color = "white"
    text_color = "red"
    font = ("Helvetica", 12)
    
    halo_items = []
    # Crear el halo
    offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in offsets:
        halo_item = canvas.create_text(x + dx, y + dy, text=selected_text, font=font, fill=halo_color, tag="text", width=size_x - 10)
        halo_items.append(halo_item)
    # Crear el texto principal
    text_item = canvas.create_text(x, y, text=selected_text, font=font, fill=text_color, tag="text", width=size_x - 10)
    
    # Iniciar el fadeout después de 5 segundos
    root.after(5000, fadeout_text, halo_items + [text_item])
    

    root.after(60000, update_text)

# Función para realizar el fadeout del texto
def fadeout_text(items, alpha=1.0, step=0.10):
    if alpha > 0:
        color = f"#{int(255 * alpha):02x}{int(255 * alpha):02x}{int(255 * alpha):02x}"
        for item in items:
            canvas.itemconfig(item, fill=color)
        root.after(100, fadeout_text, items, alpha - step)
    else:
        for item in items:
            canvas.delete(item)


# Iniciar la creación y actualización de partículas
update_countdown()
update_text()
create_particle()
update_particles()

# Posicionar la ventana en la esquina superior izquierda de la pantalla
root.geometry("+0+0")

# Ejecutar la aplicación
root.mainloop()