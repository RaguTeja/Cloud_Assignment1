from operator import itemgetter
import sys

c_w = None
prev_file_name = None
c_cnt = 0
w = None
N=0
df={}
l1=[]


for l in sys.stdin:
    l = l.strip()
    l1.append(l)
    file_name,wcnt = l.split('\t', 1)
    w,c = wcnt.split(' ', 1)
    c=int(c)
    if prev_file_name == file_name:
        N=N+c
    else:
       if prev_file_name != None:
            df[prev_file_name]=N
       N=0
       prev_file_name = file_name
df[prev_file_name]=N


for h in l1:
    file_name,wcnt = h.split('\t', 1)
    w,c = wcnt.split(' ', 1) 
    for k in df:
        if file_name == k:
           wf=w+' '+file_name
           nN=c+' '+str(df[k])
           print '%s\t%s' % (wf,nN)
    