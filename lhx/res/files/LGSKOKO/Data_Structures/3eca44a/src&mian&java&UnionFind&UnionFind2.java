package UnionFind;

/**
 * @author ：李先生
 * @date ：Created in 2020/2/2 10:12
 * @description：并查集 第二版 树型结构实现
 * @modified By：
 * @version: $
 */
public class UnionFind2 implements UF {
    private int[] parent;

    public UnionFind2(int size) {
        parent = new int[size];
        for (int i = 0; i < parent.length; i++) {
            parent[i] = i;
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

        parent[pRoot] = qRoot;
    }
}
