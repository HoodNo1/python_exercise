"""
============================================================================
  练习 1：列表基础操作
  练习 2：列表进阶与语法糖
============================================================================

本文件包含两大部分练习题，旨在帮助初学者通过实战掌握 Python 列表的用法。
请按照注释中的要求，在 ... 处补全代码，并运行验证结果。
"""

# ============================================================================
# 第一部分：列表基础操作
# ============================================================================

# ---------------------------------------------------------------------------
# 练习 1.1 —— 创建列表
# 用不同方式创建以下列表并赋值：
#   1) 空列表 empty_list
#   2) 整数列表 [1, 2, 3, 4, 5]
#   3) 混合类型列表 ["hello", 42, 3.14, True]
#   4) 用 list() 将字符串 "Python" 转为字符列表
#   5) 用 list(range(1, 6)) 创建列表
# ---------------------------------------------------------------------------

empty_list = ...
int_list = ...
mixed_list = ...
char_list = ...
range_list = ...

# print(f"空列表: {empty_list}")
# print(f"整数列表: {int_list}")
# print(f"混合列表: {mixed_list}")
# print(f"字符列表: {char_list}")
# print(f"range列表: {range_list}")

# assert empty_list == []
# assert int_list == [1, 2, 3, 4, 5]
# assert char_list == ["P", "y", "t", "h", "o", "n"]
# assert range_list == [1, 2, 3, 4, 5]
# print("练习 1.1 通过！")


# ---------------------------------------------------------------------------
# 练习 1.2 —— 列表索引
# 对于列表 lst = [10, 20, 30, 40, 50]，完成以下操作：
#   1) 获取第 1 个元素（索引 0）
#   2) 获取最后 1 个元素（索引 -1）
#   3) 获取倒数第 2 个元素
#   4) 将第 3 个元素修改为 100
#   5) 尝试越界索引（取消最后一行注释，观察错误）
# ---------------------------------------------------------------------------

lst = [10, 20, 30, 40, 50]

first = ...
last = ...
second_last = ...

# 修改第 3 个元素为 100
lst[2] = ...

# print(f"第一个: {first}, 最后一个: {last}, 倒数第二个: {second_last}")
# print(f"修改后的列表: {lst}")

# assert first == 10
# assert last == 50
# assert second_last == 40
# assert lst == [10, 20, 100, 40, 50]
# print("练习 1.2 通过！")

# 试试下面这行会怎样：
# lst[10]


# ---------------------------------------------------------------------------
# 练习 1.3 —— 列表切片
# 对于 s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，完成切片操作：
#   1) 取前 3 个元素
#   2) 取第 3 到第 6 个元素（不含第 6 个）
#   3) 取所有偶数索引元素（步长为 2）
#   4) 反转列表
#   5) 取后 3 个元素
#   6) 去掉首尾各 2 个元素
# ---------------------------------------------------------------------------

s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

part1 = ...
part2 = ...
every_other = ...
reversed_list = ...
last_three = ...
middle = ...

# print(f"前 3 个: {part1}")
# print(f"第 3-5 个: {part2}")
# print(f"步长为 2: {every_other}")
# print(f"反转: {reversed_list}")
# print(f"后 3 个: {last_three}")
# print(f"去掉首尾各 2 个: {middle}")

# assert part1 == [0, 1, 2]
# assert part2 == [2, 3, 4]
# assert every_other == [0, 2, 4, 6, 8]
# assert reversed_list == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# assert last_three == [7, 8, 9]
# assert middle == [2, 3, 4, 5, 6, 7]
# print("练习 1.3 通过！")


# ---------------------------------------------------------------------------
# 练习 1.4 —— 列表运算：+、*、in
#   1) [1, 2, 3] + [4, 5, 6]  → 拼接
#   2) ["Ha"] * 4             → 重复
#   3) 3 in [1, 2, 3]         → 成员检查
#   4) 10 not in [1, 2, 3]    → 非成员检查
# ---------------------------------------------------------------------------

concat = ...
repeat = ...
contains_3 = ...
not_contains_10 = ...

# print(f"[1,2,3] + [4,5,6] = {concat}")
# print(f"['Ha'] * 4 = {repeat}")
# print(f"3 in [1,2,3] = {contains_3}")
# print(f"10 not in [1,2,3] = {not_contains_10}")

# assert concat == [1, 2, 3, 4, 5, 6]
# assert repeat == ["Ha", "Ha", "Ha", "Ha"]
# assert contains_3 is True
# assert not_contains_10 is True
# print("练习 1.4 通过！")


# ---------------------------------------------------------------------------
# 练习 1.5 —— len()、min()、max()、sum()
# 给定 nums = [7, 2, 9, 1, 5, 6]，计算：
#   1) 列表长度
#   2) 最小值
#   3) 最大值
#   4) 总和
#   5) 平均值（总和 / 长度，返回 float）
# ---------------------------------------------------------------------------

nums = [7, 2, 9, 1, 5, 6]

length = ...
minimum = ...
maximum = ...
total = ...
average = ...

# print(f"长度: {length}")
# print(f"最小值: {minimum}, 最大值: {maximum}")
# print(f"总和: {total}, 平均值: {average}")

# assert length == 6
# assert minimum == 1
# assert maximum == 9
# assert total == 30
# assert average == 5.0
# print("练习 1.5 通过！")


# ---------------------------------------------------------------------------
# 练习 1.6 —— 添加元素：append()、insert()、extend()
# 给定 lst = [1, 2, 3]：
#   1) 在末尾追加 4
#   2) 在索引 0 处插入 0
#   3) 将 [5, 6] 扩展到列表末尾
# 每次操作后打印列表。
# ---------------------------------------------------------------------------

lst = [1, 2, 3]

# 取消注释补全代码
# lst.append(...)
# print(f"append 后: {lst}")

# lst.insert(0, ...)
# print(f"insert 后: {lst}")

# lst.extend([...])
# print(f"extend 后: {lst}")

# assert lst == [0, 1, 2, 3, 4, 5, 6]
# print("练习 1.6 通过！")


