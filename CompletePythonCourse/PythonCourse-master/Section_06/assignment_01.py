# Assignment 1:

import sys
import os
import re

# directory_containing_files = "./project_files" #sys.argv[1]
# words_to_aggregate = ["hello", "Peter", "computer"] #sys.argv[2:]

directory_containing_files = "./temp" #sys.argv[1]
words_to_aggregate = ["PSK", "SPK"] #sys.argv[2:]
# directory_containing_files = sys.argv[1]
# words_to_aggregate = sys.argv[1:]

# Expected Output:
# {"there": n, "Michael": n, "running": n}

# Your Code Below:
file_list = []
result_dir = {}
for item in words_to_aggregate:
    result_dir.update({item: [0, []]})

for paths, directories, files in os.walk(directory_containing_files):
    for file in files:
        with open(os.path.join(paths, file)) as file_to_search:
            content = file_to_search.read()
            print('content', content)
            for key in result_dir.keys():
                count_in_file = content.split().count(key)
                if count_in_file > 0:
                    result_dir[key][0] += count_in_file
                    result_dir[key][1].append(os.path.join(paths, file))

print(result_dir)









































#Solution:
# words_and_counts = {}
#
# for word in words_to_aggregate:
#     count = 0
#     for path, folder_names, file_names in os.walk(directory_containing_files):
#         for file_name in file_names:
#             file = os.path.join(path, file_name)
#             with open(file, "r") as a_file:
#                 for line in a_file:
#                     if re.search(word, line):
#                         word_list = re.findall(word, line)
#                         count += len(word_list)
#
#     words_and_counts[word] = count
#
#
#
# print(words_and_counts)