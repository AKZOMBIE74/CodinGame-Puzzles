//I created this solution first for this puzzle.
import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    //My method for making debugging easier
    public static void error(String s){
        System.err.println(s);
    }
    
    //My method to make printing stuff easier
    public static void print(String s){
        System.out.println(s);
    }
    
    /*My method for splitting the integers from a string with a space as the delimiter */
    public static int[] splits(String line){
        String[] s = line.split(" ");
        int[] p = new int[s.length];
        if (s.length>0){
            for (int i=0; i<s.length; i++){
                if (s[i]!=""){
                    int x = Integer.parseInt(s[i]);
                    p[i]=x;
                }
            }
        }
        return p;
    }
    
    /*Returns solution of a given line of the conway sequence*/
    public static String getSolutionOfLine(int[] line){
        int count = 0;//Default value
        int numberOn=-1;//Default value
        String solution="";//Solution to each line
        for (int i=0; i<line.length; i++) {//Loop through each integer of line
            if (numberOn==-1 || numberOn!=line[i]) {//Are we on the current number that is going through the loop?, if not...
                numberOn = line[i];//Put us on that number
            }
            if (numberOn==line[i]){//Is the number we are on equal to the current number?
                count+=1;//If so add 1 to count.
                if (i==line.length-1){//Is the loop on the last number on the line?
                    String baseString = solution+String.valueOf(count)+" "+String.valueOf(numberOn);//Make base solution
                    solution = baseString;//Set solution to baseString
                } else if(line[i+1]!=numberOn){//Is the next integer on the line the same as the current number? If not...
                    String baseString = solution+String.valueOf(count)+" "+String.valueOf(numberOn);//Make base solution
                    solution = baseString+" ";//Add space to baseString and set solution to that
                    count=0;//Set count to 0
                }
            } else {//If the number we are on is not equal to the current number in the loop, then...
                String baseString = solution+String.valueOf(count)+" "+String.valueOf(numberOn);//Make base solution
                solution = solution==""? baseString : " "+baseString;//If solution is not empty, add space, else don't.
                count=0;//Set count to 0
                numberOn=line[i];//We are on a new number
            }
        }
        return solution;
    }

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int R = in.nextInt();
        int L = in.nextInt();
        String currentSolution=String.valueOf(R);//This is always the first line of the sequence.
        int count = 0;//Default value

        while (count!=L-1){//Are we on the line that the puzzle wants us to print? If not...
            String stringOnLine = currentSolution;//Get our input
            int[] splitted = splits(stringOnLine);//Split the integer from the input
            String sol = getSolutionOfLine(splitted);//Get the solution
            currentSolution = sol;//Change our current solution to the one given
            count+=1;//Get ready for a new line.
        }

        print(currentSolution);//Print solution.
    }
}