# ---------------------------------------------------------------------------
# 练习 1.7 —— 删除元素：remove()、pop()、del、clear()
# 给定 lst = [10, 20, 30, 40, 50, 30]：
#   1) remove(30) —— 删除第一个匹配的 30
#   2) pop()      —— 弹出最后一个元素
#   3) del lst[0] —— 删除索引 0 处的元素
#   4) clear()    —— 清空列表
# 每次操作后观察列表变化。
# ---------------------------------------------------------------------------

lst = [10, 20, 30, 40, 50, 30]

# 取消注释补全代码
# lst.remove(...)
# print(f"remove(30) 后: {lst}")

# popped = lst.pop(...)
# print(f"pop() 后: {lst}, 弹出的值: {popped}")

del lst[0]
# print(f"del lst[0] 后: {lst}")

lst.clear()
# print(f"clear() 后: {lst}")

# assert popped == 50
# assert lst == []
# print("练习 1.7 通过！")


# ---------------------------------------------------------------------------
# 练习 1.8 —— 查找与计数：index()、count()
# 给定 lst = ["a", "b", "c", "a", "b", "a"]：
#   1) 查找 "b" 的索引
#   2) 查找 "a" 出现的次数
#   3) 从索引 2 开始查找 "a"
#   4) 查找不存在的元素（观察异常）
# ---------------------------------------------------------------------------

lst = ["a", "b", "c", "a", "b", "a"]

idx_b = ...
count_a = ...
idx_a_from_2 = ...

# print(f"'b' 的索引: {idx_b}")
# print(f"'a' 出现次数: {count_a}")
# print(f"从索引 2 开始找 'a': {idx_a_from_2}")

# assert idx_b == 1
# assert count_a == 3
# assert idx_a_from_2 == 3
# print("练习 1.8 通过！")

# 试试查找不存在的元素：
# lst.index("z")


# ---------------------------------------------------------------------------
# 练习 1.9 —— 排序与反转：sort()、sorted()、reverse()
#   1) 原地排序 lst.sort()
#   2) 返回新列表 sorted(lst)
#   3) 降序排序（reverse=True）
#   4) 原地反转 lst.reverse()
# 观察 sort() 和 sorted() 的区别（是否修改原列表）。
# ---------------------------------------------------------------------------

nums = [3, 1, 4, 1, 5, 9, 2, 6]

# 原地排序
nums.sort()
# print(f"原地排序后: {nums}")

# 降序排序
# nums.sort(reverse=...)
# print(f"降序排序: {nums}")

# sorted 返回新列表
original = [3, 1, 4, 1, 5]
sorted_copy = sorted(original)
# print(f"original: {original}")
# print(f"sorted_copy: {sorted_copy}")
# print(f"original 未被修改: {original == [3, 1, 4, 1, 5]}")

# 反转
nums.reverse()
# print(f"反转后: {nums}")

# assert sorted_copy == [1, 1, 3, 4, 5]
# assert original == [3, 1, 4, 1, 5]  # sorted() 不修改原列表
# print("练习 1.9 通过！")


# ---------------------------------------------------------------------------
# 练习 1.10 —— 列表复制：浅拷贝与深拷贝
#   1) 用 copy() 复制列表
#   2) 用 [:] 切片复制
#   3) 用 list() 复制
#   4) 验证复制的列表与原列表不是同一个对象（is 比较）
# ---------------------------------------------------------------------------

original = [1, 2, 3, 4, 5]

copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

# print(f"copy1: {copy1}, copy2: {copy2}, copy3: {copy3}")
# print(f"original is copy1: {original is copy1}")

# assert original == copy1 == copy2 == copy3
# assert original is not copy1
# print("练习 1.10 通过！")


# ---------------------------------------------------------------------------
# 练习 1.11 —— 嵌套列表
#   1) 创建嵌套列表 matrix = [[1, 2], [3, 4], [5, 6]]
#   2) 通过索引获取内层元素，如第 2 行第 1 列
#   3) 修改嵌套列表中的元素
#   4) 用 for 循环展平嵌套列表
# ---------------------------------------------------------------------------

matrix = [[1, 2], [3, 4], [5, 6]]

# 获取第 2 行第 1 列的元素（值应为 3）
element = ...

# 修改第 1 行第 2 列的元素为 99
matrix[0][1] = ...

# 展平嵌套列表
flattened = []
for row in matrix:
    for item in row:
        flattened.append(item)

# print(f"matrix: {matrix}")
# print(f"matrix[1][0] = {element}")
# print(f"展平后: {flattened}")

# assert element == 3
# assert matrix[0][1] == 99
# assert flattened == [1, 99, 3, 4, 5, 6]
# print("练习 1.11 通过！")


# ---------------------------------------------------------------------------
# 练习 1.12 —— 列表与字符串互转
#   1) 用 list("hello") 将字符串转为字符列表
#   2) 用 "".join(["h", "e", "l", "l", "o"]) 将列表合成字符串
#   3) 用 "-".join(["2024", "01", "01"]) 合成日期格式
#   4) str.split() 将字符串转为列表
# ---------------------------------------------------------------------------

s = "hello"
char_list = ...

joined = "-".join(["2024", "01", "01"])

csv = "apple,banana,orange"
split_result = ...

# print(f"list('hello'): {char_list}")
# print(f"'-'.join(...): {joined}")
# print(f"split: {split_result}")

# assert char_list == ["h", "e", "l", "l", "o"]
# assert joined == "2024-01-01"
# assert split_result == ["apple", "banana", "orange"]
# print("练习 1.12 通过！")


# ---------------------------------------------------------------------------
# 练习 1.13 —— 列表作为栈（LIFO）
# 用 append() 入栈、pop() 出栈，实现后进先出。
#   1) 空栈 stack
#   2) 依次 push 1, 2, 3
#   3) pop 两次
#   4) 观察栈的状态变化
# ---------------------------------------------------------------------------

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
# print(f"push 后: {stack}")

top1 = stack.pop()
# print(f"pop: {top1}, 栈: {stack}")

top2 = stack.pop()
# print(f"pop: {top2}, 栈: {stack}")

# assert top1 == 3
# assert top2 == 2
# assert stack == [1]
# print("练习 1.13 通过！")


