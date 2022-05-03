import creation as cr
"""
functions used by this:

    get_character(name = 'character') returns character
    conception(character_name = None) returns character
    refine_character(character, points) returns character
    points = []
        att_priority = [None, None, None]
        att_points_available = [7, 5, 3]
        abi_priority= [None, None, None]
        abi_points_available = [13, 9, 5]

        p = [att_priority, att_points_available,
            abi_priority, abi_points_available]

    get_at_depth(char, stat) returns the value of char.stat
    set_at_depth(char, stat, to) sets value of char.stat to to
    mirror(char) prints character to console

    load(char) returns character from file
    save(char) saves character to file(char.name)
"""
# i think this needs to be a template engine

# the smart thing to do would be to output the files we need

# dynamically linking them so we don't have to worry if they are
