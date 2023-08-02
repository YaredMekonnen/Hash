class ChainedHashMap:
    def __init__(self,size=10):
        self.__size = size
        self.__slots = []
        #loop to create an empty list
        #chained to each slot
        for s in range(self.__size):
            self.__slots.append([])
        self.__length = 0
        
    def hash_function(self,key):
         return hash(key)%self.__size
        
    def put(self,key,value):
        hash_value = self.hash_function(key)
        
        if  self.__slots[hash_value] == []:
            self.__slots[hash_value] = [ (key,value) ]
            self.__length += 1
        else:
            #check if this key is already in the list at this slot
            for item_num in range(len(self.__slots[hash_value])):
                #if the tuple's key matches the new key
                if self.__slots[hash_value][item_num][0] == key:
                    #replace the current value at this position with the new value
                    self.__slots[hash_value][item_num][1] = value
                    return #exits early
                
            #if we haven't exited yet, put a new tuple on the end of this list
            #and increase the length of the map by 1
            self.__slots[hash_value].append( (key,value) )
            self.__length += 1
            
    def get(self,key):
        hash_value = self.hash_function(key)
        
        if self.__slots[hash_value] == []:
            return None
        else:
            for item in self.__slots[hash_value]:
                if item[0] == key:
                    return item[1]
        return None
    
    def __len__(self):
        return self.__length
            
    
    def __repr__(self):
        
        rstring = ""
        
        for slot_num in range(self.__size):
            rstring += str(slot_num)+":"+str(self.__slots[slot_num])+"\n"
        
        return rstring
    
    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)
    def remove(self, key):
        hash_value = self.hash_function(key)
        if self.__slots[hash_value]:
            for item_num in range(len(self.__slots[hash_value])):
                if self.__slots[hash_value][item_num][0] == key:
                    del self.__slots[hash_value][item_num]
                    self.__length -= 1
                    return
        raise KeyError(f"Key '{key}' not found in the map.")
    
    def __contains__(self, key):
        hash_value = self.hash_function(key)

        if self.__slots[hash_value] == []:
            return False
        else:
            for item in self.__slots[hash_value]:
                if item[0] == key:
                    return True
        return False

cht = ChainedHashMap()
cht[54]="cat"
cht[26]="dog"
cht[93]="lion"
cht[17]="tiger"
cht[77]="bird"
cht[31]="cow"
cht[44]="goat"
cht[55]="pig"
cht[20]="chicken"

print(cht)


print(cht[54])
print(cht[44])
print(cht[12])
print(cht[10])
print(cht[20])
cht.remove(44)
cht.remove(17)
cht.remove(20)
print()
print( 54 in cht ) #True
print( 44 in cht ) #True
print( 12 in cht ) #False
print( 10 in cht ) #False
print( 20 in cht ) #True
print( len(cht) )
