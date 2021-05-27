# pyToonz-Doubly-Linked-Lists
as part of my Algorithms and Data Structures continuous assessment.
Doubly Linked List implantation in Python, to simulate a simple playlist system for music files. 
Received a grade of 90%
 
 

Track Class
  play() increments the timesplayed field belonging to that Track,
    then return the string representation of that track.
  

DLLNode Class -> node to wrap the Track instance in
  

PyToonz Class -> the Doubly linked list with track instances
  
  length() return the number of tracks in the library
  
  add_track(track) add the given track object to the end of the list 
  
  get_current() return the currently selected track - if the list is empty, this should return None
  
  add_after(track) add the given track object after the one that is currently selected
  
  next_track() change the current selection to the next one
    when the current selection is at the last track, that the selection will wrap around the list to the first track
    
  prev_track() change the current selection to the previous one
    when the current selection is at the first track, that the selection will wrap around the list to the last
    track
  
  reset() reset the current selection to the front of the list
  
  play() plays the currently selected track -simply call the track's own play() method, and print out whatever it returns,
    or print an error message if there is no currently selected track
  
  remove_current() remove the current track from the list
  
  __str__() return a single string containing each track in the list on a separate line, 
    each track is represented by its name, artiste, and the number of times it has been played.
    The currently selected track, if any, is preceded by '--> '.
    
    
    
    
    
    
    
