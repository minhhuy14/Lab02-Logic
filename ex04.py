import os
def read_data_from_file(file_name):
    script_dir=os.path.dirname(os.path.abspath(__file__))
    cwd=os.getcwd()
    file_path=os.path.join(script_dir,file_name)
    f= open(file_path, 'r')
        # Read the statement
    statement = f.readline().strip()
        
        # Read the number of clauses
    num_clauses = int(f.readline().strip())
        
        # Read the clauses
    clauses = []
    for _ in range(num_clauses):
            # Split the line into literals and remove extra spaces
            clause = f.readline().strip().split()
            # Filter out empty strings in case of multiple spaces
            clause = [literal for literal in clause if literal]
            clauses.append(clause)
    f.close()
    cnf_data={
          'statement':statement,
          'clauses':clauses
    }
    return cnf_data
print(os.getcwd())
# Example usage:
data = read_data_from_file("input.txt")
# print("Statement:", statement)
# print("CNF Clauses:", cnf_clauses)
print(data['statement'])
