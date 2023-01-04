# myfile = open('./sample.txt')
#
# print(myfile.read())
# print('------------------------------------------------')
# myfile.seek(0)
# print(myfile.read())
# print('------------------------------------------------')
# myfile.close()
#
# with open('./samplesub.txt', mode='a') as myfile: # append and can creates
#     myfile.write("\nNEW DATA APPENDED!")
#
# myfile = open('./samplesub.txt')
# print(myfile.read())
# myfile.close()
# print('------------------------------------------------')
#
# with open('./samplemy.txt', mode='w') as myfile: # replace and can creates
#     myfile.write("NEW DATA APPENDED!")

# myfile = open('./sample.txt', 'r+') # write and read only but cannot create files
# myfile.write("NEW DATA APPENDED!")
# myfile.seek(0)
# print(myfile.read())
# myfile.close()
#
# myfile = open('./sampledata.txt', 'w+') # create and write and read only but cannot create files
# myfile.write("NEW DATA APPENDED!")
# myfile.seek(0)
# print(myfile.read())
# myfile.close()

try:
    with open('./sample101.txt', mode='r+') as myfile:
        myfile.write("NEW DATA APPENDED!")
except FileNotFoundError:
    print('File doesn\'t exists')
finally:
    print('Always executes!')