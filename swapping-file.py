def swapFileData():
    file1 = input(" Enter file name: ")
    file2 = input(" Enter file name to swap: ")

    f = open(file1, "r")
    dataFromFile1 = f.read()

    with open(file2, "r") as f2:
        dataFromFile2 = f2.read()

    with open(file1, 'w') as f:
        f.write(dataFromFile2)

    with open(file2, 'w') as f2:
        f2.write(dataFromFile1)


swapFileData()
