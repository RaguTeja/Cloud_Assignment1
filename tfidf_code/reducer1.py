from operator import itemgetter
import sys

c_w = None
c_cnt = 0
w = None

for l in sys.stdin:
    l = l.strip()

    w, c = l.split('\t', 1)

    try:
        c = int(c)
    except ValueError:
        continue

    if c_w == w:
        c_cnt += c
    else:
        if c_w:
            print '%s\t%s' % (c_w, c_cnt)
        c_cnt = c
        c_w = w

if c_w == w:
    print '%s\t%s' % (c_d, c_cnt)