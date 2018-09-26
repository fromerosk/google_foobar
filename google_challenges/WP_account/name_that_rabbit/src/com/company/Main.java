package com.company;
import java.util.TreeSet;
import java.util.Comparator;

public class Main {

    public static void main(String[] args) {
        //System.out.println("abc".compareTo("acd") > 0 ? "a" : "b");
        String[] res = answer(new String[] {"annie", "bonnie", "liz"});
        //String[] res = answer(new String[] {"abcdefg", "vi"});
        for(String a : res){
            System.out.println(a);
        }
    }
    public static String[] answer(String[] names) {
        Comparator<String> comparator = new Comparator<String>(){
            @Override
            public  int compare(String o1, String o2){
                int l1 = 0;
                for (char c : o1.toCharArray()){
                    l1 += ((int)c - 96);
                }
                int l2 = 0;
                for (char c : o2.toCharArray()){
                    l2 += ((int)c - 96);
                }

                int ll = l2 - l1;
                return ll == 0 ? o1.compareTo(o2) * -1 : ll;
            }
        };

        TreeSet<String> ts = new TreeSet<>(comparator);
        for(String n : names){
            ts.add(n);
        }
        return  ts.toArray(new String[names.length]);
    }
}
