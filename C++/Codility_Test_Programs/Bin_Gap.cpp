//Finds the largest gap between zeros in the binary representation of N
//~O(log2(n)) time complexity and ~O(1) space complexity

int solution(int N) {
    int n = N, count = 0, maxCount = 0;
    while (!(n & 1)){
        n >>= 1;
    }
    while (n >= 1){
        if (n & 1){
            if (count > maxCount){
                maxCount = count;
            }
            count = 0;
            n >>= 1;
            continue;
        }
        count++;
        n >>= 1;
    }
    
    return maxCount;
}