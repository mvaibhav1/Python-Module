name=input('Enter the name of the file with extension : ')

# with open("1stfile.txt") as f:
with open(f"{name}") as f:
    content=f.read()

with open("2ndfile.txt") as p:
    content1=p.read()

if(content==content1):
    print("The files are identical")
else:
    print("files are not identical")