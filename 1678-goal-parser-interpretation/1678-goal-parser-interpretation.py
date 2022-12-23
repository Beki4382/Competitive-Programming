class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        word = ""
        goalDic = {"G":"G", "()":"o", "(al)":"al"}
        i = 0
        
        while i< len(command):
            
            if command[i] == "(" and command[i+1] == ")":
                res+= goalDic["()"]
                i+=2
                
            elif command[i] == "(" and command[i+1] != ")":
                res+=goalDic["(al)"]
                i+=4
                
            else:
                res+=command[i]
                i+=1
                
        return res
                
            
        
        