# ---------------------------------------------------------------------------
# 练习 1.14 —— enumerate() 获取索引和值
# 用 enumerate() 同时遍历列表的索引和元素值。
#   1) 将 ["a", "b", "c"] 转为 [(0, "a"), (1, "b"), (2, "c")]
#   2) 指定起始索引为 1
# ---------------------------------------------------------------------------

letters = ["a", "b", "c"]

# 用列表推导式 + enumerate 生成 (索引, 值) 对列表
indexed = ...

# 起始索引为 1
indexed_from_1 = ...

# print(f"enumerate: {indexed}")
# print(f"enumerate(start=1): {indexed_from_1}")

# assert indexed == [(0, "a"), (1, "b"), (2, "c")]
# assert indexed_from_1 == [(1, "a"), (2, "b"), (3, "c")]
# print("练习 1.14 通过！")


# ---------------------------------------------------------------------------
# 练习 1.15 —— zip() 并行遍历
# zip() 将多个列表中对应位置的元素配对。
#   1) zip([1, 2, 3], ["a", "b", "c"]) → [(1, "a"), (2, "b"), (3, "c")]
#   2) zip 两个不等长列表——结果以短的为准
#   3) 用 zip 将两个列表合并为字典
# ---------------------------------------------------------------------------

nums = [1, 2, 3]
chars = ["a", "b", "c"]

zipped = ...

# zip 不等长列表
short = [1, 2]
zipped_short = ...

# zip 转字典
keys = ["name", "age", "city"]
values = ["Alice", 25, "Beijing"]
dict_from_zip = ...

# print(f"zip 结果: {list(zipped)}")
# print(f"不等长 zip: {list(zipped_short)}")
# print(f"字典: {dict_from_zip}")

# assert list(zip(nums, chars)) == [(1, "a"), (2, "b"), (3, "c")]
# assert dict_from_zip == {"name": "Alice", "age": 25, "city": "Beijing"}
# print("练习 1.15 通过！")


# ---------------------------------------------------------------------------
# 练习 1.16 —— 列表比较运算
# Python 支持列表间的比较，按字典序逐个比较元素：
#   1) [1, 2, 3] == [1, 2, 3]     → ?
#   2) [1, 2, 3] == [3, 2, 1]     → ?
#   3) [1, 2, 3] < [1, 2, 4]      → ?（逐个比较）
#   4) [1, 2] < [1, 2, 3]         → ?（短者优先）
#   5) ["a", "b"] < ["b", "a"]    → ?（字符串码点比较）
# ---------------------------------------------------------------------------

cmp1 = ...
cmp2 = ...
cmp3 = ...
cmp4 = ...
cmp5 = ...

# print(f"[1,2,3] == [1,2,3]: {cmp1}")
# print(f"[1,2,3] == [3,2,1]: {cmp2}")
# print(f"[1,2,3] < [1,2,4]: {cmp3}")
# print(f"[1,2] < [1,2,3]: {cmp4}")
# print(f"['a','b'] < ['b','a']: {cmp5}")

# assert cmp1 is True
# assert cmp2 is False
# assert cmp3 is True
# assert cmp4 is True
# assert cmp5 is True
# print("练习 1.16 通过！")


# ---------------------------------------------------------------------------
# 练习 1.17 —— 高级 del：按步长删除
# del 不仅可以删除单个元素，还可以用切片批量删除。
#   1) 删除索引 1~3 的元素
#   2) 删除所有偶数索引位置的元素（步长切片）
#   3) del lst[:] 清空列表（与 lst.clear() 等效）
# ---------------------------------------------------------------------------

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del lst[1:4]
# print(f"删除索引1-3后: {lst}")

lst2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# del lst2[::2]
# print(f"删除偶数索引后: {lst2}")

lst3 = [1, 2, 3]
del lst3[:]
# print(f"清空后: {lst3}")

# assert lst == [0, 4, 5, 6, 7, 8, 9]
# assert lst2 == [1, 3, 5, 7, 9]
# assert lst3 == []
# print("练习 1.17 通过！")


# ---------------------------------------------------------------------------
# 练习 1.18 —— reversed() 内置函数
# reversed() 返回一个反向迭代器（不会修改原列表），
# 而 reverse() 是原地反转。
#   1) 用 reversed() + list() 反转列表
#   2) 用 for 循环遍历 reversed() 的结果
#   3) 对比 reverse() 与 reversed() 的区别
# ---------------------------------------------------------------------------

nums = [1, 2, 3, 4, 5]

# reversed() 返回迭代器，用 list() 转为列表
reversed_iter = ...

# 用 for 遍历 reversed 结果
reversed_items = []
for x in reversed(nums):
    reversed_items.append(...)

# print(f"reversed 转列表: {reversed_iter}")
# print(f"for 遍历 reversed: {reversed_items}")
# print(f"原列表被修改了吗？ {nums}")

# assert reversed_iter == [5, 4, 3, 2, 1]
# assert reversed_items == [5, 4, 3, 2, 1]
# assert nums == [1, 2, 3, 4, 5]  # reversed() 不修改原列表
# print("练习 1.18 通过！")


# ---------------------------------------------------------------------------
# 练习 1.19 —— 列表的真值测试
# Python 中空列表为 False，非空列表为 True。
# 这在 if 语句和逻辑表达式中很常用。
#   1) bool([]) 的结果
#   2) bool([0]) 的结果（注意 0 是假值，但列表非空）
#   3) bool([[]]) 的结果（空列表作为唯一元素）
#   4) 用 if lst: 判断列表非空
# ---------------------------------------------------------------------------

bool_empty = ...
bool_with_zero = ...
bool_nested_empty = ...

# 用 if 判断列表非空
def is_non_empty(lst):
    return ...

# print(f"bool([]): {bool_empty}")
# print(f"bool([0]): {bool_with_zero}")
# print(f"bool([[]]): {bool_nested_empty}")
# print(f"is_non_empty([1, 2]): {is_non_empty([1, 2])}")
# print(f"is_non_empty([]): {is_non_empty([])}")

# assert bool_empty is False
# assert bool_with_zero is True   # 列表包含元素即为 True
# assert bool_nested_empty is True
# assert is_non_empty([1, 2]) is True
# assert is_non_empty([]) is False
# print("练习 1.19 通过！")


