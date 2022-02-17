#include <iostream>
#include <ctime>
#include <Windows.h>
#include <iomanip>

using namespace std;

void initializeMatrix(float **matrix, int, int);
float getTheLastPositiveNumber(float **matrix, int, int, int *ROW, int *COL);
int getTheNumberOfElementsMoreThanX(float **matrix, int, int, float);
void display(float **matrix, int, int, float, int, int, int);
float getRandomFloatNumber();
int main() {

    srand(time(NULL));
    SetConsoleCP(CP_UTF8);
    SetConsoleOutputCP(CP_UTF8);

    int ROWS, COLS, x = 0, y = 0, counterMoreThanX;
    float X;

    cout << "Write a number of rows:";
    cin >> ROWS;
    cout << "Write a number of columns:";
    cin >> COLS;
    cout << endl;

    if(ROWS > 1 && COLS > 1) {
        float** matrix = new float *[ROWS];
        for (int i = 0; i < ROWS; i++) {
            matrix[i] = new float[COLS];
        }
        initializeMatrix(matrix, ROWS, COLS);
        X = getTheLastPositiveNumber(matrix, ROWS, COLS, &x, &y);
        counterMoreThanX = getTheNumberOfElementsMoreThanX(matrix, ROWS, COLS, X);
        display(matrix, ROWS, COLS, X, x, y, counterMoreThanX);

        for (int i = 0; i < ROWS; i++) {
            delete[] matrix[i];
        }
        delete[] matrix;
    }else{
        cout << "Invalid input data";
    }
}

float getRandomFloatNumber(){
    float random = rand() % 10000;
    int sign = 1 + rand() % 2;
    if(sign > 1){
        random = (random * -1) / 100;
    }
    else{
        random = random / 100;
    }
    return random;
}

void initializeMatrix(float **matrix, int ROWS, int COLS){
    for(int i = 0; i < ROWS; i++){
        for(int j = 0; j < COLS; j++){
            float random = getRandomFloatNumber();
            matrix[i][j] = random;
        }
    }
}

float getTheLastPositiveNumber(float **matrix, int ROWS, int COLS, int *ROW, int *COL){
    float temp = 0;
    for(int i = 0; i < COLS; i++){
        for(int j = 0; j < ROWS; j++){
            if(matrix[j][i] > 0){
                temp = matrix[j][i];
                (*ROW) = (j + 1);
                (*COL) = (i + 1);
            }
        }
    }
    return temp;
}

int getTheNumberOfElementsMoreThanX(float **matrix, int ROWS, int COLS, float X){
    int x = -1, y = 0, counter = 0, counterMoreThanX = 0;
    while(y != ROWS && y != COLS - 1){
        x++;
        if(x == COLS - 1 - counter){
            y++;
            x = -1;
            counter++;
        }
        else if (matrix[y][x] > X){
            counterMoreThanX++;
        }
    }
    return counterMoreThanX;
}

void display(float **matrix, int ROWS, int COLS, float X, int x, int y, int moreThanX){

    for(int i = 0; i < ROWS; i++){
        for(int j = 0; j < COLS; j++){
            cout << matrix[i][j] << "\t" ;
        }
        cout << "\n";
    }
    cout << endl;
    cout << "The last positive number is " << X << endl;
    cout << X << " has position: " << "[" << x << ", " << y << "]" << endl;
    cout << "The number of elements more than " << X << ": "<< moreThanX;
}
