# BOJ 14888

# 연산자 우선순위 상관없이 왼쪽에서 오른쪽으로 진행되므로
# 한 방향으로 완전 탐색을 진행한다.

# 남아있는 숫자들의 리스트, 연산자들의 리스트를 인자로 받아
# 가장 왼쪽 두 숫자에 연산자 적용 후 다음 순서를 재귀적으로 처리.

import sys
input = sys.stdin.readline

maxResult = float('-inf')
minResult = float('inf')

def computePart(num1, num2, op):
    if op == 0: # addition
        return num1 + num2
    elif op == 1: # subtraction
        return num1 - num2
    elif op == 2: # multiplication
        return num1 * num2
    elif op == 3: # division (C++14)
        res = abs(num1) // num2
        res = res if num1 >= 0 else -res
        return res

def computeRecursive(numbersRemain, operatorsRemain):

    global maxResult, minResult

    # 1. Input range 확인
    assert len(numbersRemain) == sum(operatorsRemain) + 1
    
    # 2. Base case
    if len(numbersRemain) == 1:
        result = numbersRemain[0]
        if result > maxResult:
            maxResult = result
        if result < minResult:
            minResult = result
        return

    # 3. Recursive step
    # 0: +, 1: -, 2: *, 3: //
    for i in range(4):
        if operatorsRemain[i] >= 1:
            result = computePart(numbersRemain[0], numbersRemain[1], i)
            newNumbers = [result,] + numbersRemain[2:]
            operatorsRemain[i] -= 1
            computeRecursive(newNumbers, operatorsRemain)
            operatorsRemain[i] += 1
    
    return


if __name__ == '__main__':

    # Input
    N = int(input())
    numbers = list(map(int, input().split()))
    # operator sequence: +, -, *, //
    operators = list(map(int, input().split()))

    computeRecursive(numbers, operators)

    print(maxResult, minResult, sep='\n')