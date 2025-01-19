#include<unordered_map>
#include<map>
#include<set>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
    int number_of_students;
    cin>>number_of_students;
    float total = 0;
    unordered_map<string, float> student_score;
    for(int i = 0; i < number_of_students; i++){
        string student_name;
        float score;
        cin>>student_name>>score;
        total += score;
        if(student_score.count(student_name)) {
            student_score[student_name] += score;
        }
        else { 
            student_score.insert({student_name, score});
        }
    vector<pair<float, string>> answer;
    for(const auto&[name, score] : student_score){
        pair<float, string> student;
        student.first = score;
        student.second = name;
        answer.push_back(student);
    }
    sort(answer.begin(), answer.end());
    for(int i = answer.size() - 1; i >= 0; i--){
        cout<<answer[i].second<<" "<<(answer[i].first * 100 /total)<<"%"<<endl;
    }
}
