import sys
import torch
from time import sleep

def debug_print(name, tensor):
    try:
        print(f"{name}: shape={tensor.shape}, dtype={tensor.dtype}, ", end='')
    except:
        print(f"ERROR: debug-print failed for tensor {name} on shape/dtype", file=sys.stderr)
    try:
        print(f"device={tensor.device}, ", end='')
    except:
        print(f"ERROR: debug-print failed for tensor {name} on device", file=sys.stderr)
    try:
        print(f"min={tensor.min().item():.4f}, max={tensor.max().item():.4f}, ", end='')
    except:
        print(f"ERROR: debug-print failed for tensor {name} on min/max", file=sys.stderr)
    try:
        print(f"mean={tensor.mean().item():.4f}, median={tensor.median().item():.4f}, ", end='')
    except:
        print(f"ERROR: debug-print failed for tensor {name} on mean/median", file=sys.stderr)
    try:
        print(f"has_nan={tensor.isnan().any().item()}, ", end='')
    except:
        print(f"ERROR: debug-print failed for tensor {name} on isnan", file=sys.stderr)
    try:
        print(f"has_inf={tensor.isinf().any().item()}")
    except:
        print(f"ERROR: debug-print failed for tensor {name} on isinf", file=sys.stderr)

# test tensors
tensors = [
    torch.tensor(3.14),                                  # scalar
    torch.randn(3, 4),                                   # normal 2D
    torch.zeros(2, 3, 4),                                # zeros 3D
    torch.ones(5),                                       # ones 1D
    torch.arange(10, dtype=torch.int32),                 # int dtype
    torch.randn(2, 2).to(torch.float16),                 # fp16
    torch.randn(4, 4, device='cuda' if torch.cuda.is_available() else 'cpu'),
    torch.tensor([1.0, float('nan'), 3.0]),              # has NaN
    torch.tensor([1.0, float('inf'), -float('inf')]),    # has Inf
    torch.tensor([-1e10, 0.0, 1e10]),                    # extreme range
    torch.empty(0),                                      # empty (will crash min/max/median)
    torch.randn(1, 1, 1, 1),                             # 4D
    torch.tensor([[True, False], [False, True]]),        # bool (min/max may fail)
    torch.randn(100, 100) * 1e6,                         # large scale
    torch.randperm(10),                                  # int64 permutation
]

for idx, t in enumerate(tensors):
    sleep(3)
    debug_print(f"Tensor ({idx})", t)