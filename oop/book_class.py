class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        #user = input(f"Do you want to delete the {self.title} ? (y/n): ").lower()
        #if user == 'y':
        print(f"Deleting {self.title}")
        #else:
         #   pass
        
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    