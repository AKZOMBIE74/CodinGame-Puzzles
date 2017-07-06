#include <iostream>
#include <string>
#include <vector>

using namespace std;

void error(string s){
    cerr << s << endl;
}
void print(string s){
    cout << s << endl;
}
/**
 * Don't let the machines win. You are humanity's last hope...
 **/
int main()
{
    int width; // the number of cells on the X axis
    cin >> width; cin.ignore();
    int height; // the number of cells on the Y axis
    cin >> height; cin.ignore();
    
    vector<string> grid;
    vector<string> row;
    int count;
    
    for (int i = 0; i < height; i++) {
        string line; // width characters, each either 0 or .
        getline(cin, line);
        grid.push_back(line);
    }
    vector<vector<string>> nodes;
    
    for (int y = 0; y<grid.size(); y++){
        count = 0;
        row.clear();
        for (char &c : grid[y]){
            if (c=='.'){
                row.push_back(".");
                count++;
                continue;
            }
            row.push_back(to_string(count)+" "+to_string(y));
            count++;
        }
        nodes.push_back(row);
    }

    // Three coordinates: a node, its right neighbor, its bottom neighbor
    for (int y=0; y<nodes.size(); y++){
        vector<string> line = nodes[y];
        for (int x=0; x<line.size(); x++){
            string node=line[x];
            if (node.compare(".")!=0) {
                string solution = to_string(x)+" "+to_string(y);
                int xcounter = 0;
                int ycounter = 0;
                
                while (nodes[y].size()-1>x+xcounter && (nodes[y][x+xcounter].compare(".")==0 
                || nodes[y][x+xcounter].compare(node)==0) ){
                    xcounter++;
                }
                xcounter = nodes[y][x+xcounter].compare(".")==0? 0 : xcounter;
                if (xcounter==0){
                    solution+=" -1 -1";
                } else {
                    solution+=" "+string(1,nodes[y][x+xcounter][0])+" "+string(1,nodes[y][x+xcounter][2]);
                }
                
                while (nodes.size()-1>y+ycounter && (nodes[y+ycounter][x].compare(".")==0 || nodes[y+ycounter][x].compare(node)==0)){
                    ycounter++;
                }
                ycounter = nodes[y+ycounter][x].compare(".")==0? 0:ycounter;
                if (ycounter==0){
                    solution+=" -1 -1";
                } else {
                    solution+=" "+string(1,nodes[y+ycounter][x][0])+" "+string(1,nodes[y+ycounter][x][2]);
                }
                print(solution);
            }
        }
    }
}
