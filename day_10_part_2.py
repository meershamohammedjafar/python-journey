"""8-6. City Names: Write a function called city_country() that takes in the name 
of a city and its country. The function should return a string formatted like this:
 "Santiago, Chile"
 Call your function with at least three city-country pairs, and print the 
values that are returned."""

import os
os.system('cls')

def city_country(city, country):
    return f"{city}, {country}".title()

for i in range(3):
    print(city_country('malappuram', 'india'))


"""8-7. Album: Write a function called make_album() that builds a dictionary 
describing a music album. The function should take in an artist name and an 
album title, and it should return a dictionary containing these two pieces of 
information. Use the function to make three dictionaries representing different 
albums. Print each return value to show that the dictionaries are storing the 
album information correctly.
 Use None to add an optional parameter to make_album() that allows you to 
store the number of songs on an album. If the calling line includes a value for 
the number of songs, add that value to the album’s dictionary. Make at least 
one new function call that includes the number of songs on an album."""

def make_album(artist_name, album_title, songs_number=None):
    song_dict = {'name': artist_name, 'album': album_title}

    if songs_number:
        song_dict['song'] = songs_number
    
    return song_dict

for i in range(3):
    enter_name = input("Enter the name of the Artist : ")
    enter_album_name = input("Enter the name of the album : ")
    print(make_album(artist_name=enter_name, album_title=enter_album_name))


