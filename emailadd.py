import pickle

salesmanemails = {1: 'dsb.saul@gmail.com',
                  2: 'dsb_saul@hotmail.com',
                  3: 'serviomega@gmail.com'
                  }

with open('emails.txt', 'wb') as handle:
  pickle.dump(salesmanemails, handle)