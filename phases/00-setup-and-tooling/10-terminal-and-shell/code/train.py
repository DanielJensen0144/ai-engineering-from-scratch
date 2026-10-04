import sys
from time import sleep

if len(sys.argv) == 2:
    reps = sys.argv[1]
else:
    reps = 1

for rep in reps:
    sleep(12)
    print("Epoch 1/3 - loss: 2.4531")

    sleep(10)
    print("Epoch 2/3 - loss: 1.6543")
    print("ERROR: something went wrong on epoch 2", file=sys.stderr)

    sleep(12)
    print("Epoch 3/3 - loss: 0.8765")
    print("Training complete. final_accuracy=0.9421")
