meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Una risa"
            }
            
word = input ("Introduce una palabra: ")

if word in meme_dict.keys ():
    print (meme_dict[word])
else:
    print("No está dicha palabra en el diccionario")
