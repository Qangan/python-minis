print((lambda x: [list(map(float, i.strip().split())) for i in x.split("|")])(input())[int(input())][int(input())])
