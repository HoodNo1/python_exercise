"""
============================================================================
  练习 1：数据类型与变量
  练习 2：字符串与编码
============================================================================

本文件包含两大部分练习题，旨在帮助初学者通过实战掌握 Python 的基础知识。
请按照注释中的要求，在 ... 处补全代码，并运行验证结果。
"""

# ============================================================================
# 第一部分：数据类型与变量
# ============================================================================

# ---------------------------------------------------------------------------
# 练习 1.1 —— 整数类型（int）
# 请在下方创建三个变量：
#   a = 42          （十进制）
#   b = 0x2A        （十六进制，值应等于 42）
#   c = 0b101010    （二进制，值应等于 42）
# 然后用 print() 输出它们，验证结果是否都为 42。
# ---------------------------------------------------------------------------

a = 42
b = 0x2A
c = 0b101010

# 将下面三行的注释取消，验证结果
print(f"a = {a}, b = {b}, c = {c}")
assert a == b == c == 42, "三个变量的值应该都等于 42"
print("练习 1.1 通过！")


# ---------------------------------------------------------------------------
# 练习 1.2 —— 浮点数类型（float）
# 1) 定义变量 pi = 3.1415926535，只保留两位小数输出（即 3.14）
#    提示：用 round() 或 f-string 格式化
# 2) 用 type() 检查 pi 的类型并打印
# 3) 尝试 0.1 + 0.2，观察结果，想想为什么不是精确的 0.3
# ---------------------------------------------------------------------------

pi = 3.1415926535

# 保留两位小数
pi_rounded = round(float(pi), 2)
pi_rounded = f"{pi_rounded:.2f}"
pi_rounded:float = float(pi_rounded)

pi_test = f"{pi:.3f}"

print(f"pi 保留三位小数: {pi_test}")
print(f"pi 保留两位小数: {pi_rounded}")
print(f"pi 的类型: {type(pi)}")
print(f"0.1 + 0.2 = {0.1 + 0.2}")

# 思考题（无需代码）：为什么 0.1 + 0.2 != 0.3？


# ---------------------------------------------------------------------------
# 练习 1.3 —— 布尔类型（bool）
# 判断以下表达式的结果（True 或 False）并验证：
#   1) 100 > 50
#   2) 3.14 == 3.14
#   3) "abc" < "abd"
#   4) bool(0)、bool(1)、bool("")、bool("hello")
#   5) 空列表、空字典的布尔值
# 将结果赋值给对应变量，然后用 assert 验证。
# ---------------------------------------------------------------------------

expr1 = 100 > 50   # 100 > 50
expr2 = 3.14 == 3.14   # 3.14 == 3.14
expr3 = "abc" < "abd"   # "abc" < "abd"
expr4 = bool(0)   # bool(0)
expr5 = bool(1)   # bool(1)
expr6 = bool("")   # bool("")
expr7 = bool("hello")   # bool("hello")
expr8 = bool([])   # bool([])
expr9 = bool({})   # bool({})

assert expr1 is True
assert expr2 is True
assert expr3 is True
assert expr4 is False
assert expr5 is True
assert expr6 is False
assert expr7 is True
assert expr8 is False
assert expr9 is False
print("练习 1.3 通过！")


# ---------------------------------------------------------------------------
# 练习 1.4 —— NoneType（None）
# Python 中 None 表示"没有值"或"空"。
# 1) 创建变量 result = None
# 2) 用 is None 判断它是否为 None
# 3) 用 == None 判断它是否为 None
# 4) 思考：为什么官方推荐用 is None 而不是 == None？
# 5) 定义一个函数，不写 return，观察其返回值是否为 None
# ---------------------------------------------------------------------------

result = None

# 判断是否为 None
print(f"result is None: {result is None}")
print(f"result == None: {result == None}")


def no_return():
    x = 1 + 1

print(f"无 return 的函数返回值: {no_return()}")
assert no_return() is None
print("练习 1.4 通过！")


# ---------------------------------------------------------------------------
# 练习 1.5 —— 类型转换
# 完成以下类型转换任务：
#   1) str "123"   → int
#   2) str "3.14"  → float
#   3) int 42      → str
#   4) float 9.99  → int（截断还是四舍五入？）
#   5) str "hello" → int（试试会发生什么）
# 将转换结果赋值并输出，观察哪些会报错。
# ---------------------------------------------------------------------------

s1 = "123"
s2 = "3.14"
n = 42
f = 9.99
s3 = "hello"

i_from_s1 = int(s1)   # str → int
f_from_s2 = float(s2)   # str → float
str_from_n = f"{n}"  # int → str
i_from_f = int(f)    # float → int

print(f'"{s1}" → int: {i_from_s1}')
print(f'"{s2}" → float: {f_from_s2}')
print(f"{n} → str: {str_from_n!r}")
print(f"{f} → int（截断）: {i_from_f}")

# 下面这行会报错，取消注释前请做好心理准备：
# i_from_s3 = int(s3)

assert i_from_s1 == 123
assert abs(f_from_s2 - 3.14) < 0.001
assert str_from_n == "42"
assert i_from_f == 9
print("练习 1.5 通过！")


# ---------------------------------------------------------------------------
# 练习 1.6 —— 变量命名规范
# 以下哪些是合法的 Python 变量名？把合法的赋值后打印出来。
# 非法的用注释说明原因（每行一个）。
#
#   name, 2name, my-name, _name, name!, Name, NAME, name_1, for, _123
#
# 合法与非法都要写出来（非法的写注释说明原因）。
# ---------------------------------------------------------------------------

name = "合法"
# 2name = "非法"    # 原因：不能以数字开头
# my-name = "非法"  # 原因：包含连字符，非法字符
_name = "合法"
# name! = "非法"    # 原因：感叹号不是合法字符
Name = "合法（区分大小写）"
NAME = "合法（区分大小写）"
name_1 = "合法"
# for = "非法"      # 原因：for 是 Python 关键字
_123 = "合法"

# 下面这行会报错，取消注释看看：
# print(name, 2name, my-name, _name, name!, Name, NAME, name_1, for, _123)

# 验证变量区分大小写
# assert name != Name, "name 和 Name 应是不同的变量"
# assert Name != NAME, "Name 和 NAME 应是不同的变量"
# print("练习 1.6 通过！")


# ---------------------------------------------------------------------------
# 练习 1.7 —— 多重赋值与交换
# 1) 用一行代码将 x=1, y=2, z=3 同时赋值
# 2) 不使用中间变量，交换 x 和 y 的值
# 3) 从列表 [10, 20, 30] 中拆包到 a, b, c 三个变量
# ---------------------------------------------------------------------------

x, y, z = ...

# 交换 x 和 y
x, y = ...

# 列表拆包
lst = [10, 20, 30]
a, b, c = ...

# print(f"x={x}, y={y}, z={z}")
# print(f"交换后: x={x}, y={y}")
# print(f"拆包: a={a}, b={b}, c={c}")

# assert x == 1 and y == 2 and z == 3
# assert x == 2 and y == 1  # 交换后
# assert (a, b, c) == (10, 20, 30)
# print("练习 1.7 通过！")


# ---------------------------------------------------------------------------
# 练习 1.8 —— 动态类型
# Python 是动态类型语言，同一个变量可以指向不同类型的数据。
# 1) 创建变量 var，依次赋值为 int、str、list、bool，每次赋值后打印类型
# 2) 用 type() 检查每次赋值后的类型
# ---------------------------------------------------------------------------

var = 100
# print(f"var = {var}, type = {type(var)}")

var = "现在是字符串"
# print(f"var = {var!r}, type = {type(var)}")

var = [1, 2, 3]
# print(f"var = {var}, type = {type(var)}")

var = False
# print(f"var = {var}, type = {type(var)}")

# print("练习 1.8 通过！")


# ---------------------------------------------------------------------------
# 练习 1.9 —— 数字运算
# 计算以下表达式，将结果赋值并打印：
#   1) 7 除以 3 的商（//）和余数（%）
#   2) 2 的 10 次方（**）
#   3) abs(-5) + pow(3, 3)
#   4) divmod(17, 5)  —— 返回什么？
#   5) round(3.14159, 3)  —— 保留几位？
# ---------------------------------------------------------------------------

quotient = ...
remainder = ...
power = ...
abs_pow_sum = ...
divmod_result = ...
rounded = ...

# print(f"7 // 3 = {quotient}, 7 % 3 = {remainder}")
# print(f"2 ** 10 = {power}")
# print(f"abs(-5) + pow(3, 3) = {abs_pow_sum}")
# print(f"divmod(17, 5) = {divmod_result}")
# print(f"round(3.14159, 3) = {rounded}")

# assert quotient == 2
# assert remainder == 1
# assert power == 1024
# assert abs_pow_sum == 32
# assert divmod_result == (3, 2)
# assert rounded == 3.142
# print("练习 1.9 通过！")


# ---------------------------------------------------------------------------
# 练习 1.10 —— type() 与 isinstance()
# 用 type() 和 isinstance() 检查以下变量的具体类型：
#   1) v1 = 123        → 是否为 int？
#   2) v2 = 3 + 4j     → 是什么类型？（复数 complex）
#   3) v3 = True       → bool 是否是 int 的子类？（用 issubclass 查看）
#   4) isinstance(True, int) 返回什么？
# ---------------------------------------------------------------------------

v1 = 123
v2 = 3 + 4j
v3 = True

# print(f"type(v1) = {type(v1)}")
# print(f"type(v2) = {type(v2)}")
# print(f"type(v3) = {type(v3)}")
# print(f"isinstance(v1, int) = {isinstance(v1, int)}")
# print(f"isinstance(v3, int) = {isinstance(v3, int)}")
# print(f"issubclass(bool, int) = {issubclass(bool, int)}")  # 思考输出

# assert type(v1) is int
# assert type(v2) is complex
# assert isinstance(v1, int) is True
# assert isinstance(v3, int) is True  # 为什么？
# print("练习 1.10 通过！")


# ---------------------------------------------------------------------------
# 练习 1.11 —— 不可变类型初探
# 尝试修改一个整数变量的值，用 id() 观察内存地址的变化。
# 同理，尝试修改字符串，观察 id() 的变化。
# 这说明了整数和字符串的不可变性（immutable）。
# ---------------------------------------------------------------------------

x = 100
# print(f"初始: x = {x}, id = {id(x)}")

x = x + 1
# print(f"加 1: x = {x}, id = {id(x)}")

# assert id(100) != id(101)

s = "hello"
# print(f"初始: s = {s!r}, id = {id(s)}")

s = s + " world"
# print(f"拼接后: s = {s!r}, id = {id(s)}")

# print("练习 1.11 通过！")


# ---------------------------------------------------------------------------
# 练习 1.12 —— 字面量中的下划线分隔符
# Python 3.6+ 允许在数字中使用下划线提高可读性。
# 将以下数值用下划线格式书写并验证：
#   1) 一百万：1000000
#   2) 0xFFFF 的十进制值
#   3) 科学计数法：1.23 × 10^5
# ---------------------------------------------------------------------------

million = 1_000_000
hex_val = 0xFF_FF
sci = 1.23e5

# print(f"一百万: {million}")
# print(f"0xFFFF = {hex_val}")
# print(f"1.23 × 10^5 = {sci}")

# assert million == 1000000
# assert hex_val == 65535
# assert sci == 123000.0
# print("练习 1.12 通过！")


# ---------------------------------------------------------------------------
# 练习 1.13 —— 海象运算符（:=）Python 3.8+
# 海象运算符允许在表达式中同时赋值和判断，常用于 while 和 if 语句。
#   1) 用海象运算符写一个表达式：将 len(s) 赋值给 n，同时判断 n > 0
#   2) 从键盘读取输入直到空行的场景（模拟，用列表代替）
#   3) 列表推导式中使用海象运算符
# 提示：先理解海象运算符的特性——它赋值并返回被赋的值。
# ---------------------------------------------------------------------------

# 用法1：赋值并在 if 中判断
s = "hello"
# if (n := len(s)) > 0:
#     print(f"字符串长度 n = {n}，大于 0")

# 用法2：在列表推导式中避免重复计算
# numbers = [1, 2, 3, 4, 5, 6]
# 只取偶数的平方
# result = [y for x in numbers if (y := x**2) % 2 == 0]
# print(f"偶数的平方: {result}")

# 用法3：读取数据直到结束（模拟）
# data = ["apple", "banana", "", "cherry"]
# i = 0
# while (fruit := data[i]) if i < len(data) else "":
#     print(f"处理: {fruit}")
#     i += 1

# print("练习 1.13 通过！")


# ---------------------------------------------------------------------------
# 练习 1.14 —— 联合类型（Union Types）Python 3.10+
# Python 3.10 引入了 int | str 语法，替代 typing.Union[int, str]。
#   1) 创建变量 x: int | str = 42，再赋值为 "hello"
#   2) 用 isinstance() 检查一个值是否是 int 或 str
#   3) 在函数签名中使用联合类型做类型注解
# ---------------------------------------------------------------------------

x: int | str = 42
# print(f"x = {x}, type = {type(x)}")
x = "hello"
# print(f"x = {x!r}, type = {type(x)}")

# 用 isinstance 检查联合类型
value = 3.14
is_int_or_float = ...  # isinstance(value, int | float)

# print(f"value = {value}, is_int_or_float? {is_int_or_float}")
# assert is_int_or_float is True

