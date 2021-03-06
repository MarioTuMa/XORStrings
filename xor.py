import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False



if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)



final = ""
counter = 0
keylen = len(key)
for char in inp:
    char = ord(char) ^ ord(key[counter%keylen])
    if mode == "human":
        final+=chr(char)
    if mode == "numOut":
        final+=str(hex(char)[2:]) + " "
    counter+=1
print(final)