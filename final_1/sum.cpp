#include <iostream>
using namespace std;
#include <math.h>

int sumofsquares(int a, int b) {
  int sum = 0;
  int i;
  for (i = a; i <= b; i++) {
  	int squared;
    squared = i * i;
    sum = sum + squared;
  }
  return sum;
}


int main() {
	cout << sumofsquares(2, 10) << endl;
  return 0;
}