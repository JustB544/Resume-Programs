//finds the number of unique elements in A
//~O(nlogn) time complexity and ~O(n) space complexity


#include <vector>
#include <algorithm>

using std::vector;
using std::sort;

int solution(vector<int>& A) {
    if (A.size() == 0) {
        return 0;
    }
    vector<int> a = A;
    sort(a.begin(), a.end());
    int prev = a[0];
    int count = 1;
    for (int i = 1; i < a.size(); i++) {
        if (prev == a[i]) {
            continue;
        }
        count++;
        prev = a[i];
    }
    return count;
}