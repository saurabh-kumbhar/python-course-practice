from pathlib import Path

# Supports Absolute path (Full path) and Relative path (path from current directory)

pathEcom = Path("ecommerce")
print(pathEcom.exists())

pathEmail = Path("email")
print(pathEmail.exists())
pathEmail.mkdir()
print(pathEmail.exists())
pathEmail.rmdir()
print(pathEmail.exists())

pathSearch = Path()
for file in pathSearch.glob("*"):
    print(file)
