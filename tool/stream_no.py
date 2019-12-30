import string
import random
import hashlib


class StreamNo:
    def generate(self):
        n = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        m = hashlib.md5(n.encode('utf-8')).hexdigest()
        return m


if __name__ == '__main__':
    sn = StreamNo().generate()
    dict1 = {
        'name': 'sb',
        'age': '17',
        'streamno': '1231231231'
    }
    print(dict1)
    dict2 = {
        'streamno': sn
    }
    dict1.update(dict2)
    print(dict1)