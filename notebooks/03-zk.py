import os
import torch
import json
import onnxruntime as ort
import numpy as np
import ezkl
import asyncio

# Set working directory

print("Current working directory:", os.getcwd())
os.environ["ENABLE_ICICLE_GPU"] = "true"

# Define paths
model_path = "Model/best_kyc_siamese.onnx"
settings_path = "zk/settings.json"
compiled_model_path = "zk/network.compiled"
pk_path = "zk/key.pk"
vk_path = "zk/key.vk"
witness_path = "zk/witness.json"
data_path = "zk/input.json"

# Create zk directory
os.makedirs("zk", exist_ok=True)


res = ezkl.setup(compiled_model_path, vk_path, pk_path)
print("Setup completed:", res)

