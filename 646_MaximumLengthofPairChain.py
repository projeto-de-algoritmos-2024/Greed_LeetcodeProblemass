from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1]) #Ordena pelo fim
        y_atual = float('-inf')    
        count = 0                      #Contador para a cadeia mais longa

        for par in pairs:
            #Se a corrente pode ser formada
            if par[0] > y_atual:
                count += 1
                y_atual = par[1]

        return count