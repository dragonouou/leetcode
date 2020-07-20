# There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
#
# Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
#
#
# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
#
#
# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
#
#
#  
# Constraints:
#
#
# 	The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
# 	The size of flights will be in range [0, n * (n - 1) / 2].
# 	The format of each flight will be (src, dst, price).
# 	The price of each flight will be in the range [1, 10000].
# 	k is in the range of [0, n - 1].
# 	There will not be any duplicated flights or self cycles.
#
#


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # 0:[(1,100),(2,200)]  start:[(end1, price1),(end2, price2)]
        connect_dict = {}     

        for e in flights:
            if e[0] not in connect_dict:
                connect_dict[e[0]] = [(e[1],e[2])]
            else:
                connect_dict[e[0]].append((e[1],e[2]))
        
        # (start, price)
        q = deque([(src, 0)])
        ans = math.inf
        stop = -1
        
        while len(q) > 0:
            
            for _ in range(len(q)):
                curr = q.popleft()
                place = curr[0]
                cost = curr[1]

                if (place == dst):
                    ans = min(ans, cost)
                if place in connect_dict:
                    for pair in connect_dict[place]:
                        if (cost + pair[1] > ans):
                            continue
                        q.append((pair[0], cost + pair[1]))

            stop += 1
            if stop > K:
                break
        
        return ans if ans != math.inf else -1
            
                
                    
                
        
        
#         # (start, stop, price)
#         q1 = deque([(src, 0, 0)])
#         q2 = deque([(dst, 0, 0)])
#         price_list = []

        
#         while len(q1) > 0 and len(q2) > 0:
#             if len(q1) <= len(q2):
#                 q = q1
#                 case = 1
#             else:
#                 q = q2
#                 case = 2
            
#             #node: (place, stop, price)
#             node = q.popleft()
#             place = node[0]
#             stop = node[1]
#             price = node[2]
            
#             if place in connect_dict:
#                 #value: (end, price)
#                 for value in connect_dict[place]:
#                     p = value[0]             
#                     if case == 1:
#                         result = self.checkFindResult(p, q2)
#                         if result:        
#                             for element in result:
#                                 if element[0] + stop <= K:
#                                     price_list.append(value[1] + price + element[1])
#                         else:
#                             new_node = (p, stop + 1, value[1] + price)
#                             q1.append(new_node)
                            
#                     else:
#                         result = self.checkFindResult(p, q1)
#                         if result:        
#                             for element in result:
#                                 if element[0] + stop <= K:
#                                     price_list.append(value[1] + price + element[1])
#                         else:
#                             new_node = (p, stop + 1, value[1] + price)
#                             q2.append(new_node)
                        

#         if len(price_list) > 0:
#             return min(price_list)
#         else:
#             return -1
        
#     def checkFindResult(self, place, queue):
#         result = []
#         for e in queue:
#             if place == e[0]:
#                 price = e[2]
#                 stop = e[1]
#                 result.append((stop, price))
                
#         if len(result) > 0:
#             return result
#         else:
#             return False
                
            
        
        
