
filename = 'input12.txt'
with open(filename) as f:
    arr = []
    content = f.readlines()
    for line in content:
        l = line.split(' ')
        arr.append("{},".format([int(l[0]), int(l[1].replace('\n', ''))]))

with open('testcase.txt', 'w') as f:
    for item in arr:
        f.write("%s" % item)
