import sys

import test_1

a = 2

b = 1

if __name__ == "__main__":
    if a + b + test_1.a + test_1.b > 5:
        print("FAILED")
        sys.exit(1)
    else:
        print("SUCCEEDED")
        sys.exit(0)
