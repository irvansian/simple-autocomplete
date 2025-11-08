class AutoCompleter:
    def __init__(self):
        pass
    
    @staticmethod
    def suggestWords(trie, prefix, numSuggestions):
        result = []
        root = trie.prefixNode(prefix)

        def dfs(node, curWord):
            if not node:
                return
            if node.isWord:
                result.append(prefix + curWord)
            if len(result) == numSuggestions:
                return True
            if len(node.children) == 0:
                return False
        
            for key in node.children.keys():
                if dfs(node.children[key], curWord + key):
                    return True
        dfs(root, "")

        return result

    
    