# 在函数签名中使用（补全参数注解）
def double(value: int | str) -> int | str:
    """如果 value 是 int 则返回 value*2，如果是 str 则返回 value 重复两次。"""
    ...

# print(double(21))     # → 42
# print(double("Hi"))   # → "HiHi"
# assert double(21) == 42
# assert double("Hi") == "HiHi"
# print("练习 1.14 通过！")


# ---------------------------------------------------------------------------
# 练习 1.15 —— type 语句定义类型别名（Python 3.12+）
# Python 3.12 引入 type 关键字来定义类型别名。
#   1) 定义类型别名 Vector = list[float]
#   2) 定义可选类型 Optional[T] = T | None
#   3) 在函数注解中使用类型别名
# 注意：Python 3.12 以下版本可以用 TypeAlias（typing 模块）。
# ---------------------------------------------------------------------------

# 定义类型别名
type Vector = list[float]
type NullableInt = int | None

# 使用类型别名做类型注解
def scale(v: Vector, factor: float) -> Vector:
    """将向量每个分量乘以 factor。"""
    return [x * factor for x in v]

def maybe_add_one(x: NullableInt) -> NullableInt:
    """如果 x 不为 None，返回 x+1，否则返回 None。"""
    ...

# v = scale([1.0, 2.0, 3.0], 2.0)
# print(f"向量缩放: {v}")
# assert v == [2.0, 4.0, 6.0]
# print("练习 1.15 通过！")


# ---------------------------------------------------------------------------
# 练习 1.16 —— 链式比较（Chained Comparison）
# Python 允许连续比较 a < b < c，等价于 a < b and b < c。
# 判断以下表达式的值并验证：
#   1) 1 < 2 < 3
#   2) 1 < 2 > 3
#   3) 1 == 1 == 1
#   4) 1 == 1 == 2
#   5) 1 < 2 <= 2 < 3
#   6) "a" < "b" < "c"
#   7) 3 > 2 > 1
# ---------------------------------------------------------------------------

chain1 = ...
chain2 = ...
chain3 = ...
chain4 = ...
chain5 = ...
chain6 = ...
chain7 = ...

# print(f"1 < 2 < 3: {chain1}")
# print(f"1 < 2 > 3: {chain2}")
# print(f"1 == 1 == 1: {chain3}")
# print(f"1 == 1 == 2: {chain4}")
# print(f"1 < 2 <= 2 < 3: {chain5}")
# print(f"'a' < 'b' < 'c': {chain6}")
# print(f"3 > 2 > 1: {chain7}")

# assert chain1 is True
# assert chain2 is False
# assert chain3 is True
# assert chain4 is False
# assert chain5 is True
# assert chain6 is True
# assert chain7 is True
# print("练习 1.16 通过！")


# ---------------------------------------------------------------------------
# 练习 1.17 —— 短路求值（Short-Circuit Evaluation）
# and 和 or 运算符具有短路特性：一旦能确定结果就停止计算。
# 完成以下任务：
#   1) 写出 True or (1/0) 的结果（不会报错！）
#   2) 写出 False and (1/0) 的结果（也不会报错！）
#   3) 用 or 提供默认值：None or "default"
#   4) 用 and 安全地访问属性：[] and [0]
#   5) 理解短路优先级：True or False and False
# ---------------------------------------------------------------------------

short_or = ...
short_and = ...
default_val = ...
safe_access = ...
precedence = ...

# print(f"True or (1/0): {short_or}")        # 不会计算 (1/0)
# print(f"False and (1/0): {short_and}")      # 不会计算 (1/0)
# print(f"None or 'default': {default_val!r}")
# print(f"[] and [0]: {safe_access!r}")
# print(f"True or False and False: {precedence}")

# assert short_or is True
# assert short_and is False
# assert default_val == "default"
# assert safe_access == []
# assert precedence is True  # 等价于 True or (False and False)
# print("练习 1.17 通过！")


# ---------------------------------------------------------------------------
# 练习 1.18 —— match/case 模式匹配初探（Python 3.10+）
# 用 match/case 实现一个简单的类型判断和值匹配函数。
#   1) 匹配字面量值：1, 2, 3
#   2) 匹配类型：用 guard（if 子句）或使用类型模式
#   3) 捕获变量：用 default 分支捕获未知值
# 实现函数 what_is(x)，根据 x 的值返回描述字符串。
# ---------------------------------------------------------------------------


def what_is(x) -> str:
    """用 match/case 判断 x 是什么。"""
    match x:
        case 0:
            return "零"
        case 1 | 2 | 3:
            ...
        case int():
            ...
        case str():
            ...
        case _:
            ...


# print(what_is(0))       # → "零"
# print(what_is(2))       # → "小数字"
# print(what_is(100))     # → "其他整数"
# print(what_is("hello")) # → "字符串"
# print(what_is([1,2]))   # → "未知类型"

# assert what_is(0) == "零"
# assert what_is(2) == "小数字"
# assert what_is(100) == "其他整数"
# assert what_is("hello") == "字符串"
# assert what_is([1, 2]) == "未知类型"
# print("练习 1.18 通过！")


# ---------------------------------------------------------------------------
# 练习 1.19 —— 复数类型（complex）
# Python 原生支持复数（complex），用 j 表示虚数单位。
#   1) 定义复数 c1 = 3 + 4j，c2 = 1 - 2j
#   2) 计算 c1 + c2, c1 * c2, c1 / c2, c1**2
#   3) 分别提取实部 .real 和虚部 .imag
#   4) 计算模长 abs(c1)
#   5) 获取共轭复数 .conjugate()
# ---------------------------------------------------------------------------

c1 = 3 + 4j
c2 = 1 - 2j

sum_c = ...
prod_c = ...
quot_c = ...
sq_c1 = ...

real_c1 = ...
imag_c1 = ...
mag_c1 = ...
conj_c1 = ...

# print(f"c1 = {c1}, c2 = {c2}")
# print(f"c1 + c2 = {sum_c}")
# print(f"c1 * c2 = {prod_c}")
# print(f"c1 / c2 = {quot_c}")
# print(f"c1**2 = {sq_c1}")
# print(f"c1.real = {real_c1}, c1.imag = {imag_c1}")
# print(f"|c1| = {mag_c1}")
# print(f"c1 的共轭 = {conj_c1}")

# assert real_c1 == 3
# assert imag_c1 == 4
# assert mag_c1 == 5.0  # 3-4-5 直角三角形
# print("练习 1.19 通过！")


# ---------------------------------------------------------------------------
# 练习 1.20 —— 枚举类型（Enum）
# 枚举是 Python 3.4+ 引入的类型，用来定义一组命名常量。
#   1) 定义 Color 枚举，包含 RED, GREEN, BLUE
#   2) 定义 HTTPStatus 枚举，包含 OK=200, NOT_FOUND=404, ERROR=500
#   3) 用 .name 和 .value 访问枚举成员
#   4) 通过值查找枚举成员
#   5) 遍历枚举所有成员
# ---------------------------------------------------------------------------

from enum import Enum


class Color(Enum):
    RED = 1
    ...


class HTTPStatus(Enum):
    OK = 200
    NOT_FOUND = 404
    ERROR = 500


# 访问枚举成员
fav_color = Color.RED
# print(f"fav_color = {fav_color}")
# print(f"fav_color.name = {fav_color.name}")
# print(f"fav_color.value = {fav_color.value}")

# 通过值查找
status = ...  # 用 HTTPStatus(200) 查找

# print(f"status = {status}, name = {status.name}")

# 遍历所有成员
# for color in Color:
#     print(f"{color.name} = {color.value}")

# assert Color.RED.value == 1
# assert Color.GREEN.name == "GREEN"
# assert HTTPStatus(404) == HTTPStatus.NOT_FOUND
# print("练习 1.20 通过！")


# ---------------------------------------------------------------------------
# 练习 1.21 —— 变量类型注解
# Python 3.6+ 支持为变量添加类型注解，提高代码可读性。
#   1) 为变量 name, age, height, is_student 添加类型注解
#   2) 用列表类型注解：scores: list[int]
#   3) 用字典类型注解：grades: dict[str, int]
#   4) 用 Optional 或 | None 标注可选值
#   5) 注意：注解不会强制类型，但 mypy/IDE 会检查
# ---------------------------------------------------------------------------

name: str = "Alice"
age: int = 25
height: float = 1.68
is_student: bool = True
scores: list[int] = [85, 92, 78]
grades: dict[str, int] = {"math": 90, "english": 85}
maybe_value: int | None = None

# 即使注解为 int，赋 str 也不会报错（但工具会警告）
age = "twenty-five"  # 类型检查器会警告，但 Python 不会报错

# TODO: 定义一个函数 add_student，参数和返回值都加上类型注解
def add_student(name: str, age: int, scores: list[int]) -> dict[str, int | str | list[int]]:
    """添加学生信息，返回包含学生数据的字典。"""
    ...

# student = add_student("Bob", 20, [88, 76])
# print(f"学生信息: {student}")
# assert student["name"] == "Bob"
# print("练习 1.21 通过！")


# ---------------------------------------------------------------------------
# 练习 1.22 —— None 的默认值模式
# 处理 None 的几种常用模式：
#   1) or 模式：value or "default"
#   2) 三元表达式：value if value is not None else "default"
#   3) 海象运算符配合 None 检查
# 完成函数 get_user_name，如果 name 为 None 则返回 "Anonymous"。
# ---------------------------------------------------------------------------


def get_user_name(name: str | None) -> str:
    """如果 name 为 None，返回 'Anonymous'，否则返回 name 本身。"""
    # 方式1：or 模式
    # return name or "Anonymous"
    # 方式2：三元表达式
    ...


# print(get_user_name("Alice"))   # → "Alice"
# print(get_user_name(""))        # 思考：空字符串会返回什么？
# print(get_user_name(None))      # → "Anonymous"

# assert get_user_name("Alice") == "Alice"
# assert get_user_name(None) == "Anonymous"

# 思考题：为什么 get_user_name("") 用 or 模式和三元表达式结果不同？
# print("练习 1.22 通过！")


# ---------------------------------------------------------------------------
# 练习 1.23 —— math 模块与特殊浮点值
# Python 的 math 模块提供了无穷大（inf）、非数字（nan）等特殊值。
#   1) 用 float('inf') 创建无穷大
#   2) 用 float('nan') 创建 NaN
#   3) 用 math.isinf() 和 math.isnan() 判断
#   4) 用 math.pi 和 math.tau（== 2π）
#   5) 观察 inf 的运算规则：inf + 1, inf * 0, inf / inf
#   6) 观察 nan 的比较（nan == nan 是 True 还是 False？）
# ---------------------------------------------------------------------------

import math

inf_val = float('inf')
nan_val = float('nan')

# print(f"无穷大: {inf_val}")
# print(f"非数字: {nan_val}")
# print(f"math.pi = {math.pi}")
# print(f"math.tau = {math.tau}")
# print(f"2*pi == tau: {2 * math.pi == math.tau}")
# print(f"inf + 1 = {inf_val + 1}")
# print(f"inf * 0 = {inf_val * 0}")
# print(f"inf / inf = {inf_val / inf_val}")
# print(f"math.isinf(inf_val): {math.isinf(inf_val)}")
# print(f"math.isnan(nan_val): {math.isnan(nan_val)}")

# 最反直觉的地方：NaN 不等于自身
# print(f"nan == nan: {nan_val == nan_val}")
# assert nan_val != nan_val

# 正确判断 NaN 的方法
# assert math.isnan(nan_val)
# print("练习 1.23 通过！")


# ---------------------------------------------------------------------------
# 练习 1.24 —— Decimal 类型：精确十进制运算
# float 存在精度问题（0.1 + 0.2 != 0.3），
# Decimal 提供精确的十进制运算，适合金融计算。
#   1) 从 decimal 模块导入 Decimal
#   2) 用 Decimal("0.1") + Decimal("0.2") 精确计算
#   3) 用 float 和 Decimal 分别计算 1.1 + 2.2，对比结果
#   4) 设置精度上下文（getcontext().prec）
# ---------------------------------------------------------------------------

from decimal import Decimal, getcontext

# float 的不精确
float_sum = 0.1 + 0.2
# print(f"float: 0.1 + 0.2 = {float_sum}")

# Decimal 精确
decimal_sum = Decimal("0.1") + Decimal("0.2")
# print(f"Decimal: 0.1 + 0.2 = {decimal_sum}")

# 设置精度
getcontext().prec = 6
precise_result = Decimal("1") / Decimal("3")
# print(f"1/3 保留精度: {precise_result}")

# float_vs_decimal = 1.1 + 2.2
# print(f"float: 1.1 + 2.2 = {float_vs_decimal}")
# decimal_vs = Decimal("1.1") + Decimal("2.2")
# print(f"Decimal: 1.1 + 2.2 = {decimal_vs}")

# assert str(decimal_sum) == "0.3"
# print("练习 1.24 通过！")


# ---------------------------------------------------------------------------
# 练习 1.25 —— Fraction 类型：精确分数运算
# fractions.Fraction 以分子/分母形式存储有理数。
#   1) 创建 Fraction(1, 3) 和 Fraction(2, 3)
#   2) 分数加减乘除
#   3) 从字符串创建：Fraction("1/3")
#   4) 自动约分：Fraction(2, 4) → 自动变为 1/2
#   5) 浮点数转分数：Fraction(0.25) → 1/4
# ---------------------------------------------------------------------------

