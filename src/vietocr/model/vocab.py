class Vocab():
    def __init__(self, chars):
        self.pad = 0
        self.go = 1
        self.eos = 2
        self.mask_token = 3

        self.chars = chars

        self.c2i = {c:i+4 for i, c in enumerate(chars)}

        self.i2c = {i+4:c for i, c in enumerate(chars)}
        
        self.i2c[0] = '<pad>'
        self.i2c[1] = '<sos>'
        self.i2c[2] = '<eos>'
        self.i2c[3] = '*'

    def encode(self, chars):
        return [self.go] + [self.c2i[c] for c in chars] + [self.eos]
    
    def decode(self, ids):
        22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
class Vocab():
    def __init__(self, chars):
        self.pad = 0
        self.go = 1
        self.eos = 2
        self.mask_token = 3
        self.chars = chars
        self.c2i = {c: i+4 for i, c in enumerate(chars)}
        self.i2c = {i+4: c for i, c in enumerate(chars)}
        self.i2c[0] = '<pad>'
        self.i2c[1] = '<sos>'
        self.i2c[2] = '<eos>'
        self.i2c[3] = '*'
    def encode(self, chars):
        return [self.go] + [self.c2i[c] for c in chars] + [self.eos]
    def decode(self, ids):
        first = 1 if self.go in ids else 0
        last = len(ids)
        print("ids: ",ids)
        for i, obj in enumerate(ids):
            if self.eos == obj:
                last = i
                break
        # last = ids.index[self.eos] if self.eos in ids else None
        # sent = ''.join([print("char : ",self.i2c[i]) for i in ids[first:last]])
        print("first:",first)
        print("last: ",last)
        sent = ''.join([self.i2c[i] for i in ids[first:last]])
        for i in ids[first:last]:
            print("char:",self.i2c[i])

        print("sent: " ,sent)
        return sent
    
    def __len__(self):
        return len(self.c2i) + 4
    
    def batch_decode(self, arr):
        print("arr: ",arr)
        texts = [self.decode(ids) for ids in arr]
        print("text: ",texts)
        return texts

    def __str__(self):
        return self.chars
