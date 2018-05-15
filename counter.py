import logging
import emailrun

log = logging.getLogger(__name__)
path = 'c:\Python27\Lib\site-packages\imaprelay\counter.txt'

def roundrobinemail():
    salesmanid_file = open(path, 'r')
    salesmanid = salesmanid_file.read()
    log.info('Reading last position')
    salesmanid_file.close()

    if int(salesmanid) < 0 or int(salesmanid) >=5:
        salesmanid = 0

    salesmanid = int(salesmanid) + 1
    log.info('Reading next position')

    salesmanid_file = open(path, 'w')
    salesmanid_file.write(str(salesmanid))
    salesmanid_file.close()
    log.info('Saving last position')

    return salesmanid


def emailfunction():
    # salesmanemails = {1: 'roxyjacqueline31@gmail.com',
    #                   2: 'roxy_jacqueline@hotmail.com',
    #                   3: 'dsb.saul@gmail.com',
    #                   4: 'dsb_saul@hotmail.com',
    #                   5: 'serviomega@gmail.com'
    #                   }
    salesman = roundrobinemail()
    email = emailrun.salesmanemails[salesman]
    log.info('Selected {0}'.format(email))

    return email


