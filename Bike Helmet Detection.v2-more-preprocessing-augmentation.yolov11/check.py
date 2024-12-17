import torch

# Check if CUDA is available
if torch.cuda.is_available():
    print(f"CUDA is available. Device count: {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"Device {i}: {torch.cuda.get_device_name(i)}")
else:
    print("CUDA is not available. Ensure that your GPU drivers and PyTorch are properly installed.")
