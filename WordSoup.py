from random import randint as ri
from pandas import DataFrame
from copy import deepcopy

#dimentions, words, words cant, length, table
class WordSoup:
    '''Creates a word soup'''
    #secuence, lenght
    class __Words:                                                                              #ok
        '''The class to define a new word for the word soup'''
        def __init__(self, secuence, len):
            self.secuence = secuence
            self.len = len
        @classmethod
        def auto(cls, len):
            '''Default configuration for the class "__Words"'''
            return cls([str(ri(0,9)) for v in range(len)], len)

    def __init__(self, size:tuple = (16,16), words:list = None, word_cant:int = 16, len:int = 8):
        self.size = size
        self.words = words
        self.word_cant = word_cant
        self.len = len if len >= size[0]/2 else size[0]/2
        self.table = [["/" for t in range(size[0])] for t in range(size[1])]

        self.__fill_words()
        self.__place_words()
        #self.__fill_table()

    def __fill_words(self):                                                                     #ok
        '''Verificates if words is given, and if not return the default'''
        if self.words!=None:
            self.words = [self.__Words(str(t), len(str(t))) for t in self.words]
            self.word_cant = len(self.words)
            self.len = "Unknown"
        else:
            self.words = [self.__Words.auto(self.len) for t in range(self.word_cant)]
            
    def __place_words(self):
        '''Places the words into the table'''
        for i in self.words:
            check = False
            while check != True:
                test_table = deepcopy(self.table)
                horientation = ri(1,4)
                direction = ri(0,1)
                secuence = i.secuence if direction == 0 else list(reversed(i.secuence))
                if horientation == 1:
                    #Horizontal
                    x = ri(0,self.size[0]-i.len)
                    y = ri(0,self.size[1]-1)
                    for v in secuence:
                        if self.table[y][x] == v or self.table[y][x] == "/":
                            test_table[y][x] = v
                            check = True
                        else:
                            check = False
                            break
                        x += 1
                elif horientation == 2:
                    #Vertical
                    x = ri(0,self.size[0]-1)
                    y = ri(0,self.size[1]-i.len)
                    for v in secuence:
                        if self.table[y][x] == v or self.table[y][x] == "/":
                            test_table[y][x] = v
                            check = True
                        else:
                            check = False
                            break
                        y += 1
                elif horientation == 3:
                    #Diagonal A
                    x = ri(0,self.size[0]-i.len)
                    y = ri(0,self.size[1]-i.len)
                    for v in secuence:
                        if self.table[y][x] == v or self.table[y][x] == "/":
                            test_table[y][x] = v
                            check = True
                        else:
                            check = False
                            break
                        x += 1
                        y += 1
                elif horientation == 4:
                    #Diagonal B
                    x = ri(0,self.size[0]-i.len)
                    y = ri(0,self.size[1]-i.len)
                    for v in secuence:
                        if self.table[y+i.len-1][x] == v or self.table[y+i.len-1][x] == "/":
                            test_table[y+i.len-1][x] = v
                            check = True
                        else:
                            check = False
                            break
                        x += 1
                        y -= 1
            self.table = deepcopy(test_table)

    def fill_table(self):
        self.table = [[ri(0,9) if i == "/" else i for i in v] for v in self.table]

    def get_table(self):                                                                        #ok
        '''Return the table'''
        return DataFrame(self.table)

    def get_words(self):                                                                        #ok
        '''Return a string with all the words to search'''
        return "".join(["".join(v.secuence)+"\n" for v in self.words])

if __name__ == "__main__":
    word_soup = WordSoup((10,10), None, 10, 5)
    print(word_soup.get_table())
    print("\n\n---------------------------------------------------------------------------------------------\n\n")
    word_soup.fill_table()
    print(word_soup.get_table())
    print(word_soup.get_words())
