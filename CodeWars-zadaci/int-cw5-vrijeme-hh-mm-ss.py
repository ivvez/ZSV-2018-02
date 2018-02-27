#napisi program koji unosi vrijeme u sekundama te ga ispisuje u formatu HH:MM:SS

s=int(input())
print ('{:02}:{:02}:{:02}'.format(s // 3600, s // 60 % 60, s % 60))
