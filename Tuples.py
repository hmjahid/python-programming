numTuples = (10,20,30,40,50,60,70,80)
nameTuples = ("Jahid","Alamin","Osman","Shariful")

print(numTuples[6])
print(nameTuples[2])

print(numTuples[2:7])

mixTuple = numTuples + nameTuples

print(mixTuple)

#del numTuples[3]
print(len(numTuples))

print(numTuples * 4)

for x in numTuples:
    print(x)

if 60 in numTuples:
    print("It's  a member of Tuples")
else:
    print("It's not a member of Tuples")