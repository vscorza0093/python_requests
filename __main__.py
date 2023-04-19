import requests
import iterator_class

if __name__ == "__main__":

    #iterator_object = iterator_class.BitcoinIterator("ethereum")
    iterator_object = iterator_class.BitcoinIterator("bitcoin")


    print(len(iterator_object.prices))

    i = 0
    for price in iterator_object:
        i += 1
        print(price)
