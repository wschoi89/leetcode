temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# output = [1, 1, 1, 0]


def dailyTemperatures(temperatures):

    result = [0] * len(temperatures)
    for i, t in enumerate(temperatures):
        for j in range(i+1, len(temperatures)):
            if temperatures[j] > t:
                result[i] = j - i
                break

    print(result)

dailyTemperatures(temperatures)





