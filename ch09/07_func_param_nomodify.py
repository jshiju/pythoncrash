
# return dictionary
def get_data_dict():
    return  {'subject': 'math', 'mark': '100'}

def modify_data(data):
    data.update({'group':'chem'})
    return data

data = get_data_dict()
print(data)
#modify_data(data)

# preserve by copy
# for list use copy equivalent slice operator data[:]
modify_data(data.copy())
print(data)