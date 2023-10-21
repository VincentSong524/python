file_name = 'moby_dick.txt'
count = 0

with open(file_name, encoding='utf-8') as f:
    contents = f.read()
    print(contents.count('the'))
    words = contents.split()
    for word in words:
        if word == 'the':
            count += 1
    print(count)