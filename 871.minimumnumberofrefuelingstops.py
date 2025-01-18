import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])

        fuel = startFuel
        car_position = 0
        stops_num = 0
        heap = [] 
        for position, fuel_now in stations:
            distance = position - car_position

            while fuel < distance:
                if len(heap) == 0:  
                    return -1
                fuel += -heapq.heappop(heap)
                stops_num += 1 
            fuel -= distance
            heapq.heappush(heap, -fuel_now)
            car_position = position

        return stops_num
