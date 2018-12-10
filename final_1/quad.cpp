#include <iostream>
using namespace std;
#include <math.h>
int discriminant(int a, int b, int c) {
  return ((b * b) - (4 * a * c));
}

double quadsolve(int a, int b, int c) {
  int dis = discriminant(a, b, c);
  if (dis >= 0) {
    double ans = (-b + sqrt(dis)) / (2 * a);
    return ans;
  }
  else {
    return 0;
  }
}
 	
 int main() {
 	double a = quadsolve(2.0,10.0,10.0);
 	cout << a;
 	return 0;
 }