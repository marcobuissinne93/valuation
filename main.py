from st_aggrid import AgGrid
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(df)

# import pandas as pd
# import sqlite3
# from typing import Dict, List
# con = sqlite3.connect("db.sqlite3")

# VAR_DIST: Dict[str, float] = {
#     'type': [1, 1, 1, 1, 1],
#     'status': ['fail', 'bad', 'average', 'good', 'great'],
#     'cagr': [-0.1, 0.1, 0.2, 0.4, 0.6],
#     'init_man_fees': [300_000, 300_000, 600_000, 800_000, 1_000_000],
#     'dist': [0.05, 0.15, 0.35, 0.35, 0.1],
#     'roi': [0, 2, 5, 10, 20]
# }


# df = pd.DataFrame(VAR_DIST)

# df.to_sql('test', con, if_exists='replace')

