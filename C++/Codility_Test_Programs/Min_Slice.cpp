
//Finds the minimal average of any slice containing at least two elements.
//roughly O(n) time complexity and O(1) space complexity (disregarding the input array)

#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

int solution(vector<int>& A) {
    double min = -1, minPos = 0, one, two;
    int cur = 0;
    bool oot = false;
    for (int i = 0; i < A.size() - 2; i++) {
        one = static_cast<double>(A[i] + A[i + 1] + A[i + 2]) / 3;
        if (min > one || min == -1) {
            min = one;
            minPos = i;
        }
    }
    while (cur < A.size() - 2) {
        one = static_cast<double>(A[cur] + A[cur + 1]) / 2;
        two = static_cast<double>(A[cur + 1] + A[cur + 2]) / 2;
        if (one > two) {
            cur++;
            one = two;
            oot = true;
        }
        if (min > one) {
            min = one;
            minPos = cur;
        }
        else if (min == one) {
            if (cur < minPos) {
                minPos = cur;
            }
        }
        if (!oot) {
            cur += 2;
        }
        else {
            oot = false;
        }
    }
    return minPos;
}