from fractions import Fraction

f1 = Fraction(1, 3)
f2 = Fraction(2, 3)

sum_f = ...
prod_f = ...
reciprocal = ...

auto_reduced = Fraction(2, 4)
from_float = Fraction(0.25)
from_string = Fraction("3/5")

# print(f"1/3 + 2/3 = {sum_f}")
# print(f"1/3 * 2/3 = {prod_f}")
# print(f"1/3 的倒数 = {reciprocal}")
# print(f"Fraction(2, 4) = {auto_reduced}")   # → 1/2
# print(f"Fraction(0.25) = {from_float}")     # → 1/4
# print(f"Fraction('3/5') = {from_string}")

# assert sum_f == 1
# assert prod_f == Fraction(2, 9)
# assert reciprocal == 3
# assert auto_reduced == Fraction(1, 2)
# print("练习 1.25 通过！")


# ---------------------------------------------------------------------------
# 练习 1.26 —— 字典合并运算符 |（Python 3.9+）
# 用 | 和 |= 合并两个字典。
#   1) 定义 d1 = {"a": 1, "b": 2}, d2 = {"b": 3, "c": 4}
#   2) 用 d1 | d2 合并，观察 b 的值（后面覆盖前面）
#   3) 用 {**d1, **d2} 展开合并（传统方式）
#   4) 用 d1 |= d2 原地更新
#   5) 对比与 d1.update(d2) 的异同
# ---------------------------------------------------------------------------

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

merged = ...
unpacked = ...

# print(f"d1 | d2: {merged}")
# print(f"{{**d1, **d2}}: {unpacked}")

# 原地更新
d1_copy = d1.copy()
d1_copy |= d2
# print(f"d1 |= d2: {d1_copy}")

# assert merged == {"a": 1, "b": 3, "c": 4}
# assert unpacked == {"a": 1, "b": 3, "c": 4}
# print("练习 1.26 通过！")


# ---------------------------------------------------------------------------
# 练习 1.27 —— 整数位运算与 bit_count（Python 3.8+/3.11+）
# Python 整数支持位运算，Python 3.8 新增 int.bit_length()，
# Python 3.11 新增 int.bit_count()（二进制中 1 的个数）。
#   1) 计算 42 的二进制表示 → bin(42)
#   2) 计算 bit_length（二进制位数，不含符号位）
#   3) 计算 bit_count（二进制中 1 的个数，即 population count）
#   4) 用 &、|、^、<<、>> 做位运算
#   5) 判断一个数是否是 2 的幂（用 bit_count == 1）
# ---------------------------------------------------------------------------

n = 42

binary = ...
bit_len = ...
bit_cnt = ...

# print(f"42 的二进制: {binary}")
# print(f"bit_length: {bit_len}")
# print(f"bit_count (1 的个数): {bit_cnt}")

# 位运算
bit_and = ...
bit_or = ...
bit_xor = ...
bit_shift = ...

# print(f"42 & 15 = {bit_and}")
# print(f"42 | 15 = {bit_or}")
# print(f"42 ^ 15 = {bit_xor}")
# print(f"42 << 2 = {bit_shift}")

# 判断 2 的幂
def is_power_of_two(x: int) -> bool:
    return ...  # 用 bit_count 判断

# print(f"4 是 2 的幂: {is_power_of_two(4)}")
# print(f"5 是 2 的幂: {is_power_of_two(5)}")
# print(f"1 是 2 的幂: {is_power_of_two(1)}")

# assert bin(42) == "0b101010"
# assert bit_len == 6
# assert bit_cnt == 3
# assert is_power_of_two(4) is True
# assert is_power_of_two(5) is False
# print("练习 1.27 通过！")


# ---------------------------------------------------------------------------
# 练习 1.28 —— 字面量中的类型推断与 annotated 赋值
# Python 3.6+ 中变量注解不会影响运行时行为，但 Python 3.12+
# 的 typing.type_check_only 和相关工具会利用这些信息。
# 本练习关注各种字面量写法及其类型。
#   1) 二进制字面量：0b1101
#   2) 八进制字面量：0o77
#   3) 十六进制字面量：0xFF
#   4) 科学计数法：1.5e-2（= 0.015）
#   5) 复数字面量：2j
#   6) 布尔字面量：True, False
#   7) None 字面量
#   8) 字节字面量：b"hello"
# ---------------------------------------------------------------------------

bin_val = ...
oct_val = ...
hex_val = ...
sci_val = ...
complex_val = ...
bool_val = ...
none_val = ...
bytes_val = ...

# print(f"0b1101 = {bin_val}")
# print(f"0o77 = {oct_val}")
# print(f"0xFF = {hex_val}")
# print(f"1.5e-2 = {sci_val}")
# print(f"2j 的类型: {type(complex_val)}")
# print(f"{bool_val} 是 {type(bool_val)}")
# print(f"None 的类型: {type(none_val)}")
# print(f"字节字面量: {bytes_val}")

# assert bin_val == 13
# assert oct_val == 63
# assert hex_val == 255
# assert sci_val == 0.015
# assert type(complex_val) is complex
# assert type(bool_val) is bool
# assert none_val is None
# assert type(bytes_val) is bytes
# print("练习 1.28 通过！")


# ============================================================================
# 第一部分 补充环节：综合挑战题
# ============================================================================


# ---------------------------------------------------------------------------
# 挑战 1.29 —— 猜数字类型
# 编写一个函数 guess_type(value: str) -> int | float | complex | str，
# 尝试将输入的字符串自动识别为合适的数字类型：
#   - 如果包含 "j"，尝试转 complex
#   - 如果包含 "."，尝试转 float
#   - 否则尝试转 int
#   - 如果都不行，返回原字符串
# 不要使用异常捕获（try/except），用 str 方法判断。
# ---------------------------------------------------------------------------


def guess_type(value: str) -> int | float | complex | str:
    """自动识别字符串中的数字类型。"""
    # TODO: 判断是否包含 'j'
    if ...:
        return complex(value.replace("j", "j"))  # 确保格式
    # TODO: 判断是否包含 '.'
    if ...:
        return float(value)
    # TODO: 判断是否是纯数字
    if ...:
        return int(value)
    return value


# test_values = ["42", "3.14", "1+2j", "hello", "0xFF"]
# for v in test_values:
#     result = guess_type(v)
#     print(f"'{v}' → {result} ({type(result).__name__})")

# assert guess_type("42") == 42
# assert guess_type("3.14") == 3.14
# assert guess_type("hello") == "hello"
# # assert guess_type("1+2j") == 1+2j  # 注意 complex 字符串格式
# print("挑战 1.29 通过！")


# ---------------------------------------------------------------------------
# 挑战 1.30 —— 增强版计算器（match/case + 类型安全）
# 用 match/case 实现一个简单的四则运算计算器。
# 支持 int | float 两种操作数，返回 float。
# 用运算符字符串 "+", "-", "*", "/" 匹配。
# 处理除零错误（返回字符串 "除数不能为零"）。
# ---------------------------------------------------------------------------


def calculate(a: int | float, op: str, b: int | float) -> int | float | str:
    """执行四则运算。"""
    match op:
        case "+":
            ...
        case "-":
            ...
        case "*":
            ...
        case "/":
            ...
        case _:
            ...


# print(calculate(10, "+", 3))   # → 13
# print(calculate(10, "/", 3))   # → 3.333...
# print(calculate(10, "/", 0))   # → "除数不能为零"

# assert calculate(10, "+", 3) == 13
# assert calculate(10, "-", 3) == 7
# assert calculate(10, "*", 3) == 30
# assert calculate(10, "/", 3) == 10 / 3
# assert calculate(10, "/", 0) == "除数不能为零"
# print("挑战 1.30 通过！")


# ============================================================================
# 第二部分：字符串与编码
# ============================================================================

# ---------------------------------------------------------------------------
# 练习 2.1 —— 创建字符串
# 用三种方式创建字符串 "Hello, Python!"：
#   1) 单引号
#   2) 双引号
#   3) 三引号（多行字符串），内容为多行：
#         Hello,
#         Python!
# ---------------------------------------------------------------------------

s1 = ...
s2 = ...
s3 = ...

# print(s1)
# print(s2)
# print(s3)

# assert s1 == "Hello, Python!"
# assert s2 == "Hello, Python!"
# print("练习 2.1 通过！")


# ---------------------------------------------------------------------------
# 练习 2.2 —— 转义字符
# 使用转义字符打印以下内容：
#   1) 包含单引号的字符串：It's a book.
#   2) 包含双引号的字符串：He said, "Hello!".
#   3) 包含换行和制表符的格式：
#         Name:    Alice
#         Age:     25
#   4) 打印原始反斜杠：C:\Users\Name
# ---------------------------------------------------------------------------

s_with_single = ...
s_with_double = ...
formatted = ...
path = ...

# print(s_with_single)
# print(s_with_double)
# print(formatted)
# print(path)

# assert s_with_single == "It's a book."
# assert s_with_double == 'He said, "Hello!".'
# print("练习 2.2 通过！")


# ---------------------------------------------------------------------------
# 练习 2.3 —— 原始字符串（raw string）
# 使用 r"" 避免转义，打印 Windows 路径：
#   路径：C:\Users\new_folder\test.py
# 分别用普通字符串和原始字符串表示，观察区别。
# ---------------------------------------------------------------------------

# 普通字符串（需要双反斜杠）
normal_path = "C:\\Users\\new_folder\\test.py"

# 原始字符串（用 r 前缀）
raw_path = ...

# print(f"普通字符串: {normal_path}")
# print(f"原始字符串: {raw_path}")

# assert normal_path == raw_path
# print("练习 2.3 通过！")


# ---------------------------------------------------------------------------
# 练习 2.4 —— 字符串拼接
# 有以下三个片段，请用三种不同方式拼接为完整句子：
#   "Hello", "Python", "World"
# 方法：
#   1) + 运算符
#   2) join() 方法
#   3) f-string
# 要求输出 "Hello Python World"（中间有空格）。
# ---------------------------------------------------------------------------

a, b, c = "Hello", "Python", "World"

concat_plus = ...
concat_join = ...
concat_fstring = ...

# print(concat_plus)
# print(concat_join)
# print(concat_fstring)

# assert concat_plus == "Hello Python World"
# assert concat_join == "Hello Python World"
# assert concat_fstring == "Hello Python World"
# print("练习 2.4 通过！")


# ---------------------------------------------------------------------------
# 练习 2.5 —— 字符串重复
# 用 * 运算符生成以下图案并打印：
#   1) "Ha" 重复 10 次 → "HaHaHaHaHaHaHaHaHaHa"
#   2) 打印一个 5x5 的由 "*" 组成的正方形
#   3) 利用重复和拼接打印一个简单的"阶梯"（3 行）：
#          *
#          **
#          ***
# ---------------------------------------------------------------------------

laugh = "Ha" * 10

# 正方形
square = ...
# print(f"5x5 正方形:\n{square}")

# 阶梯
step1 = "*"
step2 = "**"
step3 = "***"
# 将阶梯用换行符拼接并打印
stairs = ...
# print(f"阶梯:\n{stairs}")

# print(f"大笑: {laugh}")
# assert laugh == "HaHaHaHaHaHaHaHaHaHa"
# print("练习 2.5 通过！")


# ---------------------------------------------------------------------------
# 练习 2.6 —— 字符串索引
# 对于字符串 s = "abcdefghij"，完成以下索引操作：
#   1) 获取第 1 个字符（索引 0）
#   2) 获取最后 1 个字符（索引 -1 或 len(s)-1）
#   3) 获取倒数第 3 个字符
#   4) 尝试用一个超出范围的索引，观察错误信息
# ---------------------------------------------------------------------------

s = "abcdefghij"

first_char = ...
last_char = ...
third_last_char = ...

# print(f"第一个字符: {first_char!r}")
# print(f"最后一个字符: {last_char!r}")
# print(f"倒数第三个字符: {third_last_char!r}")

# assert first_char == "a"
# assert last_char == "j"
# assert third_last_char == "h"
# print("练习 2.6 通过！")

# 试试下面这行会怎样：
# s[100]


# ---------------------------------------------------------------------------
# 练习 2.7 —— 字符串切片
# 对于 s = "PythonProgramming"，完成以下切片操作：
#   1) 取前 6 个字符 → "Python"
#   2) 取第 7 个到第 12 个字符（不含第 12 个）→ "Progra"
#         注意：索引从 0 开始，s[6:11] 取第 7 到第 11 个字符
#   3) 每 2 个字符取一个 → 步长切片
#   4) 反转字符串
#   5) 去掉首尾各 2 个字符
# ---------------------------------------------------------------------------

s = "PythonProgramming"

part1 = ...     # "Python"
part2 = ...     # "Progr"
part3 = ...     # 步长为 2
reversed_s = ...  # 反转
middle = ...    # 去掉首尾各 2 个

# print(f"前 6 个: {part1}")
# print(f"第 7-11 个: {part2}")
# print(f"步长为 2: {part3}")
# print(f"反转: {reversed_s}")
# print(f"去掉首尾各 2 个: {middle}")

