import time
from tqdm import tqdm

# 模拟一个需要进行迭代的任务，例如处理数据或训练模型
def process_data(num_items):
    for i in tqdm(range(num_items), desc="Processing"):
        # 模拟处理每个项目的任务
        time.sleep(0.1)  # 假装处理任务需要一定时间

# 设置要处理的项目数
num_items = 100

# 调用处理数据的函数并显示进度条
process_data(num_items)
