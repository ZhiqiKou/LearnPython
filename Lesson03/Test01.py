import time

for i in range(101):
    print("\r{:=^50}".format(str(i) + '%'),end = '')
    time.sleep(0.1)
