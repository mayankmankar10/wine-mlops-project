import os

# List of directories to create
dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src",
]

# Create directories and add a .gitkeep file in each
for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:  # Create the .gitkeep file
        pass

# List of files to create
files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py"),
]

# Create the files
for file_ in files:
    with open(file_, "w") as f:
        pass
