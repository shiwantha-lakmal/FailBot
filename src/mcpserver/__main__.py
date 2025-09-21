import sys
import os

# Add the src directory to Python path
src_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from mcpserver.service import mcp

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()