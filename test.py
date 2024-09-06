import os
import json
# 指定文件夹路径
# folder_path = '/home/test02/data_domain/deepspeed_data/OCR_VQA/images/'
# # 获取文件夹下所有文件的文件名
# file_names = os.listdir(folder_path)
# with open('/home/test02/data_domain/deepspeed_data/OCR_VQA/dataset_33383.json', 'r') as fp:
#     data = json.load(fp)
# result = {}
# for item in file_names:
#     file_name = item.split(".")[0]
#     result[file_name] = data[file_name]
# with open('/home/test02/data_domain/deepspeed_data/OCR_VQA/dataset.json', 'w') as fp_out:
#     json.dump(result, fp_out, indent=4)  # indent=4 用于美化输出的 JSON 文件，使其更易读


import time
from datetime import datetime

# 记录训练开始时间
start_time = datetime.now()
print(start_time)
print(f"训练开始时间: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

# 模拟训练过程（可以替换为你的训练代码）
time.sleep(5)  # 这里用 sleep 来模拟训练时间

# 记录训练结束时间
end_time = datetime.now()
print(f"训练结束时间: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

# 计算训练时间差
training_time = end_time - start_time
print(f"训练持续时间: {training_time}")


# # 读取原始 JSON 文件
# with open('/home/test02/data_domain/deepspeed_data/OCR_VQA/dataset_copy.json', 'r') as fp:
#     data = json.load(fp)
# # 只提取前5个数据
# data_first_ = dict(list(data.items())[:33383])
# # 将提取的数据存入新的 JSON 文件
# with open('/home/test02/data_domain/deepspeed_data/OCR_VQA/dataset.json', 'w') as fp_out:
#     json.dump(data_first_, fp_out, indent=4)  # indent=4 用于美化输出的 JSON 文件，使其更易读




