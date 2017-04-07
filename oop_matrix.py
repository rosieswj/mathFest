import copy

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
    
def make2dList(rows,cols):
    result=[None]*rows
    for row in range(rows):
        result[row]=[0]*cols
    return result

class Rational(object):
    def __init__(self,a):
        if isinstance(a,Rational):self=a
        elif isinstance(a,int):
            self.n=a
            self.d=1
        elif isinstance(a,float):
            l=len(str(a)[str(a).find(".")+1:])
            self.n=int(a*10**l)
            self.d=int(10**l)
        elif isinstance(a,str):
            if "/" in a:
                self.n=int(a[:a.find("/")])
                self.d=int(a[a.find("/")+1:])
            elif "." in a:
                l=len(a[a.find(".")+1:])
                self.n=int(float(a)*10**l)
                self.d=int(10**l)
            else:
                self.n=int(a)
                self.d=1
        k=gcd(self.n,self.d)
        self.n//=k
        self.d//=k
            
    def __str__(self):
        if self.d==1: return str(self.n)
        else: return str(self.n)+"/"+str(self.d)
        
    def __hash__(self):
        return hash(str(self))
        
    def __eq__(self,other):
        if isinstance(other,int):
            return self.n==other and self.d==1
        else: return self.n==other.n and self.d==other.d
        
    def mul(self,other):
        #if (self.n==0 or other.n==0): return Rational(0)
        a=self.n*other.n
        b=self.d*other.d
        a,b=a//gcd(a,b), b//gcd(a,b)
        return Rational(str(a)+"/"+str(b))
        
    def div(self,other):
        #if (self.n==0): return Rational(0)
        a=self.n*other.d
        b=self.d*other.n
        a,b=a//gcd(a,b), b//gcd(a,b)
        return Rational(str(a)+"/"+str(b))
        
    def add(self,other):
        a=self.n*other.d+self.d*other.n
        b=self.d*other.d
        #if a==0: return Rational(0)
        a,b=a//gcd(a,b), b//gcd(a,b)
        return Rational(str(a)+"/"+str(b))
        
    def sub(self,other):
        a=self.n*other.d-self.d*other.n
        b=self.d*other.d
        #if a==0: return Rational(0)
        a,b=a//gcd(a,b), b//gcd(a,b)
        return Rational(str(a)+"/"+str(b))
        

