# python-daily

## 语法

### 注释

#### 单行注释

```python
# 单行注释
```

#### 多行注释

```python
"""
多行注释
多行注释
多行注释
"""
```

#### 特殊注释(windows不行)

```python
#!/usr/bin/evy_......
```

### 变量

- 定义

```python
a = 10
b, c = 10, 5
```

#### 注意

- 不能以**数字**开头
- 不能用**关键字**命名

### 数据类型

#### 序列

在python中，序列就是一组按照顺序排列的值【数据集合】， 存在三种内置的序列类型: 字符串、列表、元组

优点：可以支持索引和切片的操作

- 切片：
    - 定义： 根据下标获取序列对象的任意(部分)数
    - 语法： [start:end;step] step默认为1
        - 左闭右开
        - [::-1] 倒序输出

特征：

- 第一个索引为0，指向序列的最左端
- 第一个索引为负数时，指向序列的最右端
- 下标会越界，切片不会越界

#### 基本类型

##### 字符串

-支持切片

###### 常用方法：

- capitalize：首字母变大写
- endswith/startswith：是否是x开始结束
- find：检测x是否在字符串中
    - 返回下标值
    - 找不到返回 -1
- index：检测x是否在字符串中
    - 返回下标值
    - 找不到抛出异常
- isalnum：判断是否是字母或数字
- isalpha：判断是否是字母
- isdigit：判断是否是数字
- islower：判断是否小写
- join：循环取出所有值，用x去链接
- lower/upper：大小写切换
- swapcase：大写变小写，小写变大写
- lstrip/rstrip/strip：移除左/右/两侧空白
- split：切割字符串
- title：把每个单词的首字母变成大写
- replace(old, new, count)：old被替换字符串，new替换字符串，count换多少个，无count表示全部替换
- count：统计出现的次数

##### 数字

##### 布尔值

#### 高级类型

##### 字典

以键值对的形式存储任意对象

- 键不能重复，值可以重复
- 键只能是不可变类型（数字、字符串、元组）

###### 常用方法

- keys
- values
- items
- get

##### 元组(tuple)

是一种不可变序列，创建以后不能做任何的修改

- 不可变
- 数据是可以是任意类型
- 当元组中只有一个元素时，要加上逗号
- 支持切片

##### 列表(list)

一种有序数据集合

- 支持增删改查
- 列表中的数据是可变化的【数据项可以变化，内存地址不会改变】
- 数据可以是任意类型
- 支持切片

###### 常用方法

- append
- count
- extend
- index：查找指定元素的索引
    - 找不到会抛出异常
- insert
- pop：移除指定的索引值
- remove：移除指定的元素
    - del 配合切片
- reverse
- sort
-
    *

#### 共有方法

##### 合并操作（+）

两个对象相加的操作会合并两个对象， 适用于

- 字符串
- 列表
- 元组

##### 复制操作（*）

对象自身按照指定次数进行加操作 适用于

- 字符串
- 列表
- 元组

##### 判断元素是否存在（in）

判断指定元素是否存在于对象 适用于

- 字符串
- 列表
- 元组
- 字典

##### 查看类型

```python
a = 10
type(a)
```

### 运算符

#### 算数运算( + - * ** % / // )

#### 比较运算 ( == != > < >= <= )

#### 逻辑运算符 ( and or not )

- 优先级
  () > not > and > or

#### 赋值运算符 ( = += -= *= /= %= **= //=)

### 输入与输出

#### 输出

```python
print('输出')
```

#### 格式化输出

- 使用`%`做占位符，后面加数据类型

```python
name = 'biu'
age = 12
print('name:%s,age:%d' % (name, age))
```

- format

```
name = 'biu'
print('name:{}'.format(name))
```

#### 输入

- input

```python
name = input('姓名')
```

### 流程控制

#### 顺序流程

代码自上而下的执行结构

#### 选择流程/分支流程

根据某一步的判断没有选择的去执行相应的逻辑的一种结构

##### 单分支

```python
if True:
    print('true')
```

##### 双分支

```python
a = 1
if a > 10:
    print('true')
else:
    print('false')
```

##### 多分支

```python
a = 1
if a == 1:
    print(1)
elif a == 2:
    print(2)
else:
    print(3)
```

#### 循环类型

在满足一定的条件下，重复的某段代码

```python
a = 1
while a > 0:
    print(1)

lists = []
for key in lists:
    print(key)
```

#### break 和 continue

- break: 结束整个循环，不在继续
- continue: 结束当前循环，并进入下一次循环

### 函数

一系列Python语句，可以在程序里运行一次或多次。

#### 定义

```
def 函数名():
    函数体;
```

#### 参数

- 形参不占用内存地址
- 实参占用内存地址

##### 必选参数

在函数调用的时候，必须传入的参数

##### 默认参数(缺省参数)

```python
def sum1(a, b=20):
    print(a + b)
    pass
```

##### 可变长参数

当参数的个数不确定时使用

- 元组类型

```python
def get_sum(*args):
    print(args)
```

##### 关键字参数

- 参数的关键字是一个字典类型

```python
def get_sum(**args):
    print(args)


dictA = {'name': 1}
get_sum(**dictA)
get_sum(name=1)
```

#### 函数的返回值
- 函数内有`return`关键字时，返回实际的值，否则返回`None`
- 可以返回任意类型
- 一旦执行`return`语句，会直接退出函数
