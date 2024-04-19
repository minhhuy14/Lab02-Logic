import itertools
class KnowledgeBase:
    def __init__(self):
        self.clauses=[]

    def addClause(self, clause):
        if clause not in self.clauses and not self.isContainComplementaryPair(clause):
            self.clauses.append(clause)
    def isEmptyClause(self,clause):
        return len(clause)==0
    def setNegativeAtom(self,atom):
        if atom[0]=='-':
            return atom[1:]
        else:
            return '-'+atom
        
    def setNegativeStatement(self, statement):
        negated_statement = []
        for clause in statement:
            negated_clause = []
            for atom in clause:
                negated_atom = self.setNegativeAtom(atom)
                negated_clause.append(negated_atom)

            negated_statement.append(negated_clause)

        return negated_statement
    
    #Check if exists complementary pair in clause
    def isContainComplementaryPair(self, clause):
        for atom in clause:
            if self.setNegativeAtom(atom) in clause:
                return True
        return False
    
    def normalizeClause(self, clause):
        clause=list(dict.fromkeys(clause))
        ordered_atoms=[]

        #Sort atom by alphabetical ordering
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
        # print('clause i,j')
        # print(clause_i)
        # print(clause_j)
        new_clause = []
        for atom in clause_i:
            neg_atom = self.setNegativeAtom(atom)
            if neg_atom in clause_j:
                if isinstance(clause_i, str):
                    clause_i = [clause_i]
                if isinstance(clause_j, str):
                    clause_j = [clause_j]
                    
                new_clause_i = clause_i.copy()
                new_clause_j = clause_j.copy()

                new_clause_i.remove(atom)
                new_clause_j.remove(neg_atom)
                if not new_clause_i and not new_clause_j:
                    new_clause.append(['{}'])
                else:
                    clause = new_clause_i + new_clause_j
                    clause = self.normalizeClause(clause)
                    if not self.isContainComplementaryPair(clause) and clause not in self.clauses:
                        new_clause.append(clause)
            # print('current new clause: ',new_clause)

        return new_clause
    
    def PL_Resolution(self, stament):
        newKB = KnowledgeBase()
        newKB.clauses = self.clauses.copy()

        neg_stament = self.setNegativeStatement(stament)
        
        for neg_atom in neg_stament:
            newKB.addClause(neg_atom)
        
        result = []
        while True:
            clause_pairs = list(itertools.combinations(range(len(newKB.clauses)), 2))
            resolvents = []
            for pair in clause_pairs:
                resolvent = newKB.resolve(newKB.clauses[pair[0]], newKB.clauses[pair[1]])
                
                if ['{}'] in resolvent:
                    resolvents.append(resolvent)
                    resolvents = list(itertools.chain.from_iterable(resolvents))
                    result.append(resolvents)
                    return result,True
                
                if resolvent and resolvent  not in newKB.clauses and resolvent not in resolvents:
                    resolvents.append(resolvent)
                
    
       
            resolvents = list(itertools.chain.from_iterable(resolvents))
            result.append(resolvents)
            if resolvents==[] or resolvents is None:
                return result,False

            for res in resolvents:
                newKB.addClause(res)