
songs = ["Espresso", "Flowers", "Cruel Summer", "Vampire"]

#print(songs[0])      # first item  → index 0
#print(songs[2])      # third item  → index 2
#print(songs[-1])     # last item   → negative index counts from the end!
print("The number of songs is", len(songs))
songs.append("Human nature")
print(songs, len(songs))
songs[len(songs)-1] = "Du Bist gut genug"
print(songs, len(songs))
