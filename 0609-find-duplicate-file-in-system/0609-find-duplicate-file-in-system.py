class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for path in paths:
            path = path.split()
            directory = path[0]
            
            for val in path[1:]:
                val = val.split(".txt")
                file_name = val[0]
                content = val[1]
                d[content].append( directory + "/" + file_name + ".txt")
        
        output = []
        for key,val in d.items():
            if len(val) > 1:
                output.append(d[key])
        
        return output
                
            
                
                
                
                
                
            
        