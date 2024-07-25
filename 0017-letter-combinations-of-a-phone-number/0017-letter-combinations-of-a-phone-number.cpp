class Solution {
public:
    vector<string> letterCombinations(string digits) {
        this->digits = digits;
        if (!digits.size()){
            return {};
        }
        vector<string> res;
        string part;
        backtrack(res, part, 0);
        return res;
    }
private:
    string digits;
    void backtrack(vector<string> &res, string &part, int cur){
        if (cur == digits.size()) {
            res.push_back(part);
            return;
        }

        unordered_map<char, string> digitToChar = {
            {'2', "abc"}, {'3', "def"}, {'4', "ghi"},
            {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"},
            {'8', "tuv"}, {'9', "wxyz"}
        };

        for (char c: digitToChar[digits[cur]]){
            part.push_back(c);
            backtrack(res,part,cur+1);
            part.pop_back();
        }
    }
};