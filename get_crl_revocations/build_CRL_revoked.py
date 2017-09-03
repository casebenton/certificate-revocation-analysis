from urlparse import urlparse
import os.path
from multiprocessing import Process, Queue
import json

workers = 32
outfile = 'revokedCRLCerts/certs'
infile = 'certs_using_crl.json'
crlInfileName = 'megaCRL'

def doWork(i, megaCRL):
    print('starting worker ' + str(i))
    out = open(outfile + str(i) + '.json', 'w')
    while True:
        cert = json.loads(q.get())
        serial = int(cert['parsed']['serial_number'])
        urlList = cert['parsed']['extensions']['crl_distribution_points']
        url = urlparse(urlList[0])
        crlName = os.path.split(url.path)[1]
        if(isRevoked(megaCRL, crlName, serial)):
            out.write(json.dumps(cert) + '\n')

# TODO: this definition of isRevoked is outdated, and not
# the version that I used for my analysis. It doesn't account
# for instances where the wget fetch of a CRL changed its name.
# I have improved tooling, which I actually used in the final analysis,
# that I will add soon. 
def isRevoked(megaCRL, crlName, serial):
    if crlName in megaCRL:
        return serial in megaCRL[crlName]
    else:
        return False

def buildDict():
    megaCRL = {}
    crlFile = open(crlInfileName, 'r')
    for line in crlFile:
        crlName, revokedList = line.split(' ', 1)
        revokedListParsed = json.loads(revokedList)
        megaCRL[crlName] = [int(x, 16) for x in revokedListParsed]
    return megaCRL

if __name__ == '__main__':
    print('building megaCRL...')
    megaCRL = buildDict()
    q = Queue(workers * 16)
    for i in range(workers):
        p = Process(target=doWork, args=(i, megaCRL, ))
        p.start()
    try:
        ctr = 0
        for cert in open(infile, 'r'):
            q.put(cert)
            ctr += 1
            if(ctr % 10000 == 0):
                print(str(ctr) + " certificates processed")
    except KeyboardInterrupt:
        sys.exit(1)
