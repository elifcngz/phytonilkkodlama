l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
listnew = []
def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            listnew.append(i)

flatten(l)
print(listnew)
