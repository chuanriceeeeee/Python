# &
course = {'张三': ('C', 'Pyhon', '人工智能数学基础'), '李四': ('Pyhon', '人工智能','C')}

CompareList=list(set(course['张三']) & set(course['李四']))
print(CompareList)