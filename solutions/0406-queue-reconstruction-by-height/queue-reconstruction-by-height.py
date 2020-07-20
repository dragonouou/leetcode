# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
#
# Note:
# The number of people is less than 1,100.
#  
#
# Example
#
#
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#
#
#  
#


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_list = sorted(people, key = lambda person: (person[0], person[1]))                   
        init_list = [None for _ in range(len(people))]
        
        for each_person in sorted_list:
                             
            count = 0
            index = 0
                             
            while count != each_person[1]:
                if init_list[index] is None or init_list[index][0] >= each_person[0]:
                    count += 1
                index += 1
                             
            while init_list[index] is not None :
                index += 1
                             
            init_list[index] = each_person
            
        return init_list
