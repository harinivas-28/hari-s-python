n=int(input("Enter number of songs: "))
s=[]
for i in range(n):
    length=int(input("Enter length of song: "))
    s.append(length)
m=int(input("Enter the length of the song you want to search: "))
song_index=s.index(m)
print(song_index,"--> Index before Sorting")
s.sort()
print(s.index(m),"--> Index after Sorting")

