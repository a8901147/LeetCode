class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        sort(candidates.begin(),candidates.end());
        vector<int> part;
        backtrack(candidates, target, 0, 0, part, res);
        return res;
    }
    
private:
    void backtrack(const vector<int>& candidates, int target, int pos, int count, vector<int>& part, vector<vector<int>>& res) {
        if (count == target) {
            res.push_back(part);
            return;
        }

        for (int i = pos; i < candidates.size(); ++i) {
            if (i > pos && candidates[i] == candidates[i - 1]) continue;

            int nxt_count = count + candidates[i];
            if (nxt_count > target) break;

            part.push_back(candidates[i]);
            backtrack(candidates, target, i + 1, nxt_count, part, res);
            part.pop_back();
        }
    }
};