class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> hashmap;

        for (string word: strs){
            string sorted_word = word;
            sort(sorted_word.begin(), sorted_word.end());
            hashmap[sorted_word].push_back(word);
        }

        vector<vector<string>> result;
        // for (const auto& p : hashmap) {
        //     result.push_back(p.second);
        // }

        for (auto p = hashmap.begin(); p != hashmap.end(); p++) {
            result.push_back(p->second);
        }

        return result;
    }
};