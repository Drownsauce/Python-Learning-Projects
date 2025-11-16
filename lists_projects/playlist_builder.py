#Travis Delcambre

#empty list that takes strings
song_playlist: list[str]  = []

#loops through program
while True:
    #ask user to input the option # they want
    while True:
        try:
            user_choice = int(input("""Choose option:
            (1. Add song / 2. Remove song / 3. Check if song exists / 4. View playlist / 5. View reversed playlist / 6. Top N songs)
            > """))
            break
        except ValueError:
            print("Must be an integer!")

    #match case to quickly evaluate user_choice
    match user_choice:
        case 1:
            song_name = input("Enter song: ")
            song_playlist.append(song_name)

        case 2:
            song_name = input("Enter song: ")
            if song_name in song_playlist:
                song_playlist.remove(song_name)

        case 3:
            song_name = input("Enter song: ")
            if song_name in song_playlist:
                print(f"{song_name} is at index {song_playlist.index(song_name)}")

        case 4:
            for index, song in enumerate(song_playlist, start=1):
                print(f"{index}. {song}")

        case 5:
            song_playlist.reverse()
            for index, song in enumerate(song_playlist, start=1):
                print(f"{index}. {song}")

        case 6:
            while True:
                try:
                    num = int(input("Top x Songs: "))
                    break
                except ValueError:
                    print("Must be an integer")
            #Don't know why this is an error
            if num <= len(song_playlist):
                slice_end_index = num
                top_songs = song_playlist[:slice_end_index]
                print(top_songs)
            else:
                print(song_playlist)

        case _:
            break