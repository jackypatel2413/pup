def multiply(num):
    return num*num
# result=map(multiply,[2,4,6,8])
result=map(lambda i:i*i,(2,4,6,8))
print(list(result))