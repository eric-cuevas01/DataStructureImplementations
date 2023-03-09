import Book
# import ArrayList
# import ArrayQueue
# import RandomQueue
import DLList
import SLLQueue
# import ChainedHashTable
# import BinarySearchTree
# import BinaryHeap
# import AdjacencyList
import MaxQueue
import time


class BookStore:
    """
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart.
    """

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = MaxQueue.MaxQueue()

    def loadCatalog(self, fileName: str):
        """
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key,
                title, group, rank (number of copies sold) and similar books
        """
        self.bookCatalog = DLList.DLList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
            # The following line is used to calculate the total time
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        """
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input:
            i: positive integer
        """
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        """
        addBookByIndex: Inserts into the playlist the song of the list at index i
        input:
            i: positive integer
        """
        # Validating the index. Otherwise it  crashes
        if 0 <= i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix : str, cnt : int):
        """
        searchBookByInfix: Search all the books that contains infix
        input:
            infix: A string
        """
        start_time = time.time()
        found = 0
        for book in self.bookCatalog:
            if infix in book.title:
                print(book)
                found += 1
                if found >= cnt:
                    break
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        """
        removeFromShoppingCart: remove one book from the shopping cart
        """
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        """
        getCartBestSeller: prints the title of the book that is the bestseller amongst the rest of the books in the cart
        """
        if self.shoppingCart.size() > 0:
            print('getCartBestSeller returned')
            print(f"The best-seller in the shopping cart is {self.shoppingCart.max().title}")
        else:
            print("The shopping cart is empty.")
