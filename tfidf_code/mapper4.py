import sys
import os
from math import log10,sqrt

X=10.0
for l in sys.stdin:
    l = l.strip()
    wf,nNm=line.split('\t',1)
    n,N,m=nNm.split(' ',2)
    n=float(n)
    N=float(N)
    m=float(m)
    tfidf= (n/N)*log10(X/m)
    print '%s\t%s' % (wf,tfidf)