# ---------------------------------------------------------------------------
# 练习 1.20 —— 列表与元组互转
# 元组是不可变的序列，列表是可变序列。
#   1) 列表转元组：tuple([1, 2, 3])
#   2) 元组转列表：list((1, 2, 3))
#   3) 列表转元组的应用：作为字典的键（列表不行）
# ---------------------------------------------------------------------------

lst = [1, 2, 3]
tpl = ...
# print(f"列表转元组: {tpl}, 类型: {type(tpl).__name__}")

tpl2 = (4, 5, 6)
lst_from_tuple = ...
# print(f"元组转列表: {lst_from_tuple}")

# 作为字典键（列表不可哈希，元组可以）
data = {1: "a", 2: "b"}
# 将字典键值对转为 (键, 值) 元组列表
items = ...

# assert tpl == (1, 2, 3)
# assert lst_from_tuple == [4, 5, 6]
# assert items == [(1, "a"), (2, "b")]
# print("练习 1.20 通过！")


# ---------------------------------------------------------------------------
# 练习 1.21 —— 列表的 += 与 = + 的区别
# += 在列表上是原地操作（调用 __iadd__），
# = lst + other 创建新列表。
# 用 id() 验证两者的区别。
# ---------------------------------------------------------------------------

a = [1, 2, 3]
# id_before = id(a)
a += [4, 5]
# id_after = id(a)
# print(f"+= 后 id 相同: {id_before == id_after}")

b = [1, 2, 3]
# id_before = id(b)
b = b + [4, 5]
# id_after = id(b)
# print(f"= + 后 id 相同: {id_before == id_after}")

# 用 extend 实现相同效果
c = [1, 2, 3]
c.extend([4, 5])

# assert a == [1, 2, 3, 4, 5]
# assert id_before == id_after  # 仅检查 += 版本: 地址不变
# assert c == [1, 2, 3, 4, 5]
# print("练习 1.21 通过！")


# ---------------------------------------------------------------------------
# 练习 1.22 —— 列表拆包与 *
# 用 * 在列表字面量中展开其他列表（Python 3.5+）：
#   1) [*range(5)]            → 展开 range
#   2) [*[1, 2], *[3, 4]]     → 合并列表
#   3) [0, *mid, 5]           → 在中间插入
# ---------------------------------------------------------------------------

# 展开 range
expanded = ...

# 合并多个列表
a = [1, 2]
b = [3, 4]
merged = ...

# 在列表中间插入
mid = [2, 3, 4]
new_list = ...

# print(f"[*range(5)]: {expanded}")
# print(f"合并: {merged}")
# print(f"插入中间: {new_list}")

# assert expanded == [0, 1, 2, 3, 4]
# assert merged == [1, 2, 3, 4]
# assert new_list == [1, 2, 3, 4, 5]
# print("练习 1.22 通过！")


# ---------------------------------------------------------------------------
# 练习 1.23 —— max() 和 min() 的 key 参数
# max()/min() 也支持 key 参数，与 sort() 的 key 类似。
#   1) 找出最长的字符串
#   2) 找出绝对值最小的数
#   3) 找出按最后字符排序"最大"的字符串
# ---------------------------------------------------------------------------

words = ["banana", "apple", "cherry", "date"]
longest = ...

nums = [-5, 3, -2, 1, -4]
closest_to_zero = ...

# 按最后一个字符找出"最大"的字符串
last_char_max = ...

# print(f"最长单词: {longest}")
# print(f"绝对值最小: {closest_to_zero}")
# print(f"末字符最大: {last_char_max}")

# assert longest == "banana"
# assert closest_to_zero == 1
# assert last_char_max == "cherry"  # 'y' > 'e' > 'y' > 'e'
# print("练习 1.23 通过！")


# ---------------------------------------------------------------------------
# 练习 1.24 —— enumerate 与 zip 结合使用
# 同时遍历两个列表，既需要索引又需要对应元素：
#   1) 同时遍历 names 和 scores，输出 "第 i 名: name → score"
#   2) 用 enumerate + zip 实现
# ---------------------------------------------------------------------------

names = ["Alice", "Bob", "Carol"]
scores = [85, 92, 78]

# 用 enumerate + zip 生成格式化列表
formatted = ...
# print("成绩单:")
# for line in formatted:
#     print(f"  {line}")

# 反向配对：从两个列表构建字典 {name: score}
score_dict = ...

# assert formatted == ["第1名: Alice → 85", "第2名: Bob → 92", "第3名: Carol → 78"]
# assert score_dict == {"Alice": 85, "Bob": 92, "Carol": 78}
# print("练习 1.24 通过！")


# ---------------------------------------------------------------------------
# 练习 1.25 —— 列表的切片插入
# 通过给空切片赋值，可以在不删除元素的情况下插入新元素。
#   1) lst[2:2] = ["X", "Y"] 在索引 2 处插入
#   2) lst[0:0] = ["START"]  在开头插入
#   3) lst[len(lst):len(lst)] = ["END"]  在末尾插入
# 观察切片插入与 insert() 的异同。
# ---------------------------------------------------------------------------

lst = [1, 2, 5, 6]

# 在索引 2 处插入 [3, 4]
# lst[2:2] = ...
# print(f"插入后: {lst}")

# 在开头插入
# lst[0:0] = ...
# print(f"开头插入: {lst}")

# 在末尾插入
# lst[len(lst):len(lst)] = ...
# print(f"末尾插入: {lst}")

# assert lst == [0, 1, 2, 3, 4, 5, 6, 99]
# print("练习 1.25 通过！")


# ============================================================================
# 第一部分 结束
# 恭喜完成列表基础部分！
# ============================================================================


# ============================================================================
# 第二部分：列表进阶与语法糖
# ============================================================================


# ---------------------------------------------------------------------------
# 练习 2.1 —— 列表推导式基础
# 用列表推导式替代以下 for 循环写法：
#   1) [x**2 for x in range(5)] → 0, 1, 4, 9, 16
#   2) 将 ["hello", "world", "python"] 每个单词转大写
#   3) 将 [1, 2, 3, 4, 5] 每个元素转字符串
# ---------------------------------------------------------------------------

squares = ...
words = ["hello", "world", "python"]
upper_words = ...
nums = [1, 2, 3, 4, 5]
str_nums = ...

