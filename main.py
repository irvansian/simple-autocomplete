from trie import Trie
from autocomplete import AutoCompleter
from util import printSuggestions

if __name__ == "__main__":
    autoTrie = Trie()

    with open("dict.txt", "r") as f:
        for line in f:
            autoTrie.add(line.strip())
    
    numSuggegstions = int(input("Suggestions: "))
    
    while True:
        inputWord = input("Enter word: ")
        
        if inputWord == '/exit':
            break

        suggestions = AutoCompleter.suggestWords(autoTrie, inputWord, numSuggegstions)
        printSuggestions(suggestions)