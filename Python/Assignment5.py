import collections

text = ('Line 1: this is sample text with several words '
'Line 2: this is more sample text with some different words'
'Line 3: this has even more sample text with even more different words')

text_list=text.split()
print("Using Collection Module\n", collections.Counter(text_list))

d = dict()
words=text.split()
for word in words:
    if word in d:
        d[word]=d[word] +1
    else:
        d[word] =1
    result=sorted(d.items())     

print("\n Using dictionary\n", result)
