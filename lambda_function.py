import pandas as pd

def lambda_handler(event, context):
    d = {'col1': [1,2], 'col2': [2,8]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Done x1.1')

def test_func():
    print("I am inside the test_func")

test_func()