# print(f"平方数: {squares}")
# print(f"大写: {upper_words}")
# print(f"字符串: {str_nums}")

# assert squares == [0, 1, 4, 9, 16]
# assert upper_words == ["HELLO", "WORLD", "PYTHON"]
# assert str_nums == ["1", "2", "3", "4", "5"]
# print("练习 2.1 通过！")


# ---------------------------------------------------------------------------
# 练习 2.2 —— 带条件的列表推导式
# 在推导式后加 if 条件筛选元素：
#   1) 取 [0..19] 中的偶数
#   2) 取字符串列表中长度 >= 5 的单词
#   3) 取 1..20 中能被 3 或 5 整除的数
# ---------------------------------------------------------------------------

evens = ...
words = ["cat", "banana", "dog", "elephant", "fox", "giraffe"]
long_words = ...

# 1..20 中能被 3 或 5 整除的数
divisible = ...

# print(f"偶数: {evens}")
# print(f"长单词: {long_words}")
# print(f"被 3 或 5 整除: {divisible}")

# assert evens == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# assert long_words == ["banana", "elephant", "giraffe"]
# assert divisible == [3, 5, 6, 9, 10, 12, 15, 18, 20]
# print("练习 2.2 通过！")


# ---------------------------------------------------------------------------
# 练习 2.3 —— 嵌套列表推导式
#   1) 用单层推导式展平: [[1,2], [3,4], [5,6]] → [1,2,3,4,5,6]
#   2) 生成 3x3 乘法表矩阵
#      提示: [[i*j for j in range(1,4)] for i in range(1,4)]
# ---------------------------------------------------------------------------

matrix = [[1, 2], [3, 4], [5, 6]]
flattened = ...

# 3x3 乘法表
mult_table = ...

# print(f"展平: {flattened}")
# for row in mult_table:
#     print(f"  {row}")

# assert flattened == [1, 2, 3, 4, 5, 6]
# assert mult_table[0] == [1, 2, 3]
# assert mult_table[2] == [3, 6, 9]
# print("练习 2.3 通过！")


# ---------------------------------------------------------------------------
# 练习 2.4 —— 列表推导式与 if-else（三元表达式）
# 将 [1, 2, 3, 4, 5] 中的偶数变为 "even"，奇数变为 "odd"。
# 提示：在推导式中使用 x if condition else y 的形式。
# ---------------------------------------------------------------------------

nums = [1, 2, 3, 4, 5]
parity = ...

# print(f"奇偶标记: {parity}")

# assert parity == ["odd", "even", "odd", "even", "odd"]
# print("练习 2.4 通过！")


# ---------------------------------------------------------------------------
# 练习 2.5 —— 星号解包（Python 3.0+）
# 用 * 将列表元素解包到变量：
#   1) first, *middle, last = [1, 2, 3, 4, 5]
#   2) 用 * 解包列表传递给 print
#   3) 用 * 合并多个列表
# ---------------------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]
# first, *middle, last = ...
# print(f"first={first}, middle={middle}, last={last}")

# 提示：取消上面的注释，将 ... 替换为 numbers

# 用 * 合并列表
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]
merged = ...

# print(f"合并后: {merged}")

# assert first == 1
# assert last == 5
# assert middle == [2, 3, 4]
# assert merged == [1, 2, 3, 4, 5, 6]
# print("练习 2.5 通过！")


# ---------------------------------------------------------------------------
# 练习 2.6 —— 嵌套解包与下划线占位
# 处理多层嵌套列表的解包：
#   1) (a, b), point = [(1, 2), (3, 4, 5)]
#   2) 用 _ 忽略不需要的值：a, _, b = [1, 2, 3]
#   3) 用 *_ 忽略多个值：a, *_, b = [1, 2, 3, 4, 5]
# ---------------------------------------------------------------------------

pairs = [(1, 2), (3, 4, 5)]
# (a, b), point = ...

# print(f"a={a}, b={b}, point={point}")

values = [1, 2, 3, 4, 5]
# x, *_, y = ...

# print(f"x={x}, y={y}, 中间被忽略: {_}")

# assert a == 1
# assert b == 2
# assert point == (3, 4, 5)
# assert x == 1
# assert y == 5
# print("练习 2.6 通过！")


# ---------------------------------------------------------------------------
# 练习 2.7 —— 列表推导式中的海象运算符（Python 3.8+）
# 海象运算符 (:=) 可以在推导式中避免重复计算。
# 计算 [1, 2, 3, 4, 5, 6] 中偶数的平方，
# 只保留平方值大于 10 的结果。
# 参考：使用 (y := x**2) 同时完成平方计算和条件判断。
# ---------------------------------------------------------------------------

nums = [1, 2, 3, 4, 5, 6]
result = ...

# print(f"偶数平方且 > 10: {result}")

# assert result == [16, 36]
# print("练习 2.7 通过！")


# ---------------------------------------------------------------------------
# 练习 2.8 —— sort() 的 key 参数
# 用 key 参数实现自定义排序：
#   1) 按字符串长度排序
#   2) 按最后一个字符排序
#   3) 按绝对值排序（含负数）
# ---------------------------------------------------------------------------

words = ["banana", "apple", "cherry", "date"]

# 按长度排序
# sorted_by_len = sorted(words, key=...)

# 按最后一个字符排序
# sorted_by_last = sorted(words, key=...)

nums = [-5, 3, -2, 1, -4]
# sorted_by_abs = sorted(nums, key=...)

# print(f"按长度: {sorted_by_len}")
# print(f"按末字符: {sorted_by_last}")
# print(f"按绝对值: {sorted_by_abs}")

# assert sorted_by_len == ["date", "apple", "banana", "cherry"]
# assert sorted_by_abs == [1, -2, 3, -4, -5]
# print("练习 2.8 通过！")


# ---------------------------------------------------------------------------
# 练习 2.9 —— all() 与 any()
# all() 所有元素为真返回 True，any() 任一元素为真返回 True。
#   1) all([1, 2, 3])       → ?  （没有假值）
#   2) all([1, 0, 3])       → ?  （0 是假值）
#   3) any([0, "", False])   → ?  （全是假值）
#   4) any([0, "", 1])       → ?  （1 是真值）
#   5) 判断列表是否所有元素 > 0
#   6) 判断列表是否包含偶数
# ---------------------------------------------------------------------------

