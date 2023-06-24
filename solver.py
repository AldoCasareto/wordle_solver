import requests

def wordle_solver(letters, exclude_letters="", word_length=5):
    url = f"https://api.datamuse.com/words?sp={letters}*&max=1000"
    response = requests.get(url)
    words = response.json()
    solutions = [word["word"] for word in words if len(word["word"]) == word_length and all(letter not in word["word"] for letter in exclude_letters)]
    return solutions

letters = input("Enter the known letters: ")
exclude_letters = input("Enter any letters to exclude: ")
solutions = wordle_solver(letters, exclude_letters)
print(f"Possible solutions: {solutions}")