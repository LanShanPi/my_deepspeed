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





# 读取原始 JSON 文件
with open('/home/test02/data_domain/deepspeed_data/OCR_VQA/dataset_33382.json', 'r') as fp:
    data = json.load(fp)
# 只提取前5个数据
data_first_ = dict(list(data.items())[:1000])
# 将提取的数据存入新的 JSON 文件
with open('/home/test02/data_domain/deepspeed_data/OCR_VQA/dataset.json', 'w') as fp_out:
    json.dump(data_first_, fp_out, indent=4)  # indent=4 用于美化输出的 JSON 文件，使其更易读




