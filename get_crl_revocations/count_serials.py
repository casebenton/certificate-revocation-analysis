import json

crlInfileName = 'megaCRL'

print('reading megaCRL...')
megaCRL = {}
crlFile = open(crlInfileName, 'r')
for line in crlFile:
    crlName, revokedList = line.split(' ', 1)
    revokedListParsed = json.loads(revokedList)
    megaCRL[crlName] = [int(x, 16) for x in revokedListParsed]

certCtr = 0
for key in megaCRL:
    certCtr += len(megaCRL[key])
print('there are ' + str(certCtr) + ' total revocations')
