'''
   CS5001
   Fall 2022
   Elif Tirkes 
   Homework 5: REMIX MASTER!
'''

import music

MENU = [ "L", "T", "S", "P", "R", "X", "Q"]
# putting menu items in a global list to sort and match

SYMBOLS = ",.!?"
# defining punctuation and operation for
# seperation & distinction of menu items 

# retrieve song and playlist
# from imported file and store in a global variable 
PLAYLIST = music.PLAYLIST
SONG = music.SONGS


def main():
    playlist = PLAYLIST.copy()
    songs = SONG.copy()
    # makes an immediate copy of the playlist and songs
    # to allow for safe mutation of the original list

    # begin remix master with copies
    # of imported playlist and songs 
    remix_master(playlist, songs)


def get_input():
    '''
    Function -- get_input
        gets the user's input and choice
        from the available menu option
        if input value is not a valid
        menu option, prompts the user
        to try again. 
    Parameters:
        N/A
    Returns the user's selection
    in upper case if it is a valid menu option. 
    '''
    selection = input(" Your choice: ").upper()
    while selection not in MENU:
        selection = input("Invalid input, \
    please enter a valid menu option: " ).upper()
    return selection

def load_selection(selection, song_choice, backup_copy, playlist):
    '''
    Function -- load_selection 
        takes in the user's selection
        from the menu, and prompts the
        appropriate function based on the
        selection value. Imports song choice
        to prompt other functions with the
        selected song. 
    Parameters:
        selection -- str, user's menu selection
        song_choice -- list, representing the current
                        song and title
        backup_copy -- list, unmodified current song
        playlist -- list, titles of all songs 
        
    Returns the current song and the backup copy
    of the current song 
    '''
    # load a new song 
    if selection == "L":
        next_selection = get_song(playlist)
        song_choice[0].clear()
        # clears all elements of the selection list to
        # get a new song choice  
        
        # make a copy of the song to preserve
        # it from modifications 
        for index in range(len(next_selection[0])):
            song_choice[0].append(next_selection[0][index])
        song_choice[1] = next_selection[1]

        backup_copy = next_selection[0]
    # title of current song 
    elif selection == "T":
        show_title(song_choice)
    # substitute a word 
    elif selection == "S":
        create_substitute(song_choice)
    # playback current song 
    elif selection == "P":
        play_song(song_choice) 
    # reverse current song 
    elif selection == "R":
        song_choice[0] = reverse_it(song_choice[0])
    # reset to original song 
    else: # for selection "X" since "Q" is covered in remix_master
        song_choice = reset(song_choice, backup_copy)

    return song_choice, backup_copy

def play_song(song_choice):
    '''
    Function -- song_choice  
        prints a prompt statement,
        and then prints the value of the
        current song choice which is a list,
        prints a little musical design after
        the list is displayed. 
    Parameters:
        song_choice -- list containing the
            current selected song and title 
    Returns nothing, prints the current song
    choice 
    '''
    print("Turn up the 808's and drop the beat! here's your remix: ")

    for content in song_choice[0]:
        # song choice [0] are the lyrics 
        print(content)
        # prints the selected song_choice

    print(20 * "~♫")
 

def show_title(song_choice):
    '''
    Function -- show_title
        prints the title
        of the current selected
        song in a user interface
        friendly f print statement 
    Parameters:
        song_choice -- list containing the
            current selected song and title 
    Returns nothing, prints the current song
    title 
    '''
    title = song_choice[1]
    # song choice [1] is the title
    # of the selected song
    
    print(20 * "~♫")
    print(f"You are mixing the song: {title}")


def show_playlist(playlist):
    '''
    Function -- show_playlist
        prints all titles of the
        playlist to the user
        by enumerating the list using
        a for loop for each value 
    Parameters:
        playlist -- imported list containing
        all song titles 
    returns nothing, prints the list of
    available songs 
    '''
    for index, title in enumerate(playlist):
        print(f"{index + 1} : {title}")
        # lists all the songs in the playlist to the user
    print()

def get_new_selection():
    '''
    Function -- get_new_selection  
       prompts user for a digit input
       to switch songs based on available
       playlist options. Prompts a new
       value if input is not valid. If
       input is valid, returns the new song
       selection to be used by other functions. 
    Parameters:
        N/A
    Returns new, verified song choice
    from playlist 
    '''
    new_selection = input("Your choice: ").upper()
    
    while new_selection.isdigit() is False:
        new_selection = input("Sorry, please enter again: ").upper()
        
    new_selection = int(new_selection)
    return new_selection

def get_song(playlist):
    '''
    Function -- get_song
        shows the available playlist,
        prompts user for a new selection
        via the get_new_selection function,
        and loads the new song based on the
        new selection, and stores it in a
        variable called new_selection.
        Verifies that the user input is valid,
        prompts for a new input if it is not
        by running the functions again.
        returns new selection. 
    Parameters:
        playlist -- list containing
        titles of all available songs 
    Returns value of te new
    song selection 
    '''
    show_playlist(playlist)
    # displays playlist to user 
    selection = get_new_selection()
    # prompts for a new selection from user
    new_selection = load_song(selection)
    # loads the valid song selection 
    
    while not new_selection:
        # verifying that the input is valid 
        print("Sorry, your input is out of range")
        selection = get_selection()
        new_selection = load_song(selection)
    return new_selection


