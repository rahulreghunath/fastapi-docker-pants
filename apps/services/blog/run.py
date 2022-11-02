# pylint: skip-file
import uvicorn
import sys

if __name__ == "__main__":
    # freeze_support()
    sys.argv.insert(1, "apps.services.blog.main:app")
    sys.exit(uvicorn.main())
