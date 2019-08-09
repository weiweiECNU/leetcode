# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    
    alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        trans = self.transformation(words)
        samples = []
        for code in trans:
            if code not in samples:
                samples.append(code)
        return len(samples)
        
    def transformation( self, words ):
        trans = []
        for i, word in enumerate(words):
            string = ""
            for j, letter in enumerate(word):
                string += (self.alphabet[ord(letter) - ord("a")])
            trans.append(string)
        
        return trans

        

    
        