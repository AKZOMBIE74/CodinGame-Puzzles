//I created this solution 2nd for this puzzle, after I made the Java one.
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

//My method for making debugging easier
void error(string s){
	cerr << s << endl;
}

//My method to make printing stuff easier
void print(string s){
	cout << s << endl;
}

/*My method for splitting the integers from a string with a space as the delimiter */
vector<int> splitString(string line){
	vector<int> splitted;
	string i="";
	
	if (line.size()>0){
		for (int j=0; j<line.size(); j++){
			if (line[j]!=' '){
				i+=line[j];
				if (j==line.size()-1){
				    splitted.push_back(atoi(i.c_str()));
				}
			} else {
				splitted.push_back(atoi(i.c_str()));
				i="";
			}
		}
	}
	return splitted;
}

/*Returns solution of a given line of the conway sequence*/
string getSolutionOfLine(vector<int> line){
	int count = 0;//Default value
	int numberOn=-1;//Default value
	string solution="";//Solution to each line
	for (int i=0; i<line.size(); i++) {//Loop through each integer of line
		if (numberOn==-1 || numberOn!=line[i]) {//Are we on the current number that is going through the loop?, if not...
			numberOn = line[i];//Put us on that number
			count = 0;//Set count to 0
		}
		if (numberOn==line[i]){//Is the number we are on equal to the number the loop is on?
			count+=1;//If so add 1 to count.
			string countString = to_string(count);//Convert count from int to string.
			string numberOnString = to_string(numberOn);//Convert numberOn from int to string.
			if (i==line.size()-1){//Is the loop on the last number on the line?
				string baseString = countString+" "+numberOnString;//Make base solution
				solution = solution.compare("")==0? baseString : solution+" "+baseString;//If solution is not empty, add space, else don't.
			} else if(line[i+1]!=numberOn){//Is the next integer on the line the same as the current number? If not...
				string baseString = countString+" "+numberOnString;//Make base solution
				solution = solution.compare("")==0? baseString : solution+" "+baseString;//If solution is not empty, add space, else don't.
			}
		} else {//If the number we are on is not equal to the current number in the loop, then...
			string countString = to_string(count);//Convert count from int to string.
			string numberOnString = to_string(numberOn);//Conver numberOn from int to string.
			string baseString = solution+countString+" "+numberOnString;//Make base solution
			solution = solution.compare("")==0? baseString : " "+baseString;//If solution is not empty, add space, else don't.
			count=0;//Set count to 0
			numberOn=line[i];//Put us on the new number.
		}
	}
	return solution;//Give us back the solution.
}

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
int main()
{
	int R;
    cin >> R; cin.ignore();
	int L;
    cin >> L; cin.ignore();
    
	string currentSolution = to_string(R);//This is always the first line of the sequence.
	int count = 0;//Default value
    
    
    while (count!=L-1) {//Are we on the line that the puzzle wants us to print? If not...
		string stringOnLine = currentSolution;//Get our input
		vector<int> splitted = splitString(stringOnLine);//Split the integer from the input
		string sol = getSolutionOfLine(splitted);//Get the solution
		currentSolution = sol;//Change our current solution to the one given
		count+=1;//Get ready for a new line.
	}
    
    print(currentSolution);//Print solution.
}
