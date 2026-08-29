from collections import deque



def find_path(graph, start, target):
    queue = deque([[start]])
    visited = {start}
    
    
    while queue:
        path = queue.popleft()
        current = path[-1]
        
        
        if current == target:
            return path
        
        
        for next_type in graph.get(current, []):
            if next_type not in visited:
                visited.add(next_type)
                queue.append(path + [next_type])
    return None


graph = {
    "txt": ["pdf", "html"],
    "pdf": ["docx", "txt"],
    "html": ["pdf"],
    "docx": ["pdf"]
}