# all_true = all([...])
# all_with_zero = all([...])
# any_false = any([...])
# any_with_true = any([...])

nums = [1, 2, 3, 4, 5]
all_positive = all(x > 0 for x in nums)
has_even = any(x % 2 == 0 for x in nums)

# print(f"all([1,2,3]): {all_true}")
# print(f"all([1,0,3]): {all_with_zero}")
# print(f"any([0,'',False]): {any_false}")
# print(f"any([0,'',1]): {any_with_true}")
# print(f"全部正数: {all_positive}")
# print(f"包含偶数: {has_even}")

# assert all_true is True
# assert all_with_zero is False
# assert any_false is False
# assert any_with_true is True
# assert all_positive is True
# assert has_even is True
# print("练习 2.9 通过！")


# ---------------------------------------------------------------------------
# 练习 2.10 —— map() 与 filter() 对比推导式
# map() 和 filter() 是函数式编程工具，推导式是 Python 风格。
#   1) map(str.upper, ["a", "b", "c"]) 转大写
#   2) filter(lambda x: x > 0, [-2, -1, 0, 1, 2]) 取正数
#   3) 用推导式完成相同功能（对比两种风格）
# ---------------------------------------------------------------------------

words = ["a", "b", "c"]
upper_map = ...

numbers = [-2, -1, 0, 1, 2]
positive_filter = ...

# 用推导式实现相同结果
upper_comp = ...
positive_comp = ...

# print(f"map 结果: {upper_map}")
# print(f"filter 结果: {positive_filter}")
# print(f"推导式大写: {upper_comp}")
# print(f"推导式正数: {positive_comp}")

# assert upper_map == ["A", "B", "C"]
# assert positive_filter == [1, 2]
# print("练习 2.10 通过！")


# ---------------------------------------------------------------------------
# 练习 2.11 —— 列表的切片赋值
# Python 允许对切片赋值，用新列表替换切片部分。
#   1) 将 [1, 2, 3, 4, 5] 的中间 3 个替换为 [99, 100]
#   2) 使用步长切片赋值：将偶数索引位置全部改为 0
#   3) 用切片赋值清空列表
# ---------------------------------------------------------------------------

lst1 = [1, 2, 3, 4, 5]
lst1[1:4] = [99, 100]
# print(f"替换中间部分: {lst1}")

lst2 = [1, 2, 3, 4, 5, 6]
# 将偶数索引位置（0, 2, 4）替换为 [0, 0, 0]
# lst2[::2] = ...

# print(f"偶数索引置零: {lst2}")

# 用切片赋值清空列表
lst3 = [1, 2, 3, 4, 5]
lst3[:] = []

# assert lst1 == [1, 99, 100, 5]
# assert lst2 == [0, 2, 0, 4, 0, 6]
# assert lst3 == []
# print("练习 2.11 通过！")


# ---------------------------------------------------------------------------
# 练习 2.12 —— 列表排序：稳定性与多级排序
# Python 的排序是稳定的（相等元素保持原顺序）。
#   1) 按元组第一个元素排序，相同则按第二个
#   2) 先按长度排序，相同长度按字母序
#   3) 用 attrgetter 或 lambda 实现复杂排序
# ---------------------------------------------------------------------------

pairs_data = [(1, "b"), (2, "a"), (1, "a"), (2, "b")]
# sorted_pairs = sorted(pairs_data, key=...)

words = ["banana", "cat", "apple", "dog", "cherry"]
# 先按长度，再按字母序
# sorted_words = sorted(words, key=...)

# print(f"多级排序: {sorted_pairs}")
# print(f"长度+字母: {sorted_words}")

# assert sorted_pairs == [(1, "a"), (1, "b"), (2, "a"), (2, "b")]
# assert sorted_words == ["cat", "dog", "apple", "banana", "cherry"]
# print("练习 2.12 通过！")


# ---------------------------------------------------------------------------
# 练习 2.13 —— for-else 与列表搜索
# Python 的 for 循环可以带 else 子句，在循环未被 break 时执行。
# 在列表中查找第一个偶数并打印，如果没找到则打印"未找到偶数"。
# 补全以下代码，使 else 在循环未被 break 时触发。
# ---------------------------------------------------------------------------

numbers = [1, 3, 5, 7, 8, 9]

for n in numbers:
    if n % 2 == 0:
        # print(f"找到偶数: {n}")
        ...
else:
    # print("未找到偶数")
    ...


# 查找所有偶数（用列表推导式）
evens_found = ...

# print(f"列表中的偶数: {evens_found}")

# assert evens_found == [8]
# print("练习 2.13 通过！")


# ---------------------------------------------------------------------------
# 练习 2.14 —— 列表的浅拷贝与深拷贝问题
# 当列表包含可变对象时，浅拷贝可能共享内部引用。
#   1) 创建嵌套列表并浅拷贝
#   2) 修改内层元素，观察两个列表的变化
#   3) 用 copy.deepcopy() 实现深拷贝
# ---------------------------------------------------------------------------

import copy

original = [[1, 2], [3, 4]]
shallow = original.copy()

# 修改 shallow 的内层元素
shallow[0][0] = 99

# print(f"original: {original}")
# print(f"shallow: {shallow}")
# print(f"original[0][0] 被同时修改了？ {original[0][0] == 99}")

# 用 deepcopy 避免共享
original2 = [[1, 2], [3, 4]]
deep = copy.deepcopy(original2)

deep[0][0] = 99
# print(f"deepcopy original: {original2}")
# print(f"deepcopy copy: {deep}")
# print(f"original2 不受影响: {original2[0][0] == 1}")

# assert original[0][0] == 99  # 浅拷贝共享内层引用
# assert original2[0][0] == 1  # 深拷贝完全独立
# print("练习 2.14 通过！")


# ---------------------------------------------------------------------------
# 练习 2.15 —— match/case 模式匹配列表（Python 3.10+）
# 用 match/case 匹配列表的不同结构。
# 实现函数 process_list(lst)，根据列表内容返回描述：
#   - 空列表 → "空列表"
#   - 只有一个元素 → "单元素列表"
#   - 前两个元素相同 → "前两个相同"
#   - 包含 0 的列表 → "包含零"
#   - 其他 → "普通列表"
# ---------------------------------------------------------------------------


