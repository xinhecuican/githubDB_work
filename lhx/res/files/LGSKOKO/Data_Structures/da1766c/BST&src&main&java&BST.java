/**
 * @author ：李先生
 * @date ：Created in 2019/8/18 11:37
 * @description：二分搜索树的实现类
 * @modified By：
 * @version: $
 */
//这里使用泛型 因为二分搜索树必须是可比较的 所以E继承Comparable<E>（可比较接口)
public class BST<E extends Comparable<E>> {

    //内部类 实现结点
     class Node{

        public E e;//
        public Node left,right;//左右孩子
        //构造函数 创建结点
        public Node(E e){
            this.e = e;
            left = null;
            right = null;
        }
    }//end class Node

    private Node root;//根节点
    private int size;//用来记录当前树的个数
    //构造函数 创建树的根节点（相当于初始化）
    public BST(){
        root = null;
        size = 0;
    }

    public int getSize(){
        return size;
    }

    public boolean isEmpty(){
        return size == 0;
    }
}//end class BST
