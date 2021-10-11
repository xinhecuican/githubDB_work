package com.lgs.code;

/**
 * @author ：李先生
 * @date ：Created in 2019/9/5 17:42
 * @description：Map(映射)的接口
 * @modified By：
 * @version: $
 */
public interface Map<K,V> {

    void add(K key,V value);
    V remove(K key);
    boolean contains(K key);
    V get(K key);
    void set(K key,V newValue);
    int getSize();
    boolean isEmpty();
}
