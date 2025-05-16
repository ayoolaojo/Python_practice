from pathlib import Path
path1 = Path("e_commerce")
print(path1.exists())

path2 = Path('email')

path3 = Path()

print(path3.glob("*.py"))

for file in path3.glob("*.*"):
    print(file)