def process_list(lst: list) -> str:
    """用 match/case 判断列表的特征。"""
    match lst:
        case []:
            ...
        case [x]:
            ...
        case [x, y, *rest] if x == y:
            ...
        case _ if 0 in lst:
            ...
        case _:
            ...


# print(process_list([]))           # → "空列表"
# print(process_list([42]))         # → "单元素列表"
# print(process_list([1, 1, 2]))    # → "前两个相同"
# print(process_list([1, 2, 0]))    # → "包含零"
# print(process_list([1, 2, 3]))    # → "普通列表"

# assert process_list([]) == "空列表"
# assert process_list([42]) == "单元素列表"
# assert process_list([1, 1, 2]) == "前两个相同"
# assert process_list([1, 2, 0]) == "包含零"
# assert process_list([1, 2, 3]) == "普通列表"
# print("练习 2.15 通过！")


# ---------------------------------------------------------------------------
# 练习 2.16 —— itertools.chain 展平列表
# itertools.chain 可以将多个可迭代对象串联为一个迭代器。
# 比多重循环更简洁，比 sum(list, []) 更高效。
#   1) 用 chain 展平 [[1,2], [3,4], [5,6]]
#   2) 用 chain.from_iterable 展平
#   3) 对比 sum(lst, []) 的写法（效率较低）
# ---------------------------------------------------------------------------

from itertools import chain

matrix = [[1, 2], [3, 4], [5, 6]]

flat1 = ...
flat2 = ...

# 用 sum 展平（不推荐，仅供对比）
flat3 = sum(matrix, [])

# print(f"chain: {flat1}")
# print(f"from_iterable: {flat2}")
# print(f"sum: {flat3}")

# assert flat1 == [1, 2, 3, 4, 5, 6]
# assert flat2 == [1, 2, 3, 4, 5, 6]
# print("练习 2.16 通过！")


# ---------------------------------------------------------------------------
# 练习 2.17 —— 列表作队列（FIFO）
# 列表用 pop(0) 可实现队列，但效率低。
# collections.deque 是高效的双端队列。
#   1) 用列表实现队列：append() + pop(0)
#   2) 用 deque 实现队列：append() + popleft()
#   3) 对比两种方式的性能差异
# ---------------------------------------------------------------------------

from collections import deque

# 用列表模拟队列
q_list = []
q_list.append("a")
q_list.append("b")
q_list.append("c")
first_out = q_list.pop(0)
# print(f"列表队列 pop(0): {first_out}, 剩余: {q_list}")

# 用 deque 实现队列
q_deque = deque()
q_deque.append("a")
q_deque.append("b")
q_deque.append("c")
first_out2 = ...
# print(f"deque 队列 popleft: {first_out2}, 剩余: {list(q_deque)}")

# deque 也支持左侧添加
q_deque.appendleft("z")
# print(f"左侧添加后: {list(q_deque)}")

# assert first_out == "a"
# assert first_out2 == "a"
# assert list(q_deque) == ["z", "b", "c"]
# print("练习 2.17 通过！")


# ---------------------------------------------------------------------------
# 练习 2.18 —— filter(None, lst) 过滤假值
# filter(None, iterable) 会过滤掉所有假值元素
# （False、None、0、""、[] 等）。
#   1) filter(None, [0, 1, "", "hello", [], [1, 2], None])
#   2) 用列表推导式实现相同功能
#   3) 注意 0 和空字符串也被过滤掉
# ---------------------------------------------------------------------------

mixed = [0, 1, "", "hello", [], [1, 2], None]

filtered = ...
filtered_comp = ...

# print(f"filter(None): {filtered}")
# print(f"推导式: {filtered_comp}")

# 只过滤 None（保留 0 和 空字符串）
filtered_none = ...

# print(f"只过滤 None: {filtered_none}")

# assert filtered == [1, "hello", [1, 2]]
# assert filtered_comp == [1, "hello", [1, 2]]
# assert None not in filtered_none
# assert 0 in filtered_none
# assert "" in filtered_none
# print("练习 2.18 通过！")


# ---------------------------------------------------------------------------
# 练习 2.19 —— 列表推导式批量更新元素
# 用推导式对列表中满足条件的元素进行更新，不满足的保留原值。
#   1) 将列表中所有负数替换为 0
#   2) 将字符串列表中所有长度 < 4 的单词转为大写
#   3) 将嵌套列表中所有偶数替换为字符串 "even"
# ---------------------------------------------------------------------------

nums = [-3, 5, -1, 0, 2, -8, 7]
non_negative = ...

words = ["cat", "banana", "dog", "elephant", "fox"]
processed = ...

# 嵌套列表处理
matrix = [[1, 2], [3, 4], [5, 6]]
labeled = ...

# print(f"非负数: {non_negative}")
# print(f"短单词转大写: {processed}")
# print(f"奇偶标记矩阵: {labeled}")

# assert non_negative == [0, 5, 0, 0, 2, 0, 7]
# assert "CAT" in processed
# assert "elephant" in processed  # 保持不变
# assert labeled == [["odd", "even"], ["odd", "even"], ["odd", "even"]]
# print("练习 2.19 通过！")


# ---------------------------------------------------------------------------
# 练习 2.20 —— operator.itemgetter 多级排序
# itemgetter 可以替代 lambda 实现更简洁的多字段排序。
#   1) 按字典的某个键排序
#   2) 按多个键排序（先 age 再 name）
#   3) itemgetter 与 sorted 结合
# ---------------------------------------------------------------------------

from operator import itemgetter

students = [
    {"name": "Alice", "age": 25, "score": 88},
    {"name": "Bob", "age": 22, "score": 95},
    {"name": "Carol", "age": 25, "score": 80},
    {"name": "Dave", "age": 22, "score": 92},
]

# 按 age 排序
sorted_by_age = ...

# 先按 age 再按 score（降序）
sorted_by_age_score = ...

# 只看分数最高的两个学生
top2 = ...

# print(f"按年龄: {[s['name'] for s in sorted_by_age]}")
# print(f"按年龄+分数: {[s['name'] for s in sorted_by_age_score]}")
# print(f"前两名: {[s['name'] for s in top2]}")

