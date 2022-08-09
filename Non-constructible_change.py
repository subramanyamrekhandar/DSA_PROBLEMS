def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()

    currentChangeValue = 0

    for coin in coins:
        if coin > currentChangeValue + 1:
            return currentChangeValue +1
        currentChangeValue += coin    
    return currentChangeValue + 1
