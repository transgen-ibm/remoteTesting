
# <START-OF-CODE>

pandu, vundu, urdu = map(int, raw_input().split())
c = 0
for i in range(1, urdu+1):
    c += i * pandu
if c < vundu:
    print "0"
else:
    print c - vundu

# 