import pandas as pd
import json

data = pd.read_excel("test.xlsx")
item = {"wrong_sentence":None,"correct_sentence":None,"wrong_type1":None,"wrong_type2":None}
with open('output.jsonl', 'w') as f:
    for i in range(len(data)):
        item["wrong_sentence"] = data.iloc[i,0]
        item["correct_sentence"] = data.iloc[i,1]
        item["wrong_type1"] = data.iloc[i,2]
        item["wrong_type2"] = data.iloc[i,3]
        json_line = json.dumps(item,ensure_ascii=False)  # 将字典转换为 JSON 字符串
        f.write(json_line + '\n')  # 每个 JSON 对象写入新的一行


