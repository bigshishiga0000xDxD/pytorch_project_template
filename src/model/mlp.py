from torch import nn
from torch.nn import Sequential

from src.model import BaseModel


class MLPModel(BaseModel):
    """
    Simple MLP
    """

    def __init__(self, n_feats, n_class, fc_hidden=512):
        """
        Args:
            n_feats (int): number of input features.
            n_class (int): number of classes.
            fc_hidden (int): number of hidden features.
        """
        super().__init__()

        self.net = Sequential(
            # people say it can approximate any function...
            nn.Linear(in_features=n_feats, out_features=fc_hidden),
            nn.ReLU(),
            nn.Linear(in_features=fc_hidden, out_features=fc_hidden),
            nn.ReLU(),
            nn.Linear(in_features=fc_hidden, out_features=n_class),
        )

    def forward(self, data_object, **batch):
        """
        Model forward method.

        Args:
            data_object (Tensor): input vector.
        Returns:
            output (dict): output dict containing logits.
        """
        return {"logits": self.net(data_object)}
