import p1
import itertools


def test_case001_1():
    value_dict = {}
    value_dict['W'] = 8
    value_dict['Id_list'] = [0, 1, 2]
    value_dict['Wight_list'] = [10, 5, 7]
    value_dict['Value_list'] = [100, 20, 6]
    assert p1.getInputFromFile('test.csv') == value_dict


def test_case001_2():
    assert p1.getInputFromFile('new.csv') is None


def test_case002_1():
    assert p1.getMaxValueFromInput({}) == []


def test_case002_2():
    value_dict = {}
    value_dict['W'] = 0
    value_dict['Id_list'] = [0, 1, 2]
    value_dict['Wight_list'] = [10, 5, 7]
    value_dict['Value_list'] = [100, 20, 6]
    assert p1.getMaxValueFromInput(value_dict) == []


def test_case002_3():
    value_dict = {}
    value_dict['W'] = 10
    value_dict['Id_list'] = [0, 1, 2]
    value_dict['Wight_list'] = [0, 5, 7]
    value_dict['Value_list'] = [100, 20, 6]
    assert p1.getMaxValueFromInput(value_dict) == []


def test_case002_4():
    value_dict = {}
    value_dict['W'] = 10
    value_dict['Id_list'] = [0, 1, 2]
    value_dict['Wight_list'] = [10, 5, 7]
    value_dict['Value_list'] = [100, 0, 6]
    assert p1.getMaxValueFromInput(value_dict) == []


def test_case002_5():
    value_dict = {}
    value_dict['W'] = 10
    value_dict['Id_list'] = [0, 1, 2]
    value_dict['Wight_list'] = [10, 5]
    value_dict['Value_list'] = [100, 20, 6]
    assert p1.getMaxValueFromInput(value_dict) == []


def test_case002_6():
    value_dict = {}
    value_dict['W'] = 10
    value_dict['Id_list'] = [0, 1, 2]
    value_dict['Wight_list'] = []
    value_dict['Value_list'] = []
    assert p1.getMaxValueFromInput(value_dict) == []


def test_case002_7():
    value_dict = {}
    value_dict['W'] = 10
    value_dict['Id_list'] = [0, 1, 2]
    value_dict['Wight_list'] = [10, 5, 7]
    value_dict['Value_list'] = []
    assert p1.getMaxValueFromInput(value_dict) == []


def test_case003_1():
    value_dict = {}
    value_dict['W'] = 100
    value_dict['Id_list'] = [0, 1, 2]
    value_dict['Wight_list'] = [10, 5, 7]
    value_dict['Value_list'] = [100, 20, 6]
    p1.getMaxValueFromInput(value_dict)
    assert value_dict['max_value'] == 126


def test_case003_2():
    value_dict = {}
    value_dict['W'] = 10
    value_dict['Id_list'] = [0, 1, 2]
    value_dict['Wight_list'] = [10, 5, 7]
    value_dict['Value_list'] = [100, 20, 6]
    p1.getMaxValueFromInput(value_dict)
    assert value_dict['max_value'] == 100


def test_case003_3():
    value_dict = {}
    value_dict['W'] = 6
    value_dict['Id_list'] = [0, 1, 2]
    value_dict['Wight_list'] = [10, 5, 7]
    value_dict['Value_list'] = [100, 20, 6]
    p1.getMaxValueFromInput(value_dict)
    assert value_dict['max_value'] == 20


def test_case003_4():
    value_dict = {}
    value_dict['W'] = 4
    value_dict['Id_list'] = [0, 1, 2]
    value_dict['Wight_list'] = [10, 5, 7]
    value_dict['Value_list'] = [100, 20, 6]
    assert p1.getMaxValueFromInput(value_dict) == []


def getMaxValue(value_dict):
    list = value_dict['Id_list']
    combination_list = []
    for L in range(len(list) + 1):
        for subset in itertools.combinations(list, L):
            if len(subset) > 0:
                combination_list.append(subset)
    max_value = 0
    for data in combination_list:
        sum = 0
        total = 0
        for value in data:
            sum = sum + value_dict['Wight_list'][value]
            total = total + value_dict['Value_list'][value]
        if sum <= value_dict['W']:
            if total > max_value:
                max_value = total
    return max_value


def test_case004_bulk_test():
    value_dict = {}
    for w in range(1, 11):
        for w1 in range(1, 11):
            for w2 in range(1, 11):
                for w3 in range(1, 11):
                    for v1 in range(1, 11):
                        for v2 in range(1, 11):
                            for v3 in range(1, 11):
                                value_dict['W'] = w
                                value_dict['Id_list'] = [0, 1, 2]
                                value_dict['Wight_list'] = [w1, w2, w3]
                                value_dict['Value_list'] = [v1, v2, v3]
                                max_value = getMaxValue(value_dict)
                                max_combination_list = p1.getMaxValueFromInput(
                                    value_dict)
                                if max_value <= 0:
                                    assert max_combination_list == []
                                else:
                                    print(value_dict)
                                    assert value_dict['max_value'] == max_value


def test_case005_bulk_test():
    value_dict = {}
    for w in range(200, 211):
        for w1 in range(100, 105):
            for w2 in range(100, 105):
                for w3 in range(100, 105):
                    for v1 in range(100, 105):
                        for v2 in range(100, 105):
                            for v3 in range(100, 105):
                                value_dict['W'] = w
                                value_dict['Id_list'] = [
                                    0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                                value_dict['Wight_list'] = [
                                    w1, w2, w3, w1+1, w2+1, w3+1, w1+2, w2+2, w3+2, w1+3]
                                value_dict['Value_list'] = [
                                    v1, v2, v3, v1+1, v2+1, v3+1, v1+2, v2+2, v3+2, v1+3]
                                max_value = getMaxValue(value_dict)
                                max_combination_list = p1.getMaxValueFromInput(
                                    value_dict)
                                if max_value <= 0:
                                    assert max_combination_list == []
                                else:
                                    print(value_dict)
                                    assert value_dict['max_value'] == max_value
