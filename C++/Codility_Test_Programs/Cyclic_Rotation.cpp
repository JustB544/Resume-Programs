//Cycles an array A, K amount of steps to the right
//~O(n) time complexity and ~O(k) space complexity (disregarding the input array)

#include <vector>

using std::vector;

vector<int> solution(vector<int>& A, int K) {
    vector<int> save;
    if (A.size() == 0) {
        return A;
    }
    int k = K % A.size();
    for (int i = 0; i < k; i++) {
        save.push_back(A[A.size() - k + i]);
    }
    for (int i = A.size() - k; i > 0; i--) {
        A[i + k - 1] = A[i - 1];
    }
    for (int i = 0; i < k; i++) {
        A[i] = save[i];
    }
    return A;
}