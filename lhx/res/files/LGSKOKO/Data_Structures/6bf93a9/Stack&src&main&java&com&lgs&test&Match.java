package com.lgs.test;

import java.util.Stack;

/**
 * @author ：李先生
 * @date ：Created in 2019/8/11 11:03
 * @description：栈的应用：进行括号匹配
 * @modified By：
 * @version: $
 */
public class Match {

    public boolean isValid(String s){
        Stack<Character> stack = new Stack<>();
        for (int i=0; i < s.length();i++){
            //通过下标获取字符
            char c = s.charAt(i);
            //如果是左括号类型 进行入栈操作
            if(c == '(' || c == '[' || c == '{')
                stack.push(c);
            else{
                //判断是否为空栈 是返回false
                if(stack.isEmpty())
                    return false;
                //判断此时元素 和栈顶元素是否一样
                char topChar = stack.pop();
                if( c == ')' && topChar != '(')
                    return false;
                if( c == ']' && topChar != '[')
                    return false;
                if( c == '}' && topChar != '{')
                    return false;
            }
        }
        //并在这里判断栈里的元素是否为空 为空说明正确
        return stack.isEmpty();
    }

}
