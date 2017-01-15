filename = "log.txt"

def getDoorTime():
    with open(filename,'r') as f:
        read_data = f.readlines()
    f.closed
    length=len(read_data)
    if length>0:
        value=read_data[len(read_data)-1]
        v2=value.split()
        return v2[1]
    else:
        return "00:00:00AM"

def getDoorState():
    with open(filename,'r') as f:
        read_data = f.readlines()
    f.closed
    length=len(read_data)
    if length>0:
        value=read_data[len(read_data)-1]
        v2=value.split()
        return v2[0]
    else:
        return "IN"
