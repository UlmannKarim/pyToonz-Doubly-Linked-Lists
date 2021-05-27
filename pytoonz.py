# author Karim Ulmann

class Track:
    def __init__(self, name, artiste, timesplayed):
        self._name = name

        self._artiste = artiste

        self._timesplayed = timesplayed

    def __str__(self):
        return "%s %s (%s)" % (str(self._name), str(self._artiste), str(self._timesplayed))

    def get_name(self):
        return self._name

    def get_artiste(self):
        return self._artiste

    def play(self):
        self._timesplayed += 1
        return 'Playing: ' + self.__str__()


class DLLNode:
    def __init__(self, item, prevnode, nextnode):
        self.element = item
        self.next = nextnode
        self.prev = prevnode


class PyToonz:
    def __init__(self):
        self.head = DLLNode(None, None, None)
        self.tail = DLLNode(None, self.head, None)
        self.head.next = self.tail
        self.size = 0
        self.selector = None

    def length(self):
        return self.size

    def add_track(self, track):  # DOES THE SELECTOR MOVE ALONG WITH THE SONGS WE ADD? #KEEP SELECTOR TO TOP
        LastNode = self.tail.prev
        NewNode = DLLNode(track, None, None)
        NewNode.next = self.tail
        self.tail.prev = NewNode
        NewNode.prev = LastNode
        LastNode.next = NewNode
        if self.length() == 0:
            self.selector = NewNode
        self.size = self.size + 1

    def get_current(self):  # return the currently selected track - if the list is empty, this should return None
        if self.size == 0:
            return None
        else:
            return self.selector.element

    def add_after(self, track):
        if self.length() == 0:  # if list is empty add to list using normal method
            self.add_track(track)
        else:
            pointer = self.selector
            NewNode = DLLNode(track, None, None)
            old_next = pointer.next
            NewNode.next = old_next
            old_next.prev = NewNode
            NewNode.prev = pointer
            pointer.next = NewNode
            self.size = self.size + 1

    def next_track(self):
        hover = self.selector
        LastItem = self.tail.prev
        FirstItem = self.head.next
        if self.length() == 0:  # if playlist is empty maintain pointer to None
            self.selector = None
        elif LastItem == hover:
            self.selector = FirstItem
        else:
            self.selector = self.selector.next

    def prev_track(self):
        flare = self.selector
        if self.length() == 0:  # if playlist is empty maintain pointer to None
            self.selector = None
        elif self.head.next == flare:
            self.selector = self.tail.prev
        else:
            self.selector = self.selector.prev

    def reset(self):  # reset the current selection to the front of the list
        if self.length() == 0:
            self.selector == None
        else:
            self.selector = self.head.next

    def play(self):
        if self.selector is None:
            print('Failed to play, playlist is empty')
        else:
            print(self.selector.element.play())

    def remove_current(self):
        if self.length() == 0:
            print('Unable to remove from empty playlist')
        else:
            nxt = self.selector.next
            bfr = self.selector.prev
            if self.selector == self.tail.prev:  # if cursor hovers over last track in list
                self.selector.prev.next = nxt
                self.selector.next.prev = bfr
                self.size = self.size - 1
                self.reset()  # reset the cursor to the top
            else:  # if not the last track
                self.selector.prev.next = nxt
                self.selector.next.prev = bfr
                self.size = self.size - 1
                self.next_track()  # slide cursor lower down list

    def __str__(self):
        u = 0
        library = "Playlist: \n"
        Node = self.head.next
        while u < self.length():
            if Node == self.selector:
                library += "-->"
            library += str(Node.element.__str__()) + "\n"
            Node = Node.next
            u += 1

        return library
