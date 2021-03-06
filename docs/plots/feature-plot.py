import tidyms as ms
from bokeh import plotting
import numpy as np
plotting.output_file("example.html")

data = ms.fileio.load_dataset("reference-materials")

# search [M+H]+ from trp in the features
mz = 205.097
rt = 124
# get a list of features compatible with the given m/z and rt
ft_name = data.select_features(mz, rt)

data.plot.feature(ft_name[0])
