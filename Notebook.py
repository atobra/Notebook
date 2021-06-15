import datetime

last_id=0

class Note:
    '''Represents a note in the notebook with its tag attached to it.
       Also filters and brings out results from a search'''
    def __init__(self,memo,tag=''):
        '''Initializes a note with a memo and optional space-separated tags.
           Also automatically sets the creation date and note's unique id'''
        self.memo=memo
        self.tag=tag
        self.creation_date=datetime.date.today()
        global last_id
        last_id +=1
        self.id=last_id

    def match(self,filter):
        '''Returns true if search is found in either notes or tags

           Search is case-sensitive'''
        return filter in self.memo or filter in self.tag
    

class Notebook:
    '''Represents a collection of notes that can be searched, tagged and modified'''

    def __init__(self):
        'Initializes notebook with an empty list'
        self.notes=[]

    def new_note(self,memo,tag=""):
        """Adds a new note to the notebook"""
        self.notes.append(Note(memo,tag))

    def _find_note(self,note_id):
        """Finds the note with the specificied unique id"""
        for note in self.notes:
            if note.id==note_id:
                return note
        return None
        
    def modify_memo(self,note_id,memo):
        """Modifies the content of a note using its unique id"""
        self._find_note(note_id).memo=memo
            
    def modify_tag(self,note_id,tag):
        """Modifies the tag of a note using its unique id"""
        self._find_note(note_id).tag=tag

    def search(self,filter):
        '''Find all notes that match the given filter string'''
        return [note for note in self.notes if note.match(filter)]
