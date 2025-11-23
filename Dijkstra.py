import heapq

edges_data = [
    (1, 7, 1), (1, 4, 1), (1, 2, 2), (1, 3, 5),
    (7, 8, 6), (7, 4, 9), (7, 3, 4),
    (8, 6, 1),
    (6, 3, 4), (6, 4, 5), (6, 5, 3),
    (5, 3, 2), (5, 4, 9), (5, 2, 7),
    (2, 4, 3)
]
num_vertices = 8

adj = {i: [] for i in range(1, num_vertices + 1)}
for u, v, w in edges_data:
    adj[u].append((v, w))
    adj[v].append((u, w))


def dijkstra(graph_adj, s, n):
    pred = {v: -1 for v in range(1, n + 1)}
    dist = {v: float('inf') for v in range(1, n + 1)}
    pq = []

    dist[s] = 0
    heapq.heappush(pq, (0, s))

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in graph_adj[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))

    return pred, dist


start_node = 1
final_pred, final_dist = dijkstra(adj, start_node, num_vertices)

print(f"--- Результат алгоритму Дейкстри (Старт: {start_node}) ---\n")
print(f"{'Вершина (v)':<12} | {'Відстань (dist)':<15} | {'Попередник (pred)'}")
print("-" * 50)

for v in range(1, num_vertices + 1):
    p = final_pred[v]
    d = final_dist[v]
    pred_str = str(p) if p != -1 else "-"
    print(f"{v:<12} | {d:<15} | {pred_str}")