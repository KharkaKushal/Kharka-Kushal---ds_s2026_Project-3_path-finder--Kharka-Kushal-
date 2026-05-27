import json
import heapq
from collections import deque


def load_graph(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        graph = json.load(file)

    for node in graph:
        for neighbor, weight in graph[node].items():
            if weight <= 0:
                raise ValueError("Graph weights must be positive")

    return graph


def get_neighbors(graph, node):
    return graph.get(node, {})


def bfs_order(graph, start):
    if start not in graph:
        return []

    visited = set()
    order = []
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def dijkstra_distances(graph, start):
    if start not in graph:
        return {}

    for node in graph:
        for neighbor, weight in graph[node].items():
            if weight <= 0:
                raise ValueError("Graph weights must be positive")

    distances = {start: 0}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight

            if neighbor not in distances or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


def shortest_path(graph, start, target):
    if start not in graph or target not in graph:
        return []

    if start == target:
        return [start]

    for node in graph:
        for neighbor, weight in graph[node].items():
            if weight <= 0:
                raise ValueError("Graph weights must be positive")

    distances = {start: 0}
    previous = {}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == target:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight

            if neighbor not in distances or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

    if target not in distances:
        return []

    path = []
    current = target

    while current != start:
        path.append(current)
        current = previous[current]

    path.append(start)
    path.reverse()

    return path