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