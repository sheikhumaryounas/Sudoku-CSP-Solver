import copy

def read_board(file):
    board=[]
    with open(file,'r') as f:
        for line in f:
            board.append([int(x) for x in line.strip()])
    return board

def get_neighbors():
    neighbors={}
    for r in range(9):
        for c in range(9):
            n=set()
            for i in range(9):
                n.add((r,i))
                n.add((i,c))
            br=(r//3)*3
            bc=(c//3)*3
            for i in range(br,br+3):
                for j in range(bc,bc+3):
                    n.add((i,j))
            n.remove((r,c))
            neighbors[(r,c)]=n
    return neighbors

def init_domains(board):
    domains={}
    for r in range(9):
        for c in range(9):
            if board[r][c]==0:
                domains[(r,c)]=set(range(1,10))
            else:
                domains[(r,c)]={board[r][c]}
    return domains

def revise(domains,x,y):
    revised=False
    for val in set(domains[x]):
        if all(val==v for v in domains[y]):
            domains[x].remove(val)
            revised=True
    return revised

def ac3(domains,neighbors):
    queue=[(x,y) for x in domains for y in neighbors[x]]
    while queue:
        x,y=queue.pop(0)
        if revise(domains,x,y):
            if len(domains[x])==0:
                return False
            for z in neighbors[x]:
                if z!=y:
                    queue.append((z,x))
    return True

def is_complete(domains):
    return all(len(domains[v])==1 for v in domains)

def select_unassigned(domains):
    return min([v for v in domains if len(domains[v])>1], key=lambda x: len(domains[x]))

def forward_check(domains,var,value,neighbors):
    new_domains=copy.deepcopy(domains)
    new_domains[var]={value}
    for n in neighbors[var]:
        if value in new_domains[n]:
            new_domains[n].remove(value)
            if len(new_domains[n])==0:
                return None
    return new_domains

calls=0
fails=0

def backtrack(domains,neighbors):
    global calls,fails
    calls+=1

    if is_complete(domains):
        return domains

    var=select_unassigned(domains)

    for value in domains[var]:
        new_domains=forward_check(domains,var,value,neighbors)
        if new_domains:
            if ac3(new_domains,neighbors):
                result=backtrack(new_domains,neighbors)
                if result:
                    return result

    fails+=1
    return None

def solve(file):
    global calls,fails
    calls=0
    fails=0

    board=read_board(file)
    neighbors=get_neighbors()
    domains=init_domains(board)

    ac3(domains,neighbors)
    result=backtrack(domains,neighbors)

    solution=[[0]*9 for _ in range(9)]
    for (r,c) in result:
        solution[r][c]=list(result[(r,c)])[0]

    return solution,calls,fails

def print_board(board):
    for row in board:
        print(" ".join(map(str,row)))

# RUN ALL FILES
files=["easy.txt","medium.txt","hard.txt","veryhard.txt"]

for f in files:
    print("\nSolving:",f)
    sol,calls,fails=solve(f)
    print_board(sol)
    print("Backtrack Calls:",calls)
    print("Failures:",fails)