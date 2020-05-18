from collections import defaultdict
import queue

def main():
    N,M = [int(x) for x in input().split()]
    vum = defaultdict(list)
    for i in range(M):
        a,b = [int(x) for x in input().split()]
        vum[a].append(b)
        vum[b].append(a)
        
    ### bfs ###
    q = queue.Queue()
    D = [-1]*N # 最短距離
    s = 1 # 始点
    step = 0
    D[s-1] = step
    while True:
        # print('s',str(s))
        step = D[s-1] + 1
        for v in vum[s]:
            # print('v',str(v))
            if D[v-1] < 0:
                # print('append v',str(v),str(step))
                q.put(v)
                D[v-1] = step
        if q.empty():
            break
        # print(list(q.queue),V)
        s = q.get()

    if -1 in D[1:]:
        print('No')
    else:
        print('Yes')
        for d in D[1:]:
            print(d)

if __name__ == '__main__':
    main()
