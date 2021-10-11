# 十分钟入门 Python 教程

## 题记

去年和 amile 童鞋定了个小目标，决定带着点兴趣和热情，顺着全民学 Python 的热潮，随波逐流。奈何二零二零年是真的魔幻，唉，生活有你读不懂的诗，还有到不了的远方，我把那一年的辛酸过往，阉割成了一首诗。“生活似一杯苦茶，往事如逝水一般，邂逅一缕禅香，无数个赤夜里，抬头望见新月，繁星点点。“，好像还可以再阉割下，就变成了“苦茶，逝水，禅香，赤夜，新月，繁星”六个意象。而今，挤挤时间把这件事进行下去吧。。。。。。

## 准备

本文参考的教材是《Python 教程：从入门到实践》，这本书比较基础，对没有编程经验的读者异常友好，所以本教程适用于对刚刚开始学或者没有编程经验的读者。使用`jupyter notebook`作为学习这门语言入门的工具，这玩意好使，免去了初学者学习编辑器的成本，打开网页编写 `Python` 程序，点击运行即可出结果，而且它除了可以写 `Python` 之外，还支持 `Markdown` 语法，所以很适合写教程和笔记的。关于它的安装教程，可以看下这篇文章：`https://zhengjiangtao.cn/a2python/base/env.html`

给它一个特写。

![jupyter notebook](img/02-jupyter.png)

## 那个经典的“Hello World”

在 Python 语言中，我们可以通过`print`函数去打印相关的信息，比如说在 Python3 中我们要打印出一个`Hello World`，可以这样写。

```python
# encoding: utf-8

if __name__ == '__main__':

    print('Hello World')

```

## 基础知识梳理

如楼上的 Hello World 所示，在 Python 语言中，末尾是不用加分号的。Python 是一门解释型，它并不像 C、C++这样，需要有个编译的过程，将代码编译成机器码（转换成计算机可识别的二进制指令）然后运行，在编译过程中要确定变量的类型，通不过编译就不能运行。Python 语言需要一个解释器，边解释边运行，所以在定义变量的时候并不需要指出其是什么类型，遵循`变量名 = 变量值`这种方式即可，关于变量名的规范和其它语言也差不多，这里就不展开赘述了，后面的相关类型的变量赋值本身是没有什么好讲的，但是 Python 语言有意思就有意思在它的库多，你不用洋洋洒洒写很多，你只要库调的好，代码是非常简洁的。

### 字符串

比如说我们要定义一个字符串变量名`name`为`ataola`,就可以写作`name = 'ataola'`。如果说字符串很长，我们期望原样输出，那么可以这样写。

```python
long_str = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

print(long_str)
```

**注意：** 变量的命名不能跟系统的函数名，或者保留字冲突，比如这里你写作`str = 'what's wrong with you ?'`就很不好，因为`str`是系统函数，它可以把变量转成字符串类型。例如楼下这个例子，如果不用`str`函数将整型变量`age`转换成字符串类型的话，就会出现运行出错，因为他们不是一个类型的变量。

```python
age = 24
msg= "i am " + str(age) + " year old"
print(msg)
```

#### 一些常用的字符串 API

- `title`: 首字母大写

- `upper`: 大写

- `lower`: 小写

- `strip`: 去空

- `lstrip`: 左边去空

- `rstrip`: 右边去空

- `split`: 字符串转列表

- `count`: 统计字符出现的次数

##### 例子 1

**代码：**

```python
_str = 'hello world'
print('首字母大写:', _str.title())
print('大写：', _str.upper())
print('小写：', _str.lower())
```

**输出：**

```
首字母大写: Hello World
大写： HELLO WORLD
小写： hello world
```

##### 例子 2

**代码：**

```python
_str = ' happy everyday  '
print('|' + _str + '|')
print('|' + _str.strip() + '|')
print('|' + _str.lstrip() + '|')
print('|' + _str.rstrip() + '|')
print('|' + _str.lstrip().rstrip() + '|')
```

**输出：**

```
| happy everyday  |
|happy everyday|
|happy everyday  |
| happy everyday|
|happy everyday|
```

##### 例子 3

**代码：**

```python
bio = 'day day up, to be strong!'
print(bio.count('day'))
print(bio.count('up'))
```

**输出：**

```
2
1
```

由例子 2 的最后一行可见 Python 是支持函数链式调用的。

### 整型

python3 的整型范围是无限的，所以它特别适合拿来做科学计算相关的，因为你不用担心它会精度溢出。有意思的是，它允许你用`_`下划线表示数字的分隔符，提高其可读性，这并不影响其数值，比如`1_000`,它和`1000`是一样的。

#### 一些常用处理数字的 API

- `bin`: 转二进制

- `abs`: 求绝对值

- `bool`: 转布尔值

- `float`: 转浮点数

- `pow`: 幂函数

- 一些位运算。。。。。。

