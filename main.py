meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }

word = input("Введите непонятное слово:").upper()

if word in meme_dict.keys():
    print(meme_dict.get(word))

else:
    print("Извините, но слово не найдено")
