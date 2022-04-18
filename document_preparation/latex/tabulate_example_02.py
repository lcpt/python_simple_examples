from decimal import Decimal

import pandas as pd
from tabulate import tabulate

board_dict = {
    'Done': {
        'point': 0.0,
        'items': 1
    },
    'Doing': {
        'point': 24.0,
        'items': 3
    },
    'New': {
        'point': 0.0,
        'items': 2
    },
    'Stuck': {
        'point': 19.0,
        'items': 3
    },
    'Ready to Test': {
        'point': Decimal('1'),
        'items': 1
    }
}

df = pd.DataFrame(board_dict)

# ASCII output
print(tabulate(df.T, headers="keys"))

# LaTeX output
print('\nLaTeX output:')
print(tabulate(df.T, headers='keys', tablefmt='latex'))
