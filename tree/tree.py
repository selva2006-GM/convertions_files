from collections import deque

def find_path(start, target):
    graph = {
    "txt": ["pdf", "html"],
    "pdf": ["txt","html"],
    "html":[],
    "docx":[],
    "doc": [],
    "rtf": [],
    "odt": [],
    "xls": [],
    "xlsx":[],
    "csv": [],
    "ppt": [],
    "pptx":[],
    "xml": [],
    "json":[],
    "png": [],
    "jpg": [],
    "jpeg":[],
    "gif": [],
    "bmp": [],
    "webp":[],
    "tiff":[],
    "ico": [],
    "svg": [],
    "mp4": [],
    "mkv": [],
    "avi": [],
    "mov": [],
    "wmv": [],
    "flv": [],
    "webm":[],
    "mpeg":[],
    "mpg": [],
    "3gp": [],
    "mp3": [],
    "wav": [],
    "aac": [],
    "flac":[],
    "ogg": [],
    "m4a": [],
    "wma": [],
    "aiff":[],
    "opus":[],
    "py":  [],
    "java":[],
    "cpp": [],
    "c":   [],
    "js":  [],
    "ts":  [],
    "css": [],
    "php": [],
    "rb":  [],
    "go":  [],
    "rs":  [],
"swift":   [],
    "kt":  [],
    "zip": [],
    "rar": [],
    "7z":  [],
    "tar": [],
    "gz":  [],
    "bz2": [],
    "xz":  []
}
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
