from pathlib import Path

unichar = {
    "branch":"├──",
    "lastchild":"└──",
    "vertical_line":"│",
    "horizontal_line":"──",
    "space":"    ",
    }

# Returns current folder path
def path():
    #current_dir = Path.cwd()
    return "/home/yashwanth/Programs/C"
            
# Use item.name for item's name without full path
def explore(dir, prefix=""):
    dir_path = Path(dir)
    for item in dir_path.iterdir():
        if item.is_file():
            print(f"{unichar['space']}{prefix}{item.name}")
        elif item.is_dir():
            print(f"{unichar['space']}{prefix}{item.name}")
            explore(item, prefix+unichar["space"])
            