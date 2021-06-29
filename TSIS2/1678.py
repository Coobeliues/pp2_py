class Solution(object):
    def interpret(self, command):
        self.a=command
        res=''
        i=0
        while i<len(self.a):
            if self.a[i]=='G':
                res+='G'
                i+=1
            elif self.a[i]=='(':
                if self.a[i+1]==')':
                    res+='o'
                    i+=2
                elif self.a[i+1]=='a':
                    res+='al'
                    i+=3
            else:
                i+=1
                continue
        return res

# class Solution:
#     def interpret(self, command: str) -> str:
#         s = command.replace("()","o")
#         s = s.replace("(al)","al")
#         return s