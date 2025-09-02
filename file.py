with open("abc.txt") as f:
    c=f.read()
    c=c.lower()
    if("twinkle" in c ):
        print("twinkle in file")
    else:
        print("twinkle not in file") 
        