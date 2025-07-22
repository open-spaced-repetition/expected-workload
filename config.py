import numpy as np
import matplotlib.pyplot as plt
from fsrs_optimizer import DEFAULT_PARAMETER  # type: ignore
from tqdm.auto import tqdm

learn_days = 365
S_MIN = 0.001
FORGET_COST = 23.185
RECALL_COST = 7.8454
LEARN_COST = 19.4698
R_RANGE = np.arange(0.5, 0.99, 0.01)
