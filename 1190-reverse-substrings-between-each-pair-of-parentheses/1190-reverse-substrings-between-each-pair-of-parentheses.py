class Solution(object):
    def reverseParentheses(self, s):
        str_list = list(s)
        opening_index = []
        str_len = len(s)

        j = 0
        for i in range(str_len):
            if str_list[j] == '(':
                opening_index.append(j)
                j += 1
            elif str_list[j] == ')':
                last_opng_bracket = opening_index.pop()
                str_list[last_opng_bracket+ 1:j] = self.reverseSublist(str_list[last_opng_bracket+ 1:j])

                str_list.pop(j)
                str_list.pop(last_opng_bracket)
                j -= 1
            else:
                j += 1
        

        result = "".join(str_list)
        return result
    def reverseSublist(self, subarr):
        reversed = subarr
        reversed.reverse()
        return reversed


            
            
        
       
        