from operator import itemgetter
import sys

p_w = None
c = 1 
w = None
df={}
l1=[]
# input comes from STDIN
for l in sys.stdin:
    l = l.strip()
    w,z= l.split('\t', 1)
    f,nNc = z.split(' ',1)
    n,Nc=nNc.split(' ',1)
    N,c=Nc.split(' ',1)
    if p_w == w:
        c = c+int(c)
    else:
        if p_w != None:
            q=n+' '+N+' '+str(c)
            df[p_w]=q
            j=p_w+' '+f
            l1.append(j)
        c=1
        p_w = w

       
q=n+' '+N+' '+str(count)
df[p_w]=q
j=p_w+' '+f
l1.append(j)

for h in l1:
   word,file=h.split(' ',1)
   for doc in df:
       if word == doc:
          print '%s\t%s' % (h,df[d])