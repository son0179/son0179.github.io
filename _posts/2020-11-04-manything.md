## 연산자

연산을 지시하는 문자

### 연산

계산 : 컴퓨터에서는 모든게 계산으로 이뤄진다.

#### 산술연산

수학적인 계산을 하는 연산자   ex) + - * % //

#### 비교연산

수의 크기나, 같고 다름을 구하는 연산자 Ex) > < == !=

#### 논리연산

논리값(참, 거짓)을 이용하여 계산 하는 연산자

##### and : 두 값이 모두 True일 때만 True

| A\B  | 1    | 0    |
| ---- | ---- | ---- |
| 1    | 1    | 0    |
| 0    | 0    | 0    |



##### or : 두 값이 모두 False일 때만 False


| A\B  | 1    | 0    |
| ---- | ---- | ---- |
| 1    | 1    | 1    |
| 0    | 1    | 0    |


##### not : 단항연산자( Ex] + - 부호), True 를 False 로 , False를 True 로 바꿈

##### xor :  두 값이 같으면 False, 다르면 True

| A\B  | 1    | 0    |
| ---- | ---- | ---- |
| 1    | 0    | 1    |
| 0    | 1    | 0    |

#### 비트연산 : 비트끼리 계산한다.



##### 비트(bit) : 컴퓨터 연산의 가장 작은 단위

칸 하나 (0과 1을 넣을 수 있는 ) -> 2가지 경우 표현 가능



##### 바이트 (byte) : 컴퓨터가 값을 기억하는 가장 작은 단위 , 1byte = 8bit

칸이 8개 -> 2^8(256)의 경우를 표현 가능



##### 컴퓨터에서 수(정수)를 기억하는 방법

###### 기수법

372 : 삼백칠십이 라고 읽는다. 삼 칠 이 가 아니라, 왜????

3 * 100

7 * 10

2 * 1

3 * (10^2)

7 * (10^1)

2 * (10^0)



1101(2) : 뭐라고 읽어야 할까??

1*2^0

1*2^2

1*2^3

13이라고 읽으면 된다.

즉, 13은 컴퓨터 내에서 1101로 저장이 된다.

##### 비트 연산 종류

###### A&B(and) : A와 B의 모든 비트에 대해 and연산한다.

###### A|B(or) : A와 B의 모든 비트에 대해 or연산한다.

###### A^B(xor) : A와 B의 모든 비트에 대해 xor연산한다.



## XOR을 이용한 암호화

##### 왜 XOR일까?

###### and

| A    | B    | A and B |
| ---- | ---- | ------- |
| 1    | 1    | 1       |
| 1    | 0    | 0       |
| 0    | 1    | 0       |
| 0    | 0    | 0       |



값이 절대 커질 수 없다.

###### or

| A    | B    | A orB |
| ---- | ---- | ----- |
| 1    | 1    | 1     |
| 1    | 0    | 1     |
| 0    | 1    | 1     |
| 0    | 0    | 0     |



값이 절대 작아질 수 없다.



추측이 쉽다. (무조건 작은 값 or 큰 값 대입하면 됨)

##### 

###### xor

| A    | B    | A xor B |
| ---- | ---- | ------- |
| 1    | 1    | 0       |
| 1    | 0    | 1       |
| 0    | 1    | 1       |
| 0    | 0    | 0       |



값이 커질 수도 있고 작아질 수도 있다. (상대적으로 원본값 추측이 어렵다.)



###### xor 특성 : 한 값(A)에 다른 값(B)를 두 번 xor하면 원래 값(A)이 나온다.



#### 함수 : 값을 넣으면 특정한(이름에 맞는) 작업을 하고 값을 돌려주는 상자





