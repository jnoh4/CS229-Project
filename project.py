import sys
import numpy as np
import pandas

def main():
    f = np.loadtxt("NCANDA_S00033.txt")
    print(f)
    print(np.shape(f))
    print(np.min(f))
    print(np.max(f))


if __name__ == "__main__":
    main()