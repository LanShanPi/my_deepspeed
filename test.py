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





# # 读取原始 JSON 文件
# with open('/home/test02/data_domain/deepspeed_data/OCR_VQA/dataset_33382.json', 'r') as fp:
#     data = json.load(fp)
# # 只提取前5个数据
# data_first_ = dict(list(data.items())[:1000])
# # 将提取的数据存入新的 JSON 文件
# with open('/home/test02/data_domain/deepspeed_data/OCR_VQA/dataset.json', 'w') as fp_out:
#     json.dump(data_first_, fp_out, indent=4)  # indent=4 用于美化输出的 JSON 文件，使其更易读


import os
import numpy as np
from datasets import load_dataset,load_from_disk
from torch.utils.data import Subset

def get_shuffle_idx(seed, size):
    # 随机打乱
    np_rng = np.random.RandomState(seed=seed)
    dtype_ = np.uint32
    if size >= (np.iinfo(np.uint32).max - 1):
        dtype_ = np.int64
    shuffle_idx = np.arange(start=0, stop=size, step=1, dtype=dtype_)
    np_rng.shuffle(shuffle_idx)
    return shuffle_idx


def get_raw_dataset_split_index(
                                dataset_name,
                                data_size,
                                rebuild=False,
                                local_rank=None,
                                seed=1,
                                data_split="9,1",
                                split_index=0,
                                split_name="train_eval",
                                output_path="/"):
    index_file_name = f"{output_path}/{dataset_name}_seed{seed}_{split_name}_{data_split}_{split_index}.npy"
    # reindex each time when using local jsonfile since it's more likely to get modified
    if rebuild or (not os.path.isfile(index_file_name)) or (dataset_name
                                                            == 'jsonfile'):
        splits = [float(s) for s in data_split.split(',')]
        splits_sum = sum(splits)
        splits = [split / splits_sum for split in splits]
        splits_index = [0]
        for index, split in enumerate(splits):
            splits_index.append(splits_index[index] +
                                int(round(split * float(data_size))))
        diff = splits_index[-1] - data_size
        for index in range(1, len(splits_index)):
            splits_index[index] -= diff
        assert splits_index[-1] == data_size

        shuffle_idx = get_shuffle_idx(seed, data_size)
        for split_i in range(len(splits)):
            shuffle_idx_split_file_name = f"{output_path}/{dataset_name}_seed{seed}_{split_name}_{data_split}_{split_i}.npy"
            shuffle_idx_split = shuffle_idx[
                splits_index[split_i]:splits_index[split_i + 1]]
            np.save(shuffle_idx_split_file_name,
                    shuffle_idx_split,
                    allow_pickle=True)
    index = np.load(index_file_name, allow_pickle=True)
    return index.tolist()

class PromptRawDataset(object):
    def __init__(self, output_path, seed, local_rank, dataset_name,my_data=True):
        self.output_path = output_path
        self.seed = seed
        self.local_rank = local_rank
        if os.path.exists(dataset_name):
            if my_data:
                #############还需要再修改##################
                # 加载本地数据
                self.raw_datasets = load_dataset('json', data_files=dataset_name)
            else:
                self.raw_datasets = load_from_disk(dataset_name)
        elif not dataset_name == 'local/jsonfile':
            self.raw_datasets = load_dataset(dataset_name)

    def get_train_data(self):
        return

    def get_eval_data(self):
        return

    # The prompt should be in the format of: " Human: " + actual_prompt_sentence + " Assistant:"
    def get_prompt(self, sample):
        return

    # The chosen response should be in the format of: " " + actual_response_sentence
    def get_chosen(self, sample):
        return

    # The rejected response should be in the format of: " " + actual_response_sentence
    # If the dataset does not have rejected response, return None
    def get_rejected(self, sample):
        return

    def get_prompt_and_chosen(self, sample):
        return

    def get_prompt_and_rejected(self, sample):
        return


class MyMtlDataset(PromptRawDataset):
    def __init__(self,):
        self.dataset_name = "/home/kuaipan/my_deepspeed/output.jsonl"
        self.dataset_name_clean = "/home/kuaipan/my_deepspeed/output.jsonl"
        self.raw_datasets = load_dataset('json', data_files=self.dataset_name)
    def get_train_data(self):
        dataset = self.raw_datasets["train"]
        index = get_raw_dataset_split_index(dataset_name=self.dataset_name_clean,
                                            data_size=len(dataset))
        print(dataset)
        # print(index)
        dataset = Subset(dataset, index)
        return dataset


test_item = MyMtlDataset()
print(test_item.get_train_data())