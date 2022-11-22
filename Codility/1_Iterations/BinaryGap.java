// https://app.codility.com/programmers/lessons/1-iterations/binary_gap

import java.util.*;

class Solution { 

    public int solution(int N) {
        String binary = Integer.toBinaryString(N);

        List<Integer> ones = new ArrayList<>(31);
        int len = binary.length();
        for (int i = 0; i < len; i++) {
            if (binary.charAt(i) == '1') {
                ones.add(i);
            }
        }
        
        int longest = 0;
        int binary_gap = 0;
        len = ones.size();
        for (int i = 1; i < ones.size(); i++) {
            binary_gap = ones.get(i) - ones.get(i - 1) - 1;
            longest = longest < binary_gap ? binary_gap : longest;
            binary_gap = 0;
        }

        return longest;
    }
}