import os

# Define the folder structure to create
folder_structure = {
    "src": {
        "data_preprocessing": [
            "__init__.py",
            "tokenization.py",
            "augmentation.py",
            "complexity.py"
        ],
        "model": [
            "__init__.py",
            "pretraining.py",
            "fine_tuning.py",
            "evaluation.py"
        ],
        "utils": [
            "__init__.py",
            "metrics.py",
            "data_utils.py",
            "config.py"
        ]
    }
}

# Function to create the folder structure
def create_folders(base_path, structure):
    for folder, subfolders in structure.items():
        # Create the directory
        current_path = os.path.join(base_path, folder)
        os.makedirs(current_path, exist_ok=True)
        
        # If the current item is a list of files, create empty files
        if isinstance(subfolders, list):
            for file_name in subfolders:
                with open(os.path.join(current_path, file_name), 'w') as file:
                    pass  # Create empty file
        # If the current item is a dictionary, create subfolders recursively
        elif isinstance(subfolders, dict):
            create_folders(current_path, subfolders)

# Specify the root directory where you want the structure to be created
base_path = "LATS_Model/src"

# Create the folder structure
create_folders(base_path, folder_structure)

print("Folder structure created successfully!")
