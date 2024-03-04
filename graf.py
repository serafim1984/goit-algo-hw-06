import networkx as nx
import matplotlib.pyplot as plt
import heapq

G = nx.Graph()

G.add_nodes_from(["Хрещатик / Майдан Незалежності", 
                  "Золоті Ворота / Театральна", 
                  "Площа Героїв України / Палац Спорту",
                  "Кловська", "Печерська", "Дружби Народів",
                  "Лук'янівська", "Арсенальна", "Дніпро",
                  "Гідропарк", "Університет", "Вокзальна",
                  "Олімпійська", "Палац Ураїна", "Поштова Площа", 
                  "Контрактова Площа"])

G.add_edges_from([("Хрещатик / Майдан Незалежності", "Золоті Ворота / Театральна", {'weight' : 5}), 
                  ("Хрещатик / Майдан Незалежності", "Площа Героїв України / Палац Спорту", {'weight' : 3}), 
                  ("Площа Героїв України / Палац Спорту", "Золоті Ворота / Театральна", {'weight' : 4}),
                  ("Площа Героїв України / Палац Спорту", "Кловська", {'weight' : 8}),
                  ("Печерська", "Кловська", {'weight' : 3}), ("Печерська", "Дружби Народів", {'weight' : 4}),
                  ("Золоті Ворота / Театральна", "Лук'янівська", {'weight' : 6}), ("Хрещатик / Майдан Незалежності", "Арсенальна", {'weight' : 4}), 
                  ("Дніпро", "Арсенальна", {'weight' : 3}), ("Дніпро", "Гідропарк", {'weight' : 3}), ("Золоті Ворота / Театральна", "Університет", {'weight' : 2}), 
                  ("Золоті Ворота / Театральна", "Університет", {'weight' : 5}), ("Вокзальна", "Університет", {'weight' : 3}),
                  ("Хрещатик / Майдан Незалежності", "Поштова Площа", {'weight' : 3}),
                  ("Поштова Площа", "Контрактова Площа", {'weight' : 2}), ("Площа Героїв України / Палац Спорту", "Олімпійська", {'weight' : 2}),
                  ("Олімпійська", "Палац Ураїна", {'weight' : 3})])



# Draw the graph
pos = nx.kamada_kawai_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold")

# Add edge labels

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

#plt.show()

from collections import deque

def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited  



def dfs_iterative(graph, start_vertex):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]  
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(graph[vertex])  




def dijkstra(graph, start):
    shortest_path = {vertex: float('infinity') for vertex in graph}
    shortest_path[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_path[neighbor]:
                shortest_path[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_path


# Запуск алгоритму BFS
print('\n -- BFS algorithm output\n')
bfs_iterative(G, "Хрещатик / Майдан Незалежності")

print('\n')

# Виклик функції DFS
print(' -- DFS algorithm output\n')
dfs_iterative(G, "Хрещатик / Майдан Незалежності")

print('\n')

# Виклик функції Dijkstra
print(' -- Dijkstra search \n')
print(dijkstra(G, "Хрещатик / Майдан Незалежності"))

print('\n')

# Виклик функції Dijkstra
print(' -- Graph analysis \n')
degree_centrality = nx.degree_centrality(G)  
closeness_centrality = nx.closeness_centrality(G)  
betweenness_centrality = nx.betweenness_centrality(G)

print(f'degree of centrality {degree_centrality}, \n closeness of centrality {closeness_centrality}, \n betweenness of centrality {betweenness_centrality}')


plt.show()