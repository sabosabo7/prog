#%%
import numpy as np
import glob
#%%

for l in glob.glob("*.npy"):
    tmp=np.load(l)
    np.savez_compressed(l.split(".")[0],tmp)
