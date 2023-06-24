import requests


def wordle_solver():
    exclude_letters = ""
    while True:
        print(
            "Enter 'q' to quit, 'h' for help, or the known letters of the secret word:"
        )
        letters = input("> ")
        if letters == "q":
            break
        elif letters == "h":
            print("Help:")
            print(
                "- Enter the known letters of the secret word, replacing any unknown letters with a '*'."
            )
            print(
                f"- To exclude certain letters from the search, enter them after the prompt (current excluded letters: {exclude_letters})."
            )
            print("- Enter 'q' to quit the program.")
        else:
            exclude_letters = input("Enter any letters to exclude: ")
            solutions = get_solutions(letters, exclude_letters)
            print(f"Possible solutions: {solutions}")


def get_solutions(letters, exclude_letters="", word_length=5):
    url = f"https://api.datamuse.com/words?sp={letters}*&max=1000"
    response = requests.get(url)
    words = response.json()
    solutions = [
        word["word"]
        for word in words
        if len(word["word"]) == word_length
        and all(letter not in word["word"] for letter in exclude_letters)
    ]
    return solutions


wordle_solver()
