class CustomZeroDivisionError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.result = kwargs.get('result')

    def __str__(self):
        return f'{super().__str__()}, result: {self.result}'


class SecondCustomZeroDivisionError(CustomZeroDivisionError):
    pass


def normalize(a, b):
    try:
        sum = a + b
        return a / sum, b / sum
    except ZeroDivisionError:
        raise CustomZeroDivisionError('This is not possible!', result=(0, 0))
    except TypeError:
        print('Wrong types!')
        return -1, 1
    except:
        print('Another error has occurred!')


print(normalize(1, 1))
try:
    try:
        print(normalize(0, 0))
    except CustomZeroDivisionError as e:
        raise SecondCustomZeroDivisionError(e.__str__(), result=e.result)
except SecondCustomZeroDivisionError as e:
    print(e.__str__())
finally:
    print('This is the end!')

print(normalize('1', 0))
