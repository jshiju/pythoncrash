
# return dictionary
def get_data_dict():
    return  {'subject': 'math', 'mark': '100'}

# return dictionary
#def get_data_dict():
#    sub = {}
#    sub = {'subject': 'math', 'mark': '100'}
#    return sub

def modify_data(data):
    print(data)
    data.update({'group':'chem'})
    return data

#print(get_data_dict())
print(modify_data(get_data_dict()))
