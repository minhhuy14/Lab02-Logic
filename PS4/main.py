import os
import KB

def readDataFromFile(filename):
    script_dir=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(script_dir,filename)
    f= open(file_path, 'r')

    data=f.read().splitlines()

    statement=[cnf.split() for cnf in data[0:1]]
    alpha=[]
   
    for cnf in statement:
        list_atoms=[]
        for atom in cnf:
            if atom!='OR':
                list_atoms.append(atom)
        alpha.append(list_atoms)

    num_clauses = int(data[1])

    list_clauses=[cnf.split() for cnf in data[2:]]
    
    #Initialize kb object to save knowledge base clause
    kb=KB.KnowledgeBase()

    for cnf in list_clauses:
        clause=[]
        for atom in cnf:
            if atom!='OR':
                clause.append(atom)
        kb.addClause(clause)

    f.close()
    
    return kb,alpha

def writeResultToFile(result, success, filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    f= open(filename, 'w')
    for res in result:
        f.write(str(len(res)) + '\n')
        for clause in res:
            clause_str = ''
            for atom in clause:
                clause_str += atom
                if atom != clause[-1]:
                    clause_str += ' OR '
            f.writelines(clause_str + '\n')
    if success:
        f.writelines('YES')
    else: 
        f.writelines('NO')
        
    print('Save results into output.txt successfully!')
                
if __name__ == '__main__':      

    kb,alpha = readDataFromFile("input.txt")
    print('KB Clauses: ',kb.clauses)
    print('alpha statement: ',alpha)
    result,success=kb.PL_Resolution(alpha)
    print('Result: ',result)
    print('Success: ',success)

    writeResultToFile(result,success,"output.txt")


