
class Naive:
    @classmethod
    def find(cls, text: str, pattern: str) -> bool:
        """
        Find the pattern in the text using the naive algorithm.
        
        params:
            - text: The text to search in.
            - pattern: The pattern to search for.
        
        return: 
            The index of the pattern in the text, or -1 if not found.
        """
        p = len(pattern)
        t = len(text)

        for i in range(t - p):
            j = 0
            while j < p and text[i + j] == pattern[j]:
                j += 1
            
            if j == p:
                return i
        
        return - 1
    

n = Naive()

print(n.find("hello", "ll") == 2)