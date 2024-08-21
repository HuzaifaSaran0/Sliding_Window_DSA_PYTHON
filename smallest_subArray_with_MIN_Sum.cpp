// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
#include <climits>
#include <cmath>
int windStart = 0;
int currentWindSum = 0;
int minWindSum = INT_MAX;

int smallest(int arr[10],int size, int target){
    for (int windEnd = 0; windEnd < size; windEnd++){
        currentWindSum += arr[windEnd];
        while(currentWindSum >= target){
            minWindSum = min(minWindSum, windEnd - windStart + 1);
            /* windEnd - windStart + 1 
                This is To Get the size of current Window
            */
            currentWindSum -= arr[windStart]; 
              /* currentWindSum -= arr[windStart]; 
                This is To Shrink the Current Window from Left 
            */
            windStart++; // THis is to move the WindStart one step // Next
        }
    }
    //cout<<currentWindSum;
    return minWindSum;
}
int main() {
    int arr[10] = {3,2,5,6,7,8,3,6,7,3};
    cout<<smallest(arr, 10, 8);

    return 0;
}
