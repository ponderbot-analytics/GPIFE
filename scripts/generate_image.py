from diffusers import AutoPipelineForText2Image
import torch

class TextToImageGenerator:
    def __init__(self, pretrained_model_path, lora_weight_path):
        self.pretrained_model_path = pretrained_model_path
        self.lora_weight_path = lora_weight_path
        self.pipeline = None

    def load_weight(self):
        self.pipeline = AutoPipelineForText2Image.from_pretrained(self.pretrained_model_path, torch_dtype=torch.float16).to("cuda")
        self.pipeline.load_lora_weights(self.lora_weight_path, weight_name="pytorch_lora_weights.safetensors")

    def generate_image(self, prompt, num_inference_steps):
        if self.pipeline is None:
            raise ValueError("The pipeline has not been loaded. Call load_weight() first.")
        image = self.pipeline(prompt, num_inference_steps=num_inference_steps).images[0]
        return image



