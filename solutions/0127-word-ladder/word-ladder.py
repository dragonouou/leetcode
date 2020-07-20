# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
#
# 	Only one letter can be changed at a time.
# 	Each transformed word must exist in the word list.
#
#
# Note:
#
#
# 	Return 0 if there is no such transformation sequence.
# 	All words have the same length.
# 	All words contain only lowercase alphabetic characters.
# 	You may assume no duplicates in the word list.
# 	You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
#
#
#
#
#


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #BFS一层一层进行辐射传递下去，用到queue先进先出的数据结构
        # set没有顺序，可以用于查重
        word_dict = set(wordList)
        if endWord not in word_dict:
            return 0  
        
        l = len(beginWord)
        depth_dict1 = {}
        depth_dict2 = {}
        change_dict = {}
#         #需要记录每个单词对应的depth，如果在某一层有多个单词，对第一个单词进行下一层探索，
#         #然后回到第二个单词，此时的depth已经加了1层，所以需要用dict来回到之前的一层
        depth_dict1[beginWord] = 1
        depth_dict2[endWord] = 1
        
        
##双向扩展       
        q1 = deque([beginWord])
        q2 = deque([endWord])

        
        while(len(q1) > 0 and len(q2) > 0):           
            if len(q1) > len(q2):
                q = q2
                case = 2
            else:
                q = q1
                case = 1
            word = q.popleft()
            depth = depth_dict1[word] if case == 1 else depth_dict2[word]
            
            
            for i in range(l):
                if word in change_dict and i == change_dict[word]:
                    continue
                char = word[i]
                for letter in string.ascii_lowercase:
                    if letter == char:
                        continue
                    new_word = word[:i] + letter + word[i+1:]
                    if case == 1 and new_word in q2:
                        return depth + depth_dict2[new_word]
                    if case == 2 and new_word in q1:
                        return depth + depth_dict1[new_word]
                    if new_word not in word_dict:
                        continue
                    word_dict.remove(new_word)
                    change_dict[new_word] = i
                    if case == 1:
                        q1.append(new_word)
                        depth_dict1[new_word] = depth + 1
                    else:
                        q2.append(new_word)
                        depth_dict2[new_word] = depth + 1
        
        return 0
            
                    
                
        
# ## 单向扩展
#         #deque可以将list实现queue，先进先去，从开端进行pop
#         q = deque([beginWord])

     
#         while len(q) > 0:
#             word = q.popleft()
#             depth = depth_dict[word]
                  
#             #替换每一个字符，将之与wordlist进行比对，如果在里面，加入queue；
#             #如果替换的单词是要找的单词，搜索结束；如果不是，以此为新的一层继续向下
#             for i in range(l):
#                 #如果词是由上个词变化i位变化来的，那么就不需要再对这一位做变化，会变回去
#                 if word in change_dict and i == change_dict[word]:
#                     continue
#                 char = word[i]
#                 for letter in string.ascii_lowercase:
#                     if char == letter: 
#                         continue
#                     new_word = word[:i] + letter + word[i+1:]
#                     if new_word == endWord: 
#                         return depth + 1
#                     if new_word not in word_dict: 
#                         continue   
#                     #将新词去掉，保证下一次改变字符loop的时候不会回到本身
#                     word_dict.remove(new_word)
#                     change_dict[new_word] = i
#                     q.append(new_word)
#                     depth_dict[new_word] = depth + 1
            
#         #每层探索完毕，没有找到，返回0
#         return 0
            

        
