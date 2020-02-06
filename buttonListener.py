import msvcrt


def buttonListener():
    """
    A function that once called for will listen for a a T press or a Q press, when this occurs the 
    """
    while True:
        if msvcrt.kbhit():
            key_hit = msvcrt.getch()
            if (key_hit == b't' or msvcrt.getch == b'T'):
                print("Get ready to rumble!!!")
                # TODO insert initialization of the tournament realm
                break

            if (key_hit == b'q' or msvcrt.getch == b'Q'):
                print("See you next time!")
                break
                
