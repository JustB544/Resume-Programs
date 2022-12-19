//given an array with one element that occurs an odd number of times, returns that number
//~O(n) time complexity and ~O(1) space complexity (disregarding the input array)

#include<vector>

using std::vector;

int solution(vector<int>& A) {
    int x = 0;
    for (int i = 0; i < A.size(); i++) {
        x ^= A[i];
    }
    return x ^ 0;
}