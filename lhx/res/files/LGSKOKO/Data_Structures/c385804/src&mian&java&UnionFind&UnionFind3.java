package UnionFind;

/**
 * @author ：李先生
 * @date ：Created in 2020/2/2 10:51
 * @description：并查集 第三版 基于第二版根据size进行改造
 * @modified By：
 * @version: $
 */
public class UnionFind3 implements UF {
    private int[] parent;
    private int[] sz; //sz[i]表示以i为根的结合中元素的个数

    public UnionFind3(int size) {
        parent = new int[size];
        sz = new int[size];
        for (int i = 0; i < parent.length; i++) {
            parent[i] = i;
            sz[i] = 1;
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
        while (parent[index] != index)
            index = parent[index];
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
        if (sz[pRoot] < sz[qRoot]) {
            parent[pRoot] = qRoot;
            sz[qRoot] += sz[pRoot];
        } else {// sz[qRoot] <= sz[pRoot]
            parent[qRoot] = pRoot;
            sz[pRoot] += sz[qRoot];
        }
    }
}
