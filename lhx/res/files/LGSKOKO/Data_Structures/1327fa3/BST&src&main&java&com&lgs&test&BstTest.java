package com.lgs.test;

import com.lgs.code.BST;

import java.util.ArrayList;
import java.util.Random;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/30 9:57
 * @description：二分搜索树的测试类
 * @modified By：
 * @version: $
 */
public class BstTest {
    public static void main(String[] args) {

       //BstTest.simpleTest();
        //BstTest.removeMinTest();
        BstTest.removeMaxTest();
    }

    //关于二分搜索树的简单测试
    public static void simpleTest()
    {
        BST<Integer> bst = new BST<>();
        int[] nums = {5,3,6,8,4,2};
        //循环遍历数组 并将其添加到二分搜索树
        for(int num : nums)
            bst.add(num);
        /////////////////
        //      5      //
        //    /   \    //
        //   3    6    //
        //  / \    \   //
        // 2  4     8  //
        /////////////////
        System.out.println("二分搜索树的递归前序遍历:");
        bst.preOrder();//二分搜索树的递归前序遍历
        System.out.println();

        System.out.println("二分搜索树的非递归前序遍历:");
        bst.preOrderNR();//二分搜索树的非递归前序遍历
        System.out.println();

        System.out.println("二分搜索树的递归中序遍历:");
        bst.inOrder();//二分搜索树的递归中序遍历
        System.out.println();

        System.out.println("二分搜索树的递归后序遍历:");
        bst.postOrder();//二分搜索树的递归后序遍历
        System.out.println();

        System.out.println("二分搜索树的层序遍历:");
        bst.levelOrder();//二分搜索树的层序遍历
        System.out.println();

        System.out.println(bst);//打印完整的二分搜索树
    }

    //关于删除最小元素的测试
    public static void removeMinTest(){
        BST<Integer> bst = new BST<>();
        Random random = new Random();

        int n = 1000;

        // test removeMin
        for(int i = 0 ; i < n ; i ++)
            bst.add(random.nextInt(10000));

        ArrayList<Integer> nums = new ArrayList<>();
        while(!bst.isEmpty())
            nums.add(bst.removeMin());

        System.out.println(nums);
        for(int i = 1 ; i < nums.size() ; i ++)
            if(nums.get(i - 1) > nums.get(i))
                throw new IllegalArgumentException("Error!");
        System.out.println("removeMin test completed.");
    }

    //关于删除最大元素的测试
    public static void removeMaxTest(){

        BST<Integer> bst = new BST<>();
        Random random = new Random();

        int n = 1000;
        // test removeMax
        for(int i = 0 ; i < n ; i ++)
            bst.add(random.nextInt(10000));

        ArrayList<Integer> nums = new ArrayList<>();
        while(!bst.isEmpty())
            nums.add(bst.removeMax());

        System.out.println(nums);
        for(int i = 1 ; i < nums.size() ; i ++)
            if(nums.get(i - 1) < nums.get(i))
                throw new IllegalArgumentException("Error!");
        System.out.println("removeMax test completed.");
    }

}
