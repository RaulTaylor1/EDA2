import pandas as pd
import numpy as np
import re


def extraer_gb(ram):
    pattern_ram = r'(\d+\.?\d*)\s*(GB|MB)?'
    match_ram = re.match(pattern_ram, ram)
    if match_ram:
        numero = float(match_ram.group(1))
        unidad = match_ram.group(2)
        if unidad == 'MB':
            return numero / 1000 
        return numero
    return 0.0


