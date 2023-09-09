import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# alphabet_lst = list(data.letter)
# code_lst = list(data.code)
# alpha_code = dict(zip(alphabet_lst, code_lst))
# or
# alpha_code = {alphabet_lst[i] : code_lst[i] for i in range(len(alphabet_lst))}
# or
alpha_code = {row.letter: row.code for (index, row) in data.iterrows()}
is_word = True
while is_word:
    user_input = input("Enter a word: ").upper()
    try:
        alpha_code_lst = [alpha_code[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(alpha_code_lst)
        is_word = False
