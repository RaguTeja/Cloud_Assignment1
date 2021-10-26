import sys

for l in sys.stdin:
    line = l.strip()
    filename,cnt=line.split('\t',1)
    w,filename=filename.split(' ',1)
    k=w+' '+cnt;
    print '%s\t%s' % (filename, k)
        