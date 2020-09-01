#gauss-Jordan problem
#read matrices
try:
    fhand=open("A")
    ghand=open("B")
except:
    print("File not found")
else:
    M=[]
    N=[]
    A=[[0,0,0],[0,0,0],[0,0,0]]
    B=[[0],[0],[0]]
#A=1,3,2            B=2
#  2,7,7             -1
#  2,5,2              7
    for line in fhand:
        line=line.rstrip()
        li=list(line.split(","))
        c=len(li)
        M.append(li)
    for k in ghand:
        k=k.rstrip()
        lis=list(k.split(","))
        d=len(lis)
        N.append(lis)
    r=len(M)

    for i in range(r):
        B[i][0]=int(N[i][0])
        for j in range(r):
            A[i][j]=int(M[i][j])

    def partial_pivot(a,b):
        r=len(a)
        for i in range(r):
            if a[i][i]==0:
                for k in {0,1,2}:
                    if k==i or a[i][i]!=0:
                        continue
                    else:
                        if abs(a[k][i])>abs(a[i][i]):
                            c=b[i][0]
                            b[i][0]=b[k][0]
                            b[k][0]=c
                            for j in range(r):
                                pivot=a[i][j]
                                a[i][j]=a[k][j]
                                a[k][j]=pivot
        return a,b

#Gauss Jordan method
    def Gauss_Jordan(a,b):
        """Gauss Jordan method of decomposition"""
        for q in range(r):
            pivot=a[q][q]
            b[q][0]=b[q][0]/pivot
            for l in range(q,r):
                a[q][l]= a[q][l]/pivot

            for w in range(r):
                if a[w][q]==0 or q==w:
                    continue
                else:
                    factor=a[w][q]
                    b[w][0]=b[w][0]-factor*b[q][0]
                    for c in range(q,r):
                        a[w][c]=a[w][c]-factor*a[q][c]

        return a,b

    def main(A,B):
        X,Y=partial_pivot(A,B)
        A,B=Gauss_Jordan(X,Y)
        print("row echleon form:")
        for q in A:
            print(q)
        print("solution for the equation is:")
        print("x=",B[0][0])
        print("y=",B[1][0])
        print("z=",B[2][0])
    main(A,B)
#Output:row echleon form:
#        [1.0,0.0,0.0]
#        [0.0,1.0,0.0]
#        [0.0,0.0,1.0]
#       solution for the equation is:
#        x=3.0
#        y=1.0
#        z=-2.0
