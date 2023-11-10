# Single Responsibility Principle
# Seperation of Concerns

# "A module should be responsible to one, and only one, actor."[1]
# The term actor refers to a group (consisting of one or more stakeholders or users) that requires a change in the module.

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count} : {text}')
    
    def remove_entry(self, pos):
        del self.entries[pos]
    
    def __str__(self):
        return "\n".join(self.entries)
    # upto this point the class has a primary purpose:
    # to add and remove entries into a journal
    # but now we are overloading the class with a secondary responsibility 
    # to save in a file or load from a file or load from a web
    # this creates god objects
    # suppose if there's other types of class like article, book, webpage etc
    # all these types need its own save and load methods
    # so what we need is a centrally changable code with single purpose
    
    # we can comment the below
    def save(self, filename):
        file = open(filename,"w")
        file.write(str(self))
        file.close()
    
    def load(self, filename):
        pass
    
    def load_from_web(self, url):
        pass
    

j = Journal()
j.add_entry("I beleive")
j.add_entry("I ate a bug")
print(f"journal entries: {j}")


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename,'w')
        file.write(str(journal))
        file.close()
    
file = r'journal.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())
        