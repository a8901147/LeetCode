class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> hashmap;
        hashmap[0] = 1;
        int cursum = 0;
        int res = 0;

        for (int num: nums){
            cursum += num;
            if (hashmap.find(cursum-k) != hashmap.end()){
                res += hashmap[cursum-k];
            }

            if (hashmap.find(cursum) != hashmap.end()){
                hashmap[cursum] += 1;
            }else{
                hashmap[cursum] = 1;
            }
        }
        return res;
    }
};