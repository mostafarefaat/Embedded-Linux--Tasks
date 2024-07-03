import pandas as pd


def create_id():
    global id
    id = 0
def increment_id():
    global id
    id += 1
def decrement_id():
    global id
    id -= 1
def get_id():
    global id
    return id

All_Function_Names = []
All_Function_Parameters= []
All_Function_Return = []
All_Function_IDs = []

Function_return_keywords = ("void", "uint8", "uint16", "uint32", "uint64", 
                            "sint8", "sint16", "sint32", "sint64", "float32", "float64", 
                            "void*", "uint8*", "uint16*", "uint32*", "uint64*", 
                            "sint8*", "sint16*", "sint32*", "sint64*", "float32*", "float64*", 
                            "boolean", "extern", "const")
    
    
with open("gpio.h","r+") as header_file:
    file = header_file.read()

Funtions = file.split('\n')

create_id()

for Funtion in Funtions:

    list = Funtion.split('(')
    
    if list[0] != '' and list[0].split()[0] in Function_return_keywords and (" ".join(list).find(")")) != -1: 
        part_1 = list[0].split()
        Parameters = list[1][:-2]
        Return_Type = " ".join(part_1[0:-1])
        Function_Name = part_1[-1]
        All_Function_Names.append(Function_Name)
        All_Function_Parameters.append(Parameters)
        All_Function_Return.append(Return_Type)
        increment_id()
        All_Function_IDs.append("IDX"+str(get_id()))

def read_csv(file_path):
    return pd.read_csv(file_path)

data = {
    'Signature' : All_Function_Names,
    'Parameters'  : All_Function_Parameters,
    'Return' : All_Function_Return,
    'ID' : All_Function_IDs
}

df = pd.DataFrame(data)
df.to_csv('Output.csv', index=False)

print(read_csv('Output.csv'))
print('-'*30)