class Solution:
    def countOfAtoms(self, formula: str) -> str:
        d = Counter()
        stack = [d]
        i = 0
        while i < len(formula):
            if formula[i] == "(":
                d = Counter()
                stack.append(d)
                i += 1
            elif formula[i] == ")":
                atoms = stack.pop()
                i += 1
                start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                multiply = int(formula[start:i] or 1)
                for atom, val in atoms.items():
                    stack[-1][atom] += val * multiply
                d = stack[-1]
            else:
                start = i
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1
                atom = formula[start:i]

                start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                multiply = int(formula[start:i] or 1)
                stack[-1][atom] += multiply
        return "".join(atom + (str(d[atom]) if d[atom] > 1 else "") for atom in sorted(d))


                        
                 


        
        