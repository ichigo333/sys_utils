import os


def find_large_files(path: str, min_size_mb: int) -> list[dict]:
    file_list = []
    min_size_bytes = min_size_mb * 1024 * 1024

    for root, _, files in os.walk(path):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                if (size := os.path.getsize(file_path)) > min_size_bytes:
                    file_list.append(dict(file=file_path, size=size/(1024**2)))
            except OSError as e:
                print(f"Could not check '{file_path}' because {e}")

    return file_list
    

if __name__ == "__main__":
    path = "/home/"
    file_dict = find_large_files(path, 100)

    for file in file_dict:
        print(f"file: {file['file']} size: {file['size']: .2f}")