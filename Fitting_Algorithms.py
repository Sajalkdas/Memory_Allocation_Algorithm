from random import randint


def firstFit(blockSize, numOfBlocks, processSize, numOfProcess):
    original_blockSize = blockSize[:]      # Stores original block sizes for display

    allocation = [-1] * numOfProcess       # Stores block no. of the allocated process

    for i in range(numOfProcess):
        for j in range(numOfBlocks):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j                   # allocate block j to p[i] process
                blockSize[j] -= processSize[i]      # Reduce available memory in this block
                break

    print("\nFirst Fit Allocation")
    print("Initial Block Sizes: ", original_blockSize)
    print("Block Sizes after Allocation: ", blockSize)
    print("\nProcess No.    Process Size    Block No.")
    for i in range(numOfProcess):
        print(f"     {i + 1}            {processSize[i]}           ", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


def bestFit(blockSize, numOfBlocks, processSize, numOfProcess):
    original_blockSize = blockSize[:]       # Store original block sizes for display purposes

    allocation = [-1] * numOfProcess        # Stores block id of the block allocated to a process

    for i in range(numOfProcess):
        best_idx = -1
        for j in range(numOfBlocks):
            if blockSize[j] >= processSize[i]:
                if best_idx == -1 or blockSize[best_idx] > blockSize[j]:
                    best_idx = j

        # If we found a block for current process
        if best_idx != -1:
            allocation[i] = best_idx        # allocate best_idx block to p[i] process

            blockSize[best_idx] -= processSize[i]   # Reduce available memory in this block.

    print("\nBest Fit Allocation")
    print("Initial Block Sizes: ", original_blockSize)
    print("Block Sizes after Allocation: ", blockSize)
    print("\nProcess No.    Process Size    Block No.")
    for i in range(numOfProcess):
        print(f"     {i + 1}            {processSize[i]}           ", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


def worstFit(blockSize, numOfBlock, processSize, numOfProcess):
    original_blockSize = blockSize[:]       # Store original block sizes for display purposes

    allocation = [-1] * numOfProcess        # Stores block id of the block allocated to a process

    for i in range(numOfProcess):
        worst_idx = -1
        for j in range(numOfBlock):
            if blockSize[j] >= processSize[i]:
                if worst_idx == -1 or blockSize[worst_idx] < blockSize[j]:
                    worst_idx = j

        # If we found a block for current process
        if worst_idx != -1:
            allocation[i] = worst_idx       # allocate worst_idx block to p[i] process

            blockSize[worst_idx] -= processSize[i]  # Reduce available memory in this block.

    print("\nWorst Fit Allocation")
    print("Initial Block Sizes: ", original_blockSize)
    print("Block Sizes after Allocation: ", blockSize)
    print("\nProcess No.    Process Size    Block No.")
    for i in range(numOfProcess):
        print(f"     {i + 1}            {processSize[i]}           ", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


if __name__ == '__main__':
    blockSize = [1600000, 1000000, 3000000, 1500000, 5000000, 3500000, 6000000, 2400000, 2800000, 1200000, 4000000]
    processSize = [randint(20000, 2000000) for _ in range(10)]
    numOfBlocks = len(blockSize)
    numOfProcess = len(processSize)

    firstFit(blockSize[:], numOfBlocks, processSize, numOfProcess)  # Apply First Fit

    bestFit(blockSize[:], numOfBlocks, processSize, numOfProcess)   # Apply Best Fit

    worstFit(blockSize[:], numOfBlocks, processSize, numOfProcess)  # Apply Worst Fit
