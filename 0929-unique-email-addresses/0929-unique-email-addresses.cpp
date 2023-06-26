// time: o(n)
// space : o(n)
class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        
        set<string> unique;
        
        for(string email:emails){
            string local = email.substr(0 ,email.find('@'));
            local = local.substr(0,email.find('+'));
            local =regex_replace(local , regex("\\.") , "");
            string domain = email.substr(email.find('@') + 1 , email.length());
            email = local + '@' + domain;
            unique.insert(email);
        }
        return unique.size();
        
    }
};

/*
int main() {
    Solution solution;
    
    vector<string> emails = {
        "alice@example.com",
        "bob@example.com",
        "charlie@example.com"
    };
    
    int uniqueEmails = solution.numUniqueEmails(emails);
    
    cout << "Number of unique emails: " << uniqueEmails << endl;
    
    return 0;
}
This code creates an instance of the Solution class, initializes a vector of email addresses, calls the numUniqueEmails function, and prints the number of unique emails found.


*/


