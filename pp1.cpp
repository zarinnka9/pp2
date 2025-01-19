#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

int main() {
    string text;
    getline(cin, text); // Read the entire line of input
    
    map<string, int> wordCount;
    string word;
    
    // Iterate through the input string
    for (char c : text) {
        if (isalpha(c)) { // Only accumulate alphabetic characters
            word += tolower(c); // Convert characters to lowercase
        } else if (!word.empty()) { // If we encounter a non-alphabetic character and have a word
            wordCount[word]++; // Count the word
            word.clear(); // Clear word to start collecting the next word
        }
    }
    
    // If there's any remaining word at the end of the string, count it
    if (!word.empty()) {
        wordCount[word]++;
    }
    
    // Create a vector of pairs to store the word and its count
    vector<pair<string, int>> wordList(wordCount.begin(), wordCount.end());
    
    // Sort the vector first by count (in descending order), 
    // then lexicographically by word (in ascending order)
    sort(wordList.begin(), wordList.end(), [](const pair<string, int>& a, const pair<string, int>& b) {
        if (a.second == b.second) {
            return a.first < b.first; // If counts are equal, sort lexicographically
        }
        return a.second > b.second; // Otherwise, sort by count in descending order
    });
    
    // Print the sorted word counts in the desired format
    for (const auto& entry : wordList) {
        cout << entry.first << " : " << entry.second << endl;
    }
    
    return 0;
}
