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
    F = [-1]*N # 道標の先の部屋
    s = 1 # 始点
    step = 0
    while True:
        # print('s',str(s))
        for v in vum[s]:
            # print('v',str(v))
            if F[v-1] < 0:
                q.put(v)
                F[v-1] = s
        if q.empty():
            break
        # print(list(q.queue),V)
        s = q.get()

    if -1 in F[1:]:
        print('No')
    else:
        print('Yes')
        for d in F[1:]:
            print(d)

if __name__ == '__main__':
    main()
