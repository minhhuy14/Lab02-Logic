import os
def read_data_from_file(file_name):
    script_dir=os.path.dirname(os.path.abspath(__file__))
    cwd=os.getcwd()
    file_path=os.path.join(script_dir,file_name)
    f= open(file_path, 'r')
        # Read the statement
    data=[]

    data=f.read().splitlines()

    print(data)
    statement=data[0]
    print('statement',statement)
    alpha_statement=[]
   
    st_clause=statement.split()
    st_clause=list(filter(lambda x:x!='OR',st_clause))
    alpha_statement.append(st_clause)
          
    statement_clause=list(filter(lambda x: x!= 'OR',statement))

    print(statement_clause)

    num_clauses = int(data[1])
    
    list_clauses=data[2:]
    print('list',list_clauses)
        # Read the clauses
    kb_clauses = []
    for cnf in list_clauses:
        clause= cnf.split()
        clause=list(filter(lambda x:x!='OR',clause))
        kb_clauses.append(clause)
    f.close()
    
    cnf_data={
          'alpha_statement':alpha_statement,
          'kb_clauses':kb_clauses
    }
    return cnf_data

print(os.getcwd())
# Example usage:
data = read_data_from_file("input.txt")
# print("Statement:", statement)
# print("CNF Clauses:", cnf_clauses)
print(data)