# assert part1 == "Python"
# assert part2 == "Progr"
# assert reversed_s == "gnimmargorPnohtyP"
# assert middle == "thonProgrammi"
# print("练习 2.7 通过！")


# ---------------------------------------------------------------------------
# 练习 2.8 —— len() 函数
# 计算以下字符串的长度并验证：
#   1) "Hello"              → 5
#   2) "你好"               → 2（中文每个字算一个字符）
#   3) "Hello\nWorld"       → 11（\n 是一个字符）
#   4) 空字符串 ""          → 0
#   5) 带空格的字符串 " a "  → 3
# ---------------------------------------------------------------------------

len1 = ...
len2 = ...
len3 = ...
len4 = ...
len5 = ...

# print(f"len('Hello') = {len1}")
# print(f"len('你好') = {len2}")
# print(f"len('Hello\\nWorld') = {len3}")
# print(f"len('') = {len4}")
# print(f"len(' a ') = {len5}")

# assert len1 == 5
# assert len2 == 2
# assert len3 == 11
# assert len4 == 0
# assert len5 == 3
# print("练习 2.8 通过！")


# ---------------------------------------------------------------------------
# 练习 2.9 —— 字符串方法（上）
# 对于 s = "  Hello, Python World!  "，依次完成：
#   1) strip()  —— 去掉首尾空格
#   2) lower()  —— 全部小写
#   3) upper()  —— 全部大写
#   4) title()  —— 每个单词首字母大写
#   5) swapcase() —— 大小写互换
#   6) capitalize() —— 首字母大写，其余小写
# 每一步打印结果，观察各方法的作用。
# ---------------------------------------------------------------------------

s = "  Hello, Python World!  "

stripped = ...
lowered = ...
uppered = ...
titled = ...
swapped = ...
capitalized = ...

# print(f"原始:      {s!r}")
# print(f"strip:     {stripped!r}")
# print(f"lower:     {lowered!r}")
# print(f"upper:     {uppered!r}")
# print(f"title:     {titled!r}")
# print(f"swapcase:  {swapped!r}")
# print(f"capitalize: {capitalized!r}")

# assert stripped == "Hello, Python World!"
# assert lowered == "  hello, python world!  "  # 注意：strip 不会改变原始空格
# 注：lower/upper/title 等不会自动 strip，这里期望包含首尾空格
# 更准确的是对 stripped 后的结果进行操作：
# assert stripped.lower() == "hello, python world!"
# print("练习 2.9 通过！")


# ---------------------------------------------------------------------------
# 练习 2.10 —— 字符串方法（中）
# 对于 s = "apple,banana,orange,grape,kivi"，完成：
#   1) split(",")  —— 按逗号切分 → 列表
#   2) replace("banana", "blueberry") —— 替换
#   3) find("orange")  —— 查找子串（返回索引）
#   4) find("watermelon") —— 查找不存在的子串（返回 -1）
#   5) index("orange") —— 与 find 类似但失败时不同
#   6) count("a") —— 统计 "a" 出现的次数
#   7) startswith("apple")  —— 是否以指定字符串开头
#   8) endswith("kivi")     —— 是否以指定字符串结尾
# ---------------------------------------------------------------------------

s = "apple,banana,orange,grape,kivi"

parts = ...
replaced = ...
pos_orange = ...
pos_missing = ...
idx_orange = ...
count_a = ...
starts_with_apple = ...
ends_with_kivi = ...

# print(f"切分: {parts}")
# print(f"替换: {replaced}")
# print(f"find('orange') = {pos_orange}")
# print(f"find('watermelon') = {pos_missing}")
# print(f"count('a') = {count_a}")
# print(f"startswith('apple')? {starts_with_apple}")
# print(f"endswith('kivi')? {ends_with_kivi}")

# assert parts == ["apple", "banana", "orange", "grape", "kivi"]
# assert "blueberry" in replaced
# assert pos_orange == 13
# assert pos_missing == -1
# assert count_a == 4
# assert starts_with_apple is True
# assert ends_with_kivi is True
# print("练习 2.10 通过！")


# ---------------------------------------------------------------------------
# 练习 2.11 —— 字符串方法（下）
# 对于 s = "123abcABC"，完成：
#   1) isdigit()  —— 是否全是数字
#   2) isalpha()  —— 是否全是字母
#   3) isalnum()  —— 是否全是字母和数字
#   4) isspace()  —— 是否全是空白字符
#   5) 用 "42" 测试 isdecimal() 和 isnumeric()
#   6) 用 "Ⅳ"（罗马数字 4）测试 isdecimal() 和 isnumeric() 的区别
# ---------------------------------------------------------------------------

s = "123abcABC"

check_digit = ...
check_alpha = ...
check_alnum = ...
check_space = ...

# print(f"'{s}' isdigit? {check_digit}")
# print(f"'{s}' isalpha? {check_alpha}")
# print(f"'{s}' isalnum? {check_alnum}")
# print(f"'{s}' isspace? {check_space}")

# assert check_alnum is True

# --- isdecimal vs isnumeric 的区别 ---
s2 = "42"
roman = "Ⅳ"  # 罗马数字 4（Unicode U+2163）

# print(f"'{s2}' isdecimal={s2.isdecimal()}, isnumeric={s2.isnumeric()}")
# print(f"'{roman}' isdecimal={roman.isdecimal()}, isnumeric={roman.isnumeric()}")

# 思考：为什么罗马数字 isdecimal() 返回 False 而 isnumeric() 返回 True？
# print("练习 2.11 通过！")


# ---------------------------------------------------------------------------
# 练习 2.12 —— f-string 格式化
# 给定 name="Alice", age=30, height=1.68, score=92.5，用 f-string 输出：
#   1) "My name is Alice, I am 30 years old."
#   2) "Height: 1.68m"（保留两位小数）
#   3) "Score: 92.50"（保留两位小数，宽度为 6，右对齐）
#   4) 用 f-string 打印一个 3x3 的乘法表
# ---------------------------------------------------------------------------

name, age, height, score = "Alice", 30, 1.68, 92.5

intro = ...
height_str = ...
score_str = ...

# print(intro)
# print(height_str)
# print(score_str)

# 打印 3x3 乘法表
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"...", end="\t")
#     print()

# assert intro == "My name is Alice, I am 30 years old."
# assert score_str == " 92.50"  # 宽度为 6，右对齐
# print("练习 2.12 通过！")


# ---------------------------------------------------------------------------
# 练习 2.13 —— format() 方法
# 用 str.format() 方法重写练习 2.12 中的 f-string 内容。
# 要求输出相同的结果。
# ---------------------------------------------------------------------------

name, age, height, score = "Alice", 30, 1.68, 92.5

intro = ...
height_str = ...
score_str = ...

# print(intro)
# print(height_str)
# print(score_str)

# assert intro == "My name is Alice, I am 30 years old."
# print("练习 2.13 通过！")


# ---------------------------------------------------------------------------
# 练习 2.14 —— 占位符格式化（% 运算符）
# 用 % 格式化（类似 C 语言 printf）重写练习 2.12 的内容。
# 要求输出相同的结果。
# ---------------------------------------------------------------------------

name, age, height, score = "Alice", 30, 1.68, 92.5

intro = ...
height_str = ...
score_str = ...

# print(intro)
# print(height_str)
# print(score_str)

# assert intro == "My name is Alice, I am 30 years old."
# print("练习 2.14 通过！")


# ---------------------------------------------------------------------------
# 练习 2.15 —— 字符串对齐
# 给定 s = "Python"，用以下方法将其格式化为宽度 10：
#   1) center(10, '-') → 居中，两侧用 - 填充
#   2) ljust(10, '*')  → 左对齐，右侧用 * 填充
#   3) rjust(10, '#')  → 右对齐，左侧用 # 填充
#   4) zfill(10)       → 右对齐，左侧补 0（常用于数字）
# 打印每种结果，观察区别。
# ---------------------------------------------------------------------------

s = "Python"

centered = ...
left_aligned = ...
right_aligned = ...
zero_filled = ...

# print(f"center:  {centered!r}")
# print(f"ljust:   {left_aligned!r}")
# print(f"rjust:   {right_aligned!r}")
# print(f"zfill:   {zero_filled!r}")

# assert centered == "--Python---"
# assert left_aligned == "Python****"
# assert right_aligned == "####Python"
# assert zero_filled == "0000Python"
# print("练习 2.15 通过！")


# ---------------------------------------------------------------------------
# 练习 2.16 —— 字符串的 in 和 not in 操作符
# 判断子串是否在字符串中：
#   1) "lo" 在 "Hello" 中 → True
#   2) "xyz" 不在 "Hello" 中 → True
#   3) "123" 在 "abc123def" 中 → True
#   4) 检查字符串是否只包含某个字符集（如只含数字和字母）
# ---------------------------------------------------------------------------

contains_lo = ...
not_contains_xyz = ...
contains_123 = ...

# 检查字符串 "Hello123" 中是否只包含字母和数字
text = "Hello123"
is_alphanumeric = ...

# print(f"'lo' in 'Hello': {contains_lo}")
# print(f"'xyz' not in 'Hello': {not_contains_xyz}")
# print(f"'123' in 'abc123def': {contains_123}")
# print(f"'{text}' 只含字母和数字? {is_alphanumeric}")

# assert contains_lo is True
# assert not_contains_xyz is True
# assert contains_123 is True
# assert is_alphanumeric is True
# print("练习 2.16 通过！")


# ---------------------------------------------------------------------------
# 练习 2.17 —— 字符串比较
# 字符串比较基于字典序（lexicographical order），即逐个比较字符的 ASCII/Unicode 码点。
# 判断以下表达式的结果并验证：
#   1) "apple" < "banana"     → True（a 的码点小于 b）
#   2) "Apple" < "apple"      → True（大写字母码点小于小写）
#   3) "10" < "5"             → True! 为什么？
#   4) sorted(["banana", "apple", "Cherry"])  → 排序结果是什么？
# ---------------------------------------------------------------------------

cmp1 = ...
cmp2 = ...
cmp3 = ...

fruits = ["banana", "apple", "Cherry"]
sorted_fruits = ...

# print(f"'apple' < 'banana': {cmp1}")
# print(f"'Apple' < 'apple': {cmp2}")
# print(f"'10' < '5': {cmp3}")
# print(f"排序后: {sorted_fruits}")

# assert cmp1 is True
# assert cmp2 is True
# assert cmp3 is True
# # 为什么 "10" < "5" 是 True？
# print("练习 2.17 通过！")


# ---------------------------------------------------------------------------
# 练习 2.18 —— ord() 和 chr()
# ord() 获取字符的 Unicode 码点，chr() 将码点转回字符。
#   1) 获取 'A', 'Z', 'a', 'z', '中', '文' 的 Unicode 码点
#   2) 将码点 65, 97, 20013, 25991 转回字符
#   3) 打印所有 ASCII 可打印字符（码点 32~126）
#   4) 验证：chr(ord('A') + 32) == 'a'（大小写字母码点差 32）
# ---------------------------------------------------------------------------

ord_A = ...
ord_Z = ...
ord_a = ...
ord_zhong = ...
ord_wen = ...

chr_65 = ...
chr_97 = ...
chr_20013 = ...
chr_25991 = ...

# print(f"ord('A') = {ord_A}, ord('Z') = {ord_Z}")
# print(f"ord('a') = {ord_a}, ord('z') = {ord('z')}")
# print(f"ord('中') = {ord_zhong}, ord('文') = {ord_wen}")
# print(f"chr(65) = {chr_65}, chr(97) = {chr_97}")
# print(f"chr(20013) = {chr_20013}, chr(25991) = {chr_wen}")

# 打印 ASCII 可打印字符（32~126）
# ascii_chars = ""
# for i in range(32, 127):
#     ascii_chars += chr(i)
# print(f"ASCII 可打印字符: {ascii_chars}")

# 大小写转换
# lower_a = chr(ord('A') + 32)
# print(f"chr(ord('A') + 32) = {lower_a!r}")
# assert lower_a == 'a'

# assert ord_A == 65
# assert ord_Z == 90
# assert ord_a == 97
# assert chr_65 == 'A'
# assert chr_20013 == '中'
# print("练习 2.18 通过！")


# ---------------------------------------------------------------------------
# 练习 2.19 —— 字符串编码：encode() 和 decode()
# 将字符串 "Hello, 世界！" 编码为不同格式，再解码回来。
#   1) encode()          → UTF-8（默认）
#   2) encode("utf-16")  → UTF-16
#   3) encode("gbk")     → GBK（简体中文编码，如果系统支持）
#   4) 编码后的类型是什么？（bytes）
#   5) 将编码后的 bytes 解码回字符串
#   6) 尝试用错误的编码解码，观察发生了什么
# ---------------------------------------------------------------------------

text = "Hello, 世界！"

utf8_bytes = ...
utf16_bytes = ...

# print(f"原始字符串: {text}")
# print(f"UTF-8 编码: {utf8_bytes}")
# print(f"UTF-16 编码: {utf16_bytes}")
# print(f"UTF-8 字节数: {len(utf8_bytes)}")
# print(f"UTF-16 字节数: {len(utf16_bytes)}")

# 解码回字符串
decoded_utf8 = ...
# print(f"解码回字符串: {decoded_utf8}")

# 尝试用 ASCII 编码中文（会报错）
# try:
#     text.encode("ascii")
# except UnicodeEncodeError as e:
#     print(f"ASCII 编码中文报错: {e}")

