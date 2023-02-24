x = 0
try:
    x = 1 / 0
except ZeroDivisionError as err:
    print('Handling run-time error :', err)
print(x + 1)