##### 例子 4

**代码：**

```python
print(bin(8)) # 十进制转二进制
print(abs(-10)) # 绝对值
print( 1 and 0 == 1 & 0) # 按位于
print ((1 or 0) == (1 | 0)) # 按位或
print(~11 == -12)# 取反（二进制的负数表示方法：正数按位取反再加1）
print(2 ^ 3 ^ 2 == 3) # 异或
print(8 << 1 ==16) # 左移
print(8 >> 1 == 4) # 右移
print(10 % 3 == 1) # 取余
print(3 ** 2 == pow(3, 2)) # 次方运算符 和 幂函数
print(bool(1) == True ) # 转布尔类型，除0外都是True
print(bool(0) == True ) # 转布尔类型，除0外都是True
print(float(100)) # 整数转浮点

```

**输出：**

```
0b1000
10
True
True
True
True
True
True
True
True
True
False
100.0
```

### 浮点

#### 为什么`0.1 + 0.2 != 0.3`， `3 * 0.1 != 0.3`, 而是`0.30000000000000004 `?

我们知道计算机只能识别二进制，所以浮点数会被转换成二进制，0.1 转成二进制是`0.0001100110011001100110011001100110011001100110011001101`, 0.2 转成二进制是`0.001100110011001100110011001100110011001100110011001101`,相加得到的结果是`0.0100110011001100110011001100110011001100110011001101`. 简单的说就是像 0.1 这种无法被二进制完整表示。

这里我们可以通过`round(num, digits)`去使结果符合预期，例如`print(round(0.1 + 0.2, 1))`,就能得到 0.3

**注意：**

十进制整数转二进制方法：除 2 取余；十进制小数转二进制方法：乘 2 除整

### 布尔值

在 Python 中，用`True`表示真，用`False`表示假，注意这里是区分大小写的。

我们来看下面这个例子

##### 例子 5

**代码：**

```python
print(1 == True) # True
print(0 == False) # False
print('' == True) # False
print(' ' == True) # False
print('' == False) # False
print(' ' == False) # False
print(bool('')) # False
print(bool(' ')) # True
```

可以看到在 Python 中，数字 0 也可以表示 False，其它数字可以表示 True， 而字符串它不能表示成真或假,但是可以通过`bool`函数将其转回成真假

### 列表

列表是一系列按特定顺序排列的元素组成，类似于 Javascript 中的数组。值得一提的是，在列表访问的时候，它的索引下标可以为负数，例如`a[-1]`就是表示列表 a 中的倒数第一个元素

#### 一些常用的列表 API

- `sort`: 排序

- `reverse`: 反转

- `len`: 长度

- `append`: 从列表末尾插入元素

- `insert`: 列表任意位置插入元素

- `pop`: 从列表末尾弹出元素

- `remove`: 从右往左移除第一个遇到的目标元素

我们一起来看下面这个例子，

##### 例子 5

**代码：**

```python
season  = ['spring', 'summer', 'autumn', 'winter']
print(season)
season.sort()
print(season)
season.sort(reverse=True)
print(season)
print(sorted(season))
print(season)
season.reverse()
print(season)
print(len(season))
```

**输出：**

```
['spring', 'summer', 'autumn', 'winter']
['autumn', 'spring', 'summer', 'winter']
['winter', 'summer', 'spring', 'autumn']
['autumn', 'spring', 'summer', 'winter']
['winter', 'summer', 'spring', 'autumn']
['autumn', 'spring', 'summer', 'winter']
4
```

从楼上的例子，我们不难发现，通过`list.sort()`，这种方式它会改变列表的原值，而且在函数中可以传一个参数`reverse`来表示是顺着排序还是倒着排序。

我们再来看一个例子

##### 例子 6

**代码：**

```python
arr = [1, 2, 3, 4, 5]
print(arr[0])
print(arr[-1])
arr.append(6)
print(arr)
arr.insert(4, 4.5)
print(arr)
del arr[4]
print(arr)
arr.pop()
print(arr)
arr.pop(2)
print(arr)
arr.remove(4)
print(arr)

```

**输出：**

```
1
5
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 4.5, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5]
[1, 2, 4, 5]
[1, 2, 5]
```

楼上的例子首先我定义了一个列表`arr = [1, 2, 3, 4, 5]`,然后我去访问了它的第一个元素和最后一个元素，接着我通过`append`函数在列表后面追加了`6`，之后我又通过`insert`函数在第五个元素的位置插入了`4.5`,紧接着我用`del`又把它删除了，然后我通过调用`pop`弹出了列表最后的元素，之后我又给它穿了个参数`2`,表示将第三个元素弹出，最后我通过`remove`函数去删除了从列表最后往前找到的第一个目标元素。

### 字典

字典是一系列的键值对，类似于 JavaScript 中的对象。我们还是以具体的示例来看下。

##### 例子 7

**代码：**

