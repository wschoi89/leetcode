prices = [1, 0, 2, 1, 0, 3, 2, 1]


def maxProfit(prices) -> int:
    low_price = prices[0]

    max_profit = 0

    for i in range(1, len(prices)):
        high_price = prices[i]

        profit = high_price - low_price

        if profit >=max_profit:
            max_profit = profit

        if low_price > high_price:
            low_price = high_price

    return max_profit


