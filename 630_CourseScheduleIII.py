import heapq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1]) #Ordena pelo fim (ultimo dia)
        
        tempo = 0
        max_heap = []
        
        for duracao, fim in courses:
            heapq.heappush(max_heap, -duracao) 
            tempo += duracao
            
            #Se o tempo estourar o prazo, desenfileira o curso mais longo
            if tempo > fim:
                tempo += heapq.heappop(max_heap)
        
        return len(max_heap)