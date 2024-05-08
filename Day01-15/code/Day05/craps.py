"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
from random import randint

guest_init = 0
host_init = 0
round = 1000000

import time
from tqdm import tqdm


# 模拟一个需要进行迭代的任务，例如处理数据或训练模型
def process_data(guest, host, num_items):
    for i in tqdm(range(num_items), desc="Processing"):
        first = randint(1, 6) + randint(1, 6)
        if first == 7 or first == 11:
            guest += 1
        elif first == 2 or first == 3 or first == 12:
            host += 1
        else:
            while True:
                current = randint(1, 6) + randint(1, 6)
                if current == 7:
                    host += 1
                    break
                elif current == first:
                    guest += 1
                    break
    print("玩家赢的概率为：%.2f" % (guest / round))
    print("庄家赢的概率为：%.2f" % (host / round))


# 调用处理数据的函数并显示进度条
process_data(guest_init, host_init, round)

money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= debt
    else:
        needs_go_on = True

    while needs_go_on:
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
            needs_go_on = False
        elif current == first:
            print('玩家胜')
            money += debt
            needs_go_on = False

print('你破产了, 游戏结束!')
