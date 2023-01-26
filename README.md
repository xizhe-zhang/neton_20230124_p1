# neton_20230124_p1
problem solve issue


---python version---
```
Python 3.10.9 (main, Dec 15 2022, 18:18:30) [Clang 14.0.0 (clang-1400.0.29.202)] on darwin
```


---pip package---
```
Package         Version
--------------- --------
attrs           22.2.0
autopep8        2.0.1
coverage        7.1.0
exceptiongroup  1.1.0
iniconfig       2.0.0
numpy           1.24.1
packaging       23.0
pandas          1.5.3
pip             22.3.1
pluggy          1.0.0
pycodestyle     2.10.0
pytest          7.2.1
pytest-cov      4.0.0
python-dateutil 2.8.2
pytz            2022.7.1
setuptools      65.6.3
six             1.16.0
tomli           2.0.1
wheel           0.38.4
```

---command---
```
python p1.py
```


---sample result---
```
Check input OK.
Get valid Wight.
Get all combinations.
{'W': 8, 'Id_list': [0, 1, 2], 'Wight_list': [10, 5, 7], 'Value_list': [100, 20, 6], 'Id_valid_list': [1, 2], 'valid_combination_list': [(1,), (2,)], 'valid_combination_value': [20, 6], 'max_combination_list': [(1,)], 'max_value': 20}
Max_value = 20
```


---Data format---
```
id,weight,value
W,,8
0,10,100
1,5,20
2,7,6
```

---Pytest---
```
export PYTHONPATH=**pathOfRepo**/neton_20230124_p1/src
cd test
pytest
```

---sample result---
```
====================================================== test session starts ======================================================
platform darwin -- Python 3.10.9, pytest-7.2.1, pluggy-1.0.0
rootdir: neton_20230124_p1/test
plugins: cov-4.0.0
collected 15 items                                                                                                              

test_p1.py::test_case001_1 PASSED                                                                                         [  6%]
test_p1.py::test_case001_2 PASSED                                                                                         [ 13%]
test_p1.py::test_case002_1 PASSED                                                                                         [ 20%]
test_p1.py::test_case002_2 PASSED                                                                                         [ 26%]
test_p1.py::test_case002_3 PASSED                                                                                         [ 33%]
test_p1.py::test_case002_4 PASSED                                                                                         [ 40%]
test_p1.py::test_case002_5 PASSED                                                                                         [ 46%]
test_p1.py::test_case002_6 PASSED                                                                                         [ 53%]
test_p1.py::test_case002_7 PASSED                                                                                         [ 60%]
test_p1.py::test_case003_1 PASSED                                                                                         [ 66%]
test_p1.py::test_case003_2 PASSED                                                                                         [ 73%]
test_p1.py::test_case003_3 PASSED                                                                                         [ 80%]
test_p1.py::test_case003_4 PASSED                                                                                         [ 86%]
test_p1.py::test_case004_bulk_test PASSED                                                                                 [ 93%]
test_p1.py::test_case005_bulk_test PASSED                                                                                 [100%]

---------- coverage: platform darwin, python 3.10.9-final-0 ----------
Name                                                        Stmts   Miss Branch BrPart  Cover
---------------------------------------------------------------------------------------------
/Users/sdlontry/Project/repo3/neton_20230124_p1/src/p1.py      97      0     44      0   100%
---------------------------------------------------------------------------------------------
TOTAL                                                          97      0     44      0   100%


================================================ 15 passed in 2143.57s (0:35:43) ================================================
```