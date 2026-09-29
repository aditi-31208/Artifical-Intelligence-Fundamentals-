#DFS Autonomous Mine Inspection Robot
mine = {
    "Tunnel X":["Tunnel A","Tunnel B"],
    "Tunnel A":["Tunnel U","Tunnel V"],
    "Tunnel B":["Tunnel Q"],
    "Tunnel U":["Tunnel P"],
    "Tunnel V":["Tunnel R","Tunnel S"],
    "Tunnel Q":[],
    "Tunnel P":[],
    "Tunnel R":[],
    "Tunnel S":[]
}
visited = set()
def dfs(node):
    visited.add(node)
    print("Robot Inspecting:",node)
    for neighbour in mine[node]:
        if neighbour not in visited:
            dfs(neighbour)
dfs("Tunnel X")
