package com.company;

public class Main {

    public static void main(String[] args) {
        System.out.println(answer(new int[] {1, 4, 1}));
        //System.out.println(answer(new int[] {1, 2}));
    }

    public static int answer(int[] x) {
        int max = 0;
        int sum = 0;
        for (int n : x){
            sum += n;
        }

        double ave = (float) sum / x.length;
        if (ave < 0) return sum;
        if (ave > (int)ave) return x.length - 1;

        return x.length;
    }
}
