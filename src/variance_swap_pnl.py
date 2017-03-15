import numpy as np
import pandas as pd


def generate_pnl(spx, vix, N=30):
    vol = (vix/100)**2  # convert percentage into float points and volatility to variance
    spx_ret = np.log(spx/spx.shift(1))
    vol_diff = vol.diff()
    return (252*spx_ret**2 - vol)/N + vol_diff

