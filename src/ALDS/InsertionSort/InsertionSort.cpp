#include <iostream>
#include <algorithm>

using namespace std;

void insertionSort(int *A, int N)
{
    int v, j;
    int temp;
    for (int i = 1; i < N; i++)
    {
        v = A[i];
        j = i - 1;
        while (j >= 0 && A[j] > v)
        {
            temp = A[j + 1];
            A[j + 1] = A[j];
            A[j] = temp;
            j--;
        }
        A[j + 1] = v;
        for (int k = 0; k < N - 1; k++)
            cout << A[k] << " ";
        cout << A[N - 1] << endl;
    }
}

int main()
{
    int n;
    cin >> n;
    int A[n];

    for (int i = 0; i < n; i++)
        cin >> A[i];

    for (int i = 0; i < n - 1; i++)
        cout << A[i] << " ";
    cout << A[n - 1] << endl;
    insertionSort(A, n);
    return 0;
}
