#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int max = -200000000;
    int min;
    int buf, diff;
    cin >> min;
    for (int i = 1; i < n; i++)
    {
        cin >> buf;
        diff = buf - min;
        if (diff > max)
        {
            max = diff;
        }

        if (buf < min)
        {
            min = buf;
        }
    }
    cout << max << endl;
    return 0;
}
