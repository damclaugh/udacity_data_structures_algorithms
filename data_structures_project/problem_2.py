
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    # check path exists
    if not os.path.isdir(path):
        return 'Invalid path'

    path_items = os.listdir(path)
    
    # get files with suffix
    files = [file for file in path_items if ('.' + suffix) in file]
    # get folders
    folders = [folder for folder in path_items if '.' not in folder]   
    # search for folders recursively
    for folder in folders:
        files.extend(find_files(suffix=suffix, path=path + '/' + folder))

    return files


# TEST CASE 1
print(find_files('c', './testdir'))
# ['t1.c', 'b.c', 'a.c', 'a.c']

# TEST CASE 2
print(find_files('c', './testdir/subdir2'))
# []

# TEST CASE 3
print(find_files('A', './testdir'))
# []

# TEST CASE 4
print(find_files('', './testdir'))
# ['.DS_Store', 't1.c', 't1.h', '.gitkeep', '.DS_Store', 'b.h', 'b.c', '.gitkeep', 'a.h', 'a.c', 'a.h', 'a.c']

# TEST CASE 5
print(find_files('c', 'A'))
# Invalid path