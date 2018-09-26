package com.company;

import java.util.HashSet;

public class Main {

    public static void main(String[] args) {
        //System.out.println("1".compareTo("0"));

        //[[5, 1, 5], [10, 1, 2]]
        //[[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]

        //int[] r = answer(new int[][] {new int[] {15, 3, 15}, new int[] { 5, 1, 5}, new int[] {10, 1, 2}});
        //int[] r = answer(new int[][] {new int[] { 5, 1, 5}, new int[] {10, 1, 2}});
        //int[] r = answer(new int[][] {new int[] { 390, 185, 624}, new int[] {686, 351, 947}, new int[] {276, 1023, 1024}, new int[] {199, 148, 250}});
        int[][] minions = new int[][] {new int[] {15, 3, 15}, new int[] { 5, 1, 5}, new int[] {10, 1, 2}};
        int[] array = new int[minions.length];
        for(int i = 0; i < minions.length; i++){
            array[i] = minions[i][0];
        }
        HashSet<String> hset = new HashSet<>();
        Permute(minions.length, array, hset);

        //return array;
    }

    public static void Permute(int n, int[] array, HashSet<String> hset){
        if (n == 1){
            //hset.add(getStr(array));
        }
        else{
            for (int i = 0; i < n -1; i++){
                Permute(n -1, array, hset);
                if (n % 2 == 0){
                    int s = array[i];
                    array[i] = array[n-1];
                    array[n-1] = s;
                    //hset.add(getStr(array));
                }
                else{
                    int s = array[0];
                    array[0] = array[n-1];
                    array[n-1] = s;
                    //hset.add(getStr(array));
                }
            }
            Permute(n-1, array, hset);
        }
    }

    public static String getStr(int[] array){
        String res = "";
        for (int i = 0; i < array.length; i++){
            res += array[i] + "-";
        }
        return res;
    }

    public static int[] answer(int[][] minions) {
        double[] exp_values = new double[minions.length];
        double totExpected = 0;

        for (int i = 0; i < minions.length; i++){
            double exp_val = ((double)minions[i][0] + ((double)minions[i][0] * ((double)minions[i][1] / (double)minions[i][2]))) / 2;
            exp_values[i] = exp_val;
            totExpected += exp_val;
        }






        int[] res = new int[minions.length];
        return res;
    }
}


        /*double min_expected_last = Double.MAX_VALUE;
        int min_expected_last_idx = -1;
        for (int i = 0; i < minions.length; i++){
            double exp = totExpected - exp_values[i] + minions[i][0];
            if (exp < min_expected_last){
                min_expected_last = exp;
                min_expected_last_idx = i;
            }
            else if (exp == min_expected_last){
                if (minions[i][0] > minions[min_expected_last_idx][0]){
                    min_expected_last_idx = i;
                }
            }
        }*/

        /*Comparator<double[]> comparator = new Comparator<double[]>(){
            @Override
            public  int compare(double[] o1, double[] o2){
                if (o1[1] == o2[1])
                    return o1[0] == o2[0] ? 0 : o1[0] > o2[0] ? 1 : -1;

                return o1[1] > o2[1] ? 1 : -1;
            }
        };*/

        /*TreeSet<int> ts = new TreeSet<>();
        for (int i = 0; i < minions.length; i++){
            if(i != min_expected_last_idx){
                //ts.add(minions);
            }
        }*/
    /*
    public static int[] answer(int[][] minions) {
        Comparator<int[]> comparator = new Comparator<int[]>(){
            @Override
            public  int compare(int[] o1, int[] o2){
                double d1 = ((double)o1[1] / (double)o1[2]) / (double)o1[0] * 1000000000;
                double d2 = ((double)o2[1] / (double)o2[2]) / (double)o2[0] * 1000000000;

                if (d1 == d2)
                    return o1[0] - o2[0];

                return d2 > d1 ? 1 : -1;
            }
        };

        TreeSet<int[]> ts = new TreeSet<>(comparator);
        for(int[] m : minions){
            ts.add(m);
        }

        int[] res = new int[minions.length];

        int ri = 0;
        for(int[] v : ts) {
            for(int i = 0; i < minions.length; i++){
                if(minions[i][0] == v[0]){
                    res[ri] = i;
                    break;
                }
            }

            ri++;
        }
        return res;
    }
    */