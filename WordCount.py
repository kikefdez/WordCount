
def word_distribution(s, word_list = None):
    respuesta = 'There is no string to analyze'
    if (len(s) > 0 ):
        word_list = {}
        lista_s = s.split()
        for palabra in lista_s:
            palabra = palabra.lower()
            if not palabra[len(palabra) -1].isalpha():
                palabra = palabra[0:len(palabra) - 1]
            if palabra in word_list:
                word_list[palabra] += 1
            else:
                word_list[palabra] = 1
        respuesta = word_list
    return respuesta



s = "Hello. How are you? Please say hello if you don't love me!"
print(word_distribution(s))