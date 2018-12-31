import pytest
import csv
import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import xlrd
from Calculator import Calculator

def prepareData(operator):
  df = pd.read_excel('./testdata/TestData.xlsx', sheet_name = operator)
  thisList = []
  for i in df.index:
    temp = (df['Operand1'][i], df['Operand2'][i], df['Result'][i])
    thisList.append(temp)  
  return thisList

@pytest.mark.parametrize("operand1, operand2, expectedResult", prepareData('Add'))
def test_add(operand1, operand2, expectedResult):
  cal = Calculator()
  assert cal.add(operand1, operand2) == expectedResult

@pytest.mark.parametrize("operand1, operand2, expectedResult", prepareData('Subtract'))
def test_subtract(operand1, operand2, expectedResult):
  cal = Calculator()
  assert cal.subtract(operand1, operand2) == expectedResult


#@pytest.fixture()
#def setup():
#  print("\nSetup")
#  yield 5
#  print("\nTear down 1")
#
#@pytest.fixture()
#def setup1(request):
#  print("\nSetup1")
#  def teardown_a():
#    print("\nTear down A")
#  def teardown_b():
#    print("\nTear down B")
#  
#  request.addfinalizer(teardown_a)
#  request.addfinalizer(teardown_b)


