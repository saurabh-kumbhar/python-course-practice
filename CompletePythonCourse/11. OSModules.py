import os

# Get Current Working Dir
# print(os.getcwd())

# # Change Dir
# os.chdir('/Users/saurabh.kumbhar/Desktop')
#
# # Get Current Working Dir
# print(os.getcwd())
#
# # Print all files
# print(os.listdir())

# Create Directory
# if 'myfolder' not in os.listdir():
#     os.mkdir('myfolder')
# print(os.listdir())

# Create Directories
# if 'myfolder' not in os.listdir():
#     os.makedirs('myfolder/yourolder/theirfolder')

# Remove File
#os.remove('myfolder/yourolder/theirfolder/hey.png')

# Remove Directory
# os.rmdir('myfolder/yourolder')

# Remove directory including inside content
# os.removedirs('myfolder/yourolder')

# print(os.listdir())
# os.rename('sample.txt', 'sample101.txt')

# print('path | directory list | file list')
#
# for path, dirs, files in os.walk('./myfolder'):
#     print('---------------------')
#     print(path, '|', dirs, '|', files)

# print(os.environ.get('HOME') + '/' + 'file.txt')

# # add '/' automatically
# print(os.path.join(os.environ.get('HOME'), 'topdir', 'subdir', 'file.txt'))
#
# # give file name only
# print(os.path.basename('/Users/saurabh.kumbhar/topdir/subdir/file.txt'))
#
# # give folder names only
# print(os.path.dirname('/Users/saurabh.kumbhar/topdir/subdir/file.txt'))
#
# # return tuple with folder path and file name
# print(os.path.split('/Users/saurabh.kumbhar/topdir/subdir/file.txt'))
#
# # check if exists
# print(os.path.exists('/Users/saurabh.kumbhar/topdir/subdir/file.txt'))
# print(os.path.exists('/Users/saurabh.kumbhar/Desktop/honor.jpg'))

# check obj is file
print(os.path.isfile('/Users/saurabh.kumbhar/Desktop/honor.jpg'))
# check obj is folder
print(os.path.isdir('/Users/saurabh.kumbhar/Desktop/'))

# file full path and extensino in tuple
print(os.path.splitext('/Users/saurabh.kumbhar/Desktop/honor.jpg'))