```python
user ={ 'name': 'ataola', 'age': 24, 'sex': '男' }
print(user)
print('Hello ', user['name'])
```

**输出：**

```
{'name': 'ataola', 'age': 24, 'sex': '男'}
Hello  ataola
```

这里我们定义了一个用户信息的字典，然后试着把它打印出来，通过键值对的键可以访问它的值，接着我们试着构造字符串去试着访问它。

##### 例子 8

**代码：**

```python
for key, value in user.items():
    print(key, value)
```

**输出：**

```
name ataola
age 24
sex 男
```

上面这个例子就是遍历字典的键值对的方法。

如果我只是想遍历它的键或者值呢？通过`keys()`表示键，通过`values()`表示值。

**代码：**

```python
for key in user.keys():
    print(key)
```

**输出：**

```
name
age
sex
```

**代码：**

```python
for value in user.values():
    print(value)
```

**输出：**

```
ataola
24
男
```

这里再进一步思考下，如果说我遍历的值有很多重复呢？我怎么让它不重复呢？嗯，对，答案就是集合去重。当然，这里答案不唯一。

**代码：**

```python
favorite_language = { 'alice': 'JAVA', 'Bob': 'C++', 'ataola': 'Javascript', 'daming': 'Javascript', 'wuyifan': 'Javascript' }
for value in set(favorite_language.values()):
    print(value)
```

**输出：**

```
JAVA
Javascript
C++
```

### 循环和判断

这里把循环和判断放在一起讲吧，循环在大多数编程语言里都差不多，不外乎`for`循环和`while`循环，条件判断也都类似，不外乎`if`,`else`这种。

#### while 循环

**代码：**

```python
while message != 'quit':
    message = input('please input something:')
    print(message)
```

**输出：**

```
please input something:11
11
please input something:22
22
please input something:33
33
please input something:quit
quit
```

这个程序是这样子的，当用户输入`quit`的时候，那么我就退出这个程序，不然我就原样输出。

#### 条件判断

**代码：**

```python
num = input('please input a number: ')
num = int(num)
if num > 10:
    print('big')
elif num <= 10 and num > 5:
    print('normal')
else:
    print('small')
```

**输出:**

```
please input a number: 8
normal
```

这个程序是这样子的，提示用户输入一个数，然后判断这个数的大小，通过`if`,`elif`,`else`来判断输入的数是大还是小，抑或是正常，这就是个例子，本身没有什么意义。

#### for 循环

**代码：**

```python
numbers = list(range(1, 20))
for num in numbers:
    if num % 2 == 0:
        print(num, '是个偶数')
    else:
        print(num, '是个奇数')
print(numbers)
```

**输出：**

```
1 是个奇数
2 是个偶数
3 是个奇数
4 是个偶数
5 是个奇数
6 是个偶数
7 是个奇数
8 是个偶数
9 是个奇数
10 是个偶数
11 是个奇数
12 是个偶数
13 是个奇数
14 是个偶数
15 是个奇数
16 是个偶数
17 是个奇数
18 是个偶数
19 是个奇数
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

楼上的这个例子，我们用了一个 for 循环遍历了列表 numbers 里面的项，然后结合 if 判断这个项是奇数还是偶数。

## 函数

函数本质是带名字的代码段，在 python 中我们可以通过`def`去定义一个函数。

**代码：**

```python
def sayHello(name = 'zjt'):
    return 'hello ' + name

for i in range(1, 10):
    if i % 2 == 0:
        print(i, sayHello())
    else:
        print(i, sayHello('ataola'))
```

## 输出

```
1 hello ataola
2 hello zjt
3 hello ataola
4 hello zjt
5 hello ataola
6 hello zjt
7 hello ataola
8 hello zjt
9 hello ataola
```

上面这个例子中我们定义了一个函数`sayHello`,然后给函数的形参一个初始值，如果调用函数没有传的话就取默认值，这个例子本身没有什么意义，就作为演示意思下。

## 类

讲到类，就不得不提面向对象了，以及封装继承多态啦。这里我们作为入门环节，简单地用一个例子感受下。

我们先创建一个类`Person`,然后我们再创建一个类`Robot`去继承`Person`.

**代码：**

```python
class Person():
    """ 人类 """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(self.name.title(), ' is speaking.')

class Robot(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


ataola = Person('zheng jiangtao', 24)
ataola.speak()
robot = Robot('xiao ai', 3)
robot.speak()
```

**输出：**

```
Zheng Jiangtao  is speaking.
Xiao Ai  is speaking.
```

我们实例化了一个 Person 类 ataola，然后调用了 speak 方法，我们还实例化了一个 Robot 类，然后调用了其继承 Person 类的 speak 方法。

## 说明

本文首发于 GitHub 仓库https://github.com/ataola/a2python，线上阅读地址：https://zhengjiangtao.cn/a2python/，转载请注明出处，谢谢！
