result = []
def divider(a, b):
    try:
        if a < b:
            result.append(res)
        if b > 100:
            result.append(res)
        if type(a) == "str":
            result.append(res)
            if b == 0:
                raise ZeroDivisionError
    except IndexError:
        print('Error index')
    except ValueError:
        print('Error value')
    except TypeError:
        print('Error type')
        return
    except ZeroDivisionError:
        print('Error ZeroDivisionError')
        return
    return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, 8 : 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)