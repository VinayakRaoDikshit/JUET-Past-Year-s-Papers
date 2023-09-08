import os
import re

def is_valid_folder_name(folder_name, patterns):
    for pattern in patterns:
        if re.match(pattern, folder_name):
            return True
    return False

def check_naming_conventions(root_dir):
    folder_patterns = [
        r'^CSE$', r'^ECE$', r'^ME$', r'^CHE$', r'^CE$',
        r'^T1$',r'^T2',r'^T3',
        r'Sem I', r'Sem II', r'Sem III', r'Sem IV', r'Sem V', r'Sem VI', r'Sem VII', r'Sem VIII', 
        r'^Batch 2\d+-2\d+$'
    ]
    # ^ and $ anchor the pattern to the start and end of the string, respectively, ensuring that the entire string matches the pattern.
    with open(".github/workflows/counts.txt", "r") as count_file:
        folder_count1 = int(count_file.readline().strip())
        file_count1 = int(count_file.readline().strip())

    file_count=0
    folder_count=0

    
    for root, dirs, files in os.walk(root_dir):
        # for folder in root:
        for folder in dirs:
            if is_valid_folder_name(folder, folder_patterns):
                print(folder)
                folder_count += 1
            else:
                return False    
              # with open("counts.txt", "w") as count_file:
              # count_file.write(f"Folder: {os.path.join(root, folder)}\n")

        for file in files:
            file_count += 1
            # with open("counts.txt", "w") as count_file:
            #  count_file.write(f"File: {os.path.join(root, file)}\n")
    if(file_count>=file_count1 and folder_count>=folder_count1): #Ensuring that no files or folders are deleted. Only added

        with open(".github/workflows/counts.txt", "w") as count_file:
            count_file.write(f"{folder_count}\n")
            count_file.write(f"{file_count}\n")
    else:
        return False

    return True

if __name__ == "__main__":
    # repository_root = "D:\Vinayak\JUET-Past-Year-s-Papers\Papers\CSE"  
    # Set this to the path of your repository root
    # current_directory = os.path.dirname(__file__)
    # repository_root=os.path.join(current_directory, '..', 'papers')
    # print("cd: ", current_directory)  
    # print("reporoot: ", repository_root)
    repository_root="Papers/CSE"
    if not check_naming_conventions(repository_root):
        print("Naming conventions not met.")
        exit(1)
    else:
        print("Naming conventions met.")

    # Open and read the "counts.txt" file
    # with open("counts.txt", "r") as count_file:
    #     file_contents = count_file.read()

    # Print the contents to the console
    # print(file_contents)