# assert utf8_bytes == b"Hello, \xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81"
# assert decoded_utf8 == text
# print("练习 2.19 通过！")


# ---------------------------------------------------------------------------
# 练习 2.20 —— bytes 与 bytearray
# bytes 是不可变的字节序列，bytearray 是可变的。
#   1) 从字符串创建 bytes：b"hello"
#   2) 从列表创建 bytes：bytes([72, 73, 74])
#   3) 尝试修改 bytes（应该失败）
#   4) 从列表创建 bytearray：bytearray([72, 73, 74])
#   5) 修改 bytearray 的一个元素
# ---------------------------------------------------------------------------

b1 = b"hello"
b2 = ...

# print(f"b1 = {b1}")
# print(f"b2 = {b2}")
# print(f"b2 解码: {b2.decode()}")

# 下面这行会报错，因为 bytes 不可变
# b1[0] = 100

ba = bytearray([72, 73, 74])
# print(f"bytearray: {ba}")
# print(f"bytearray 解码: {ba.decode()}")

# 修改 bytearray
ba[0] = ...
# print(f"修改后: {ba}")
# print(f"修改后解码: {ba.decode()}")

# assert b2 == b"HIJ"
# assert ba[0] == 87  # 'W'
# print("练习 2.20 通过！")


# ---------------------------------------------------------------------------
# 练习 2.21 —— 不可变性的深入理解
# 字符串的 += 操作看似"修改"了字符串，实际上创建了新对象。
# 用 id() 证明这一点。
#   1) 创建 s = "hello"，记录 id(s)
#   2) 执行 s += " world"，记录 id(s) —— 是否相同？
#   3) 对列表重复同样实验：lst = [1,2,3]; lst += [4,5]
#   4) 观察列表的 id 是否发生了变化
# 这说明字符串是不可变类型（immutable），列表是可变类型（mutable）。
# ---------------------------------------------------------------------------

s = "hello"
# id_before = id(s)
s += " world"
# id_after = id(s)
# print(f"字符串 id 变化前: {id_before}，变化后: {id_after}")
# print(f"id 是否相同: {id_before == id_after}")

lst = [1, 2, 3]
# lst_id_before = id(lst)
lst += [4, 5]
# lst_id_after = id(lst)
# print(f"列表 id 变化前: {lst_id_before}，变化后: {lst_id_after}")
# print(f"id 是否相同: {lst_id_before == lst_id_after}")

# assert id_before != id_after
# assert lst_id_before == lst_id_after
# print("练习 2.21 通过！")


# ---------------------------------------------------------------------------
# 练习 2.22 —— 多行字符串与文本处理
# 有一首小诗（如下），完成以下任务：
#   1) 用三引号创建多行字符串存储
#   2) 统计总字符数（含换行符）
#   3) 按行切分（splitlines()）
#   4) 统计每行的字数
#   5) 查找字符 "风" 出现的次数
#   6) 将 "风" 替换为 "wind"
# ---------------------------------------------------------------------------

poem = """床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。"""

total_chars = ...
lines = ...
line_lengths = ...
count_feng = ...
replaced_poem = ...

# print(f"总字符数: {total_chars}")
# print(f"行数: {len(lines)}")
# print(f"每行字数: {line_lengths}")
# print(f"'风'字出现次数: {count_feng}")
# print(f"替换后:\n{replaced_poem}")

# assert total_chars == 20  # 包含 3 个换行符
# assert len(lines) == 4
# print("练习 2.22 通过！")


# ---------------------------------------------------------------------------
# 练习 2.23 —— 去除字符串中的指定字符
# strip() 默认去除空白字符，也可以指定要去除的字符集。
#   1) "...Hello..." 去掉所有 . → strip(".")
#   2) "  Hello  " 默认 strip → "Hello"
#   3) "  H e l l o  " 只 strip 空格（不会去掉中间的空格）
#   4) lstrip() 和 rstrip() 的区别
# ---------------------------------------------------------------------------

s1 = "...Hello..."
s2 = "  Hello  "
s3 = "  H e l l o  "

stripped1 = ...
stripped2 = ...
stripped3 = ...

# print(f"strip('.'): {stripped1!r}")
# print(f"strip(): {stripped2!r}")
# print(f"strip() 中间空格: {stripped3!r}")

# assert stripped1 == "Hello"
# assert stripped2 == "Hello"
# print("练习 2.23 通过！")


# ---------------------------------------------------------------------------
# 练习 2.24 —— partition() 和 split() 的区别
#   s = "one-two-three-four"
#   1) split("-")     → 返回所有片段
#   2) partition("-") → 只从第一次出现的位置分割，返回 3 元组
#   3) rpartition("-") → 从最后一次出现的位置分割
#   4) split("-", 2)  → 最多切 2 次
# 观察每种方法返回值的区别。
# ---------------------------------------------------------------------------

s = "one-two-three-four"

parts_all = ...
parts_once = ...
parts_last = ...
parts_limit = ...

# print(f"split: {parts_all}")
# print(f"partition: {parts_once}")
# print(f"rpartition: {parts_last}")
# print(f"split(max=2): {parts_limit}")

# assert parts_all == ["one", "two", "three", "four"]
# assert parts_once == ("one", "-", "two-three-four")
# assert parts_last == ("one-two-three", "-", "four")
# assert parts_limit == ["one", "two", "three-four"]
# print("练习 2.24 通过！")


# ---------------------------------------------------------------------------
# 练习 2.25 —— 综合应用题：用户名验证
# 编写一段代码（补全 TODO 处），验证用户输入的字符串是否符合规则：
#   规则：
#     - 长度在 3~16 个字符之间
#     - 只能包含字母、数字和下划线
#     - 不能以数字开头
#     - 不能包含大写字母（要求全小写）
#   请补全 is_valid_username 函数。
# ---------------------------------------------------------------------------


def is_valid_username(username: str) -> bool:
    """验证用户名是否符合规则。"""
    # TODO: 检查长度
    if ...:
        return False
    # TODO: 检查字符集（只含字母、数字、下划线）
    if ...:
        return False
    # TODO: 检查首字符不能是数字
    if ...:
        return False
    # TODO: 检查不能包含大写字母
    if ...:
        return False
    return True


# --- 测试用例 ---
# test_usernames = ["alice", "alice_123", "123abc", "AB", "a", "ab", "a" * 17, "hello world", "", "user_name"]
# for name in test_usernames:
#     result = is_valid_username(name)
#     print(f"'{name}' -> {'✅' if result else '❌'}")

# assert is_valid_username("alice") is True
# assert is_valid_username("alice_123") is True
# assert is_valid_username("a_b_c") is True
# assert is_valid_username("123abc") is False       # 数字开头
# assert is_valid_username("AB") is False            # 大写字母
# assert is_valid_username("a") is False              # 长度小于 3
# assert is_valid_username("a" * 17) is False         # 长度超过 16
# assert is_valid_username("hello world") is False    # 包含空格
# assert is_valid_username("") is False                # 空字符串
# print("练习 2.25 通过！")


# ---------------------------------------------------------------------------
# 练习 2.26 —— 综合应用题：敏感词屏蔽
# 编写一个函数 censor(text, word_list)，将文本中的敏感词替换为 ***。
#   要求：
#     - 大小写不敏感（"Hello" 和 "hello" 都要被屏蔽）
#     - 替换为 * 的数量与单词长度相同
#     - 例如：censor("Hello world", ["hello"]) → "***** world"
# 提示：先全部转小写比较，再在原字符串中替换。
# ---------------------------------------------------------------------------


def censor(text: str, word_list: list[str]) -> str:
    """将文本中的敏感词替换为等长星号。"""
    result = text
    for word in word_list:
        # TODO: 构建替换字符串（等长星号）
        replacement = ...
        # TODO: 大小写不敏感替换（提示：可先用小写形式查找）
        # 这里需要用一些技巧：不能直接用 replace，因为要保留原大小写
        # 简单实现：用小写版本来定位，再替换原字符串对应位置
        lower_result = result.lower()
        lower_word = word.lower()
        start = 0
        while True:
            pos = lower_result.find(lower_word, start)
            if pos == -1:
                break
            result = result[:pos] + replacement + result[pos + len(word):]
            lower_result = result.lower()
            start = pos + len(replacement)
    return result


# --- 测试用例 ---
# print(censor("Hello world, hello python", ["hello"]))  # → "***** world, ***** python"
# print(censor("ABC abc Abc", ["abc"]))                   # → "*** *** ***"
# print(censor("This is a test", ["is", "test"]))         # → "Th** ** a ****"

# assert censor("Hello world", ["hello"]) == "***** world"
# assert censor("ABC abc", ["abc"]) == "*** ***"
# assert censor("This is a test", ["is"]) == "Th** ** a test"
# print("练习 2.26 通过！")


# ---------------------------------------------------------------------------
# 练习 2.27 —— 综合应用题：统计文本信息
# 编写一个函数 analyze_text(text)，返回一个字典包含：
#   - total_chars: 总字符数（含空格和换行）
#   - char_count_no_space: 不含空格的字符数
#   - word_count: 单词数（按空格切分）
#   - line_count: 行数
#   - digit_count: 数字个数
#   - letter_count: 字母个数
#   - uppercase_count: 大写字母个数
#   - space_count: 空格（含空白字符）个数
# ---------------------------------------------------------------------------


def analyze_text(text: str) -> dict:
    """分析文本，返回统计信息字典。"""
    result = {}
    result["total_chars"] = ...
    result["char_count_no_space"] = ...
    result["word_count"] = ...
    result["line_count"] = ...
    result["digit_count"] = ...
    result["letter_count"] = ...
    result["uppercase_count"] = ...
    result["space_count"] = ...
    return result


# --- 测试用例 ---
# sample = "Hello World!\nPython is great 123"
# stats = analyze_text(sample)
# for key, value in stats.items():
#     print(f"{key}: {value}")

# assert stats["total_chars"] == 30
# assert stats["word_count"] == 5
# assert stats["line_count"] == 2
# assert stats["digit_count"] == 3
# print("练习 2.27 通过！")


# ---------------------------------------------------------------------------
# 练习 2.28 —— 挑战题：字符串压缩
# 实现一个简单的字符串压缩算法：
#   将连续重复的字符替换为「字符 + 重复次数」。
#   例如："aaabbbbc" → "a3b4c1"
#   注意：如果压缩后的字符串不比原串短，返回原串。
#   例如："abc" → "abc"（而不是 "a1b1c1"）
# ---------------------------------------------------------------------------


def compress_string(s: str) -> str:
    """压缩连续重复字符。"""
    if not s:
        return s

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            ...
        else:
            compressed.append(...)
            count = 1

    # 处理最后一组
    compressed.append(...)

    result = "".join(compressed)
    return result if len(result) < len(s) else s


# --- 测试用例 ---
# print(compress_string("aaabbbbc"))      # → "a3b4c1"
# print(compress_string("abc"))           # → "abc"（未缩短）
# print(compress_string("aabb"))          # → "aabb"（未缩短）
# print(compress_string("aaaa"))          # → "a4"
# print(compress_string(""))              # → ""

# assert compress_string("aaabbbbc") == "a3b4c1"
# assert compress_string("abc") == "abc"
# assert compress_string("aaaa") == "a4"
# assert compress_string("") == ""
# print("练习 2.28 通过！")


# ---------------------------------------------------------------------------
# 练习 2.29 —— 挑战题：回文字符串判断
# 回文是指正读和反读都一样的字符串，忽略空格、标点和大小写。
# 例如："A man, a plan, a canal: Panama" 是回文。
# 实现 is_palindrome 函数。
# 提示：先用 str.isalnum() 过滤非字母数字字符，再统一转小写比较。
# ---------------------------------------------------------------------------


def is_palindrome(s: str) -> bool:
    """判断字符串是否为回文（忽略空格、标点、大小写）。"""
    # TODO: 提取所有字母和数字字符，转为小写
    filtered = ...
    # TODO: 判断 filtered 是否等于其反转
    return ...


# --- 测试用例 ---
# test_cases = [
#     ("A man, a plan, a canal: Panama", True),
#     ("race a car", False),
#     ("上海自来水来自海上", True),  # 中文回文
#     ("", True),
#     ("aba", True),
#     ("abc", False),
# ]
# for s, expected in test_cases:
#     result = is_palindrome(s)
#     status = "✅" if result == expected else "❌"
#     print(f"{status} is_palindrome({s!r}) = {result}, expected = {expected}")

# assert is_palindrome("A man, a plan, a canal: Panama") is True
# assert is_palindrome("race a car") is False
# assert is_palindrome("上海自来水来自海上") is True
# assert is_palindrome("") is True
# assert is_palindrome("aba") is True
# print("练习 2.29 通过！")


# ---------------------------------------------------------------------------
# 练习 2.30 —— 挑战题：单词反转
# 实现 reverse_words(s)，反转字符串中单词的顺序，但单词内部字符顺序不变。
#   要求：
#     - 单词之间可能有多个空格
#     - 结果中只保留一个空格分隔
#     - 去掉首尾空格
#   例如："  Hello   world  Python  " → "Python world Hello"
# ---------------------------------------------------------------------------


def reverse_words(s: str) -> str:
    """反转字符串中单词的顺序。"""
    # TODO: 切分单词（自动处理多个空格），反转，重新拼接
    ...


