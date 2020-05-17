import math

def main():
    A,B,H,M = [int(x) for x in input().split()]
    degH = (0.5*H*60 + 0.5*M)
    degM = 6*M
    theta = abs(degH-degM)
    if theta == 180:
        print(A+B)
        return
    if theta > 180:
        theta = 180 - (theta - 180)
    print(math.sqrt(A**2 + B**2 - 2*A*B*math.cos(math.radians(theta))))

if __name__ == '__main__':
    main()
