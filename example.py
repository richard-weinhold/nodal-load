    
from pathlib import Path
import pandas as pd
from dataload_nodal_demand import nodal_demand


nodes = pd.read_csv("nodes.csv", index_col=0)
demand = pd.read_csv("load.csv", header=0)

demand.timestep = pd.to_datetime(demand.timestep, utc=True).astype('datetime64[ns]')
demand.set_index("timestep", inplace=True)

ddir = Path(r"C:\Users\riw\Documents\repositories\nodal_demand") 

d = nodal_demand(ddir, ["DE"], demand, nodes)

