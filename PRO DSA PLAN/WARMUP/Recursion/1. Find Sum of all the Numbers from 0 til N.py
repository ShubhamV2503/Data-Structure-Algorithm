
# https://docs.google.com/document/d/1sZW6PuHeSrkxmlMbD5e96ZWHrIWlrjL1KRabd52Z6hI/edit?usp=sharing


def recursion(n):

    if n == 0:
        return 0  ## Now process start to send answer upward
    
    return n + recursion(n-1)


n = 10
print(recursion(n))





