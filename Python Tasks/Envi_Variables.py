import os

for i,j in os.environ.items():
    print(f"{i} = {j}")
    
print("-----------------------------------------")
print(os.environ['HOME'])
print("-----------------------------------------")
print(os.environ['PATH'])