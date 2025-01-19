#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;  
    vector<pair<string, int>> students(N);
    
    for (int i = 0; i < N; ++i) {
        cin >> students[i].first >> students[i].second;
    }
    
   
    sort(students.begin(), students.end(), [](const pair<string, int>& a, const pair<string, int>& b) {
        if (a.first == b.first) {
            return a.second < b.second; 
        }
        return a.first < b.first; 
    });
    
    for (const auto& student : students) {
        cout << student.first << " " << student.second << endl;
    }
    
    return 0;
}
