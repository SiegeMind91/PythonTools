import numpy

numpy.set_printoptions(sign=' ')
a = numpy.array(input().split(),float)

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))

#Sum and Prod
lines, count = map(int, input().split())
arr = numpy.array([input().split() for _ in range(lines)], int)
print(numpy.prod(numpy.sum(arr, axis=0)))

#Min and Max
lines, count = map(int, input().split())
arr = numpy.array([input().split() for _ in range(lines)], int)
print(numpy.max(numpy.min(arr, axis=1)))

#Mean, Var, Std
lines, count = map(int, input().split())
arr = numpy.array([input().split() for _ in range(lines)], int)
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis = 0))
print("{:.11f}".format(numpy.std(arr, axis=None))) #The formatting on this one was due to some bugs that HackerRank hadn't fixed yet

