class Solution(object):
    def sortSentence(self, s):
        words = s.split(" ")
        words_list = []
        for i in range(len(words)):
            min = i
            for j in range(i+1, len(words)):
                if (words[j][-1] < words[min][-1]):
                    min = j
            words[i], words[min] = words[min], words[i]
            words_list.append(words[i][:-1])
        return " ".join(words_list)
       
      
