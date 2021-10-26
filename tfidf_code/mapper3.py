import sys
import os


for l in sys.stdin:
    l = l.strip()
    wf,N=l.split('\t',1)
    w,f=wf.split(' ',1)
    k=f+' '+N+' '+str(1)
    print '%s\t%s' % (w,k)