import os

#RECURSIVE EXTRACTION FUNCTION: A simple application to extract meaningful files from vastly recursive unpopulated folders.
def RecursiveExtract():
    file_paths_list = []
    path = input("Enter FULL path to folder to be analyzed: \n\n")
    exists = os.path.exists(path)

    if exists:
        if os.path.isdir(path):
            files = os.listdir(path)
            for file in files:
                file_path = os.path.join(path, file)
                print(file)
                RecursiveExtract(file_path)
        else:
            file_paths_list.append(path)
            
        return file_paths_list
    
    else:
        return "Filepath not found!\n"

#HELPER FUNCTION IS TO BE CALLED WITH OUTPUT OF RECURSIVEEXTRACT
def RecursiveExtractHelper(FilePathsList):
    if len(FilePathsList) > 0:
        print("\nList of file paths:")
        for FilePath in FilePathsList:
            print(FilePath)

        root_dir_path = input("\n\nEnter the FULL path to your desired directory: ")
        folder_name = input("\n\nChoose a name for a new folder on your specified directory containing these files: ")
        exists = os.path.exists(root_dir_path)

        if exists:
            root_dir = os.path.join(root_dir_path, folder_name)
            os.mkdir(root_dir)

            for file_path in FilePathsList:
                file_name = os.path.basename(file_path)
                new_file_path = os.path.join(root_dir, file_name)
                os.rename(file_path, new_file_path)

    print(f"\n\nSuccess. View your files in: {folder_name}")


