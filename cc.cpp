#include <iostream>
using namespace std;

int main() {
    int n; // Number of cards
    cin >> n;
    int arr[n];

    int evens[100], odds[100]; // Arrays to store even and odd numbers
    int even_count = 0, odd_count = 0; // Counters for even and odd numbers

    for (int i = 0; i < n; i++) {
        cin >> arr[n];

        if (arr[n] % 2 == 0) {
            evens[even_count++] = arr[n]; // Store even cards
        } else {
            odds[odd_count++] = arr[n]; // Store odd cards
        }
    }

    // Print all even cards first (Daniil's cards)
    for (int i = 0; i < even_count; i++) {
        cout << evens[i] << " ";
    }

    // Then print all odd cards (Vanya's cards)
    for (int i = 0; i < odd_count; i++) {
        cout << odds[i] << " ";
    }

    cout << endl;

    return 0;
}