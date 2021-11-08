import sys

sys.argv.remove(sys.argv[0])
sys.argv = sys.argv[::-1]
for arg in sys.argv:
    if (arg == sys.argv[-1]):
        print(arg[::-1].swapcase())
    else:
        print(arg[::-1].swapcase(), end=' ')

