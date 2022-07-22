import asyncio

import matplotlib.pyplot as plt
import numpy as np

# source to riddle video: https://www.youtube.com/watch?v=iSNsgj1OCLA

passed = 0
passedArr = []


async def sim() -> bool:
    boxes = np.arange(1, 101)
    np.random.shuffle(boxes)
    found = []
    for prisoner in range(100):
        tries = 0
        num = boxes[prisoner]
        while tries < 50:
            if num == prisoner:
                found.append(True)
                print(
                    f"Prisoner {prisoner} found their number.")
                break
            else:
                print(
                    f"Prisoner {prisoner} did not find their number. They have {50 - tries} tries(try) left.")
                num = boxes[num - 1]
            if tries == 49:
                found.append(False)
            tries += 1
    if len(found) < 99:
        pass
    elif False not in found:
        print("EVERYONE PASSED!!!")
        passed += 1
        passedArr.append(passed)
    else:
        print(f"FAILED. {found.count(True)} fround their numbers")
        passedArr.append(passed)

if __name__ == "__main__":
    numStr = input("How many times should the simulation be run? ")
    num = int(numStr)
    for i in range(num):
        asyncio.run(sim())
    print(len([i for i in range(1, num)]))
    print(len(passedArr))
    plt.plot([i for i in range(1, num)], passedArr)
