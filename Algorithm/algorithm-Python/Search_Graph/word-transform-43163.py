from collections import defaultdict
from collections import deque


def can_diff(word1, word2):
    count = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    return count == 1


def solution(begin, target, words):
    graph = defaultdict(set)
    visited = {begin}
    all_words = words + [begin]

    # 노드 연결하기: 인접 리스트로 만들기
    for word1 in all_words:
        for word2 in all_words:
            if can_diff(word1, word2):
                graph[word1].add(word2)
                graph[word2].add(word1)

    # 큐 안에 (노드, 거리)를 함께 넣어서 BFS 진행
    queue = deque([(begin, 0)])

    while queue:
        cur_node, dist = queue.popleft()

        if cur_node == target:
            return dist

        for next_node in graph[cur_node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, dist + 1))

    return 0
