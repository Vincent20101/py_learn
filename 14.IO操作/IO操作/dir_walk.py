import os

def dir_walk(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for f in files:
            file_list.append(os.path.join(root, f))

    return file_list

if __name__ == '__main__':
    directory_path = r'E:\BaiduNetdiskDownload\python-study'
    all_files = dir_walk(directory_path)
    for file in all_files:
        print(file)

