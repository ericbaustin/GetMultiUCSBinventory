#!/usr/bin/env python

import os,glob,shutil,requests

from ucsmsdk.utils.inventory import get_inventory
from ucsmsdk.ucshandle import UcsHandle

def GetUCSBinventory():
    with open ('hostlist-B', "r") as filename:
        lines = [line.rstrip() for line in filename]
        print(lines)
        IPlistToString = " "
        IPlistToString.join(lines)
        print(IPlistToString)
    for IP in lines:
        try:
            handle = UcsHandle(IP,"admin","PASSWORD",timeout=5)
            print(handle)
            handle.login()
            get_inventory(handle, component='all', file_format='html', file_name='UCSBinventory_%s' % IP)
        except:
            with open ('UCSBinventory_%s' % IP , "w") as exceptionfile:
                exceptionfile.write('Domain %s failed to respond' % IP)
                exceptionfile.close()
            pass
    return GetUCSBinventory

if __name__ == "__main__":
    GetUCSBinventory()
