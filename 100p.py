"""
100명의 죄수 문제 시뮬레이션

100명의 죄수가 각각 최대 50번의 시도로 자신의 번호를 찾아야 합니다.
두 가지 전략을 비교합니다:
1. 랜덤 전략: 각 죄수가 무작위로 서랍을 선택
2. 전략적 전략: 각 죄수가 자신의 번호로 시작하여 그 서랍의 번호를 따라가는 전략

def play_random(n):
def play_optimal(n):

"""

import random

def play_random(n):
    # using 0-99 instead of ranges 1-100
    pardoned = 0
    in_drawer = list(range(100))
    sampler = list(range(100))
    for _round in range(n):
        random.shuffle(in_drawer)
        found = False
        for prisoner in range(100):
            found = False
            for reveal in random.sample(sampler, 50):
                card = in_drawer[reveal]
                if card == prisoner:
                    found = True
                    break
            if not found:
                break
        if found:
            pardoned += 1
    return pardoned / n * 100   # %

def play_optimal(n):
    # using 0-99 instead of ranges 1-100
    pardoned = 0
    in_drawer = list(range(100))
    for _round in range(n):
        random.shuffle(in_drawer)
        for prisoner in range(100):
            reveal = prisoner
            found = False
            for go in range(50):
                card = in_drawer[reveal]
                if card == prisoner:
                    found = True
                    break
                reveal = card
            if not found:
                break
        if found:
            pardoned += 1
    return pardoned / n * 100   # %

if __name__ == '__main__':
    n = 100_000
    print(" Simulation count:", n)
    print(f" Random play wins: {play_random(n):4.1f}% of simulations")
    print(f"Optimal play wins: {play_optimal(n):4.1f}% of simulations")