# --- 测试用例 ---
# print(reverse_words("  Hello   world  Python  "))  # → "Python world Hello"
# print(reverse_words("a b c"))                      # → "c b a"
# print(reverse_words("single"))                     # → "single"
# print(reverse_words(""))                           # → ""

# assert reverse_words("  Hello   world  Python  ") == "Python world Hello"
# assert reverse_words("a b c") == "c b a"
# assert reverse_words("") == ""
# print("练习 2.30 通过！")


# ============================================================================
# 第二部分 补充练习（新增）
# ============================================================================


# ---------------------------------------------------------------------------
# 练习 2.31 —— f-string 调试语法（Python 3.8+）
# f"{var=}" 可以快速打印变量名和值，非常适合调试。
#   1) 定义 x = 42，用 f"{x=}" 输出
#   2) 输出 f"{x=:#010b}"（二进制格式，宽度 10）
#   3) 输出 f"{x=:#06x}"（十六进制格式，宽度 6）
#   4) 对表达式使用：f"{2+3*4=}"
#   5) 多个变量同时调试：f"{x=} {y=}"
# ---------------------------------------------------------------------------

x, y, z = 42, "hello", 3.14

debug1 = ...   # f"{x=}"
debug2 = ...   # f"{x=:#010b}"
debug3 = ...   # f"{x=:#06x}"
debug4 = ...   # f"{2+3*4=}"
debug5 = ...   # f"{x=} {y=} {z=}"

# print(debug1)  # 输出: x=42
# print(debug2)  # 输出: x=0b00101010
# print(debug3)  # 输出: x=0x002a
# print(debug4)  # 输出: 2+3*4=14
# print(debug5)  # 输出: x=42 y=hello z=3.14

# assert debug1 == "x=42"
# assert debug4 == "2+3*4=14"
# print("练习 2.31 通过！")


# ---------------------------------------------------------------------------
# 练习 2.32 —— f-string 嵌套与高级格式说明符
# f-string 支持在大括号内嵌套 f-string，以及丰富的格式说明符。
#   1) 嵌套：f"{'hello':>{10}}"（在 10 宽度内右对齐）
#   2) 用变量指定格式：width=20, align="^"
#   3) 嵌套格式化输出表格
#   4) 百分比格式：f"{0.1234:.2%}" → 12.34%
#   5) 千位分隔符：f"{1234567:,}" → 1,234,567
# ---------------------------------------------------------------------------

width = 20
align = "^"
text = "hello"

nested = ...   # f"{'hello':>{width}}" 或动态格式

percent = ...
thousands = ...

# print(f"右对齐宽度{width}: {nested!r}")
# print(f"百分比: {percent}")
# print(f"千位分隔: {thousands}")

# 动态填充对齐
# fill_char = "="
# print(f"动态格式: {f'{text':{fill_char}{align}{width}'}}")

# assert thousands == "1,234,567"
# assert percent == "12.34%"
# print("练习 2.32 通过！")


# ---------------------------------------------------------------------------
# 练习 2.33 —— str.removeprefix() 和 str.removesuffix()（Python 3.9+）
# 这两个方法更直观地去除字符串前缀/后缀，比切片更可读。
#   1) "HelloWorld".removeprefix("Hello") → "World"
#   2) "HelloWorld".removesuffix("World") → "Hello"
#   3) "HelloWorld".removeprefix("XXXX")  → 不匹配则返回原串（无报错）
#   4) "test.txt".removesuffix(".txt")
#   5) 对比 lstrip：lstrip 会删除字符集中的任意字符，而非完整前缀
# ---------------------------------------------------------------------------

s = "HelloWorld"

removed_prefix = ...
removed_suffix = ...
no_match = ...
file_name = ...

# 对比 lstrip 和 removeprefix 的区别
s2 = "abcabc"
lstrip_result = s2.lstrip("ab")       # → "c"
removeprefix_result = s2.removeprefix("ab")  # → "cabc"

# print(f"removeprefix('Hello'): {removed_prefix!r}")
# print(f"removesuffix('World'): {removed_suffix!r}")
# print(f"removeprefix('XXXX'): {no_match!r}")    # 不匹配返回原串
# print(f"文件名去掉后缀: {file_name!r}")
# print(f"lstrip('ab') = {lstrip_result!r}")
# print(f"removeprefix('ab') = {removeprefix_result!r}")

# assert removed_prefix == "World"
# assert removed_suffix == "Hello"
# assert no_match == "HelloWorld"
# assert file_name == "test"
# print("练习 2.33 通过！")


# ---------------------------------------------------------------------------
# 练习 2.34 —— str.casefold()：更强的大小写折叠
# casefold() 比 lower() 更激进，用于大小写不敏感匹配。
# 某些语言中（如德语 "ß" 大写为 "SS"），casefold 和 lower 行为不同。
#   1) 对比 "ß".lower() 和 "ß".casefold()
#   2) 对比 "straße".upper() 和 "STRASSE".casefold()
#   3) 验证 "straße".casefold() == "STRASSE".casefold()
#   4) 思考：什么时候用 lower()，什么时候用 casefold()？
# ---------------------------------------------------------------------------

sharp_s = "ß"
lower_result = ...
casefold_result = ...

strasse_lower = "straße".lower()
strasse_casefold = "straße".casefold()

# print(f"'ß'.lower() = {lower_result!r}")
# print(f"'ß'.casefold() = {casefold_result!r}")
# print(f"'straße'.casefold() == 'STRASSE'.casefold(): {strasse_casefold == 'STRASSE'.casefold()}")

# 国际象棋中的 KΩΝΣΤΑΝΤΙΝΟΣ 测试
# greek = "ΚΩΝΣΤΑΝΤΙΝΟΣ"
# print(f"Greek casefold: {greek.casefold()}")

# assert lower_result == "ß"
# assert casefold_result == "ss"
# assert strasse_casefold == "strasse"
# print("练习 2.34 通过！")


# ---------------------------------------------------------------------------
# 练习 2.35 —— str.isascii()（Python 3.7+）
# 判断字符串是否全部由 ASCII 字符组成。
#   1) "hello".isascii() → True
#   2) "你好".isascii() → False
#   3) "hello123!@#".isascii() → True
#   4) "hello\n\t".isascii() → True（控制字符也是 ASCII）
#   5) 过滤字符串中的非 ASCII 字符
# ---------------------------------------------------------------------------

ascii_check1 = "hello".isascii()
ascii_check2 = ...
ascii_check3 = ...
ascii_check4 = ...

# 过滤字符串中的非 ASCII 字符
mixed = "hello你好world世界"
filtered = ...  # 用 isascii() 过滤保留 ASCII 字符

# print(f"'hello' isascii: {ascii_check1}")
# print(f"'你好' isascii: {ascii_check2}")
# print(f"'hello123!@#' isascii: {ascii_check3}")
# print(f"'hello\\n\\t' isascii: {ascii_check4}")
# print(f"过滤后: {filtered!r}")

# assert ascii_check1 is True
# assert ascii_check2 is False
# assert ascii_check3 is True
# assert ascii_check4 is True
# assert filtered == "helloworld"
# print("练习 2.35 通过！")


# ---------------------------------------------------------------------------
# 练习 2.36 —— str.maketrans() 和 str.translate()
# 用 maketrans 创建字符映射表，translate 执行批量替换。
# 比多次 replace 效率更高。
#   1) 将 "aeiou" 映射为 "12345"
#   2) 将 "hello world" 中的元音替换为数字
#   3) 用 maketrans 的第三个参数删除指定字符
#   4) 利用 str.maketrans 实现 ROT13（凯撒密码的一种）
# ---------------------------------------------------------------------------

# 元音替换
trans_table = str.maketrans("aeiou", "12345")
vowel_replaced = ...

# 带删除字符的翻译表
# 删除所有空格和标点
trans_table2 = str.maketrans("", "", " ,.!?")
cleaned = ...

# print(f"元音替换: {vowel_replaced!r}")
# print(f"删除空格标点: {cleaned!r}")

# ROT13 实现
def rot13(text: str) -> str:
    """用 maketrans 和 translate 实现 ROT13 加密。"""
    lower_from = "abcdefghijklmnopqrstuvwxyz"
    lower_to = ...   # 平移 13 位
    upper_from = lower_from.upper()
    upper_to = lower_to.upper()
    table = str.maketrans(lower_from + upper_from, lower_to + upper_to)
    return text.translate(table)

# print(rot13("Hello, World!"))                # → "Uryyb, Jbeyq!"
# print(rot13(rot13("Hello, World!")))         # → "Hello, World!"（还原）

# assert vowel_replaced == "h2ll4 w3rld"
# assert rot13("Hello") == "Uryyb"
# print("练习 2.36 通过！")


# ---------------------------------------------------------------------------
# 练习 2.37 —— string.Template 模板字符串
# Template 提供简单的字符串替换，使用 $ 标记占位符。
# 相比 f-string，Template 更安全（不会执行任意表达式）。
#   1) 用 $name 和 $age 创建模板
#   2) 用 substitute() 填充模板
#   3) 用 safe_substitute() 安全填充（缺失占位符不报错）
#   4) 用 $$ 输出美元符号
# ---------------------------------------------------------------------------

from string import Template

t = Template("$name 今年 $age 岁。")
filled = ...

# safe_substitute 允许缺失
t2 = Template("Hello, $name! 你的分数是 $score。")
safe_filled = ...   # 只提供 name，不提供 score

# print(filled)
# print(safe_filled)  # score 保留为 $score

# 带 $$ 的模板
price_template = Template("总价: $$$price")  # $$ → 字面量 $
price_filled = ...

# print(price_filled)

# assert filled == "Alice 今年 30 岁。"
# assert "$score" in safe_filled
# print("练习 2.37 通过！")


# ---------------------------------------------------------------------------
# 练习 2.38 —— textwrap 模块
# textwrap 用于格式化和包装文本，控制输出宽度。
#   1) wrap(text, width)：将文本切成指定宽度的行列表
#   2) fill(text, width)：将文本重新包装为单字符串
#   3) shorten(text, width)：截断并添加省略号
#   4) dedent(text)：去除公共前导空白
#   5) indent(text, prefix)：添加前缀
# ---------------------------------------------------------------------------

import textwrap

long_text = "Python 是一种广泛使用的解释型、高级编程语言，由 Guido van Rossum 于1991年创建。"

wrapped = textwrap.wrap(long_text, width=20)
filled = textwrap.fill(long_text, width=20)
shortened = textwrap.shorten(long_text, width=30, placeholder="...")

# print(f"wrap (每行20字符):")
# for i, line in enumerate(wrapped, 1):
#     print(f"  {i}: {line}")
# print(f"\nfill 结果:\n{filled}")
# print(f"\nshorten: {shortened}")

# dedent 和 indent
indented_text = "    hello\n    world"
dedented = ...
reindented = ...

# print(f"dedent:\n{dedented!r}")
# print(f"indent:\n{reindented!r}")

# assert len(shortened) <= 33  # 30字符 + "..."
# print("练习 2.38 通过！")


# ---------------------------------------------------------------------------
# 练习 2.39 —— repr() 与 str() 的区别
# str() 面向用户，repr() 面向开发者，应能重建对象。
# 很多类型的 repr() 可以用 eval() 重建。
#   1) str("hello\nworld")  vs repr("hello\nworld")
#   2) str(42) vs repr(42)  —— 对于简单类型通常相同
#   3) str([1,2,3]) vs repr([1,2,3])  —— 通常相同
#   4) str(datetime.now()) vs repr(datetime.now())
#   5) ascii() 将非 ASCII 字符转义（Python 3）
# ---------------------------------------------------------------------------

from datetime import datetime

hello = "hello\nworld"

str_result = ...
repr_result = ...

now = datetime.now()
str_now = ...
repr_now = ...

ascii_hello = ...
ascii_chinese = ascii("你好")

# print(f"str: {str_result}")
# print(f"repr: {repr_result}")
# print(f"str(now): {str_now}")
# print(f"repr(now): {repr_now}")
# print(f"ascii('hello\\nworld'): {ascii_hello!r}")
# print(f"ascii('你好'): {ascii_chinese!r}")

# 对于很多类型，eval(repr(x)) == x
# assert eval(repr(42)) == 42
# assert eval(repr([1, 2, 3])) == [1, 2, 3]
# print("练习 2.39 通过！")


# ---------------------------------------------------------------------------
# 练习 2.40 —— Unicode 正规化（unicodedata）
# Unicode 有多种编码方式，同一个字符可能有不同码点序列。
# 例如 "é" 可以是单个码点 U+00E9，也可以是 e + ́ 组合（U+0065 U+0301）。
#   1) 用 unicodedata.normalize('NFC', s) 组合式正规化
#   2) 用 unicodedata.normalize('NFD', s) 分解式正规化
#   3) 比较正规化前后的长度差异
#   4) 获取字符的 Unicode 名称
# ---------------------------------------------------------------------------

import unicodedata

combined = "é"            # é（单个码点）
decomposed = "é"    # e + ́（两个码点）

# print(f"组合: {combined!r} ({len(combined)} 个码点)")
# print(f"分解: {decomposed!r} ({len(decomposed)} 个码点)")
# print(f"视觉上相等: {combined == decomposed}")  # False！
# print(f"NFC 后相等: {unicodedata.normalize('NFC', combined) == unicodedata.normalize('NFC', decomposed)}")

