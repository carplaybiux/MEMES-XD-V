meme_dict = {
    "LOL": "Una respuesta a algo gracioso",
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo/enojado",
    "GPI": "manera sarcastica de demostrar enojo por no ser invitado a algun evento",
    "GG": "manera de demostrar de que algo esta terminado y fue muy facil",
    "OMATOPOPPIH": "Dicese de la cancion de el hipopotamo al revez",
}

print("¡Bienvenido al diccionario de memes!")
print("Por favor, introduce 5 palabras en mayúsculas para conocer su significado:")
for _ in range(5):
    word = input("Palabra: ")
    if word in meme_dict:
        print("Significado:", meme_dict[word])
    else:
        print("Lo siento, esa palabra no está en el diccionario de memes.")
