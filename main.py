import os

path = input("Enter FULL path to folder to be analyzed: ")
print("\n\n")
file_paths_list = []

def main(path):
    exists = os.path.exists(path)

    if exists:
        if os.path.isdir(path):
            files = os.listdir(path)
            for file in files:
                file_path = os.path.join(path, file)
                print(file)
                main(file_path)
        else:
            file_paths_list.append(path)
    else:
        return "Filepath not found!\n"

main(path)

if len(file_paths_list) > 0:
    print("\n")
    print("List of file paths:")

    for file_path in file_paths_list:
        print(file_path)

    root_dir_path = input("\n\n Enter the FULL path to your desired directory: ")
    folder_name = input("\n\n Choose a name for a new folder on your specified directory containing these files: ")


    exists = os.path.exists(root_dir_path)

    if exists:
        
        root_dir = os.path.join(root_dir_path, folder_name)
        os.mkdir(root_dir)

        for file_path in file_paths_list:
            file_name = os.path.basename(file_path)
            new_file_path = os.path.join(root_dir, file_name)
            os.rename(file_path, new_file_path)

print("\n\nSuccess.")
print(f"\n\n View your files in: {folder_name}")


