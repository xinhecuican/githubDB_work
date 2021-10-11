package UnionFind;

/**
 * @author ：李先生
 * @date ：Created in 2020/2/2 13:12
 * @description：并查集 第五版  基于第四版进行路径压缩
 * @modified By：
 * @version: $
 */
public class UnionFind5 implements UF {
    private int[] parent;
    private int[] rank; //rank[i]表示以i为根的结合中元素的高度

    public UnionFind5(int size) {
        parent = new int[size];
        rank = new int[size];
        for (int i = 0; i < parent.length; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
    }

    @Override
    public int getSize() {
        return parent.length;
    }

    //查找过程，查找元素index所对应的集合编号
    //o(h)复杂度，h为树的高度
    private int find(int index) {
        if (index < 0 || index >= parent.length)
            throw new IllegalArgumentException("illegal index");
        while (parent[index] != index) {
            parent[index] = parent[parent[index]];
            index = parent[index];

        }

        return index;
    }

    //查找两个结点 是否属于同一个集合
    @Override
    public boolean isConnected(int p, int q) {
        return find(p) == find(q);
    }

    //合并元素p和元素q所属的集合
    //O(h)复杂度，h为树的高度
    @Override
    public void unionElements(int p, int q) {
        int pRoot = find(p);
        int qRoot = find(q);

        if (pRoot == qRoot) return;

        //根据两个元素所在的树的元素个数的不同 判断合并方向
        //将元素少的集合 合并到 元素个数多的集合上
        if (rank[pRoot] < rank[qRoot])
            parent[pRoot] = qRoot;
        else if (rank[pRoot] > rank[qRoot])
            parent[qRoot] = pRoot;
        else {// rank[qRoot] == rank[pRoot]
            parent[qRoot] = pRoot;
            rank[pRoot] += 1;
        }
    }
}
