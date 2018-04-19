# 英文版文本词频统计

def getText():
    txt = open('Hamlet.txt', 'r').read()
    # 将单词同一转换为小写
    txt = txt.lower()
    # 将特殊符号同一替换为空格
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_\'{|}':
        txt = txt.replace(ch," ")
    return txt

hamletTxt = getText()
# .split方法，默认用空格分隔，并返回一个列表
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
