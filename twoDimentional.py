import numpy as np
twoDArray=np.array([[1,2,3],[3,5,6],[9,6,8],[9,8,8]])
print(twoDArray)
newtwoDArray=np.insert(twoDArray,1,[[3,4,5]],axis=0)
print(newtwoDArray)
def tranvese(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
def search(array,val):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if(array[i][j]==val):
                print(i,j)
search(twoDArray,5)
newdelarray=np.delete(twoDArray,0,axis=1)
print(newdelarray)