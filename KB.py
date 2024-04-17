import itertools
class KnowledgeBase:
    def __init__(self):
        self.clauses=[]

    def addClause(self, clause):
        if clause not in self.clauses and not self.isContainComplementaryPair(clause):
            self.clauses.append(clause)

    def setNegativeAtom(self,atom):
        if atom[0]=='-':
            return atom[1:]
        else:
            return '-'+atom
    def setNegativeStatement(self, statement):
        negated_statement = []

        # Duyệt qua từng mệnh đề con trong statement
        for clause in statement:
            negated_clause = []

            # Đảo ngược dấu của mỗi nguyên tử trong mệnh đề con
            for atom in clause:
                negated_atom = self.setNegativeAtom(atom)
                negated_clause.append(negated_atom)

            negated_statement.append(negated_clause)

        return list(itertools.chain.from_iterable(negated_statement))
    # def isContainSubClause(self,clause,list_clauses):
    #     for c in list_clauses:
    #         if set(c).issubset(set(clause)):
    #             return True
    #     return False
    
    # def removeSubClause(self,list_clauses):
    #     result=[]
    #     for c in list_clauses:
    #         if not self.isContainSubClause(c,result):
    #             result.append(c)
    #     return result
    def removeSubClauses(self, list_clauses):
        result = []
    
        for clause in list_clauses:
            is_subclause = False
        
            for current_clause in result:
                if set(clause).issubset(set(current_clause)):
                    is_subclause = True
                    break
                
            if not is_subclause:
                result.append(clause)

        return result
    
    def isContainComplementaryPair(self, clause):
        for atom in clause:
            if self.setNegativeAtom(atom) in clause:
                return True
        return False
    
    def normalizeClause(self, clause):
        
        clause=list(dict.fromkeys(clause))

        ordered_atoms=[]

        for atom in clause:
            if atom[0] == '-':
                ordered_atoms.append((atom[1], -1))
            else:
                ordered_atoms.append((atom[0], 1))

        ordered_atoms.sort()
        
        normalized_clause = []
        for item in ordered_atoms:
                if item[1] == -1:
                    normalized_clause.append('-' + item[0])
                else:
                    normalized_clause.append(item[0])
            
        return normalized_clause
    
    def resolve(self, clause_i, clause_j):
        print('clause i,j')
        print(clause_i)
        print(clause_j)
        new_clause = []
        for atom in clause_i:
            neg_atom = self.setNegativeAtom(atom)
            if neg_atom in clause_j:
                if isinstance(clause_i, str):
                    clause_i = [clause_i]
                if isinstance(clause_j, str):
                    clause_j = [clause_j]
                temp_c_i = clause_i.copy()
                temp_c_j = clause_j.copy()
                print('temp')
                print(temp_c_i)
                print(temp_c_j)
                temp_c_i.remove(atom)
                temp_c_j.remove(neg_atom)
                if not temp_c_i and not temp_c_j:
                    new_clause.append(['{}'])
                else:
                    clause = temp_c_i + temp_c_j
                    clause = self.normalizeClause(clause)
                    print('clause after normalize ',clause)
                    if not self.isContainComplementaryPair(clause) and clause not in self.clauses:
                        new_clause.append(clause)
            print('current new clause: ',new_clause)

        return new_clause
    
    def PL_Resolution(self, stament):
        tempKB = KnowledgeBase()
        tempKB.clauses = self.clauses.copy()

        neg_query = self.setNegativeStatement(stament)
        print(neg_query)
        for neg_atom in neg_query:
            tempKB.addClause(neg_atom)
        
        print(tempKB.clauses)
        result = []
        while True:
            clause_pairs = list(itertools.combinations(range(len(tempKB.clauses)), 2))
            resolvents = []
            for pair in clause_pairs:
                resolvent = tempKB.resolve(tempKB.clauses[pair[0]], tempKB.clauses[pair[1]])
                print('resolvent',resolvent)
                if resolvent and resolvent not in resolvents:
                    resolvents.append(resolvent)

            resolvents = list(itertools.chain.from_iterable(resolvents))
            result.append(resolvents)

            if not resolvents:
                return result, False
            else:
                if ['{}'] in resolvents:
                    return result, True
                else:
                    for res in resolvents:
                        tempKB.addClause(res)