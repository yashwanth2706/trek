from pathlib import Path

unichar = {
    "branch":"├──",
    "lastchild":"└──",
    "vertical_line":"│   ",
    "horizontal_line":"──",
    "space":"    ",
    }
            
# Use item.name for item's name without full path
def explore(dir, prefix="", files = 0, directories = 0):
    dir_path = Path(dir)
    entries = sorted(list(dir_path.iterdir()))
    
    for index, item in enumerate(entries):
        is_last = (index == len(entries)-1)
        roots = unichar["lastchild"] if is_last else unichar["branch"]
        files += 1
        print(f"{prefix}{roots}{item.name}")
        if item.is_dir():
            directories += 1
            extension = unichar["space"] if is_last else unichar["vertical_line"]
            explore(item, prefix+extension)
    
    return {"directories":directories-1, "files":files-1}