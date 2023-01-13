//checks if any three numbers in A can make up the side lengths of a triangle
//O(nlog(n)) time complexity, and O(0) space complexity (disregrading the input array)
#include <vector>
#include <algorithm>

using std::vector;
using std::sort;
int solution(vector<int>& A) {
    sort(A.begin(), A.end());
    for (int i = 2; i < A.size(); i++) {
        if (A[i - 2] > A[i] - A[i - 1]) {
            return 1;
        }
    }
    return 0;
}