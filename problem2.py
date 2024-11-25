input_list = ["Book A - 6", "Book B - 10", "Book C - 5", "Book B - 8"]
# initilze dictionary
books = {} 
for i in input_list:
    title,days = i.split(" - ")
    # casting to int 
    days = int(days) 
    # add books title and days in  dictionary 
    if title not in books:
        books[title] = days
    else:
        books[title] += days
# the benifit of word key = book.get is :
#  use the key to tell Python how to make the comparison.
# in this ex to compare the value of days using (book.get)

most_borrowed =  max(books,key=books.get)
least_borrowed =  min(books,key=books.get)         
total_average = sum(books.values())/len(books)

# find uniqe titles of books
uniqe_titles = set(books.keys())


# sort books
# key=lambda item : item[1]  is used to To determine on what basis the comparison is made
#  item[1] تدل علي هختار علي اساس العنصر التاني الي هو عدد الايام
# reverse = True : sort in descending order.
sorted_books = sorted(books.items(),key=lambda item : item[1], reverse=True)


print("most borrowed =" , most_borrowed)
print("least borrowed =" , least_borrowed)
print("uniqe_titles =" , uniqe_titles)
print("sorted books", sorted_books)










