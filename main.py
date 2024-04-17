import os
import KB

def read_data_from_file(file_name):
    script_dir=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(script_dir,file_name)
    f= open(file_path, 'r')
    
    data=f.read().splitlines()
    
    alpha=data[0:1]

    statement=[]
   
    for cnf in alpha:
        st_clause=cnf.split()
        st_clause=list(filter(lambda x:x!='OR',st_clause))
        statement.append(st_clause) 

    num_clauses = int(data[1])
    
    list_clauses=data[2:]
    
    kb=KB.KnowledgeBase()

    for cnf in list_clauses:
        clause= cnf.split()
        clause=list(filter(lambda x:x!='OR',clause))
        kb.addClause(clause)

    f.close()
    
    return kb,statement

kb,alpha = read_data_from_file("input.txt")

print(kb.clauses)
result,check=kb.PL_Resolution(alpha)
print(result)
print(check)

for loop_res in result:
            print(len(loop_res))
            for clause in loop_res:
                string = ''
                for c in clause:
                    string += c
                    if c != clause[-1]:
                        string += ' OR '
                print(string)
                
if check:
           print('YES')
else:
            print('NO')
