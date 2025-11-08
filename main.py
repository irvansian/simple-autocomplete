from trie import Trie
from autocomplete import AutoCompleter
from util import printSuggestions

if __name__ == "__main__":
    autoTrie = Trie()

    with open("dict.txt", "r") as f:
        for line in f:
            autoTrie.add(line.strip())

    print("\033[34mA simple in-memory autocompleter. Type /exit to exit the terminal." +
        "\nFirst put in the number of suggestions you want.\033[0m")

    numInput = input("> ")
    numSuggestions = 3

    if numInput == "/exit":
        exit()
    elif numInput.isdigit():
        numSuggestions = int(numInput)
    else:
        print("\033[34mYou didn\'t type a number. Num of suggestions is 3 (default).\n\033[0m")

    print("\033[34mWrite the word you want to autocomplete on.\033[0m")

    while True:
        inputWord = input("> ")
        
        if inputWord == '/exit':
            break

        suggestions = AutoCompleter.suggestWords(autoTrie, inputWord, numSuggestions)
        printSuggestions(suggestions)