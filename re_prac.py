import re
ts = "Jessa 48 is a Python 3104\n developer, and \nHer salary is 8000\nExp is 16\n."
result = re.findall(r"^([A-Z].*?)\s",ts)
# try again by removińg huńgry operator ?
print("ts is: ",ts,"\n1Matching value", result)
result = re.findall(r"\d.*?$", ts,re.M) #try re.S also
print("ts is: ",ts,"\n3Matching value", result)
result = re.findall(r"\A([A-Z].*?)\s",ts)
print("ts is: ",ts,"\n2Matching value", result)
result = re.findall(r"\d.*?\Z", ts)
print("ts is: ",ts,"\n4Matching value", result)
result = re.findall(r"^([A-Z].*?)\s",ts,re.M)
print("ts is: ",ts,"\n5Matching value", result)
result = re.findall(r"^([A-Z].*?)\s",ts,re.M)
print("ts is: ",ts,"\n6Matching value", result)
result = re.findall(r"\d.*?$", ts,re.M)
print("ts is: ",ts,"\n7Matching value", result)
result = re.findall(r"\d.*?\Z", ts,re.M)
print("ts is: ",ts,"\n8Matching value", result)
