import sys


a = 1

b = 3

if __name__ == "__main__":
    if (a + b) > 5:
        print("Failed!")
        sys.exit(1)
    else:
        print("Succeeded!")
        sys.exit(0)
