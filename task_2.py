def countCows(n):
    count = 1
    inc = 1  # increment
    for i in range(2, n):
        if n < 3:
            # print("Breaking")
            break
        if i % 4 == 0:
            print("Multiplying")
            inc = inc*2
        count += inc
    return count

countCows(1)
countCows(3)
countCows(4)
countCows(5)
countCows(6)
countCows(7)
countCows(10)