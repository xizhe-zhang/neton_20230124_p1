######################################################################################################
# デモ用の Python3 プログラム
######################################################################################################
import itertools
import pandas as pd
import sys


######################################################################################################
# CSV ファイルから入力データを取得する
# weight[i],value[i]は整数
######################################################################################################
def getInputFromFile():
    try:
        df = pd.read_csv('test.csv', sep=',')
        value_dict = {}
        value_dict['W'] = int(df['value'].iloc[0])
        df_value = df.iloc[1:, :]
        value_dict['Id_list'] = df_value.iloc[:, 0].astype(int).tolist()
        value_dict['Wight_list'] = df_value.iloc[:, 1].astype(int).tolist()
        value_dict['Value_list'] = df_value.iloc[:, 2].astype(int).tolist()
    except:
        # エラーでプログラムを終了します
        sys.exit("Read CSV file error!")
    return value_dict


######################################################################################################
# 制約をチェック
# ・1 < n <= 100
# ・1 <= weight[i],value[i] <= 1000
# ・1 <= W <= 10000
######################################################################################################
def checkInput(value_dict):
    if value_dict['W'] <= 0 or value_dict['W'] > 10000:
        print(F"Error input value[W={value_dict['W']}]!")
        return False
    if len(value_dict['Wight_list']) <= 0 or len(value_dict['Wight_list']) > 100:
        print(F"Error Wight_list length[len={len(value_dict['Wight_list'])}]!")
        return False
    if len(value_dict['Value_list']) <= 0 or len(value_dict['Value_list']) > 100:
        print(F"Error Value_list length[len={len(value_dict['Value_list'])}]!")
        return False
    if len(value_dict['Value_list']) != len(value_dict['Wight_list']):
        print(
            F"Error length not equal[Value_list={len(value_dict['Value_list'])}] [Wight_list={len(value_dict['Wight_list'])}]!")
        return False
    for value in value_dict['Wight_list']:
        if value <= 0 or value > 10000:
            print(F"Error input Wight_list value[W={value}]!")
            return False
    for value in value_dict['Value_list']:
        if value <= 0 or value > 10000:
            print(F"Error input Value_list value[W={value}]!")
            return False
    return True


######################################################################################################
# 総重量と比較して有効なデータを取得する
######################################################################################################
def getValidValue(value_dict):
    value_dict['Id_valid_list'] = []
    for index in value_dict['Id_list']:
        if value_dict['Wight_list'][index] <= value_dict['W']:
            value_dict['Id_valid_list'].append(index)
    return value_dict


######################################################################################################
# 品物のすべての組み合わせを取得する
######################################################################################################
def getAllCombinations(list):
    combination_list = []
    for L in range(len(list) + 1):
        for subset in itertools.combinations(list, L):
            if len(subset) > 0:
                combination_list.append(subset)
    return combination_list


######################################################################################################
# 品物組み合わせの重みを計算する
######################################################################################################
def getCalculatedWeight(list, value_dict):
    value_list = []
    for data in list:
        sum = 0
        for value in data:
            sum = sum + value_dict['Wight_list'][value]
        value_list.append(sum)
    return value_list


######################################################################################################
# 総重量と比較して有効な品物組み合を取得する
######################################################################################################
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


###################################################
# 最大重量の組み合わせを取得する
###################################################
def getMaxCombination(value_dict, max_value):
    value_dict['max_combination_list'] = []
    for idx, value in enumerate(value_dict['valid_combination_value']):
        if value == max_value:
            value_dict['max_combination_list'].append(
                value_dict['valid_combination_list'][idx])
    return value_dict


######################################################################################################
# n個の品物があり、i番目の品物のそれぞれ重さと価値が weight[i],value[i]となっている (i=0,1,...,n−1)。
# これらの品物から重さの総和がWを超えないように選んだときの、価値の総和の最大値を求めよ。
######################################################################################################
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


######################################################################################################
# 最初の関数
######################################################################################################
def main():
    value_dict = getInputFromFile()
    max_combination_list = getMaxValueFromInput(value_dict)
    # print(value_dict) ## デバッグ用
    if max_combination_list != []:
        print(F"価値の総和の最大値 = {value_dict['max_value']}")
    else:
        print("検索結果はありません!")


if __name__ == "__main__":
    main()
