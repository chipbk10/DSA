int findGCD(int m, int n) {
  int a = Math.abs(m);
  int b = Math.abs(n);

  if (a == 0 && b == 0) return 1;
  
  while (b != 0) {
    int temp = b;
    b = a%b;
    a = temp;
  }
  
  return a;
}
