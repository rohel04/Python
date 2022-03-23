import numpy as np
grid=np.array(['','','','','','','','',''])


player1=[]
player2=[]

winningConditions=[
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6],
]

turn="p1"
for i in range(8):
    if turn=='p1':
        move=input(f"{turn} Enter position: ")
        player1.append(int(move))
        
        print(grid.reshape(3,3))
       
        turn='p2'
    if turn=='p2':
        move=input(f"{turn} Enter position: ")
        player2.append(int(move))
        np.insert(grid,int(move),'O')
        turn='p1'
        print(grid.reshape(3,3))
        

