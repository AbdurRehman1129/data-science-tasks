#include <iostream>
#include <vector>
#include <numeric>
#include <chrono>

int sumWithLoop(const std::vector<int> &array)
{
    int sum = 0;
    for (int val : array)
    {
        sum += val;
    }
    return sum;
}

int sumWithAccumulate(const std::vector<int> &array)
{
    return std::accumulate(array.begin(), array.end(), 0);
}

int main()
{
    std::vector<int> smallArray(100, 1);
    std::vector<int> largeArray(1000, 1);

    auto start1 = std::chrono::high_resolution_clock::now();
    int loopSumSmall = sumWithLoop(smallArray);
    auto end1 = std::chrono::high_resolution_clock::now();

    auto start2 = std::chrono::high_resolution_clock::now();
    int loopSumLarge = sumWithLoop(largeArray);
    auto end2 = std::chrono::high_resolution_clock::now();

    auto start3 = std::chrono::high_resolution_clock::now();
    int accumulateSumSmall = sumWithAccumulate(smallArray);
    auto end3 = std::chrono::high_resolution_clock::now();

    auto start4 = std::chrono::high_resolution_clock::now();
    int accumulateSumLarge = sumWithAccumulate(largeArray);
    auto end4 = std::chrono::high_resolution_clock::now();

    auto duration1 = std::chrono::duration_cast<std::chrono::microseconds>(end1 - start1).count();
    auto duration2 = std::chrono::duration_cast<std::chrono::microseconds>(end2 - start2).count();
    auto duration3 = std::chrono::duration_cast<std::chrono::microseconds>(end3 - start3).count();
    auto duration4 = std::chrono::duration_cast<std::chrono::microseconds>(end4 - start4).count();

    std::cout << "Small array (loop): Sum = " << loopSumSmall << ", Time = " << duration1 << " microseconds\n";
    std::cout << "Large array (loop): Sum = " << loopSumLarge << ", Time = " << duration2 << " microseconds\n";
    std::cout << "Small array (accumulate): Sum = " << accumulateSumSmall << ", Time = " << duration3 << " microseconds\n";
    std::cout << "Large array (accumulate): Sum = " << accumulateSumLarge << ", Time = " << duration4 << " microseconds\n";

    return 0;
}
