## Random
```java
import java.util.Random;
Random rand = new Random();
int n = 1000;
rand.randInt(n); // choose a random integer in range (0,n-1)
```

## Map
```java
Map<String, Integer> map = new HashMap<>();
for (Map.Entry<String, Integer> entry: map.entrySet()) {
  System.out.println("key = " + entry.getKey() + " value = " + entry.getValue());
}

for (String key: map.keySet()) {
  System.out.println("key = " + key + " value = " + map.get(key));
}
```

## String
```java
int x = 3;
String s = String.valueOf(x);
```

## StringBuilder
```java
StringBuilder sb = new StringBuilder()
sb.append('a') // O(1)
sb.setLength(sb.length() - 1); // O(1)
```

## Others
- **@Todo**: how to represent a negative number?
  - The most significant bit (bit 31) is the sign bit: 0 for non-negative numbers, 1 for negative numbers.
  - Negative numbers are represented by inverting the bits of the positive number and adding 1 (two's complement).
- **Bit Manipulation**: **@Todo**
  - XOR (^) 2 same numbers will be 0

