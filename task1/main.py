from lib import *

create_shelve_links({}, "links_repository.dat")
while 'off':
    choice = input("Press 'off' if you want to exit: ").strip().lower()
    if choice == 'off':
        break

    add_link_to_shelve(input_link(), "links_repository.dat")

display_links("links_repository.dat")

add_link_to_shelve(input_link(), "links_repository.dat")
display_links("links_repository.dat")
