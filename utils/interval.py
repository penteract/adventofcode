
class I:
    """half open intervals of integers """
    __slots__ = ["s","e"]
    def __init__(self,start,end=None,len=None):
        assert (end is None) != (len is None)
        if end is None:
            end = start + len
        if end<start:
            end=start
        self.s=start
        self.e=end
    def __len__(self):
        return self.e-self.s
    def __iter__(self):
        return range(self.s,self.e)
    def __and__(self,other):
        x,e = self.s,self.e
        a,b = other.s,other.e
        return I(max(x,a),min(e,b))
    def __add__(self,k):
        return I(self.s+k,self.e+k)
    def __sub__(self,k):
        if isinstance(k,I):
            x,e = self.s,self.e
            a,b = k.s,k.e
            if a>=b:
                return [self] # could argue that it should split using empty intervals
            res=[]
            if x<a:
                res.append(I(x,min(a,e)))
            if e>b:
                res.append(I(x,max(x,b)))
            return res
        else:
            raise TypeError("Set difference must be between two intervals")
            #return I(self.s-k,self.e-k)
