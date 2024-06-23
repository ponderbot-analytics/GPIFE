
# Generating Product Image for E-commerce

Build a model to generate the high quality product image for e-commerce from a given prompt


## Dataset
This repository used the cloth [dataset](https://huggingface.co/datasets/hahminlew/kream-product-blip-captions) to fine-tune the stable diffusion model.
## Results

### 1. Pre-trained Distilled Stable Diffusion Model  

![1](https://github.com/ponderbot-analytics/GPIFE/assets/163169121/018f67ec-7b38-44b2-9f8e-d3a0c6147f06)

### 2. Fine-Tuned Distilled Stable Diffusion Model  

![2](https://github.com/ponderbot-analytics/GPIFE/assets/163169121/dd6f80fd-d018-4d05-9ac6-b4259317f4a5)  

### 3. Fine-Tuned Distilled Stable Diffusion Model With Hyperparameter Optimization  

![3](https://github.com/ponderbot-analytics/GPIFE/assets/163169121/92379078-40a2-4192-a7b8-d1a8b711e0b9)  

### 4. Fine-Tuned ControlNet Stable Diffusion Model  

![4](https://github.com/ponderbot-analytics/GPIFE/assets/163169121/6c93634b-8528-421f-b225-872491dda2b5)  

![5](https://github.com/ponderbot-analytics/GPIFE/assets/163169121/14fdbd23-2f1e-47f7-a6e9-c1bd432cd927)  

### 5. Fine-Tuned Model With LoRA Technique  

![6](https://github.com/ponderbot-analytics/GPIFE/assets/163169121/a354a75c-d258-46aa-8766-48610a28a842)  

### 6. Evaluation of Different Model  

![metric](https://github.com/ponderbot-analytics/GPIFE/assets/163169121/d0d06c76-0500-4c05-a93b-45d217ee71b7)  
Higher the CLIP scores imply better the performance of model to generate high quality image
## Installation

Install the repository

```bash
pip install git+https://github.com/ponderbot-analytics/GPIFE.git
```
    
## Inference

Import the TextToImageGenerator class
```bash
from scripts.inference import TextToImageGenerator
```

Download the model weight ([pretrained model weights](https://drive.google.com/drive/folders/1oCSQ4Skdm5FjwnsTr1Mj8fp0U3HVsvRO) and [lora weight](https://drive.google.com/drive/folders/1t3IE_nQlZ_eaMBmrv8t6r5AtbYCPgAxa)) 

Create the text_to_image object

```bash
text_to_image = TextToImageGenerator(pretrained_model_path, lora_weight_path)
```

Load the weights
```bash
text_to_image.load_weight()
```

Generate the image by providing the prompt
```bash
image = text_to_image.generate_image(prompt)
```
## Training

Clone the repository

```bash
git clone https://github.com/ponderbot-analytics/GPIFE.git
```

Go to the GPIFE directory

```bash
cd GPIFE
```

Install dependencies

```bash
pip install -r requirements.txt
```

Go to the script directory

```bash
cd scripts
```

Run the train.py script

```bash
accelerate launch train.py \
  --pretrained_model_name_or_path=$model_path \
  --mixed_precision="fp16" \
  --resolution=512 \
  --dataset_name=$dataset_path \
  --train_batch_size=1 \
  --num_train_epochs=5 \
  --learning_rate=1e-06 \
  --output_dir=$output_dir_path \
  --checkpointing_steps=1000 \
  --center_crop \
  --random_flip \
```

