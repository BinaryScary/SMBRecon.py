#!/usr/bin/python3
from impacket.smbconnection import SMBConnection
from impacket.smb import SMB_DIALECT
import sys


if len(sys.argv) < 2:
    print("Usage: smbRecon.py [Host]")
    exit()
smbv1 = False

try:
    smb = SMBConnection(sys.argv[1], sys.argv[1], preferredDialect=SMB_DIALECT)
    smbv1 = True
except:
    # SMBv1 is disabled
    pass

try: 
    smb = SMBConnection(sys.argv[1], sys.argv[1])
    smb.login("","")
except:
    pass

attri = smb._SMBConnection._Session

print("DomainName:           ", attri['ServerDNSDomainName'])
print("DomainNBT:            ", attri['ServerDomain'])
print("ComputerNBT:          ", attri['ServerName'])
print("Build:                ", attri['ServerOS'])
print("SMBSigning(relaying): ", attri['ServerOS'])
print("SMBv1(EternalBlue):   ", smbv1)
