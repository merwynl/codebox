'''

Exception handling - An event that interrupts the flow of a program
                   - (ZeroDivision, TypeError, ValueError)
                   - Try, Except, Finally

'''

# Try's & excepts are useful for catching any potential errors & prevents a program from crashing.
try:
    # answer = 10/0
    number = int(input('数字を入力してください: '))
    print(1 / number)

# Without a specified clause, it will catch any and all errors. ZeroDivisionError catches if a return value is 0.
except ZeroDivisionError as err:
    print('ゼロから割れ切れています')

# Without a specified clause, it will catch any and all errors.
except ValueError:
    print('申し訳ございます。それは数字ではありません!')

# Catches all exceptions. Considered bad practice as it's too broad and vague. Last resort.
except Exception:
    print("Something went wrong.")

# Always executes. Usually used to perform cleanup operations. Not always used.
finally:
    print("Do some clean up here.")


