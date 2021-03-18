def common_letters(word_one, word_two):
    temp = ''
    com = ""
    for i in word_one:
        temp = i
        if temp in word_two:
            com = com + temp
    joined_com = ', '.join(com)
    print(f"Common letters: {joined_com}")
    
common_letters(word_one, word_two)