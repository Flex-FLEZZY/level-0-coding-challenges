def vowel(str_vowel):
    vow = ""
    str_vowel = str_vowel.lower();
    for i in str_vowel:
        if i in ("a", "e", "i", "o", "u"):
            if i in vow:
                vow = vow
            else:
                vow = vow + i
    joined_vow = ', '.join(vow)
    print(f"Vowels: {joined_vow}")
            
vowel(str_vowel)