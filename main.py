import os
import KB

def read_data_from_file(file_name):
    script_dir=os.path.dirname(os.path.abspath(__file__))
    cwd=os.getcwd()
    file_path=os.path.join(script_dir,file_name)
    f= open(file_path, 'r')
    
    data=[]

    data=f.read().splitlines()
    

    statement=data[0]

    alpha_statement=[]
   
    st_clause=statement.split()
    st_clause=list(filter(lambda x:x!='OR',st_clause))
    alpha_statement.append(st_clause) 

    num_clauses = int(data[1])
    
    list_clauses=data[2:]
    
    kb=KB.KnowledgeBase()

    for cnf in list_clauses:
        clause= cnf.split()
        clause=list(filter(lambda x:x!='OR',clause))
        kb.addClause(clause)
    f.close()
    
    return kb,alpha_statement

print(os.getcwd())
# Example usage:
kb,alpha = read_data_from_file("input.txt")
# print("Statement:", statement)
# print("CNF Clauses:", cnf_clauses)
print(kb.clauses)
result,check=kb.PL_Resolution(alpha)
print(result)
print(check)
