import pandas as pd
timepass = [2, 4, 5, 6]
sleep_hours = [5, 6, 7, 8]
making_notes = [10, 7, 8, 9]
stu_name = ['vidya', 'kavya', 'shivani', 'thanu']
dict1 = {
    "timepass": timepass,
    "sleephours": sleep_hours,
    "stuname": stu_name
}
print(dict1)
df = pd.DataFrame(dict1)
print(df)