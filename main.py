
import random
import time

import core

QUANT = 7

locations = core.get_available_locations()
random.shuffle(locations)
r_loc = locations[:QUANT]

kinds = core.get_tower_types()
random.shuffle(kinds)
r_kind = kinds[:QUANT]

test = {l: k for l, k in zip(r_loc, r_kind)}


tini = time.time()
score = core.start(test, drawing=True)
delta = time.time() - tini
print("Finished for {} quant! Score: {} (took {:.3f})".format(QUANT, score, delta))
input("Press any key to continue")
