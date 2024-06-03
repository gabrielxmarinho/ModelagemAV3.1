from ortools.linear_solver import pywraplp
filename = "adjMatrix.txt"
f=open(filename,'r')
conteudo=f.read().split("\n")
n = int(conteudo[0])
MA = []
for i in range(1,len(conteudo)-1):
    linha = conteudo[i].split(" ")
    #convertendo para valores inteiros
    MA.append(linha)
        
pesos = conteudo[len(conteudo)-1].split(" ")

solver = pywraplp.Solver.CreateSolver("SAT")

X=[]

for i in range(0,n):
    X.append(solver.IntVar(0,1,f"X[{i}]"))

for i in range(0,n):
    for j in range(i+1,n):
        ct = solver.Constraint(0,1,"ct")
        ct.SetCoefficient(X[i],int(MA[i][j]))
        ct.SetCoefficient(X[j],int(MA[i][j]))
objective = solver.Objective()
for i in range(0,n):
    objective.SetCoefficient(X[i],float(pesos[i]))
objective.SetMaximization()
#Resolvendo
solver.Solve()
print("Saída:")
print("Solução = ", objective.Value())
Vertices = []
for i in range(0,n):
    if X[i].solution_value()==1:
        Vertices.append(f"X[{i}]")
print(f"Conjunto de Variáveis: {Vertices}")