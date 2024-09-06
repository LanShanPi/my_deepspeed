#!/bin/bash
# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0
# DeepSpeed Team

#EVAL_DATSET=eval_robustness  eval_single eval_comprehensive (see the json in the folder ./eval_data/*.json)
MAIN_PATH=/home/test02/my_deepspeed/applications/DeepSpeed-VisualChat/training/output/Epoch6_LR1e-3_data_ocr_vqa_all_3_2_1_1_1_1_1_1_1/
# VISION_MODEL=/blob/transformers_cache/qwen-clip #openai/clip-vit-large-patch14
# LLM=/blob/transformers_cache/Llama-2-13b-hf #meta-llama/Llama-2-7b 
VISION_MODEL=/home/test02/model_domain/deepspeed_model/clip-vit-large-patch14
LLM=/home/test02/model_domain/deepspeed_model/Llama-2-7b-hf
for EVAL_DATSET in eval_single eval_comprehensive eval_robustness 
do
    SAVE_PATH=eval/results/${EVAL_DATSET}
    mkdir ${SAVE_PATH}
    # for CKPT_NAME in final best_eval
    for CKPT_NAME in epoch-2
    do
    #NOTE: to run multi-GPU, you simple do "export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7;"
    export CUDA_VISIBLE_DEVICES=0; python eval/batch_generation.py --model_name dsvl --vis_proj baseline --max_seq_len 4096 \
        --lm_model_name_or_path  ${LLM} --vision_model_name_or_path ${VISION_MODEL} \
        --checkpoint_path $MAIN_PATH  --checkpoint_names $CKPT_NAME --eval_data ${EVAL_DATSET} \
        --enable_mmca_attention --output_filename ${SAVE_PATH}/ours_${CKPT_NAME} &> ${SAVE_PATH}/ours_${CKPT_NAME}.log
    done
done

