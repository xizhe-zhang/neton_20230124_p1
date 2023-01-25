import p1


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
