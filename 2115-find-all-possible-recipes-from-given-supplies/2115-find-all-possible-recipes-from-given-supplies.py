class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        incomming = defaultdict(int)
        graph = defaultdict(list)
        n = len(recipes)
        order = []
        
        for i in range(n):
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
            
        
        for i in range(n):
            incomming[recipes[i]] = len(ingredients[i])
        
        
        queue = deque()
        for ing in supplies:
            queue.append(ing)
        
        
        while queue:
            ingredient = queue.popleft()
            for child in graph[ingredient]:
                if incomming[child] != 0:
                    incomming[child] -= 1
                    if incomming[child] == 0:
                        order.append(child)
                        queue.append(child)
                    
        return order
        
