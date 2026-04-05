class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        minimizer = init
        for _ in range(iterations):
            derivative = 2 * minimizer #error was using const value of init as instead of updating each step
            minimizer = minimizer - learning_rate * derivative
        return round(minimizer,5)