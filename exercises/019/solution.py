import sys
import operator

if len(sys.argv) == 3:
    print(operator.add(int(sys.argv[1]), int(sys.argv[2])))
else:
    sys.exit("usage: python3 solution.py OP1 OP2")
