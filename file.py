import pickle
'''
d = dict(name = 'BOB',age = 20,score = 88)
print(pickle.dumps(d))
with open('d:\\dump.txt','wb')as f:
    pickle.dump(d,f)
'''
with open('d:\\dump.txt','rb') as f:
    d = pickle.load(f)
print(d)