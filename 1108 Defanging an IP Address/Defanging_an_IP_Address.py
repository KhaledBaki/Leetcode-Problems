class Solution(object):
    def defangIPaddr(self, address):
        address = address.split(".")
        newAddress = "" + address[0]

        
        for i in range(1, len(address)):
            newAddress += "[.]"
            newAddress += address[i]
        
        return newAddress
