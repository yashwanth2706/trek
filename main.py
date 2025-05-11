import sys, argparse
from src.trek import explore

# Main function
def main(args):
    
    parser = argparse.ArgumentParser(description="Command line tool inspired by tree to visualize directry structure")
    parser.add_argument("path", metavar="p", type=str, nargs="+", help="path to visualize directry")
    args = parser.parse_args()
    
    if args.path:
        target = args.path
        target_directry = target[1]
        explore(target_directry)

if __name__ == "__main__":
    main(sys.argv[1:])
    