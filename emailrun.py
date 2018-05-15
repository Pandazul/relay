import pickle

with open('emails.txt', 'rb') as handle:
    salesmanemails = pickle.loads(handle.read())