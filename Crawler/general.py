import os


#Each website crawled will be a separate project/folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Crating project" + directory)
        os.makedirs(directory)


# Create queue ad crawled files
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Creates new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


#Add data to existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


#Delete contents of file
def delete_file_contents(path):
    with open(path, 'w'):
        pass


#File to set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

#Set to file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
