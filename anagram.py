from collections import Counter
def anagrams(word, words):
    #your code here
    answer = []
    for i in words:
        
        if Counter(word) == Counter(i) :
            answer.append(i)
    print(answer)

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
