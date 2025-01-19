

#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> sequence;
    int num;

    // Read integers until 0 is encountered
    while (cin >> num && num != 0) {
        sequence.push_back(num);
    }

    vector<int> results;

    // Process the sequence in pairs
    for (size_t i = 0; i < sequence.size(); i += 2) {
        if (i + 1 < sequence.size()) {
            results.push_back(sequence[i] * sequence[i + 1]); // Multiply pairs
        } else {
            results.push_back(sequence[i]); 
        }
    }

    // Output the results
    for (size_t i = 0; i < results.size(); i++) {
        cout << results[i];
        if (i < results.size() - 1) cout << " "; // Avoid trailing space
    }
    cout << endl;

    return 0;
}
