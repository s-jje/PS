class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        String binary;

        for (int i = 0; i < arr1.length; i++) {
            binary = String.format("%16s", Integer.toBinaryString(arr1[i] | arr2[i]))
                    .substring(16 - n)
                    .replaceAll("1", "#")
                    .replaceAll("0", " ");
            answer[i] = binary;
        }
        return answer;
    }
}