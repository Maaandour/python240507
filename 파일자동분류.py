import os
import shutil

def organize_downloads_folder():
    download_folder = r'C:\Users\김민수\Downloads'
    
    # Create directories if they don't exist
    directories = ['images', 'data', 'docs', 'archive']
    for directory in directories:
        directory_path = os.path.join(download_folder, directory)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
    
    # Move files to appropriate folders
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)
        if os.path.isfile(file_path):
            if filename.lower().endswith(('.jpg', '.jpeg')):
                destination_folder = os.path.join(download_folder, 'images')
            elif filename.lower().endswith(('.csv', '.xlsx')):
                destination_folder = os.path.join(download_folder, 'data')
            elif filename.lower().endswith(('.txt', '.doc', '.pdf')):
                destination_folder = os.path.join(download_folder, 'docs')
            elif filename.lower().endswith('.zip'):
                destination_folder = os.path.join(download_folder, 'archive')
            else:
                continue  # Ignore files that don't match any criteria
            shutil.move(file_path, destination_folder)

if __name__ == "__main__":
    organize_downloads_folder()
