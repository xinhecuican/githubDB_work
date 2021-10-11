package UnionFind;

/**
 * @author ：李先生
 * @date ：Created in 2020/2/2 9:26
 * @description：并查集接口
 * @modified By：
 * @version: $
 */
public interface UF {

    int getSize();//获取大小

    boolean isConnected(int p, int q);//两个结点是否连接

    void unionElements(int p, int q);//将两个集合 进行合并
}
