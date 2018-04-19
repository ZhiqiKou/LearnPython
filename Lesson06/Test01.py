# 基本统计值计算

# 获取用户输入的数字
def getNum():
    nums = []
    iNumStr = input("请输入数字（回车退出）：")
    while iNumStr != '':
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）：")
    return nums

# 求平均数
def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s + num
    return s/len(numbers)

# 求方差
def dev(numbers,mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev/(len(numbers) - 1), 0.5)

# 求中位数
def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size // 2 - 1] + numbers[size // 2]) / 2
    else:
        med = numbers[size // 2]
    return med

n = getNum()
m = mean(n)
print("平均数：{}，方差：{:.2}，中位数：{}".format(m, dev(n, m), median(n)))