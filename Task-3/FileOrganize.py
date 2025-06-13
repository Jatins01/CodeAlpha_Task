import os
import shutil

def organize_files(directory):
    # Define the mapping of file extensions to folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
        'Spreadsheets': ['.xlsx', '.csv'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Audio': ['.mp3', '.wav'],
        'Others': []
    }

    # Create subfolders if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to their respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    moved = True
                    break
            if not moved:
                # Move to 'Others' if no extension matches
                shutil.move(file_path, os.path.join(directory, 'Others', filename))

if __name__ == "__main__":
    # Specify the directory to organize
    target_directory = r'C:\Users\Jatin\OneDrive\Pictures\Documents'  # Use raw string
    organize_files(target_directory)
    print("Files organized successfully!")

