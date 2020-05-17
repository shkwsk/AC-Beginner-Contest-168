from collections import defaultdict
import itertools
import math

def dfs(vum,s,visit,depth):
    # print('first')
    # print(s,depth,visit)
    if visit[s-1] >= 0:
        return visit
    visit[s-1] = depth
    depth += 1
    # print(vum[s])
    for u in vum[s]:
        # print('now', str(s), str(u), str(depth))
        if visit[u-1] >= 0:
            # print('skip', str(u))
            if visit[u-1] > depth:
                visit[u-1] = depth
                # print('update', str(u))
            continue
        visit = dfs(vum,u,visit,depth)
    return visit


def main():
    N,M = [int(x) for x in input().split()]
    vum = defaultdict(list)
    for i in range(M):
        a,b = [int(x) for x in input().split()]
        vum[a].append(b)
        vum[b].append(a)
        
    s = 1 # 現在地 (初期値はゴールを設定)
    visit = [-1]*N # 訪問リスト
    depth = 0 # 移動数(深さ)
    visit = dfs(vum,s,visit,depth)
    if -1 in visit:
        print('No')
        return
    else:
        print('Yes')
    for v in visit[1:]:
        print(v)

if __name__ == '__main__':
    main()
