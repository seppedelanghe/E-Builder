from ebuilder.examples.planets import env as planet_env
from ebuilder.examples.spaceship import env as space_env
from ebuilder.examples.bounce import env as bounce_env
from ebuilder.examples.reuse import env as reuse_env
from ebuilder.examples.edge import env as edge_env
from ebuilder.examples.removal import env as removal_env
from ebuilder.examples.springs import env as spring_env
from ebuilder.examples.simple import env as simple_env

from ebuilder.examples.nodrawing import env as nodrawing_env


# planet_env.start()
# space_env.start()
# bounce_env.start()
# reuse_env.start()
# edge_env.start()
# removal_env.start()
# spring_env.start()
# simple_env.start()

import time

# Run without visuals
start = time.time()
nodrawing_env.start()
end = time.time()
elapsed = end - start

# Run with visuals
nodrawing_env.drawVisuals = True

start = time.time()
nodrawing_env.start()
end = time.time()
elapsed2 = end - start

print("With drawing: {}s, without drawing: {}s.".format(elapsed2, elapsed))