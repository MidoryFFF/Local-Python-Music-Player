from playlist_manager import PlayList

def main():
    playlist = PlayList()
    print_help_menu()

    while True:
        inn = input()
        if inn == "q":
            return
        inn = inn.split()
        print(inn)

        match (inn[0]):
            case "add":
                playlist.add_to_playlist(inn[1])
            case "rem":
                playlist.remove_from_playlist_by_index(inn[1])
            case "pri":
                print(playlist.get_playlist())
            case "ply":
                playlist.start_playlist()
            case "vol":
                if inn[1] >= 0:
                    playlist.volume = inn[1]
            case "h":
                print_help_menu()
            case _:
                print(f"Error no {inn[0]} command found")

def print_help_menu():
    print("""
add [trak_path] - add trak to playlist
rem [id] - remove trak from play list
vol [volume_value] - changing the volume value 0-100
pri - prints the playlist
ply - start playing playlist
q - quit the programm
h - show this menu
    """)

main()
