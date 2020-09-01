try:
      fhand=open("C")
      ghand=open("D")
except:
  print("File not found")
else:
    M=[]
    N=[]
    A=[[0,0,0],[0,0,0],[0,0,0]]
    D=[[0,0,0],[0,0,0],[0,0,0]]
    B=[[0,0,0],[0,0,0],[0,0,0]]
    #A=0,2,5           B=1
    #  3,-1,2           -2
    #  1,-1,3            3

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
      for j in range(r):
          B[i][j]=int(N[i][j])
          A[i][j]=int(M[i][j])



    def partial_pivot(a,b,col):
        """This function does partial pivoting of passed matrices"""
        r=len(a)
        for i in range(r):
            if a[i][i]==0:
                for k in {0,1,2}:
                    if k==i or a[i][i]!=0:
                        continue
                    else:
                        if abs(a[k][i])>abs(a[i][i]):
                            c=b[i][col]
                            b[i][col]=b[k][col]
                            b[k][col]=c
                            for j in range(r):
                                pivot=a[i][j]
                                a[i][j]=a[k][j]
                                a[k][j]=pivot
        return a,b


    def Gauss_Jordan(a,b,col):
        """Gauss Jordan method of decomposition"""
        for q in range(r):
            pivot=a[q][q]
            for l in range(q,r):
                a[q][l]= a[q][l]/pivot
                b[q][col]=b[q][col]/pivot
            for w in range(r):
                if a[w][q]==0 or q==w:
                    continue
                else:
                    factor=a[w][q]
                    b[w][col]=b[w][col]-factor*b[q][col]
                    for c in range(q,r):
                        a[w][c]=a[w][c]-factor*a[q][c]

        return a,b

    def mult(M,N):
        E=[[0,0,0],[0,0,0],[0,0,0]]
        I=[[1,0,0],[0,1,0],[0,0,1]]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    E[i][j]+=M[i][k]*N[k][j]
        if E==I:
            print("result is identity matrix")
        for r in E:
            print(r)


    for i in range(r):
        for j in range(r):
          for k in range(r):
              D[j][k]=int(M[j][k])
        X,Y=partial_pivot(D,B,i)
        I,Ainv=Gauss_Jordan(X,Y,i)

    print("A matrix=")
    for q in A:
        print(q)
    print("A inverse=")
    for k in Ainv:
        print(k)
    print("check multipling:")
    mult(A,Ainv)

#ouput:A matrix=
#        [1,-3,7]
#        [-1,4,-7]
#        [-1,3,-6]
#        A inverse=
#        [-3.0,3.0,-7.0]
#        [1.0,1.0,0.0]
#        [1.0,0.0,1.0]
#        check multiplying:
#        result id identity matrix
#        [0.0,1.0,0.0]
#        [0.0,0.0,1.0]
