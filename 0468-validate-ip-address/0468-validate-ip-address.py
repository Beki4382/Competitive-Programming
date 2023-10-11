class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.isIPv4(IP):
            return "IPv4"
        elif self.isIPv6(IP):
            return "IPv6"
        else:
            return "Neither"
    
    
    def isIPv6(self, IP) -> bool:
        arr = IP.split(':')
        if len(arr) != 8:
            return False
        for val in arr:
            if len(val) > 4 or len(val) == 0:
                return False
            elif self.isValidHexa(val):
                continue
            else:
                return False
        return True
    
    def isIPv4(self, IP) -> bool:
        arr = IP.split('.')
        if len(arr) != 4:
            return False
        for val in arr:
            if len(val) > 1 and val[0] == '0':
                return False
            if val.isdigit() and int(val) <= 255:
                continue
            else:
                return False
        return True
    
    def isValidHexa(self, val) -> bool:
        if val.isdigit():
            return True
        for char in val:
            if char.isdigit():
                continue
            elif ord(char) >= ord('a') and ord(char) <= ord('f'):
                continue
            elif ord(char) >= ord('A') and ord(char) <= ord('F'):
                continue
            else:
                return False
        return True