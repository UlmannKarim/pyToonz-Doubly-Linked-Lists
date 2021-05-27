from pytoonz import *

playlist = PyToonz()

TheRush = Track('The Rush', 'Reality Club', 0)
BoRap = Track("Bohemian Rhapsody", "Queen", 0)
Baka = Track("Bakamitai", "Kazuma Kuroda", 0)
TrapAnt = Track("Trap Anthem", "MC Virgins", 0)

playlist.add_track(TheRush)
playlist.add_track(Baka)
playlist.add_track(TrapAnt)
playlist.add_after(BoRap)

print(playlist)
playlist.play()
playlist.next_track()
print(playlist)
playlist.next_track()
print(playlist)
playlist.next_track()
print(playlist)
playlist.next_track()
print(playlist)

print(playlist.get_current())

print()
print('----------------------------------------------------')
print()

playlist.next_track()
playlist.next_track()
playlist.next_track()

print(playlist)
playlist.remove_current()
print(playlist)
#
playlist.remove_current()
print(playlist)
playlist.remove_current()
print(playlist)
playlist.remove_current()
print(playlist)

playlist.next_track()
playlist.next_track()
playlist.next_track()
playlist.reset()

playlist.remove_current()

print(playlist.get_current())

print(playlist.length(), '----------------------------here-------------------------')
playlist.play()

print(playlist)
lemonade = Track("Lemonade", "Internet Money / Gunna / Toliver", 0)
playlist.add_after(lemonade)
print(playlist)
love = Track("Love in my Pocket", "Rich Brian", 0)
playlist.add_after(love)
print(playlist)
playlist.add_track(TheRush)
print(playlist)
playlist.add_track(Baka)
print(playlist)
playlist.add_track(TrapAnt)
print(playlist)
playlist.add_track(BoRap)
print(playlist)
playlist.next_track()
print(playlist.get_current())
playlist.play()
playlist.reset()
print(playlist.get_current())
playlist.prev_track()
print(playlist)

print('---------------------------------')

print(playlist.get_current(), '------------------')

print('----------------------------------')

print(playlist.length())
print(playlist.get_current())
playlist.play()
playlist.next_track()
playlist.play()
playlist.reset()
playlist.remove_current()
print(playlist)
playlist.remove_current()
print(playlist)
playlist.remove_current()
print(playlist)
playlist.remove_current()
print(playlist)
playlist.remove_current()
print(playlist)
playlist.remove_current()
print(playlist)
playlist.remove_current()
print(playlist)
playlist.remove_current()
print(playlist)

print('---------------------------------')


