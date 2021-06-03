import pandas as pd
import numpy as np
import math
from datetime import datetime, date
import os, sys
import  time

Actions =['r','G']
def build_q_table(step, actions):
    table = pd.DataFrame(
        np.zeros((step, len(actions))),   # q_table initial values
        columns=actions,    # actions's name
    )
    return table
print(build_q_table(1200,Actions).iloc[0,0])
