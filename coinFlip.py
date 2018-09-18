import random
import time

start = time.time()

heads = 0
tails = 0
flipped = 0

amountFlipped = 0

while amountFlipped < 10000000:
    flipped = random.randint(0,1)
    if flipped == 0:
        heads += 1
    else:
        tails += 1
    amountFlipped += 1

end = time.time()

print('Heads was printed ' + str(heads) + ' times and tails was printed ' + str(tails) + ' times.')
print('The average was ' + str(round((heads / amountFlipped) * 100, 2)) + '%.')
print('This took ' + str(round(end - start, 2)) + ' seconds to figure out.')
