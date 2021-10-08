package SegmentTree;

/**
 * @author ：李先生
 * @date ：Created in 2020/1/29 11:43
 * @description： 一个接口：用于定义在线段树中merger的业务流程
 * @modified By：
 * @version: $
 */
public interface Merger<E> {
    E merger(E a,E b);
}
