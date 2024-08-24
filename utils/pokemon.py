import requests
import os
from PIL import Image
import numpy as np

def buscar_pokemon_aleatorio():
    import random
    random_id = random.randint(1, 150) # Pokémons da 1ª Geração
    url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"
    response = requests.get(url)
    pokemon = response.json()
    return pokemon

def download_imagem_pokemon(imagem_url, nome_pokemon):
    pasta_imagens = os.path.join(os.getcwd(), "imagens")
    caminho_arquivo = os.path.join(pasta_imagens, f"{nome_pokemon}.jpg")

    if not os.path.exists(pasta_imagens):
        os.makedirs(pasta_imagens)

    img_data = requests.get(imagem_url).content
    with open(caminho_arquivo, 'wb') as handler:
        handler.write(img_data)

def resize_image(image_path, width, height):
    with Image.open(image_path) as img:
        img = img.resize((width, height))
        return img

def convert_to_ascii(image):
    ascii_chars = " .:-=+*#%@"
    img_array = np.array(image.convert('RGB'))
    gray_scale = np.dot(img_array[...,:3], [0.299, 0.587, 0.114])
    ascii_image = np.zeros((gray_scale.shape[0], gray_scale.shape[1]), dtype=str)
    
    for y in range(gray_scale.shape[0]):
        for x in range(gray_scale.shape[1]):
            gray = gray_scale[y, x]
            index = int(gray / 255.0 * (len(ascii_chars) - 1))
            ascii_image[y, x] = ascii_chars[index]
    
    return ascii_image

def imagem_para_ascii(nome_pokemon):
    pasta_imagens = os.path.join(os.getcwd(), "imagens")
    caminho_arquivo = os.path.join(pasta_imagens, f"{nome_pokemon}.jpg")
    width, height = 90, 45

    image = resize_image(caminho_arquivo, width, height)
    ascii_image = convert_to_ascii(image)

    for row in ascii_image:
        print("".join(row))
