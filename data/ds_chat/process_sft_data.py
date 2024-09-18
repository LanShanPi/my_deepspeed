import pandas as pd
import json
import os

# 指定文件夹路径
folder_path = "/home/share/shucshqyfzyxgsi/home/lishuguang/my_deepspeed/data/ds_chat/sft_data/"
# 获取文件夹下的所有文件名
file_names = os.listdir(folder_path)



item = {"wrong_sentence":None,"correct_sentence":None,"wrong_type1":None,"wrong_type2":None}
with open(folder_path+'data.jsonl', 'w',encoding='utf-8',errors='replace') as f:
    for file_name in file_names:
        print(file_name)
        data = pd.read_excel(folder_path+file_name)
        for i in range(len(data)):
            item["wrong_sentence"] = data.iloc[i,0]
            item["correct_sentence"] = data.iloc[i,1]
            item["wrong_type1"] = data.iloc[i,2]
            item["wrong_type2"] = data.iloc[i,3]
            json_line = json.dumps(item,ensure_ascii=False)  # 将字典转换为 JSON 字符串
            f.write(json_line + '\n')  # 每个 JSON 对象写入新的一行



# import pandas as pd
# import json
# import os

# # 指定文件夹路径
# folder_path = "/home/kuaipan/my_deepspeed/data/ds_chat/sft_data/"
# # 获取文件夹下的所有文件名
# file_names = os.listdir(folder_path)

# # 用于存储所有数据的列表
# all_data = []

# for file_name in file_names:
#     # 只处理 Excel 文件
#     if file_name.endswith(('.xlsx', '.xls')):
#         print(f"Processing file: {file_name}")
#         try:
#             data = pd.read_excel(os.path.join(folder_path, file_name))
#             for index, row in data.iterrows():
#                 # 使用数据行的索引来确保列的存在
#                 item = {
#                     "wrong_sentence": row[0] if len(row) > 0 else None,
#                     "correct_sentence": row[1] if len(row) > 1 else None,
#                     "wrong_type1": row[2] if len(row) > 2 else None,
#                     "wrong_type2": row[3] if len(row) > 3 else None
#                 }
#                 all_data.append(item)
#         except Exception as e:
#             print(f"Error processing file {file_name}: {e}")

# # 保存所有数据到一个 JSON 文件
# with open(os.path.join(folder_path, 'data.json'), 'w', encoding='utf-8', errors='replace') as f:
#     json.dump(all_data, f, ensure_ascii=False, indent=4)


