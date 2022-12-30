class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cpDict = {}
        for string in cpdomains:
            rep, domain = string.split()
            rep = int(rep)
            
            subDomain = domain.split(".")
            for i in range(len(subDomain)):
                
                cpDict['.'.join(subDomain[i:])] = rep + cpDict.get('.'.join(subDomain[i:]),0) 
            
        res = [f"{count} {dom}" for dom,count in cpDict.items()]
        return res
                
            
                
                
            

                
            
        