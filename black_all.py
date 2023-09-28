import os
def is_python_file(file_path):
    # Get the file extension
    file_extension = os.path.splitext(file_path)[1]

    # Check if the file extension is ".py" (case-insensitive)
    return file_extension.lower() == ".py"


def walk_directory(start_dir):
    for root, directories, files in os.walk(start_dir):
        #print(f'{root}, {directories}, {files}')
        if '.git' in root:
            continue
        
        for filename in files:
            file_path = os.path.join(root, filename)
            if is_python_file(file_path) == True:
                #print(file_path)
                os.system(
                    f'python3 -m black {file_path}'
                )


def main():
    walk_directory('code')

if __name__ == '__main__':
    main()

