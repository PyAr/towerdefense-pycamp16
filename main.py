
import random
import time

import core

locations = core.get_available_locations()
r_loc = random.choice(locations)

kinds = core.get_tower_types()
r_kind = random.choice(kinds)

test = {r_loc: r_kind}

tini = time.time()
score = core.start(test, drawing=True)
delta = time.time() - tini
print("Finished! Score: {} (took {:.3f})".format(score, delta))
input("Press any key to continue")