# 获取字符名称
char_name = unicodedata.name("中")
# print(f"'中' 的 Unicode 名称: {char_name}")

# 用 lookup 反向查找
char_from_name = unicodedata.lookup("SNOWMAN")
# print(f"SNOWMAN: {char_from_name}")

# assert combined != decomposed  # 码点不同
# assert unicodedata.normalize('NFC', combined) == unicodedata.normalize('NFC', decomposed)
# print("练习 2.40 通过！")


# ---------------------------------------------------------------------------
# 练习 2.41 —— 编码错误处理策略
# 编码时可能遇到无法编码的字符，Python 提供多种错误处理策略。
#   1) "strict"（默认）：遇到无法编码的字符抛出 UnicodeEncodeError
#   2) "ignore"：静默忽略无法编码的字符
#   3) "replace"：用 ? 替换无法编码的字符
#   4) "xmlcharrefreplace"：用 XML 实体 &#NNN; 替换
#   5) "backslashreplace"：用 \\uNNNN 转义序列替换
# ---------------------------------------------------------------------------

text = "Hello 世界 🌍"

# encode_strict = text.encode("ascii", "strict")  # 会报错

encode_ignore = ...
encode_replace = ...
encode_xml = ...
encode_backslash = ...

# print(f"ignore: {encode_ignore}")
# print(f"replace: {encode_replace}")
# print(f"xmlcharrefreplace: {encode_xml}")
# print(f"backslashreplace: {encode_backslash}")

# 解码时的错误处理
# bytes_data = b"Hello \xff\xfe\xff"
# decode_replace = bytes_data.decode("utf-8", "replace")
# print(f"解码 replace: {decode_replace!r}")

# assert b" " in encode_ignore
# assert b"?" in encode_replace
# assert b"&#" in encode_xml
# assert b"\\u" in encode_backslash
# print("练习 2.41 通过！")


# ---------------------------------------------------------------------------
# 练习 2.42 —— eval() 与安全性
# eval() 可以执行任意 Python 表达式，但存在安全风险。
# ast.literal_eval() 只安全地求值字面量。
#   1) 用 eval 计算字符串表达式："2 ** 10"
#   2) 用 eval 将字符串转列表："[1, 2, 3]"
#   3) 用 ast.literal_eval 安全求值
#   4) 观察 literal_eval 拒绝非字面量表达式
# ---------------------------------------------------------------------------

import ast

expr_result = ...    # eval("2 ** 10")
list_from_str = ...  # eval("[1, 2, 3]")

safe_list = ast.literal_eval("[1, 2, 3]")
safe_dict = ast.literal_eval("{'a': 1, 'b': 2}")

# print(f"eval('2 ** 10') = {expr_result}")
# print(f"eval('[1, 2, 3]') = {list_from_str}")
# print(f"literal_eval 列表: {safe_list}")
# print(f"literal_eval 字典: {safe_dict}")

# 下面这行会报错，因为 literal_eval 不允许调用函数
# ast.literal_eval("__import__('os').system('ls')")

# assert expr_result == 1024
# assert list_from_str == [1, 2, 3]
# assert safe_list == [1, 2, 3]
# assert ast.literal_eval("True") is True
# assert ast.literal_eval("None") is None
# print("练习 2.42 通过！")


# ---------------------------------------------------------------------------
# 练习 2.43 —— 格式说明符迷你语言（Format Specification Mini-Language）
# 深入了解 f-string 和 format() 的完整格式规则：
#   [[fill]align][sign][#][0][width][grouping][.precision][type]
#   1) fill+align："{:*<10}"（左对齐，* 填充）
#   2) sign："{:+}", "{:-}", "{: }"（正号显示）
#   3) #：二进制/十六进制前缀 "{:#b}", "{:#x}"
#   4) 0：前导零 "{:010}"
#   5) width：宽度
#   6) grouping："," 或 "_" 千位分隔
#   7) .precision：精度
#   8) type：b/o/x/X/d/f/e/g/%
# ---------------------------------------------------------------------------

n = 42
pi = 3.1415926535
big_num = 1234567890

# fill + align
fmt1 = ...  # f"{n:*<10}"  → "42********"

# sign
fmt2 = ...  # f"{n:+}"     → "+42"
fmt3 = ...  # f"{n: }"     → " 42"（正号用空格替代）

# # (alternate form)
fmt4 = ...  # f"{n:#b}"    → "0b101010"
fmt5 = ...  # f"{n:#06x}"  → "0x002a"

# width + zero
fmt6 = ...  # f"{n:010}"   → "0000000042"

# grouping
fmt7 = ...  # f"{big_num:,}" → "1,234,567,890"
fmt8 = ...  # f"{big_num:_}" → "1_234_567_890"

# type
fmt9 = ...  # f"{pi:.2f}"   → "3.14"
fmt10 = ... # f"{pi:.2%}"  → "314.16%"? (不对, pi=3.14, 所以是 314.16%)

# print(f"左对齐填充: {fmt1!r}")
# print(f"正号: {fmt2!r}")
# print(f"空格正号: {fmt3!r}")
# print(f"二进制前缀: {fmt4!r}")
# print(f"十六进制前缀宽度6: {fmt5!r}")
# print(f"前导零宽度10: {fmt6!r}")
# print(f"千位逗号: {fmt7!r}")
# print(f"千位下划线: {fmt8!r}")
# print(f"两位小数: {fmt9!r}")

# assert fmt1 == "42********"
# assert fmt2 == "+42"
# assert fmt4 == "0b101010"
# assert fmt7 == "1,234,567,890"
# assert fmt9 == "3.14"
# print("练习 2.43 通过！")


# ---------------------------------------------------------------------------
# 练习 2.44 —— sys.intern() 字符串驻留
# 字符串驻留（interning）可以节省内存和加速比较。
# Python 自动驻留短字符串（通常 < 20 字符且是字面量）。
# 手动驻留适合大量重复字符串比较的场景。
#   1) 用 is 比较两个相同值但不同方式创建的字符串
#   2) 用 sys.intern 手动驻留后 is 比较为 True
#   3) 性能对比：intern 后用 is 替代 == 比较
# ---------------------------------------------------------------------------

import sys

s1 = "hello"
s2 = "".join(["h", "e", "l", "l", "o"])

# print(f"s1 = {s1!r}, s2 = {s2!r}")
# print(f"s1 == s2: {s1 == s2}")
# print(f"s1 is s2: {s1 is s2}")  # 可能 False（不同对象）

# 手动驻留
s1_interned = sys.intern(s1)
s2_interned = sys.intern(s2)
# print(f"驻留后 s1 is s2: {s1_interned is s2_interned}")  # True!

# 短字符串自动驻留演示
# a = "abc"
# b = "abc"
# print(f"短字面量 is: {a is b}")  # 通常是 True

# assert s1_interned is s2_interned
# print("练习 2.44 通过！")


# ---------------------------------------------------------------------------
# 练习 2.45 —— collections.Counter 统计字符
# Counter 是字典子类，用于统计可哈希对象的频次。
#   1) 用 Counter("mississippi") 统计字符频次
#   2) 获取出现最多的字符：most_common(3)
#   3) Counter 的 +、-、&、| 运算
#   4) 对比 str.count() 和 Counter 的区别
# ---------------------------------------------------------------------------

from collections import Counter

word = "mississippi"
counter = Counter(word)

most_common3 = ...

# print(f"字符统计: {dict(counter)}")
# print(f"出现最多的 3 个: {most_common3}")

# Counter 运算
c1 = Counter("hello")
c2 = Counter("world")
combined = c1 + c2
# print(f"c1 + c2: {dict(combined)}")

# 手动用 str.count 统计
s = "banana"
count_a = ...
# print(f"'banana' 中 'a' 的个数: {count_a}")

# assert counter["i"] == 4
# assert counter["s"] == 4
# assert count_a == 3
# print("练习 2.45 通过！")


# ---------------------------------------------------------------------------
# 练习 2.46 —— bytes.hex() 和 bytes.fromhex()（Python 3.5+）
# 以十六进制字符串形式查看和创建字节数据。
#   1) b"hello".hex() → "68656c6c6f"
#   2) bytes.fromhex("68656c6c6f") → b"hello"
#   3) 用 sep 参数添加分隔符（Python 3.8+）：hex(":")
#   4) 编码与十六进制互转
# ---------------------------------------------------------------------------

data = b"hello"
hex_str = ...
restored = ...

# 带分隔符（Python 3.8+）
# hex_with_sep = data.hex(":")  # → "68:65:6c:6c:6f"

# print(f"hex: {hex_str}")
# print(f"fromhex: {restored}")
# print(f"带冒号: {hex_with_sep}")

# 整数转十六进制字节
# num = 255
# hex_num = format(num, "x")
# print(f"255 → hex: {hex_num}")

# assert hex_str == "68656c6c6f"
# assert restored == b"hello"
# print("练习 2.46 通过！")


# ---------------------------------------------------------------------------
# 练习 2.47 —— str.isidentifier() 与 keyword 模块
# 判断字符串是否是合法的 Python 标识符（变量名）。
#   1) "hello".isidentifier() → True
#   2) "2hello".isidentifier() → False
#   3) "hello_world".isidentifier() → True
#   4) "for".isidentifier() → True（但 for 是关键字，不能作为变量名）
#   5) 用 keyword.iskeyword() 区分关键字
# ---------------------------------------------------------------------------

import keyword

id1 = "hello".isidentifier()
id2 = ...
id3 = ...
id4 = ...

is_keyword = ...

# 找出所有合法的变量名
candidates = ["foo", "2bar", "baz_123", "class", "if", "x y", "_private"]
valid_vars = ...
# for name in candidates:
#     if name.isidentifier() and not keyword.iskeyword(name):
#         valid_vars.append(name)
# print(f"合法变量名: {valid_vars}")

# assert id1 is True
# assert id2 is False
# assert id4 is True
# assert keyword.iskeyword("for") is True
# assert keyword.iskeyword("hello") is False
# print("练习 2.47 通过！")


# ---------------------------------------------------------------------------
# 练习 2.48 —— 字符串连接性能对比
# 大量字符串连接时，join() 比 += 快得多，因为字符串不可变。
# 本练习测试两种方式的性能差异。
#   1) 用 += 连接 1000 个字符串
#   2) 用 join() 连接 1000 个字符串
#   3) 对比两种方式的时间（感受性能差异）
#   4) 理解原因：+= 每次创建新字符串，join() 预分配
# ---------------------------------------------------------------------------

import time

n = 10000
parts = ["hello"] * n

# 方式1：join
start = time.perf_counter()
result_join = "".join(parts)
time_join = time.perf_counter() - start

# 方式2：+=
start = time.perf_counter()
result_plus = ""
for p in parts:
    result_plus += p
time_plus = time.perf_counter() - start

# print(f"join 耗时: {time_join:.6f} 秒")
# print(f"+= 耗时: {time_plus:.6f} 秒")
# print(f"join 比 += 快 {time_plus/time_join:.1f} 倍")

# assert result_join == result_plus  # 结果应相同
# print("练习 2.48 通过！")


# ---------------------------------------------------------------------------
# 练习 2.49 —— Base64 编码
# Base64 将二进制数据编码为 ASCII 字符串，常用于数据传输。
#   1) 将字符串编码为 Base64：base64.b64encode()
#   2) 解码 Base64 为原字符串：base64.b64decode()
#   3) URL 安全的 Base64：base64.urlsafe_b64encode()
#   4) Base64 编码图片/文件的场景思考
# ---------------------------------------------------------------------------

import base64

text = "Hello, Python! 你好"
encoded = ...
decoded = ...

url_safe_encoded = base64.urlsafe_b64encode(b"hello??world")
url_safe_decoded = ...

# print(f"原始: {text}")
# print(f"Base64 编码: {encoded}")
# print(f"解码: {decoded}")

# print(f"URL 安全编码: {url_safe_encoded}")
# print(f"URL 安全解码: {url_safe_decoded}")

# assert decoded == text
# assert url_safe_decoded == b"hello??world"
# print("练习 2.49 通过！")


# ---------------------------------------------------------------------------
# 练习 2.50 —— splitlines() 与 split("\n") 的区别
# splitlines() 能处理多种换行符（\n, \r\n, \r 等），
# 而 split("\n") 只按 \n 切分。
#   1) "a\nb\r\nc\rd".splitlines()  vs split("\n")
#   2) splitlines(True) 保留换行符
#   3) 处理空行时的行为差异
# ---------------------------------------------------------------------------

text = "a\nb\r\nc\rd"

lines1 = ...
lines2 = ...
lines3 = ...

# print(f"splitlines: {lines1}")
# print(f"splitlines(True): {lines3}")
# print(f"split('\\n'): {lines2}")

# assert lines1 == ["a", "b", "c", "d"]
# assert lines2 != ["a", "b", "c", "d"]  # 因为包含 \r
# print("练习 2.50 通过！")


# ---------------------------------------------------------------------------
# 练习 2.51 —— str.expandtabs()
# expandtabs() 将制表符替换为空格，默认制表宽度为 8。
#   1) "a\tb".expandtabs() → "a       b"（8 格）
#   2) "a\tb".expandtabs(4) → "a   b"（4 格）
#   3) "a\tb\tc".expandtabs(3)
# ---------------------------------------------------------------------------

