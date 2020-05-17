import math

def main():
    A,B,H,M = [int(x) for x in input().split()]
    degH = (0.5*H*60 + 0.5*M)
    degM = 6*M
    theta = abs(degH-degM)
    print(math.sqrt(A**2 + B**2 - 2*A*B*math.cos(math.radians(theta))))

if __name__ == '__main__':
    main()
