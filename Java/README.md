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
