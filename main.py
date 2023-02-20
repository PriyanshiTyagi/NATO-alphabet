import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data=pandas.read_csv("nato_phonetic_alphabet.csv")
data={row.letter:row.code for (index,row) in data.iterrows()}



# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def asking_input():
    user = input("Enter a word:").strip().upper()
    try:
        phonetics= [data[letter] for letter in user]

    except KeyError:
        print("Sorry only alphabets are allowed...")
        asking_input()
    else:
        print(phonetics)
asking_input()
