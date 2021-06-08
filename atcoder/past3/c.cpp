#include <iostream>
#include <stdio.h>

int main()
{

    long a, r, n, ans;

    std::cin >> a >> r >> n;
    ans = a;
    for (int i = 1; i < n; i++)
    {
        ans = ans * r;
        if (ans > 1e9)
        {
            std::cout << "large" << std::endl;
            return 0;
        }
    }
    printf("%ld", ans);
    return 0;
}
