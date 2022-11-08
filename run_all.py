from itertools import product
import os
import time

# envs = [
#     "antmaze-umaze-v0",
#     "antmaze-umaze-diverse-v0",
#     "antmaze-medium-diverse-v0",
#     "antmaze-medium-play-v0",
# ]
envs = [
    "hopper-medium-replay-v2",
    "walker2d-medium-replay-v2",
    "halfcheetah-medium-replay-v2",
    "hopper-medium-v2",
    "walker2d-medium-v2",
    "halfcheetah-medium-v2",
    "hopper-medium-expert-v2",
    "walker2d-medium-expert-v2",
    "halfcheetah-medium-expert-v2",
]
# envs = [
#     "antmaze-large-play-v0",
#     "antmaze-large-diverse-v0",
# ]
seeds = range(10)
cuda_devs = [0, 1, 6, 7]

for i, (s, e) in enumerate(product(seeds, envs)):
    if i == 32:
        break
    os.system(f"python -m SimpleSAC.conservative_sac_main --logging.output_dir './experiment_output' --seed {s} --env {e} --device cuda:{cuda_devs[i % 4]} > {i}.out 2>&1&")
    if not (i + 1) % 16:
        time.sleep(60 * 60 * 9)


