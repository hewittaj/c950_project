class HashMap:
    def __init__(self):  # References fig 7.8.1 from ZyBooks and https://www.youtube.com/watch?v=9HFbhPscPU0
        # Set size equal to 10 as we want to have a smaller map, and can just linear search for packages beyond that
        self.size = 10
        self.map = [None] * self.size

    """
    Create a hash value for the function. 
    We mod 100 as our the number of packages IDs are currently less than 100.
    """
    def create_hash(self, key):
        return int(key) % len(self.map)

    """
    Insert a package into our hash table using the create_hash function.
    References figure 7.8.2 in the book.
    """
    def insert(self, key, value):
        hash_key = self.create_hash(key)  # Get the index value where we will place package
        key_value = [key, value]  # What we actually want to insert into that cell
        if self.map[hash_key] is None:  # If index is empty then we will simply add to the list our key and value(s)
            self.map[hash_key] = list([key_value])
            return True

        else:
            # Check for a match in the map
            for match in self.map[hash_key]:
                # If it matches the current key, update the value
                if match[0] == key:
                    match[1] = value
                    return True
                # If it doesn't match, we will append the value
                self.map[hash_key].append(key_value)
                return True

    """
    This function gets the value if it matches at the cell
    """
    def get_val(self, key):
        hash_key = self.create_hash(key)
        if self.map[hash_key] is not None:
            for match in self.map[hash_key]:
                if int(match[0]) == key:
                    return match[1]
        return None

    """
    This function deletes the value from the hash map
    """
    def delete(self, key):
        hash_key = self.create_hash(key)
        if self.map[hash_key] is None:
            return False
        else:
            for i in range(0, self.map[hash_key]):
                if self.map[hash_key][i][0] == key:
                    self.map[hash_key].pop(i)
                    return True
                return False
