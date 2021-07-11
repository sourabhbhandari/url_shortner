import random
import string 

#Constants
random.randint(10,20)
letters_lower = string.ascii_lowercase
letter_upper = string.ascii_uppercase
digits = string.digits
options = letters_lower+letter_upper+digits

# URL Database
URL_DB = {}

def get_short_url(url):
    
    l = random.randint(4,6)
    short_url = "https://sourabh.in/"
    
    for i in range(l):
        short_url += random.choice(options)
        
    if URL_DB.get(short_url) is not None:
        return get_short_url(url)
    
    else:
        URL_DB[short_url] = url
    
    
    return short_url


def get_long_url(short_url):
    if URL_DB.get(short_url) is None:
        return "URL doesn't exist."
    else:
        return URL_DB[short_url]
    
    
my_url = "https://hexacode.com/hackeahiuybujkawnejlhikwaxwe68748erwcewawerfsdgsg"
tmp = get_short_url(my_url)
print(p)
short_url = tmp
print(get_long_url(short_url))
