//counts the number of 2 disk overlaps between disks located at (i, 0) with radius A[i] (returns -1 when output is greater than 10,000,000)
// runs in less than O(b*n) time complexity where b is the largest radius in A, and ~O(n) space complexity
#include <vector>

using std::vector;

int solution(vector<int>& A) {
    long min[A.size()], max[A.size()], maxR = -1, finalCount = 0;
    for (long i = 0; i < A.size(); i++) {
        if (A[i] > maxR) {
            maxR = A[i];
        }
        min[i] = i - A[i];
        max[i] = i + A[i];
    }

    for (long i = 0; i < A.size(); i++) {
        for (long j = 1; j <= maxR + A[i]; j++) {
            if (j + i >= A.size()) {
                break;
            }
            if (max[i] >= min[j + i]) {
                finalCount++;
            }
        }
        if (finalCount > 10000000) {
            return -1;
        }
    }
    return finalCount;
}