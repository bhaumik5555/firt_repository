import time

def num(n):
    for i in range(1, n+1):
        if i%2 == 0:
            yield i


# numbers10 = list(num(10))
# print(numbers10)

# for num in num(10):
#     print(num)

print(list(num(5)))
print(list(num(5)))


def gene_numbers(a):
    for i in range(0,a+1):
        yield i


t1=time.time()
num_list1 = gene_numbers(1000000000000000)
t2=time.time()
print(t2-t1)

t1=time.time()
num_list1 = list(gene_numbers(10000000))
t2=time.time()
print(t2-t1)