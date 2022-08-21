import torch
import numpy
import random
import errno
import os


# Get PyTorch device
def get_device():
    return "cuda" if torch.cuda.is_available() else "cpu"


# Fix randomization for PyTorch/Numpy
def fix_rnd(seed=7):
    # for numpy randomness
    numpy.random.seed(seed)
    # for randomness in image augmentation
    random.seed(seed)
    # every PyTorch thing can be fixed with these two lines
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


# Check if directory exist
def check_dir(src):
    if os.path.isdir(src) is False:
        raise FileNotFoundError(
            errno.ENOENT, os.strerror(errno.ENOENT), src)


# Make a directory
def make_dir(src):
    try:
        os.makedirs(src, exist_ok=True)
    except OSError:
        print(f"Could not create {src}.")
        os.exit()


# Normalize a path of directory
def norm_dir(src):
    dst = os.path.normpath(src)
    dst = os.path.join(dst, "")
    return dst
