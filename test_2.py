import sys

a = 2

b = 0

if a + b > 5:
    print("FAILED")
    sys.exit(1)
else:
    print("SUCCEEDED")
    sys.exit(0)
