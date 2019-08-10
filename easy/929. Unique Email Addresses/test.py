# https://leetcode.com/problems/unique-email-addresses/

addresses = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
    
        addressList = []
        for email in emails:
            local, domain = splitAddresses(email)
            acutualAddress = getActualAddresses(local, domain)
            if acutualAddress not in addressList:
                addressList.append(acutualAddress)
    
        return len(addressList)
    
def splitAddresses( address):
    [local,domain] = address.split("@")
    return local, domain


def dotAddresses( address ):

    parts = address.split(".")
    result = ""
    for part in parts:
        result += part
    return result

def plusAddresses(address):
    parts = address.split("+")
    return parts[0]



def getActualAddresses(local, domain):
    local = plusAddresses(local)
    local = dotAddresses(local)

    return local+"@"+domain