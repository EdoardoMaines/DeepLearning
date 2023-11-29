import os
import argparse
from easydict import EasyDict
from tensorboardX import SummaryWriter
import pprint
import time
import datetime
import torch
import json
import math
import torch.nn.functional as F

class DeCLIP():
    