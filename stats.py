def get_num_words(filepath):
    with open(filepath) as f:
        file = f.read()
        num_words = len(file.split())
        return num_words
def get_dic_letter_counter(filepath):
    with open(filepath) as f:
        file = f.read()
        list_char_couter = []
        dic_letter_counter = {}
        for letter in file:
            if letter.isalpha():
                if letter.lower() in dic_letter_counter:
                    dic_letter_counter[letter.lower()] += 1
                else:
                    dic_letter_counter[letter.lower()] = 1
        for char, count in dic_letter_counter.items():
            list_char_couter.append({"char": char, "num": count})
        list_char_couter.sort(key=lambda x: x["num"], reverse=True)
        return list_char_couter   
