class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        ## create a hashset to store unique stringd
        unique = set()
        
        for e in emails:
            ## split the string before @ symbol as local and after @ symbol as domain
            local,domain = e.split("@")
            ##consider local that are before + sign and 0 indicates just before the + sign
            local = local.split("+")[0]
            local = local.replace("." , "")
            unique.add((local,domain))
            
        return len(unique)     
    
    
##emails = ["test.email+foo@example.com", ##"test.email.bar@example.com", "test.email@example.com"]
##solution = Solution()
##result = solution.numUniqueEmails(emails)
##print(result)

        