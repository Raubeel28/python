class books:

    total_pages =0
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
        books.total_pages+=pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    def __eq__(self,other):
        return self.title == other.title and self.author==other.author
    def __lt__(self,other):
        return self.pages < other.pages
    def __gt__(self,other):
        return self.pages > other.pages
    @classmethod

    def pg(cls):
        return f"The total number of pages in all books combined is {cls.total_pages}"
    
    def __add__(self,other):
        return self.pages + other.pages
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self,key):
        if key == "title":
            return self.title
        else:
            return f"key {key} was not found"

book1=books("harry potter","Pablo Excobar",754)
book2=books("The Hobbit","Calvin clein",847)
book3=books("The lion King","Lion Father",847)

print(book1)
print(book1==book2)
print(book2<book1)
print(book2>book1)
print(books.pg())
print(book1+book2)
print("Lion" in book3)
print(book1['hello'])