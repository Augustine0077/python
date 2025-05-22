### Practical : Reading LArge Files

def read_large_file(file_path):
    with open(file_path,'r') as file:
        for line in file:
            yield line
            file_path='large_file.txt'

for line in read_large_file(file_path):
    print(line.strip())