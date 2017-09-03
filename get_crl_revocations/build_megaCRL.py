import multiprocessing
import OpenSSL
import json
import os

outfile = 'megaCRL'
inpath = 'rawCRL/' # point this to the folder containing all raw CRL files

def mp_worker(crl_name):
    revoked_data = {}
    revoked_data['crl'] = crl_name
    revoked_data['cert_serials'] = []
    infile = open(inpath + crl_name, 'rb') # read as binary
    rawtext = infile.read()
    infile.close()
    try:
        crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_ASN1, rawtext)
    except:
        try:
        crl = OpenSSL.crypto.load_crl(OpenSSL.crypto.FILETYPE_PEM, rawtext)
        except:
            print("couldn't open " + crl_name)
            return json.dumps(revoked_data)
    revoked = crl.get_revoked()
    if revoked is None:
        print(crl_name + " is empty")
        return json.dumps(revoked_data)
    for rvk in revoked:
        serial = rvk.get_serial().decode('utf-8')
        revoked_data['cert_serials'].append(serial)
    return json.dumps(revoked_data)


def mp_handler():
    p = multiprocessing.Pool(4)
    crl_names = os.listdir(inpath)
    with open(outfile, 'w') as f:
        for result in p.imap(mp_worker, crl_names):
            f.write(result + '\n')

if __name__=='__main__':
    mp_handler()
