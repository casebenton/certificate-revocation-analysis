import json

INFILE_NAME = "certificates.json"
crl_outfile = open("CRL_servers", "w")
cert_crl_outfile = open("certs_using_crl.json", "w")
cert_nocrl_outfile = open("certs_without_crl.json", "w")
certificates
certCounter = 0
INDICATOR  = 1000000
INDICATOR_STR = "M"


with open(INFILE_NAME, "r") as f:
    print("processing certificates...")
    for line in f:
        certCounter += 1
        if not(certCounter % INDICATOR):
            print(str(certCounter / INDICATOR) + INDICATOR_STR + " certificates processed")
        try:
            cert = json.loads(line)
            if cert["parsed"]["extensions"]["crl_distribution_points"]:
                cert_crl_outfile.write(json.dumps(cert) + '\n')
                crlCertCounter += 1
                if not(crlCertCounter % INDICATOR):
                    print(str(crlCertCounter / INDICATOR) + INDICATOR_STR + " certificates with crl")
                for crl in cert["parsed"]["extensions"]["crl_distribution_points"]:
                    crl_outfile.write(crl + '\n')
        except KeyError: # the certificate does not have a CRL listed
            cert = json.loads(line)
            cert_nocrl_outfile.write(json.dumps(cert) + '\n')
            noCrlCertCounter += 1
            if not(noCrlCertCounter % INDICATOR):
                    print(str(noCrlCertCounter / INDICATOR) + INDICATOR_STR + " certificates without crl")

        except:
            print("error parsing certificate...")