def create_substitute(song_choice):
    '''
    Function -- create_substitute
        substitutes new user-picked words
        into an existing word in the current song
        choice. Checks whether user-input old
        word exists in the song using the
        substitute function. prints error
        message if the word does not exist. 
    Parameters:
        song_choice -- list containing current
        song and title 
    Returns a mutated version of the current
    selected song as a value. 
    '''
    old_word = input("What word do you want to"
                     "replace in the existing song? ").strip().lower()
    new_word = input("What new word do you want to"
                     "use for the song? ").strip().lower()

    song = song_choice[0]
    value = substitute(song, old_word, new_word)
    
    if value is True:
        # if the substitute() function returns false,
        # then the old word does not exist
        # in the current song 
        song_choice[0] = song
    else:
        print(f"Sorry. I didn't find {old_word} in the existing song.")

def substitute(song, old_word, new_word):
    '''
    Function -- substitute 
        inputs the current song, old word,
        and new word that the user wants to
        substitute from create_substitute().
        sets a bool value, runs through the
        content of the current selected song,
        creates spaces using split(), strips
        symbols, and matches stripped list
        value to every element in the song
        list. if the content matches the
        old word, replaces old word with
        the new word. 
    Parameters:
        song -- list containing multiple strings with
            lyrics
        old_word -- str user input old_word
        new_word -- str user input new word to substitute 
    Returns the bool called value,
    and mutated list of the song choice with the desired
    old word substituted, if the bool is true. 
    '''
    value = False
    # sets a bool value to return based on whether the words
    # are successfully substituted or not 
    
    for index, content in enumerate(song):
        content_list = content.split(' ')
        # splits str to list and adds spaces to each
        
        for word_index in range(len(content_list)):
            content_list[word_index] = content_list[word_index].strip(SYMBOLS)
            
            if content_list[word_index].lower() == old_word:
                # if lower case input of old word
                # matches a lyric, replace
                # with new word 
                content_list[word_index] = new_word
                value = True
                
        song[index] = ' '.join(content_list)
        # joins words after splitting to search the
        # song list 

    return value
    # returns a bool value indicating whether the
    # substitution was successful 

def reset_song(song_choice, backup_copy):
    '''
    Function -- reset_song
        resets the selected song choice
        back to its original copy by matching it
        with the backup copy made of the song
    Parameters:
        song_choice -- list containing current
            song lyrics and title
        backup_copy -- list containing the
            original song lyrics and title
            of selected song 
    Returns the original song_choice lyrics
    for the selected song 
    '''
    song_choice[0] = backup_copy.copy()
    # copies the copy to avoid mutating the
    # backup copy 
    return song_choice


def reverse_it(song):
    '''
    Function -- reverse_it
        reverses all the words in the
        list for the current selected song
    Parameters:
        song -- list containing the
        contents of the current selected
        song 
    Returns a mutated, reversed
    version of the current selected song 
    '''
    for index, content in enumerate(song):
        content_list = content.split(' ')
        # splits the song into a list 
        content_list = content_list[-1::-1]
        # reverses the list and stores it in
        # the original content list value 
        
        for word_index in range(len(content_list)):
            content_list[word_index] = content_list[word_index].strip(SYMBOLS)
            # strips and joins the symbols after reversing the song 
            song[index] = ' '.join(content_list)
    return song


def remix_master(playlist, songs):
    '''
    Function -- remix_master 
        welcomes the user, starts program
        by defaulting to the first song in the
        playlist. Creates a backup copy of the
        default selection, plays the default
        selection, and sends user to
        load_selection to pick from the menu
        and get a new input
        as long as the user input
        does not == to 'Q', which would prompt
        the program to end. 
    Parameters:
        playlist -- imported list of song titles
        songs -- imported list of song content 
    Returns nothing 
    '''
    
    # Play the default song, prompt welcome 
    print("Welcome to ReMix-Master. You can remix the greatest hits!")
    default_selection = [songs[0], playlist[0]]
    # makes the first song in the playlist the default selection 

    # create value song_choice to store initial values 
    song_choice = [[], []]
    # creates an empty nested list to store choice selection 
    
    for index in range(len(default_selection[0])):
        song_choice[0].append(default_selection[0][index])
        # appends the chosen number to the default choice
        
    song_choice[1] = default_selection[1]
    
    backup_copy = default_selection[0]
    # backs up the song 
    selection = "P"
    # plays the song on first boot by selecting P 

    # Step 3: Load ReMix-Master
    while selection != "Q": # quits the remix master if choice is Q  
        song_choice, backup_copy = load_selection(selection,
                                                  song_choice,
                                                  backup_copy,
                                                  playlist)
        show_menu()
        selection = get_input()

def show_menu():
    '''
    Function -- show_menu 
        prints the available menu to the user  
    Parameters:
        N/A
    Returns nothing
    '''
    print("\nReMix-Master:\n"
          " L: Load a different song\n"
          " T: Title of current song\n"
          " S: Substitute a word\n"
          " P: Playback your song\n"
          " R: Reverse it!\n"
          " X: Reset it\n"
          " Q: Quit?\n")


def load_song(selection):
    '''
    Function -- load_song  
        loads the song that the user selected.
        adjust the index of the user selection
        to the actual index. Returns empty
        list if selection is out of range,
        changing nothing.
        If selection is valid, places the
        correct values for the song choice
        in the song_choice variable to be
        used in other functions. 
    Parameters:
        selection -- int, number
        corresponding the the song that the
        user wants to choose 
    Returns new value of song_choice 
    '''
    index = selection - 1
    # makes sure to map user-centered selection to index by minusing 1
    
    if selection <= 0 or selection > len(PLAYLIST):
        empty = []
        return empty
        # returns an empty list if the user selection is out of range
        
    else:
        song_choice = [SONG[index], PLAYLIST[index]]
        return song_choice
        # loads the song choice if the user selection
        # corresponds to a song in the playlist 


if __name__ == "__main__":
    main()
