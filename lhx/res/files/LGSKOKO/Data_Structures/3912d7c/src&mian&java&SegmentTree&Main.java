package SegmentTree;

/**
 * @author ：李先生
 * @date ：Created in 2020/1/29 11:50
 * @description：主函数
 * @modified By：
 * @version: $
 */
public class Main {

    public static void main(String[] args) {
        Integer[] nums= {-2,0,3,-5,2,-1};
        SegmentTree<Integer> segTree = new SegmentTree<Integer>(nums,(a,b) -> a+b);
        System.out.println(segTree);

        System.out.println(segTree.query(0,2));
        System.out.println(segTree.query(2,5));
        System.out.println(segTree.query(0,5));


    }
}
