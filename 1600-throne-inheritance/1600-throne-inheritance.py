class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.throneInheritance = [self.kingName]
        self.kingdom = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.kingdom[parentName].append(childName)
        self.kingdom[childName].append(parentName)

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        visited = set()
        ans = []
        def dfs(successor):
            if successor not in self.dead:
                ans.append(successor)

            visited.add(successor)  # Move this line here to mark the current node as visited

            for child in self.kingdom[successor]:
                if child not in visited:  # Check for child's presence in the visited set
                    dfs(child)
            
            return ans

        return dfs(self.kingName)

            
            
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()