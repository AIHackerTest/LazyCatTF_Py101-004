from sys import *
script, weather_info = argv

d = {}
with open(weather_info, 'r', encoding = 'utf-8') as f:
    for line in f.readlines():
        l = line.strip().split(',')
        d[l[0]] = l[1]
#    line = f.readline()
#    while line:
#        l = line.strip().split(',')
#        d[l[0]] = l[1]
#        line = f.readline()

his = "\n查询历史\n--------------"

hel = """
                 **帮助文档**
     / 输入   城市名称    查询当地天气 /
    / 输入   h / help    获取帮助文档 /
   / 输入   history     获取查询历史 /
  / 输入   q / quit    退出查询程序 /"""

print ("\n欢迎使用天气通~\n如需帮助请输入 h / help")

while True:
    instruction = input("\n请输入城市名或其他关键词：\n> ")
    if instruction in d:
        print (d[instruction])
        his += '\n' + instruction + ' ' + d[instruction]
    elif instruction == 'help' or instruction == 'h':
        print (hel)
    elif instruction == 'history':
        print (his)
    elif instruction == 'quit' or instruction == 'q':
        print ("\n感谢你的使用，再见~ ^u^")
        exit(0)
    else:
        print ("\n未知关键词 TAT?? 请重新输入\n如需帮助请输入 h / help")