tab_str = "Name\tAge\tCity\nAlice\t30\tBeijing"

expanded_default = ...
expanded_4 = ...

# print(f"原始:\n{tab_str!r}")
# print(f"默认制表:\n{expanded_default}")
# print(f"宽度 4:\n{expanded_4}")

# assert "\t" not in expanded_default
# assert len(expanded_4.split("\n")[0].split("   ")) >= 3
# print("练习 2.51 通过！")


# ---------------------------------------------------------------------------
# 练习 2.52 —— Unicode 双向文本与零宽字符
# Unicode 中有一些特殊的控制字符：
#   ​ = 零宽空格（ZERO WIDTH SPACE）
#   ‌ = 零宽非连接符
#   ‍ = 零宽连接符（用于 emoji 序列）
#   1) 零宽空格对字符串长度的影响
#   2) 用零宽连接符组合自定义 emoji
#   3) ﻿（BOM）对字符串的影响
# ---------------------------------------------------------------------------

normal = "hello"
with_zwsp = "he​llo"

# print(f"普通字符串: {normal!r} (len={len(normal)})")
# print(f"含零宽空格: {with_zwsp!r} (len={len(with_zwsp)})")
# print(f"视觉相同: {normal == with_zwsp}")
# print(f"显示效果:")
# print(f"  '{normal}'")
# print(f"  '{with_zwsp}'")  # 视觉上几乎一样

# Emoji 组合（肤色修饰符）
# emoji = "\U0001F44D"           # 👍（大拇指）
# emoji_light = "\U0001F44D\U0001F3FB"  # 👍🏻（浅肤色）
# print(f"大拇指: {emoji}")
# print(f"浅肤色: {emoji_light}")

# assert len(with_zwsp) == 6
# assert normal != with_zwsp
# print("练习 2.52 通过！")


# ---------------------------------------------------------------------------
# 练习 2.53 —— itertools 与字符串操作
# itertools 模块提供高效的迭代器工具，可以与字符串搭配使用。
#   1) itertools.cycle：无限循环字符串
#   2) itertools.permutations：字符串全排列
#   3) itertools.combinations：组合
#   4) itertools.product：笛卡尔积
# ---------------------------------------------------------------------------

from itertools import cycle, permutations, combinations, product

# cycle 循环
c = cycle("ABC")
# first_6 = "".join(next(c) for _ in range(6))
# print(f"cycle('ABC') 取 6 个: {first_6}")

# 全排列
perms = ["".join(p) for p in permutations("ABC", 2)]
# print(f"ABC 的 2 排列: {perms}")

# 组合
combs = ["".join(c) for c in combinations("ABC", 2)]
# print(f"ABC 的 2 组合: {combs}")

# 笛卡尔积
prods = ["".join(p) for p in product("AB", "12")]
# print(f"A/B × 1/2: {prods}")

# assert first_6 == "ABCABC"
# assert ("AB", "AC", "BA", "BC", "CA", "CB") == ...
# assert sorted(combs) == ["AB", "AC", "BC"]
# print("练习 2.53 通过！")


# ---------------------------------------------------------------------------
# 练习 2.54 —— str.format_map() 动态格式化
# format_map 接受一个映射对象（如字典）来填充占位符。
# 和 format(**dict) 类似，但可以直接使用 dict 子类。
#   1) "{name} is {age}".format_map({"name": "Alice", "age": 30})
#   2) 使用 defaultdict 作为格式映射（缺失键返回默认值）
#   3) 使用自定义 mapping 类实现动态值
# ---------------------------------------------------------------------------

info = {"name": "Bob", "age": 25}
formatted = ...

# print(formatted)

# 使用 defaultdict 处理缺失键
from collections import defaultdict

default_info = defaultdict(lambda: "未知")
default_info.update(info)
template = "姓名: {name}, 年龄: {age}, 城市: {city}"
result_with_default = ...

# print(result_with_default)

# assert formatted == "Bob is 25"
# assert "未知" in result_with_default
# print("练习 2.54 通过！")


# ---------------------------------------------------------------------------
# 挑战 2.55 —— 凯撒密码破解器
# 凯撒密码是将字母按固定位数偏移的简单加密方法。
# 已知一段凯撒密文（只含英文字母），请暴力破解所有 25 种偏移：
#   密文: "Zkdw lv wkh zhdwkhuhq wkhuh, brx olnh?"
# 提示：chr(ord("A") + offset)，注意大写和小写字母分开处理。
#   只处理英文字母，非字母字符保持原样。
# ---------------------------------------------------------------------------


def caesar_decrypt(cipher: str, shift: int) -> str:
    """将密文字母向后移动 shift 位解密。"""
    result = []
    for char in cipher:
        if "a" <= char <= "z":
            ...
        elif "A" <= char <= "Z":
            ...
        else:
            result.append(char)
    return "".join(result)


def brute_force_caesar(cipher: str) -> None:
    """暴力破解凯撒密码，打印所有 25 种可能。"""
    for shift in range(1, 26):
        decrypted = caesar_decrypt(cipher, shift)
        # print(f"偏移 {shift:2d}: {decrypted}")


cipher = "Zkdw lv wkh zhdwkhuhq wkhuh, brx olnh?"
# brute_force_caesar(cipher)

# 手动找出正确的那一行（提示：偏移量为 3 时，Z → C 而不是 W）
# 实际上，对于凯撒密码，偏移 3 表示每个字母向前移 3 位，
# 但在解密时，我们需要向后移。上面的 decrypt 已经实现了向后移。
# 即 encrypt(word, shift) = chr(ord(c) + shift 循环)
# 那么 decrypt(cipher, shift) = chr(ord(c) - shift 循环)

# assert caesar_decrypt("Khoor", 3) == "Hello"  # 验证解密函数
# print("挑战 2.55 通过！")


# ---------------------------------------------------------------------------
# 挑战 2.56 —— Vigenère 密码
# Vigenère 密码是凯撒密码的升级版，使用关键词决定每个字母的偏移量。
# 关键词循环使用，每个字母决定当前明文字母的偏移量。
# 实现 vigenere_encrypt(plain, key) 和 vigenere_decrypt(cipher, key)。
# 提示：偏移量 = key[i % len(key)] 中字母在字母表中的位置（A=0, B=1, ...）
# ---------------------------------------------------------------------------


def vigenere_encrypt(plain: str, key: str) -> str:
    """用 Vigenère 密码加密。"""
    result = []
    key = key.upper()
    key_idx = 0
    for char in plain:
        if "A" <= char <= "Z":
            shift = ord(key[key_idx % len(key)]) - ord("A")
            encrypted = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            result.append(encrypted)
            key_idx += 1
        elif "a" <= char <= "z":
            shift = ord(key[key_idx % len(key)]) - ord("A")
            encrypted = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            result.append(encrypted)
            key_idx += 1
        else:
            result.append(char)
    return "".join(result)


def vigenere_decrypt(cipher: str, key: str) -> str:
    """用 Vigenère 密码解密。"""
    # TODO: 实现解密（加密的逆操作）
    ...


# encrypted = vigenere_encrypt("HELLO", "KEY")
# decrypted = vigenere_decrypt(encrypted, "KEY")
# print(f"加密: {encrypted}")
# print(f"解密: {decrypted}")

# assert vigenere_encrypt("HELLO", "KEY") == "RIJVS"
# assert vigenere_decrypt("RIJVS", "KEY") == "HELLO"
# print("挑战 2.56 通过！")


# ---------------------------------------------------------------------------
# 挑战 2.57 —— 字符串全排列（递归）
# 实现函数 all_permutations(s)，返回字符串所有排列的集合。
# 例如 "abc" 的排列：{"abc", "acb", "bac", "bca", "cab", "cba"}
# 要求用递归实现，返回 set 类型。
# 提示：递归思路——选一个字符作为开头，对剩余部分求排列。
# ---------------------------------------------------------------------------


def all_permutations(s: str) -> set[str]:
    """递归计算字符串的所有排列。"""
    if len(s) <= 1:
        return {s}
    result = set()
    for i, char in enumerate(s):
        # 取出第 i 个字符，对剩余的字符递归求排列
        rest = s[:i] + s[i+1:]
        for perm in all_permutations(rest):
            ...
    return result


# perms = all_permutations("abc")
# print(f"排列数: {len(perms)}")  # 6
# print(f"排列: {sorted(perms)}")

# assert len(all_permutations("abc")) == 6
# assert len(all_permutations("ab")) == 2
# assert len(all_permutations("a")) == 1
# assert "abc" in all_permutations("abc")
# print("挑战 2.57 通过！")


# ---------------------------------------------------------------------------
# 挑战 2.58 —— 编辑距离（Levenshtein Distance）
# 编辑距离是两个字符串之间互相转换所需的最小操作次数。
# 操作包括：插入、删除、替换一个字符。
# 例如：kitten → sitting 的编辑距离为 3：
#   kitten → sitten（替换 k→s）
#   sitten → sittin（替换 e→i）
#   sittin → sitting（插入 g）
# 实现 levenshtein_distance(s1, s2) 函数。
# 提示：使用动态规划（DP）二维表，或递归+记忆化。
# ---------------------------------------------------------------------------


def levenshtein_distance(s1: str, s2: str) -> int:
    """计算两个字符串的编辑距离。"""
    m, n = len(s1), len(s2)
    # 创建 (m+1) x (n+1) 的 DP 表
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化边界
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # TODO: 填充 DP 表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                ...
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # 删除
                    dp[i][j - 1],      # 插入
                    ...
                )

    return dp[m][n]


# print(levenshtein_distance("kitten", "sitting"))  # → 3
# print(levenshtein_distance("hello", "world"))     # → 4
# print(levenshtein_distance("", "abc"))             # → 3

# assert levenshtein_distance("kitten", "sitting") == 3
# assert levenshtein_distance("hello", "world") == 4
# assert levenshtein_distance("", "abc") == 3
# assert levenshtein_distance("abc", "abc") == 0
# print("挑战 2.58 通过！")


# ---------------------------------------------------------------------------
# 挑战 2.59 —— 最长公共子串（Longest Common Substring）
# 找到两个字符串中最长的公共连续子串。
# 例如 "abcdef" 和 "zbcdf" 的最长公共子串是 "bcd"。
# 实现 longest_common_substring(s1, s2) 函数。
# 提示：使用 DP 或滑动窗口。
# ---------------------------------------------------------------------------


def longest_common_substring(s1: str, s2: str) -> str:
    """找到两个字符串中的最长公共子串。"""
    m, n = len(s1), len(s2)
    max_len = 0
    end_idx = 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_idx = i
            else:
                dp[i][j] = 0

    return s1[end_idx - max_len:end_idx]


# print(longest_common_substring("abcdef", "zbcdf"))   # → "bcd"
# print(longest_common_substring("hello", "world"))    # → "l"
# print(longest_common_substring("abc", "xyz"))        # → ""

# assert longest_common_substring("abcdef", "zbcdf") in ("bcd", "cd")
# assert longest_common_substring("hello", "world") == "l"
# assert longest_common_substring("abc", "xyz") == ""
# print("挑战 2.59 通过！")


# ---------------------------------------------------------------------------
# 挑战 2.60 —— 字符串通配符匹配
# 实现简单的通配符匹配，支持 ?（匹配任意一个字符）和 *（匹配任意多个字符）。
# 例如：
#   "hello".match("h*") → True
#   "hello".match("h?l?o") → True
#   "hello".match("h?llo") → True
#   "hello".match("h?x*o") → False
# 实现 wildcard_match(s, pattern) 函数。
# 提示：可以用双指针或递归。
# ---------------------------------------------------------------------------


def wildcard_match(s: str, pattern: str) -> bool:
    """通配符匹配，? 匹配一个字符，* 匹配零个或多个字符。"""
    i = j = 0
    star_pos = -1
    match_pos = 0

    while i < len(s):
        if j < len(pattern) and pattern[j] in (s[i], "?"):
            i += 1
            j += 1
        elif j < len(pattern) and pattern[j] == "*":
            star_pos = j
            match_pos = i
            j += 1
        elif star_pos != -1:
            j = star_pos + 1
            match_pos += 1
            i = match_pos
        else:
            ...
            break
    else:
        while j < len(pattern) and pattern[j] == "*":
            j += 1
        return j == len(pattern)

    return False


# print(wildcard_match("hello", "h*"))       # → True
# print(wildcard_match("hello", "h?l?o"))    # → True
# print(wildcard_match("hello", "h?llo"))    # → True
# print(wildcard_match("hello", "h?x*o"))    # → False
# print(wildcard_match("", "*"))             # → True
# print(wildcard_match("abc", "a*c"))        # → True

# assert wildcard_match("hello", "h*") is True
# assert wildcard_match("hello", "h?l?o") is True
# assert wildcard_match("hello", "h?x*o") is False
# assert wildcard_match("", "*") is True
# assert wildcard_match("abc", "a*c") is True
# print("挑战 2.60 通过！")


# ============================================================================
# 结束
# ============================================================================
# 恭喜你完成了所有练习！
# 本文件共包含两大部分 60 道练习题（第一部分 30 题 + 第二部分 30 题）。
# 请逐一取消每个练习中的 print/assert 注释，运行脚本验证你的答案。
# 运行方式：uv run python practice_01_datatypes_strings.py
# ============================================================================
