def calculator(expression: list) -> int:
    cleaned_expression = ''.join(expression)
    cleaned_expression = ''.join(
        i for i in cleaned_expression if not i.isalpha()
        )
    return eval(cleaned_expression)


if __name__ == "__main__":
    print('Hello, please enter regular arithmetic expression:')
    expression = input().split()
    print(calculator(expression))
