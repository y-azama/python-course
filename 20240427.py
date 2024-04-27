# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 12:56:59 2024

@author: y_azama
01.プログラミングの基礎
- 変数
- if文
- for文

02以降
-> 配列
-> 関数
-> ファイルの入出力
"""

"""
print(xxx)
-> xxxを出力します
"""

""" コメントアウト(複数行 )
#: これより後ろの文字は意味がない（1行コメント）
"""

# 変数・代入
## 変数:数字
suuji1 = 1 + 1
suuji2 = suuji1 + int(1)
print(1 + 1) # -> 2
print("1 + 1") # -> 1 + 1
print("1" + "1") # -> 11

print(1 * 2) # -> 2
print("1 * 2") # -> 1 * 2
print("1" * 2) # -> 11

## 変数：文字
moji = "あいうえお"
print("あいうえお" + "あいうえお") # -> あいうえおあいうえお

"""　演算子（数字）
+ : 足し算
- : 引き算
* : 掛け算
/ : 割り算
% : mod (あまり)

a == b : a = b -> true, false
a != b : a と bは違う　(Excel: a <> b )
a > b  : aがbよりおおきい -> true, false
a >= b : a = b か a > b -> true, false
a < b  : aはbよりちいさい -> true, false
a <= b : a = b か　a < b -> true, false

and, or:
エクセル
=AND(条件1, 条件2, ...)
条件1,条件2, ... が全部正しい
-> 1個でも間違っていたら アウト

=OR(条件1, 条件2, ...)
条件1,条件2, ... のどれかが正しい
-> 1個でも正しければOK

"""

if 1 + 1 == 2 and 1 + 2 == 2:
    print("本当か？")


""" 演算子（文字）
+ : 連結
* : 繰り返し
"""
moji = "あいうえお" * 3
print(moji)

# エクセルだと...
# =IF(tensuu >= 90, "合格",　IF(tensuu >= 80, "追試", "不合格"))
# if文
tensuu = 90
# 条件1
if tensuu > 90 or tensuu == 90:
    # 条件1が正しいとき
    print('合格')
# 条件2
elif tensuu >= 80:
    # 条件1は正しくないけど条件2は正しい
    print("追試")
elif tensuu >= 70:
    print("残念")
else:
    # それ以外
    print('不合格')

うまい棒 = 10
合計 = 100
明細 = うまい棒 * 11
# 合計 = 100
# 明細 = 110
# 合計 != 明細 -> true
if 合計 != 明細:
    print("あなたは間違っている")
else:
    # 上の条件以外
    print("残念、あなたの方が正しいようだ")

# for文：繰り返し
"""
i を 0 -> 99まで繰り返し
goukei = 0
for i in range(100):
    goukei = goukei + i
print(goukei)
"""
goukei = 0
for i in range(100):
    goukei = goukei + i
print(goukei)

"""
偉い人（ダイクストラ）
順次実行（上から順番に読みます）, 
条件分岐（if文),
ループ（for文:繰り返し）の3つですべてのプログラムは記述できる
"""
