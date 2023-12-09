
def get_string_with_removed_chars(st, *chars_to_quit):
    st_to_return = ''
    for char in st:
        if char in chars_to_quit:
            st_to_return += ''
        else:
            st_to_return += char
    return st_to_return

        
