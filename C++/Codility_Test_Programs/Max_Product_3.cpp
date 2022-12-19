//finds the largest product of 3 numbers in an array A
//~O(n) time complexity and ~O(1) space complexity (disregrading the input array)

#include <vector>

using std::vector;

int solution(vector<int>& A) {
    int posMax, oneMax, twoMax, threeMax, oneMin, twoMin, threeMin, pos1Max, negMax;
    posMax = -1;
    pos1Max = -1;
    oneMax = -1;
    twoMax = -1;
    threeMax = -1;
    oneMin = -1;
    twoMin = -1;
    threeMin = -1;
    negMax = -1;
    for (int i = 0; i < A.size(); i++) {
        if ((posMax == -1 && 0 <= A[i]) || A[posMax] < A[i]) {
            posMax = i;
        }

        if ((oneMax == -1 && 1 < abs(A[i])) || abs(A[oneMax]) < abs(A[i])) {
            if (A[threeMax] >= 0) {
                pos1Max = threeMax;
            }
            else {
                negMax = threeMax;
            }
            threeMax = twoMax;
            twoMax = oneMax;
            oneMax = i;
        }
        else if ((twoMax == -1 && 1 < abs(A[i])) || abs(A[twoMax]) < abs(A[i])) {
            if (A[threeMax] >= 0) {
                pos1Max = threeMax;
            }
            else {
                negMax = threeMax;
            }
            threeMax = twoMax;
            twoMax = i;
        }
        else if ((threeMax == -1 && 1 < abs(A[i])) || abs(A[threeMax]) < abs(A[i])) {
            if (A[threeMax] >= 0) {
                pos1Max = threeMax;
            }
            else {
                negMax = threeMax;
            }
            threeMax = i;
        }
        else {
            if ((pos1Max == -1 && 0 <= A[i]) || A[pos1Max] < A[i]) {
                pos1Max = i;
            }
            if ((negMax == -1 && 0 > A[i]) || A[negMax] > A[i]) {
                negMax = i;
            }
        }

        if ((oneMin == -1 && -1 >= A[i]) || A[oneMin] < A[i]) {
            threeMin = twoMin;
            twoMin = oneMin;
            oneMin = i;
        }
        else if ((twoMin == -1 && -1 >= A[i]) || A[twoMin] < A[i]) {
            threeMin = twoMin;
            twoMin = i;
        }
        else if ((threeMin == -1 && -1 >= A[i]) || A[threeMin] < A[i]) {
            threeMin = i;
        }
    }
    int count = 0;
    int track = 0;
    if (A[oneMax] < 0) {
        count++;
        track = 1;
    }
    if (A[twoMax] < 0) {
        count++;
        track = 2;
    }
    if (A[threeMax] < 0) {
        count++;
        track = 3;
    }
    if (!(count & 1)) {
        return (A[oneMax] * A[twoMax] * A[threeMax]);
    }
    if (posMax == -1) {
        return (A[oneMin] * A[twoMin] * A[threeMin]);
    }
    if (count == 3) {
        return(A[oneMax] * A[twoMax] * A[posMax]);
    }
    if (track == 1) {
        if (A[oneMax] * A[twoMax] * A[negMax] > A[twoMax] * A[threeMax] * A[pos1Max]) {
            return A[oneMax] * A[twoMax] * A[negMax];
        }
        return A[twoMax] * A[threeMax] * A[pos1Max];
    }
    if (track == 2) {
        if (A[oneMax] * A[twoMax] * A[negMax] > A[oneMax] * A[twoMax] * A[pos1Max]) {
            return A[oneMax] * A[twoMax] * A[negMax];
        }
        return A[oneMax] * A[twoMax] * A[pos1Max];
    }
    if (A[oneMax] * A[threeMax] * A[negMax] > A[oneMax] * A[twoMax] * A[pos1Max]) {
        return A[oneMax] * A[threeMax] * A[negMax];
    }
    return A[oneMax] * A[twoMax] * A[pos1Max];
}