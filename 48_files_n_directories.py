from pathlib import Path

# Absolute, from root of Hard, "c:\" or "/" in linux


dir_path = Path("45_packages\email")
try:
    print(dir_path.mkdir())
except:
    print(dir_path.rmdir())

dir_path = Path("45_packages")
for file in dir_path.glob("*"):
# for file in dir_path.glob("*.*"):
    print(file)



# Relative paath