#include <bits/stdc++.h>
using namespace std;
void printSolution(vector<vector<int>> &board, int N)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}
bool isSafe(vector<vector<int>> &board, int row, int col, int N)
{
    int i, j;
    for (i = 0; i < col; i++)
    {
        if (board[row][i])
            return false;
    }
    for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;

    for (i = row, j = col; j >= 0 && i < N; i++, j--)
        if (board[i][j])
            return false;
    return true;
}
bool solveNQUtil(vector<vector<int>> &board, int col, int N)
{
    if (col >= N)
        return true;
    for (int i = 0; i < N; i++)
    {
        if (isSafe(board, i, col, N))
        {
            board[i][col] = 1;
            if (solveNQUtil(board, col + 1, N))
                return true;
            board[i][col] = 0; // BACKTRACK
        }
    }
    return false;
}
bool solveNQ(vector<vector<int>> &board, int N)
{
    if (solveNQUtil(board, 0, N) == false)
    {
        return false;
    }
    return true;
}
int main()
{
    cout << "Enter Number of size of chess : " << endl;
    int N;
    cin >> N;
    vector<vector<int>> board(N, vector<int>(N, 0));
    cout << "The Solution for N-Queen Problem is " << endl;
    if (solveNQ(board, N))
    {
        printSolution(board, N);
    }
    else{
        cout<<"Solution doesn't exist."<<endl;
    }
    return 0;
}