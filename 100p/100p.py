"""
100명의 죄수 문제 시뮬레이션

100명의 죄수가 각각 최대 50번의 시도로 자신의 번호를 찾아야 합니다.
두 가지 전략을 비교합니다:
1. 랜덤 전략: 각 죄수가 무작위로 서랍을 선택
2. 전략적 전략: 각 죄수가 자신의 번호로 시작하여 그 서랍의 번호를 따라가는 전략
"""

import random
from typing import List, Tuple


# 상수 정의
PRISONERS = 100
DRAWERS = 100
MAX_ATTEMPTS = 50
MAX_TRIALS = 10000


def create_drawers() -> List[int]:
    """
    서랍 배열을 생성합니다. 각 서랍에는 1부터 DRAWERS까지의 번호가 들어있습니다.
    
    Returns:
        List[int]: 서랍 배열
    """
    return list(range(1, DRAWERS + 1))


def shuffle_drawers(drawers: List[int]) -> List[int]:
    """
    서랍 배열을 무작위로 섞습니다.
    
    Args:
        drawers: 서랍 배열
    
    Returns:
        List[int]: 섞인 서랍 배열
    """
    shuffled = drawers.copy()
    random.shuffle(shuffled)
    return shuffled


def random_strategy(prisoner_num: int, drawers: List[int], max_attempts: int) -> bool:
    """
    랜덤 전략: 죄수가 무작위로 서랍을 선택합니다.
    
    Args:
        prisoner_num: 죄수의 번호
        drawers: 서랍 배열
        max_attempts: 최대 시도 횟수
    
    Returns:
        bool: 죄수가 자신의 번호를 찾았으면 True, 아니면 False
    """
    for _ in range(max_attempts):
        drawer_index = random.randint(0, len(drawers) - 1)
        if drawers[drawer_index] == prisoner_num:
            return True
    return False


def strategic_strategy(prisoner_num: int, drawers: List[int], max_attempts: int) -> bool:
    """
    전략적 전략: 죄수가 자신의 번호로 시작하여 그 서랍의 번호를 따라갑니다.
    이 전략은 순환 구조를 이용하여 성공률이 높습니다.
    
    Args:
        prisoner_num: 죄수의 번호
        drawers: 서랍 배열
        max_attempts: 최대 시도 횟수
    
    Returns:
        bool: 죄수가 자신의 번호를 찾았으면 True, 아니면 False
    """
    current_drawer = prisoner_num - 1  # 0-based index
    
    for _ in range(max_attempts):
        if drawers[current_drawer] == prisoner_num:
            return True
        current_drawer = drawers[current_drawer] - 1  # 다음 서랍으로 이동
    
    return False


def simulate_trial() -> Tuple[bool, bool]:
    """
    한 번의 시뮬레이션을 실행합니다.
    
    Returns:
        Tuple[bool, bool]: (랜덤 전략 성공 여부, 전략적 전략 성공 여부)
    """
    drawers = shuffle_drawers(create_drawers())
    
    random_success = True
    strategic_success = True
    
    for prisoner_num in range(1, PRISONERS + 1):
        if not random_strategy(prisoner_num, drawers, MAX_ATTEMPTS):
            random_success = False
        
        if not strategic_strategy(prisoner_num, drawers, MAX_ATTEMPTS):
            strategic_success = False
    
    return random_success, strategic_success


def run_simulation(trials: int = MAX_TRIALS) -> Tuple[int, int]:
    """
    여러 번의 시뮬레이션을 실행하여 성공률을 계산합니다.
    
    Args:
        trials: 시뮬레이션 실행 횟수
    
    Returns:
        Tuple[int, int]: (랜덤 전략 성공 횟수, 전략적 전략 성공 횟수)
    """
    random_wins = 0
    strategic_wins = 0
    
    for _ in range(trials):
        random_success, strategic_success = simulate_trial()
        
        if random_success:
            random_wins += 1
        
        if strategic_success:
            strategic_wins += 1
    
    return random_wins, strategic_wins


def print_results(trials: int, random_wins: int, strategic_wins: int):
    """
    시뮬레이션 결과를 출력합니다.
    
    Args:
        trials: 시뮬레이션 실행 횟수
        random_wins: 랜덤 전략 성공 횟수
        strategic_wins: 전략적 전략 성공 횟수
    """
    random_rate = (random_wins / trials) * 100
    strategic_rate = (strategic_wins / trials) * 100
    
    print(f"TRIALS: {trials}")
    print(f"  RANDOM= {random_rate:.2f}%   STRATEGY= {strategic_rate:.2f}%")


def main():
    """메인 함수"""
    while True:
        random_wins, strategic_wins = run_simulation(MAX_TRIALS)
        print_results(MAX_TRIALS, random_wins, strategic_wins)
        
        user_input = input("\tFIN = q: ")
        if user_input.lower() == "q":
            break


if __name__ == "__main__":
    main()
