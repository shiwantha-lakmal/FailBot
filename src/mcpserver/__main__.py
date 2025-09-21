import sys
import os

# Add the src directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))  # /path/to/FailBot/src/mcpserver
src_dir = os.path.dirname(current_dir)  # /path/to/FailBot/src
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from mcpserver.service import mcp

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()