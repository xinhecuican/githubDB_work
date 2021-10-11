package UnionFind;

/**
 * @author ：李先生
 * @date ：Created in 2020/2/2 9:40
 * @description：并查集 第一版 使用数组实现
 * @modified By：
 * @version: $
 */
public class UnionFind1 implements UF {

    private int[] id;

    public UnionFind1(int size) {
        id = new int[size];
        for (int i = 0; i < id.length; i++) {
            id[i] = i;
        }
    }

    //
    @Override
    public int getSize() {
        return id.length;
    }

    //查找元素 对应的集合编号
    private int find(int index) {
        if (index < 0 || index >= id.length)
            throw new IllegalArgumentException("illegal index");
        return id[index];
    }

    //查看元素p和元素q是否属于一个集合
    @Override
    public boolean isConnected(int p, int q) {
        return find(p) == find(q);
    }

    //合并元素p和元素q所属的集合
    @Override
    public void unionElements(int p, int q) {
        int pID = find(p);
        int qID = find(q);
        if (pID == qID) return;
        for (int i = 0; i < id.length; i++) {
            if (id[i] == qID)
                id[i] = pID;
        }
    }
}
