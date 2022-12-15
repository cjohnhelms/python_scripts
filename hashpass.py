#!/usr/bin/env python3

import getpass,sys,os,hashlib

if __name__ == '__main__' :
    if len(sys.argv) == 2 :
        passwd = str(getpass.getpass('Enter password: '))
        cpasswd = str(getpass.getpass('Confirm password: '))
        if passwd == cpasswd :
            if sys.argv[1] == 'sha256' :
                print(hashlib.sha256(passwd.encode('utf-8')).hexdigest())
            if sys.argv[1] == 'sha512' :
                print(hashlib.sha512(passwd.encode('utf-8')).hexdigest())
    else :
        print('Usage: ' + os.path.basename(sys.argv[0]) + ' [sha256 or sha512]')
        sys.exit(1)


