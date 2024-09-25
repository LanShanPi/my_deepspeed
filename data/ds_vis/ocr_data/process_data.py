import os
import json

# 指定要读取的文件夹路径
folder_path = '/root/my_deepspeed/data/ds_vis/ocr_data/images'

# 获取文件夹中所有文件的名字
file_names = os.listdir(folder_path)



# 指定 JSON 文件的路径
dataset_path = '/root/my_deepspeed/data/ds_vis/ocr_data/dataset.json'

# 读取 JSON 文件
with open(dataset_path, 'r', encoding='utf-8') as file:
    data = json.load(file)


# 根据images中的文件截取data.json中的数据
result = {}
for file_name in file_names:
    item_name = file_name.split(".")[0]
    result[item_name] = data[file_name]


json_file_path = '/root/my_deepspeed/data/ds_vis/ocr_data/dataset_10000.json'
# 将字典保存为 JSON 文件
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)