# assert sorted_by_age[0]["name"] == "Bob"  # age=22
# assert top2[0]["name"] == "Bob"           # score=95
# print("练习 2.20 通过！")


# ---------------------------------------------------------------------------
# 练习 2.21 —— 矩阵转置（zip(*matrix)）
# 用 zip(*matrix) 可以将矩阵的行列互换，实现转置。
#   1) 将 3x2 矩阵转置为 2x3
#   2) 用列表推导式实现相同效果
#   3) 理解 *matrix 将每行作为独立参数传给 zip
# ---------------------------------------------------------------------------

matrix = [[1, 2], [3, 4], [5, 6]]

# 转置为 [[1, 3, 5], [2, 4, 6]]
transposed = ...

# 用嵌套推导式实现
transposed_comp = ...

# print(f"原矩阵: {matrix}")
# print(f"转置后: {transposed}")
# print(f"推导式转置: {transposed_comp}")

# assert transposed == [[1, 3, 5], [2, 4, 6]]
# assert transposed_comp == [[1, 3, 5], [2, 4, 6]]
# print("练习 2.21 通过！")


# ---------------------------------------------------------------------------
# 练习 2.22 —— 递归展平不定深度嵌套列表
# 嵌套列表的深度不确定时，需要递归展平。
# 实现函数 deep_flatten(nested)，将任意深度的嵌套列表展平。
#   例如: deep_flatten([1, [2, [3, 4], 5], 6]) → [1, 2, 3, 4, 5, 6]
# ---------------------------------------------------------------------------


def deep_flatten(nested):
    """递归展平任意深度的嵌套列表。"""
    result = []
    for item in nested:
        if isinstance(item, list):
            ...
        else:
            ...
    return result


# print(deep_flatten([1, [2, [3, 4], 5], 6]))    # → [1, 2, 3, 4, 5, 6]
# print(deep_flatten([1, 2, 3]))                  # → [1, 2, 3]
# print(deep_flatten([]))                          # → []

# assert deep_flatten([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]
# assert deep_flatten([1, 2, 3]) == [1, 2, 3]
# assert deep_flatten([]) == []
# print("练习 2.22 通过！")


# ---------------------------------------------------------------------------
# 练习 2.23 —— 列表分组：itertools.groupby
# groupby 将连续相同键的元素分组，注意需要先排序。
#   1) 对字符串按首字母分组
#   2) 对数字按奇偶分组
# ---------------------------------------------------------------------------

from itertools import groupby

# 按首字母分组
words = ["apple", "banana", "apricot", "blueberry", "cherry", "avocado"]
# words.sort(key=...)  # 按首字母排序（groupby 需要已排序数据）

groups = {}
# for key, group in groupby(words, key=...):
#     groups[key] = list(group)
# print(f"按首字母分组: {groups}")

# 按奇偶分组
nums = [1, 2, 3, 4, 5, 6, 7, 8]
# nums.sort(key=...)
parity_groups = {}
# for key, group in groupby(nums, key=lambda x: x % 2 == 0):
#     parity_groups[key] = list(group)
# print(f"按奇偶分组: {parity_groups}")

# assert "a" in groups
# assert len(groups["a"]) == 3  # apple, apricot, avocado
# print("练习 2.23 通过！")


# ---------------------------------------------------------------------------
# 练习 2.24 —— 列表类型注解进阶
# Python 3.9+ 支持 list[type] 语法标注列表元素类型。
# 复杂类型注解提高代码可读性和 IDE 支持。
#   1) list[int | float]：数字列表
#   2) list[list[int]]：嵌套整数矩阵
#   3) list[dict[str, int | str]]：字典列表
# 为以下函数补全类型注解。
# ---------------------------------------------------------------------------

from typing import assert_type  # Python 3.11+


# 矩阵加法：两个相同形状的矩阵逐元素相加
def matrix_add(
    a: ...,  # list[list[int | float]]
    b: ...,  # list[list[int | float]]
) -> ...:   # list[list[int | float]]
    """两个矩阵逐元素相加。"""
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


# print(matrix_add([[1, 2], [3, 4]], [[5, 6], [7, 8]]))  # → [[6, 8], [10, 12]]

# assert matrix_add([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[6, 8], [10, 12]]
# print("练习 2.24 通过！")


# ---------------------------------------------------------------------------
# 练习 2.25 —— 综合挑战：列表频率统计与 Top K
# 实现函数 top_k(lst, k)，返回列表中出现频率最高的前 k 个元素及其次数。
#   要求：
#     - 返回 [(元素, 次数), ...] 按次数降序排列
#     - 次数相同时按元素大小升序
#     - 如果 k 大于不同元素个数，返回全部
#   例如：
#     top_k([1, 1, 1, 2, 2, 3], 2) → [(1, 3), (2, 2)]
# ---------------------------------------------------------------------------


def top_k(lst: list, k: int) -> list[tuple]:
    """返回列表中出现频率最高的前 k 个元素。"""
    # TODO: 统计每个元素出现的次数（用字典或 Counter）
    # TODO: 按次数降序，次数相同按元素升序排序
    # TODO: 取前 k 个
    ...


# print(top_k([1, 1, 1, 2, 2, 3], 2))  # → [(1, 3), (2, 2)]
# print(top_k(["a", "a", "b", "c", "c", "c"], 3))  # → [("c", 3), ("a", 2), ("b", 1)]
# print(top_k([1, 2, 3], 5))  # → [(1, 1), (2, 1), (3, 1)]

# assert top_k([1, 1, 1, 2, 2, 3], 2) == [(1, 3), (2, 2)]
# assert top_k(["a", "a", "b", "c", "c", "c"], 2) == [("c", 3), ("a", 2)]
# assert len(top_k([1, 2, 3], 5)) == 3
# print("练习 2.25 通过！")


# ============================================================================
# 结束
# ============================================================================
# 恭喜你完成了所有列表练习！
# 本文件共两大部分，涵盖 50 道练习题（每部分 25 题）。
# 请逐一取消每个练习中的 print/assert 注释，运行脚本验证你的答案。
# 运行方式：uv run python practice_02_list.py
# ============================================================================
