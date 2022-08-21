import argparse
import cv2
import torch
import numpy as np

from utils import get_device
from utils import fix_rnd
from utils import check_dir
from utils import make_dir
from utils import norm_dir


def parse_args():
    parser = argparse.ArgumentParser()
    return parser.parse_args()


def main():
    cfg = parse_args()


if __name__ == '__main__':
    main()
