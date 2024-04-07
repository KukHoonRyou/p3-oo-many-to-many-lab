class Author:
    
    all = []

    def __init__ (self, name):
        self.name=name
        Author.all.append(self)

    #     self._contracts = []
    #     self._books = []

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    # def add_contract(self, contract):
    #     if not isinstance(contract, Contract):
    #         raise Exception("contract must be instance of Contract class")
    #     else:
    #         self._contracts.append(contract)
        
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
    
    # def add_book(self, book):
    #     if not isinstance(book, Book):
    #         raise Exception("book mush be instance of Book class")
    #     else:
    #         self._books.append(book)

class Book:

    all = []

    def __init__ (self, title):
        self.title=title
        Book.all.append(self)
    #     self._contracts = []

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    # def add_contract(self, contract):
    #     if not isinstance(contract, Contract):
    #         raise Exception("contract must be instance of Contract class")
    #     else:
    #         self._contracts.append(contract)

    def authors(self):
        return [contract.author for contract in self.contracts()]
    
    # def add_author(self, author):
    #     if not isinstance(author, Author):
    #         raise Exception("author mush be instance of Author class")
    #     else:
    #         self._authors.append(author)


class Contract:

    all = []

    def __init__ (self, author, book, date, royalties):
        self.author=author
        self.book=book
        self.date=date
        self.royalties=royalties
        Contract.all.append(self)
        
        if not isinstance(author, Author):
            raise Exception("author must be instance of Author class")
        
        if not isinstance(book, Book):
            raise Exception("book must be instance of Book class")
        
        if not isinstance(date, str):
            raise Exception("date must be str")
        
        if not isinstance(royalties, int):
            raise Exception("royalties must be int")
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]