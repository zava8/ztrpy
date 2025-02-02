from ztrzstopy import u_to_i
from zava8.e_to_i import ztrei
import datetime
# import csv
def getHinJ5(ustr):
    ioz = {'i':ustr,'o':''}
    u_to_i(ioz)
    return(ioz['o'])
def getiNgJ5(istr):
    ztreio = ztrei(istr)
    ztreio.e_to_i()
    return(ztreio.i)
a="I after goinG to school"
a=getiNgJ5(a)
print(a)