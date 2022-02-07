from pydes import encrypt
from matplotlib import pyplot as plt


def countHammingDis(text1, text2):
    # In order to count the hamming distance of the two plaintext
    cnt = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            cnt += 1

    return cnt


def hexToBin(val):
    # return binary valaues of the hex as a list of integer numbers
    return [int(i) for i in str(bin(int(val, 16)))[2:].zfill(64)]


# Test 1 -------------------------------
print("Result of test1 with fixed key but plaintexts having hamming distance of 1")

k1 = '2247BA5687FE09CE'
p1_list = [
    ['AB3456FA7BF07D12', 'AB3456FA79F07D12'],
    ['13BEF5C5C6EFF098', '13BEF5CDC6EFF098'],
    ['BD657AC12CFE89AC', 'BD657AC12CFE8DAC'],
    ['4092BFE671498ACD', '4892BFE671498ACD'],
    ['BBD456CAFE90FE5C', 'BBD456DAFE90FE5C']
]
# Convert Key to binary list and setup plt
k1 = hexToBin(k1)
plt.figure(figsize=(12, 6))
plt.axes().grid()
plt.xlabel('Round Number')
plt.ylabel('Hamming Distances')
plt.xlim((0, 17))
plt.xticks(ticks=[i for i in range(17)])
plt.ylim((0, 64))

for i in range(5):
    _, res1 = encrypt(hexToBin(p1_list[i][0]), k1)
    _, res2 = encrypt(hexToBin(p1_list[i][1]), k1)
    dis = []
    for j in range(17):
        dis.append(countHammingDis(res1[j], res2[j]))

    plt.plot([i for i in range(17)], dis, label="p"+str(i))

plt.legend(loc="upper left")
plt.show()
print("Test1 done")

# Test 2 -------------------------------
print("Result of Test 2 with fixed key but plaintext pairs with different hamming distance")
k2 = 'AB50D0E4F2B89AC5'
p2_list = [
    ['D0C045E34C87A91F', 'D0C04DE34C87A91F'],
    ['ABDE40F0478912CC', 'AB5E40F04789128C'],
    ['9345BDEFACD87129', 'F345BDEFECD87129'],
    ['FFD0AE432C78DE56', 'F0D0AE432C78DE56'],
    ['EED456CA9087073A', 'EED4F6CA9787073A']]

# Convert Key to binary list and setup plt
k2 = hexToBin(k2)
plt.figure(figsize=(12, 6))
plt.axes().grid()
plt.xlabel('Round Number')
plt.ylabel('Hamming Distances')
plt.xlim((0, 17))
plt.xticks(ticks=[i for i in range(17)])
plt.ylim((0, 64))

for i in range(5):
    _, res1 = encrypt(hexToBin(p2_list[i][0]), k2)
    _, res2 = encrypt(hexToBin(p2_list[i][1]), k2)
    dis = []
    for j in range(17):
        dis.append(countHammingDis(res1[j], res2[j]))

    plt.plot([i for i in range(17)], dis, label="HD"+str(i+1))

plt.legend(loc="upper left")
plt.show()
print("Test2 done")

# Test 3 -------------------------------
print("Result of Test 3 with fixed plainText but different key pairs with hamming distance 1")
p3 = 'BAD4560932872F1E'
k3_list = [
    ['BDEF00FA7BFDED12', 'BCEF00FE7BFDED13'],
    ['B12EF5BDE412F098', 'B12FFDBDE412F098'],
    ['FED38AC12CFDE87C', 'FED38AC12CF5E97C'],
    ['98BDACE671498FED', '98BCACE471498FED'],
    ['A05FE3CAFE905DFB', 'A15FE3CAFE9055FB']]

# Convert plainText to binary list and setup plt
p3 = hexToBin(p3)
plt.figure(figsize=(12, 6))
plt.axes().grid()
plt.xlabel('Round Number')
plt.ylabel('Hamming Distances')
plt.xlim((0, 17))
plt.xticks(ticks=[i for i in range(17)])
plt.ylim((0, 64))

for i in range(5):
    _, res1 = encrypt(p3, hexToBin(k3_list[i][0]))
    _, res2 = encrypt(p3, hexToBin(k3_list[i][1]))
    dis = []
    for j in range(17):
        dis.append(countHammingDis(res1[j], res2[j]))

    plt.plot([i for i in range(17)], dis, label="k"+str(i))

plt.legend(loc="upper left")
plt.show()
print("Test3 done")
