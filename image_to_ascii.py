import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage
from tkinter.ttk import Progressbar, Style
from PIL import Image, ImageDraw, ImageEnhance
import math
import sys
import os

def resource_path(relative_path):
    """ Obtém o caminho absoluto do recurso, funciona para dev e para PyInstaller """
    try:
        # PyInstaller cria uma pasta temporária e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def get_some_char(h):
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?- _+~<>i!lI;:,\"^`'. "[::-1]
    char_arr = list(chars)
    l = len(char_arr)
    mul = l / 256
    return char_arr[math.floor(h * mul)]

def enhance_saturation(image, factor):
    """
    Ajusta a saturação da imagem.

    Args:
        image (PIL.Image): A imagem a ser ajustada.
        factor (float): O fator de saturação. 1.0 significa nenhuma mudança,
                        menor que 1.0 significa menos saturação, maior que 1.0 significa mais saturação.

    Returns:
        PIL.Image: A imagem com a saturação ajustada.
    """
    converter = ImageEnhance.Color(image)
    return converter.enhance(factor)

def convert_image_to_ascii(input_file, output_file):
    try:
        image = Image.open(input_file)
        scale_fac = 0.4  # Reduzindo o fator de escala para melhorar o desempenho
        char_width = 10
        char_height = 18
        w, h = image.size
        image = image.resize((int(scale_fac * w), int(scale_fac * h * (char_width / char_height))), Image.NEAREST)

        # Aumentar a saturação da imagem
        image = enhance_saturation(image, 1.5)

        w, h = image.size
        pixels = image.load()

        output_image = Image.new('RGB', (char_width * w, char_height * h), color=(0, 0, 0))
        draw = ImageDraw.Draw(output_image)

        total_pixels = w * h
        progress = 0

        for i in range(h):
            for j in range(w):
                try:
                    # Obtemos a cor do pixel
                    pixel = pixels[j, i]
                    if isinstance(pixel, int):
                        r, g, b = pixel, pixel, pixel
                    else:
                        r, g, b = pixel[:3]

                    # Calculamos o cinza
                    grey = int((r / 3 + g / 3 + b / 3))

                    # Desenhamos o caractere ASCII na imagem de saída
                    char = get_some_char(grey)
                    draw.text((j * char_width, i * char_height), char, fill=(r, g, b))

                except Exception as e:
                    messagebox.showerror("Erro", f"Ocorreu um erro ao converter a imagem:\n{str(e)}")

                # Atualizamos a barra de progresso a cada linha processada
                progress += 1
                if progress % w == 0:
                    percent = (progress / total_pixels) * 100
                    progress_var.set(int(percent))  # Atualizamos a variável da barra de progresso
                    root.update_idletasks()  # Atualizamos a interface gráfica

        output_image.save(output_file)
        messagebox.showinfo("Sucesso", "Imagem convertida com sucesso!")

        # Abrir a imagem após conversão
        open_image(output_file)

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao converter a imagem:\n{str(e)}")

def open_image(image_path):
    try:
        if os.path.exists(image_path):
            os.startfile(image_path)  # Abre o arquivo no visualizador padrão
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao abrir a imagem:\n{str(e)}")

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if output_path:
            convert_image_to_ascii(file_path, output_path)

# Cria a janela principal
root = tk.Tk()
root.title("Conversor de Imagem para ASCII")

# Definir o ícone da janela (substitua com o caminho correto para seu arquivo .ico)
img_path = resource_path("mobile1.png")
img = PhotoImage(file=img_path)
root.iconphoto(False, img)

# Estilo dos widgets
style = Style()
style.configure('TButton', font=('Segoe UI', 12), padding=5)
style.configure('TLabel', font=('Segoe UI', 12), padding=5)
style.configure('TFrame', padding=10)

# Frame para os widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Label de instrução
label = tk.Label(frame, text="Selecione um arquivo de imagem (.jpg, .png, .jpeg) para converter:", font=('Segoe UI', 12))
label.pack()

# Barra de progresso
progress_var = tk.DoubleVar()
progress_bar = Progressbar(frame, orient='horizontal', length=300, mode='determinate', variable=progress_var)
progress_bar.pack(pady=10)

# Botão de seleção de arquivo com cor azul
button_select = tk.Button(frame, text="Selecionar Imagem", command=select_file, bg="#007BFF", fg="white", activebackground="#0056b3", activeforeground="white", font=('Segoe UI', 12))
button_select.pack(pady=10)

# Rodapé
footer_label = tk.Label(root, text="Developed by Edu Zaminelli", font=('Segoe UI', 10), fg='gray')
footer_label.pack(side=tk.BOTTOM, pady=10)

# Centraliza a janela na tela
window_width = 510
window_height = 205  # Ajustado para incluir o rodapé
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# Mantém a janela aberta até que seja fechada pelo usuário
root.mainloop()
