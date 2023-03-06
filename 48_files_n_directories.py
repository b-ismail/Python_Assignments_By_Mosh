from pathlib import Path

# Absolute, from root of Hard, "c:\" or "/" in linux
dir_path = Path("45_packages\email")
try:
    print(dir_path.mkdir())
except:
    print(dir_path.rmdir())

# Relative paath