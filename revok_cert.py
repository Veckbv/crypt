import os
import ssl
import requests
from cryptography import x509
from cryptography.hazmat.backends import default_backend


def get_crl_distrib_points():
    cert_file_name = os.path.join(os.path.dirname(__file__), 'www.google.com')
    cert_dict = ssl._ssl._test_decode_cert(cert_file_name)
    return cert_dict['crlDistributionPoints'][0]

def get_revok_date_and_ser_number():
    with open(crl_path, 'rb') as crl_file:
        data = crl_file.read()
    crl = x509.load_der_x509_crl(data, default_backend())

    for r in crl:
        print(f'{r.revocation_date} {r.serial_number}')

if __name__ == '__main__':
    crl_dist_point = get_crl_distrib_points()
    crl_path = os.path.join(os.path.dirname(__file__), crl_dist_point.split('/')[-1])
    crl = requests.get(crl_dist_point)
    crl_path = os.path.join(os.path.dirname(__file__), crl_dist_point.split('/')[-1])
    with open(crl_path, 'wb') as f:
        f.write(crl.content)
    get_revok_date_and_ser_number()
