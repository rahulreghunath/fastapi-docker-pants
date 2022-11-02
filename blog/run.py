import uvicorn
import sys

if __name__ == '__main__':
    # freeze_support()
    sys.argv.insert(1, "blog.main:app")
    sys.exit(uvicorn.main())