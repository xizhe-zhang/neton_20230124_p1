# Python3 program to demonstrate
import itertools
import pandas as pd


def getInputFromFile():
    df = pd.read_csv('test.csv', sep=',')
    value_dict = {}
    value_dict['W'] = int(df['value'].iloc[0])
    df_value = df.iloc[1:, :]
    value_dict['Id_list'] = df_value.iloc[:, 0].astype(int).tolist()
    value_dict['Wight_list'] = df_value.iloc[:, 1].astype(int).tolist()
    value_dict['Value_list'] = df_value.iloc[:, 2].astype(int).tolist()
    return value_dict


def checkInput(value_dict):
    if value_dict['W'] <= 0 or value_dict['W'] > 10000:
        print(F"Error input value[W={value_dict['W']}]!")
        return False
    print("Check input OK.")
    return True


def getValidValue(value_dict):
    print("Get valid Wight.")
    value_dict['Id_valid_list'] = []
    for index in value_dict['Id_list']:
        if value_dict['Wight_list'][index] <= value_dict['W']:
            value_dict['Id_valid_list'].append(index)
    return value_dict


def getAllCombinations(list):
    print("Get all combinations.")
    combination_list = []
    for L in range(len(list) + 1):
        for subset in itertools.combinations(list, L):
            if len(subset) > 0:
                combination_list.append(subset)
    return combination_list


def getCalculatedWeight(list, value_dict):
    value_list = []
    for data in list:
        sum = 0
        for value in data:
            sum = sum + value_dict['Wight_list'][value]
        value_list.append(sum)
    return value_list


def getValidCombination(list, weight_list, value_dict):
    value_dict['valid_combination_list'] = []
    value_dict['valid_combination_value'] = []
    for idx, weight in enumerate(weight_list):
        if weight <= value_dict['W']:
            value_dict['valid_combination_list'].append(list[idx])
            value = 0
            for id in list[idx]:
                value = value + value_dict['Value_list'][id]
            value_dict['valid_combination_value'].append(value)
    return value_dict


def getMaxCombination(value_dict, max_value):
    value_dict['max_combination_list'] = []
    for idx, value in enumerate(value_dict['valid_combination_value']):
        if value == max_value:
            value_dict['max_combination_list'].append(
                value_dict['valid_combination_list'][idx])
    return value_dict


def getMaxValueFromInput(value_dict):
    if not checkInput(value_dict):
        value_dict['max_combination_list'] = []
        print("Check input OK.")
        return []
    value_dict = getValidValue(value_dict)
    if len(value_dict["Id_valid_list"]) <= 0:
        value_dict['max_combination_list'] = []
        print("No valid list.")
        return []
    list = getAllCombinations(value_dict['Id_valid_list'])
    weight_list = getCalculatedWeight(list, value_dict)
    value_dict = getValidCombination(list, weight_list, value_dict)
    if len(value_dict['valid_combination_list']) <= 0:
        value_dict['max_combination_list'] = []
        print("No valid combination.")
        return []
    max_value = max(value_dict['valid_combination_value'])
    value_dict = getMaxCombination(value_dict, max_value)
    value_dict['max_value'] = max_value
    return value_dict['max_combination_list']


def main():
    value_dict = getInputFromFile()
    max_combination_list = getMaxValueFromInput(value_dict)
    print(value_dict)
    if max_combination_list != []:
        print(F"Max_value = {value_dict['max_value']}")
    else:
        print("No result!")


if __name__ == "__main__":
    main()
