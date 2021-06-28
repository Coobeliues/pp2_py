class Solution(object):
    def defangIPaddr(self, address):
        self.a = address
        return self.a.replace('.', '[.]')
