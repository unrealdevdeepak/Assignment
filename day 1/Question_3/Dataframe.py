import pandas as pd


std_dict = {'Name': ['Deepak', 'Jyoti', 'Shusil'], 'Age': [26, 22, 29], 'Marks': [99.6, 80.56, 70.58]}
student_df = pd.DataFrame(std_dict,index = ["record_1", "record_2", "record_3"])
print(student_df)