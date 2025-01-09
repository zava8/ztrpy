import os
import csv
import re
from ztrzstopy import u_to_i
ioz = {"i": "क्ष राजनीतिज्ञों के पास जो कार्य करना चाहिए, वहवह करने कि अनुमति क्षनहीं है .", "o": ""}
u_to_i(ioz)
print(ioz['o'])
# sh rαzniтigyo ke pαs zo kαry krnα ćαнie, vн krne ki anumтi shnнi нei .
# sh rαzniтigyo ke pαs zo kαry krnα ćαнie, vнvн krne ki anumтi shnнi нei .
def append_to_csv(file_name, data):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
# data_to_append = ["John", 25, "New York"]
# append_to_csv("/kaggle/working/my_data.csv", data_to_append)
#with open('/kaggle/input/english-hindi-latin31-translation-data-set/English_vowelHinDi_zava8_gitHub_io.csv', 'r') as file:
#    csv_reader = csv.reader(file)
#    for row in csv_reader:
#        print(row)