class Matrix(object):
    def __init__(self,lst):
        self.entry=copy.deepcopy(lst)
        for row in range(len(lst)):
            for col in range(len(lst[0])):
                if isinstance(lst[row][col],int):
                    self.entry[row][col]=Rational(lst[row][col])
                else:
                    self.entry[row][col]=Rational(str(lst[row][col]))
        self.steps=[]
        self.helperSteps=[]
        self.procedures=[]
                    
    def elements(self):
        rep=copy.deepcopy(self.entry)
        for row in range(len(rep)):
            for col in range(len(rep[0])):
                rep[row][col]=str(self.entry[row][col])
        return rep
                    
    def __str__(self):
        rep=copy.deepcopy(self.entry)
        for row in range(len(rep)):
            for col in range(len(rep[0])):
                rep[row][col]=str(self.entry[row][col])
        return str(rep)
                
    def __eq__(self,other):
        if other==None: return False
        return self.entry==other.entry
        
    def add(self,other):
        if (len(self.entry)!=len(other.entry) or 
            len(self.entry[0])!=len(other.entry[0])):
            return None
        new=copy.deepcopy(self.entry)
        for row in range(len(new)):
            for col in range(len(new[0])):
                new[row][col]=new[row][col].add(other.entry[row][col])
        return Matrix(new)
        
    def sub(self,other):
        if (len(self.entry)!=len(other.entry) or 
            len(self.entry[0])!=len(other.entry[0])):
            return None
        new=copy.deepcopy(self.entry)
        for row in range(len(new)):
            for col in range(len(new[0])):
                new[row][col]=new[row][col].sub(other.entry[row][col])
        return Matrix(new)
                    
    def mul(self,other):
        if isinstance(other,int) or isinstance(other,float):
            result=make2dList(self.entry,self.entry[0])
            for row in range(len(result)):
                for col in range(len(result[0])):
                    result[row][col]=self[row][col].mul(other)
            return Matrix(result)
        if (len(self.entry[0])!=len(other.entry)):
            return None
        result=make2dList(len(self.entry),len(other.entry[0]))
        for row in range(len(self.entry)):
            for col in range(len(other.entry[0])):
                sum=Rational(0)
                for i in range(len(other.entry)):
                    sum=sum.add(self.entry[row][i].mul(other.entry[i][col]))
                result[row][col]=sum
        return Matrix(result)
        
    def transpose(self):
        result=make2dList(len(self.entry[0]),len(self.entry))
        for row in range(len(self.entry[0])):
            for col in range(len(self.entry)):
                result[row][col]=self.entry[col][row]
        return Matrix(result)
        
    @staticmethod
    def makeIdentity(size):
        result=[None]*size
        for row in range(size):
            result[row]=[0]*size
            result[row][row]=1
        return Matrix(result)
        
    @staticmethod
    def makeEmptyMatrix(rows,cols):
        return Matrix(make2dList(rows,cols))
        
    def findSubMatrix(self,row,col):
        size=len(self.entry)
        new=[]
        for r in range(size):
            if r!=row:
                v=[]
                for c in range(size):
                    if c!=col: v.append(self.entry[r][c])
                new.append(v)
        return Matrix(new)
        
    def det(self):
        if len(self.entry) != len(self.entry[0]):
            return False
        size=len(self.entry)
        if size==1: return self.entry[0][0]
        else:
            result=Rational(0)
            for col in range(size):
                result=result.add(self.entry[0][col].
                mul(Rational((-1)**col)).mul(self.findSubMatrix(0,col).det()))
        return result
        
    def simplify(self,helper):
        size=len(self.entry)
        for row in range(size):
            if (self.entry[row][row]!=Rational(0) and self.entry[row]
                                 [row]!=Rational(1)):
                const=self.entry[row][row]
                for col in range(size):
                    self.entry[row][col]=self.entry[row][col].div(const)
                    helper.entry[row][col]=helper.entry[row][col].div(const)
                self.steps.append(self.elements())
                self.helperSteps.append(helper.elements())
                self.procedures.append(["multiply",row,
                                    str(Rational(1).div(const))])
                
    def rowOperation(self,r1,r2,c):
        for col in range(len(self.entry[0])):
            self.entry[r2][col]=self.entry[r2][col].add(self.entry[r1][col].
               mul(c))
               
    def GaussJordanElim(self,helper):
        size=len(self.entry)
        for col in range(size):
            if self.entry[col][col]==Rational(0):
                for c in range(col+1,size):
                    if self.entry[c][col]!=Rational(0):
                        (self.entry[col],self.entry[c])=(self.entry[c],
                                self.entry[col])
                        (helper.entry[col],helper.entry[c])=(helper.entry[c],
                                helper.entry[col])
                        #print(self,helper, end="\n")
                        self.steps.append(self.elements())
                        self.helperSteps.append(helper.elements())
                        self.procedures.append(["swap",col,c])
                        break
            for row in range(col+1,size):
                multiplier=(Rational(-1).mul(self.entry[row][col])).div(self.
                            entry[col][col]) 
                self.rowOperation(col,row,multiplier)
                helper.rowOperation(col,row,multiplier)
                if multiplier!=Rational(0):
                    self.steps.append(self.elements())
                    self.helperSteps.append(helper.elements())
                    self.procedures.append(["add",row,col,str(multiplier)])
                    #print(self,helper, end="\n")
        self.simplify(helper)
        #print(self,helper, end="\n")
        for col in range(size-1,0,-1):
            for row in range(col):
                multiplier=Rational(-1).mul(self.entry[row][col])
                self.rowOperation(col,row,multiplier)
                helper.rowOperation(col,row,multiplier)
                #print(self,helper, end="\n")
                self.steps.append(self.elements())
                self.helperSteps.append(helper.elements())
                self.procedures.append(["add",row,col,str(multiplier)])
                
    def rank(self):
        self.steps=[self.elements()]
        r=0
        for col in range(len(self.entry[0])):
            swapped=True
            if self.entry[r][col]==Rational(0):
                swapped=False
                for c in range(r+1,len(self.entry)):
                    if self.entry[c][col]!=Rational(0):
                        (self.entry[col],self.entry[c])=(self.entry[c],
                                self.entry[col])
                        self.steps.append(self.elements())
                        self.procedures.append(["swap",col,c])
                        swapped=True
                        break
            if swapped:
                for row in range(r+1,len(self.entry)):
                    multiplier=(Rational(-1).mul(self.entry[row][col])).div(self.
                            entry[r][col]) 
                    self.rowOperation(r,row,multiplier)
                    if multiplier!=Rational(0):
                        self.steps.append(self.elements())
                        self.procedures.append(["add",row,col,str(multiplier)])
                r+=1
        count=0
        for row in range(len(self.entry)):
            if self.entry[row]!=[Rational(0)]*len(self.entry[0]):
                count+=1
        return count
                
    def inverse(self, helper=None):
        if (len(self.entry) != len(self.entry[0])):
            return None
        size=len(self.entry)
        if helper==None: helper=Matrix.makeIdentity(size)
        self.steps=[self.elements()]
        self.helperSteps=[helper.elements()]
        self.procedures=[]
        if self==Matrix.makeIdentity(size): return helper
        elif self.det()==Rational(0): return None
        else:
            #print(self,helper, end="\n")
            self.GaussJordanElim(helper)
            self=helper
            return self
            
    def swapCol(self,col1,col2):
        for row in range (len(self.entry)):
            (self.entry[row][col1],self.entry[row][col2])=(self.entry[row][col2],
            self.entry[row][col1])      
            
    def decomp(self):
        L=Matrix.makeIdentity(len(self.entry))
        P=Matrix.makeIdentity(len(self.entry))
        U=self
        self.steps=[self.elements()]
        self.helperSteps=[L.elements()]
        self.procedures=[]
        size=len(self.entry)
        if self==Matrix.makeIdentity(size):
            return [P.elements(),self.elements(),L.elements,self.elements()]
        else:
            r=0
            for col in range(len(U.entry[0])):
                swapped=True
                if U.entry[r][col]==Rational(0):
                    swapped=False
                    for c in range(r+1,len(U.entry)):
                        if U.entry[c][col]!=Rational(0):
                            (U.entry[col],U.entry[c])=(U.entry[c],
                                U.entry[col])
                            P.swapCol(c,col)
                        #print(U,helper, end="\n")
                        self.steps.append(U.elements())
                        self.helperSteps.append(L.elements())
                        self.procedures.append(["swap",col,c])
                        swapped=True
                        break
                if swapped:
                    for row in range(r+1,len(U.entry)):
                        multiplier=U.entry[row][col].div(U.entry[r][col]) 
                        U.rowOperation(r,row,Rational(-1).mul(multiplier))
                        L.entry[row][col]=multiplier
                        if multiplier!=Rational(0):
                            self.steps.append(U.elements())
                            self.helperSteps.append(L.elements())
                            self.procedures.append(["add",row,col,
                                    str(multiplier)])
                        #print(U,L, end="\n")
                    r+=1
            return [P.elements(),self.elements(),L.elements(),U.elements()]
            
    def solveLinearEquation(self,vec):
        if len(self.entry)!=len(self.entry[0]): return None
        for k in range(len(vec)):
            vec[k]=[vec[k]]
        m=Matrix(vec)
        try:
            return self.inverse().mul(m)
        except:
            return None
            
#a=Matrix([[1,0,"-1/3",2,1],[1,0,0,0,0],[0,0,'-1/3',2,1]])
#print(a.rank())
#print(a)
#print(a.steps)
#print(a.helperSteps)
#print(a.procedures)
        