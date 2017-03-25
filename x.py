#!/usr/bin/env python
import sys
fni=sys.argv[1]
fno=fni[:-1]+'o'
fi,fo=open(fni),open(fno,'w')
fo.write("z v0.0.0.0.0\n")
for line in fi:
    print("LINE", line)
    fo.write(line)

