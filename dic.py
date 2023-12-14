y={'john':40,'alex':2,'benny':32,'denny':3}
l=list(y.items())
l.sort()
print("ascending order is",l)
l=list(y.items())
l.sort(reverse=True)
print("desending order is",l)
