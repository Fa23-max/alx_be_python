class Book:
  def __init__(self,title,author):
    self.title = title
    self.author = author
    self.__is_checked_out = False
    Book.no_of_Books += 1
  
  def set_checkOut(self):
    self.__is_checked_out = True
  
  def return_book(self):
    self.__is_checked_out = False

  def get_checkout(self):
    return self.__is_checked_out

  
class Library:
  def __init__(self):
    self._books = []

  def add_book(self,Book):
    self._books.append(Book)

  def get_books(self):
    return self._books
  
  def check_out_book(self,title):
    for item in self._books:
      if title == item.title:
        item.set_checkOut()
        break
  
  def return_book(self,title):
    for item in self._books:
      if title == item.title:
        if item.get_checkout():
          item.return_book()
        break

  def list_available_books(self):
    to_print = []
    for item in self._books:
      if not item.get_checkout():
        to_print.append(f"{item.title} by {item.author}")
    for str in to_print:
      print(str)