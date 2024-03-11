class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        for (int r=0;r<matrix.size()/2; r++){
            int reverse = matrix.size()-1-r;
            swap(matrix[r],matrix[reverse]);
        }

        for (int r=0;r<matrix.size(); r++){
            for (int c=r+1;c<matrix[0].size(); c++){
                swap(matrix[r][c],matrix[c][r]);
            }
        }
    }
};