from pathlib import Path

unichar = {
    "branch":"├──",
    "lastchild":"└──",
    "vertical_line":"│",
    "horizontal_line":"──",
    "space":"    ",
    }
            
# Use item.name for item's name without full path
def explore(dir, prefix=""):
    dir_path = Path(dir)
    entries = list(dir_path.iterdir())
    entries.sort()
    for index, item in enumerate(entries):
        is_last = (index == len(entries)-1)
        roots = unichar["lastchild"] if is_last else unichar["branch"]
        print(f"{prefix}{roots}{item.name}")
        
        if item.is_dir():
            extension = unichar["space"] if is_last else unichar["vertical_line"]
            explore(item, prefix+extension)
            