import pyautogui as pg
import time

print("Typing will start in 3 seconds...")
time.sleep(3)

text_to_write = '''
import java.util.Scanner;

class FibonacciCalculator {
static int calculateFibonacci(int n) {
if (n == 0) return 0;
if (n == 1) return 1;
int a = 0, b = 1, c = 0;
for (int i = 2; i <= n; i++) {
c = a + b;
a = b;
b = c;
}
return b;
}

static String checkEvenOddAndSumDigits(int num) {
String type = (num % 2 == 0) ? "Even" : "Odd";
int sum = 0;
int temp = num;
while (temp > 0) {
sum += temp % 10;
temp /= 10;
}
return type + ", Digit Sum: " + sum;
}
}

'''

pg.write(text_to_write, interval=0.03)