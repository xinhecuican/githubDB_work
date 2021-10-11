package com.lgs.test;

import com.lgs.code.BSTSet;
import com.lgs.code.FileOperation;

import java.util.ArrayList;

/**
 * @author ：李先生
 * @date ：Created in 2019/9/3 15:35
 * @description：关于以BST为基础实现的集合的测试类
 * @modified By：
 * @version: $
 */
public class BSTSetTest {

    public static void main(String[] args) {

        System.out.println("Pride and Prejudice");

        ArrayList<String> words1 = new ArrayList<>();
        if(FileOperation.readFile("Set/src/main/pride-and-prejudice.txt", words1)) {
            System.out.println("Total words: " + words1.size());

            BSTSet<String> set1 = new BSTSet<>();
            for (String word : words1)
                set1.add(word);
            System.out.println("Total different words: " + set1.getSize());
        }

        System.out.println();


        System.out.println("A Tale of Two Cities");

        ArrayList<String> words2 = new ArrayList<>();
        if(FileOperation.readFile("Set/src/main/a-tale-of-two-cities.txt", words2)){
            System.out.println("Total words: " + words2.size());

            BSTSet<String> set2 = new BSTSet<>();
            for(String word: words2)
                set2.add(word);
            System.out.println("Total different words: " + set2.getSize());
        }

    }
}
