## 解题思路

第一个想到的答案是递归，虽然直到可能会超时，但还是试了试。

## 我的答案

```js
function fibonacci(n) {
    if(n === 1 || n ===2) return 1;
    return fibonacci(n-1) + fibonacci(n-2);
}
```
不通过
您的代码已保存
运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
case通过率为66.67%

明天再做吧，先提交。

## 牛客题解
