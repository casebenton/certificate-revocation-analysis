import json

INFILE_NAME = "../certificates.json"
crl_outfile = open("CRL_servers", "w")
cert_crl_outfile = open("../certs_using_crl.json", "w")
cert_nocrl_outfile = open("../certs_without_crl.json", "w")

certCounter = 0
INDICATOR  = 1000000
INDICATOR_STR = "M"

def hasCRL(cert):
    if "extensions" in cert["parsed"]:
        return "crl_distribution_points" in cert["parsed"]["extensions"]
    return False

with open(INFILE_NAME, "r") as f:
    print("processing certificates...")
    for line in f:
        # print stats
        certCounter += 1
        if not(certCounter % INDICATOR):
            print(str(certCounter / INDICATOR) + INDICATOR_STR + " certificates processed")
        # read certificate
        cert = json.loads(line)
        if hasCRL(cert):
            cert_crl_outfile.write(json.dumps(cert) + '\n')
            for crl in cert["parsed"]["extensions"]["crl_distribution_points"]:
                crl_outfile.write(crl + '\n')
        else:
            cert = json.loads(line)
            cert_nocrl_outfile.write(json.dumps(cert) + '\n')
