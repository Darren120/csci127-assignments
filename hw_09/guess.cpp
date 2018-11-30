#include <iostream>
using namespace std;

int main() {
	int num;
	int lower = 0;
	int upper = 99;
	int guess = (lower+upper) / 2;
	int input;
	cout << "please pick a number between 0-99" << endl;
	cin >> num;

	if (num <= lower || num >= upper) {
		main();
	} else {
		cout << "is your number " << guess << " ? "<<endl;
	cout << "-1 to represent that the number is lower than the guess, 1 to represent that the number is higher than the guess and 0 if the number i the guess" << endl;
    cin >> input;
	while (input != 0) {
    if (input == -1) {
      upper = guess;
    }
    else {
      lower = guess;
    }
    guess = (lower + upper)/2;

    cout << "is your number " << guess << "?"<<endl;
    cout<< "-1 to represent that the number is lower than the guess, 1 to represent that the number is higher than the guess and 0 if the number i the guess "<< endl;
    cin >> input;
  }
  cout << "I got it!" << endl;
	}
	

	return 0;
}