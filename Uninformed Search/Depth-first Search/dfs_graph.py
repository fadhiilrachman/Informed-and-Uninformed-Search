import time

graph = {'A': set(['B', 'C']),
	'B': set(['A', 'D', 'E']),
	'C': set(['A', 'F']),
	'D': set(['B']),
	'E': set(['B', 'F']),
	'F': set(['C', 'E'])}

def dfs_paths(graph, start, goal, path=None):
	if path is None:
		path = [start]
	if start == goal:
		yield path
	for next in graph[start] - set(path):
		yield from dfs_paths(graph, next, goal, path + [next])

def dfs_shortest_path(graph, start, goal):
	start_time = time.time()
	try:
		routes = next(dfs_paths(graph, start, goal))
		print("Spent time:", (time.time() - start_time), "seconds.")
		return routes
	except StopIteration:
		return None

dfs_sp = dfs_shortest_path(graph, 'B', 'F')
print("Best Route: ", dfs_sp)