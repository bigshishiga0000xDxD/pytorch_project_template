import torch
from torch import nn


class Loss(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, **batch):
        return {"loss": None}
