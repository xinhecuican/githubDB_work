package SegmentTree;

/**
 * @author ：李先生
 * @date ：Created in 2020/1/29 11:15
 * @description：线段树的数据结构定义
 * @modified By：
 * @version: $
 */
public class SegmentTree<E> {

    private E[] data;
    private E[] tree;
    private Merger<E> merger;

    //构造函数
    public SegmentTree(E[] arr, Merger<E> merger) {
        this.merger = merger;
        data = (E[]) new Object[arr.length];
        for (int i = 0; i < arr.length; i++)
            data[i] = arr[i];
        tree = (E[]) new Object[4 * arr.length];
        buildSegmentTree(0, 0, data.length - 1);
    }

    //在treeIndex的位置创建表示区间[l....r]的线段树
    private void buildSegmentTree(int treeIndex, int l, int r) {
        //递归终止条件
        if (l == r) {
            tree[treeIndex] = data[l];
            return;
        }
        int leftTreeIndex = leftChild(treeIndex);
        int rightTreeIndex = rightChild(treeIndex);
        int mid = l + (r - l) / 2; //因为 直接l+r /2 可能会溢出
        buildSegmentTree(leftTreeIndex, l, mid);
        buildSegmentTree(rightTreeIndex, mid + 1, r);

        tree[treeIndex] = merger.merger(tree[leftTreeIndex], tree[rightTreeIndex]);
    }

    public int getSize() {
        return data.length;
    }

    public E get(int index) {
        if (index < 0 || index >= data.length)
            throw new IllegalArgumentException();
        return data[index];
    }

    //返回完全二叉树的数组中，一个索引所表示的元素的左孩子节点的索引
    public int leftChild(int index) {
        return 2 * index + 1;
    }

    //返回完全二叉树的数组中，一个索引所表示的元素的右孩子节点的索引
    public int rightChild(int index) {
        return 2 * index + 2;
    }

    //返回区间[queryL，queryR]的值
    public E query(int queryL, int queryR) {
        if (queryL < 0 || queryL >= data.length ||
                queryR < 0 || queryR >= data.length || queryL > queryR)
            throw new IllegalArgumentException("Index is illegal");
        return query(0, 0, data.length - 1, queryL, queryR);
    }

    //在以treeID为根的线段树中[l...r]的范围里，搜索区间[queryL，queryR]的值
    private E query(int treeIndex, int l, int r, int queryL, int queryR) {

        if (l == queryL && r == queryR)
            return tree[treeIndex];

        int mid = l + (r - l) / 2;
        int leftTreeIndex = leftChild(treeIndex);
        int rightTreeIndex = rightChild(treeIndex);

        if (queryL >= mid + 1)
            return query(rightTreeIndex, mid + 1, r, queryL, queryR);
        else if (queryR <= mid)
            return query(leftTreeIndex, l, mid, queryL, queryR);

        E leftResult = query(leftTreeIndex, l, mid, queryL, mid);
        E rightResult = query(rightTreeIndex, mid + 1, r, mid + 1, queryR);

        return merger.merger(leftResult, rightResult);

    }

    //更新
    public void set(int index,E e)
    {
        if(index<0 || index>=data.length)
            throw new IllegalArgumentException("Index is illegal");
        data[index] = e;
        set(0,0,data.length-1,index,e);
    }

    //在以treeIndex为根的线段树中更新index的值为e
    private void set(int treeIndex,int l,int r,int index,E e) {
        if(l==r)
        {
            tree[treeIndex] = e;
            return;
        }
        int leftTreeIndex = leftChild(treeIndex);
        int rightTreeIndex = rightChild(treeIndex);
        int mid = l+(r-l) /2;
        if(index >=mid+1)
            set(rightTreeIndex,mid+1,r,index,e);
        else
            set(leftTreeIndex,l,mid,index,e);

        tree[treeIndex] = merger.merger(tree[leftTreeIndex],tree[rightTreeIndex]);
    }

    @Override
    public String toString() {
        StringBuffer res = new StringBuffer();
        res.append("[");
        for (int i = 0; i < tree.length; i++) {
            if (tree[i] != null)
                res.append(" "+tree[i]);
            else if (tree[i] == null)
                res.append(" null");

            if (i == tree.length - 1)
                res.append("]");
        }
        return res.toString();
    }
}
