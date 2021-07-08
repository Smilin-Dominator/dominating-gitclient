#include <iostream>
#include <fstream>
using namespace std;

void interface(const string &path) {
    string changedir = "cd ";
    changedir += path;
    system(changedir.c_str());
    cout << system("ls");
}

string configcheck() {
    string path;
    ifstream file;
    file.open("./data.txt", ios::in);
    if (file.is_open()) {
        file >> path;
        file.close();
        return path;
    } else {
        ofstream write ("./data.txt", ios::out);
        cout << "[*] File Not Found... Creating A New One.." << endl;
        cout << "[*] Enter The Absolute Path To The Directory: ";
        cin >> path;
        write << path;
        write.close();
        return path;
    }
}

int main() {
    cout << "\nWelcome To SmilinGitGud, The Git Client Made By Devisha Padmaperuma!\n" << endl;
    string path = configcheck();
    interface(path);
    return 0;
}
