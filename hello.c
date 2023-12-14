#include <stdio.h>
#include <math.h>

// 関数のプロトタイプ宣言
void calculateStatistics(int scores[], int size, double *average, double *stdDev, int *total);
void calculateZScores(int scores[], int size, double average, double stdDev, double zScores[]);
void sortScores(int scores[], double zScores[], int size);

int main() {
    // テストの点数データ
    int scienceScores[] = {65, 80, 67, 35, 58, 60, 72, 75, 68, 92, 36, 50, 25, 85, 46, 42, 78, 62, 84, 70};
    int englishScores[] = {44, 87, 100, 63, 52, 60, 58, 73, 55, 86, 29, 56, 89, 23, 65, 84, 64, 27, 86, 84};
    int size = sizeof(scienceScores) / sizeof(scienceScores[0]);

    // 理科の統計情報
    double scienceAverage, scienceStdDev;
    int scienceTotal;
    calculateStatistics(scienceScores, size, &scienceAverage, &scienceStdDev, &scienceTotal);

    // 英語の統計情報
    double englishAverage, englishStdDev;
    int englishTotal;
    calculateStatistics(englishScores, size, &englishAverage, &englishStdDev, &englishTotal);

    // 理科と英語の偏差値
    double scienceZScores[size], englishZScores[size];
    calculateZScores(scienceScores, size, scienceAverage, scienceStdDev, scienceZScores);
    calculateZScores(englishScores, size, englishAverage, englishStdDev, englishZScores);

    // 点数の高い順にソート
    sortScores(scienceScores, scienceZScores, size);
    sortScores(englishScores, englishZScores, size);

    // 結果の表示
    printf("理科の平均点: %.2f\n", scienceAverage);
    printf("理科の標準偏差: %.2f\n", scienceStdDev);
    printf("理科の合計点: %d\n", scienceTotal);

    printf("\n英語の平均点: %.2f\n", englishAverage);
    printf("英語の標準偏差: %.2f\n", englishStdDev);
    printf("英語の合計点: %d\n", englishTotal);

    printf("\n理科の点数（高い順）と偏差値:\n");
    for (int i = 0; i < size; i++) {
        printf("%d : %.2f\n", scienceScores[i], scienceZScores[i]);
    }

    printf("\n英語の点数（高い順）と偏差値:\n");
    for (int i = 0; i < size; i++) {
        printf("%d : %.2f\n", englishScores[i], englishZScores[i]);
    }

    return 0;
}

// 統計情報を計算する関数
void calculateStatistics(int scores[], int size, double *average, double *stdDev, int *total) {
    *total = 0;
    for (int i = 0; i < size; i++) {
        *total += scores[i];
    }

    *average = (double)*total / size;

    double sumSquares = 0.0;
    for (int i = 0; i < size; i++) {
        sumSquares += pow(scores[i] - *average, 2);
    }

    *stdDev = sqrt(sumSquares / size);
}

// 偏差値を計算する関数
void calculateZScores(int scores[], int size, double average, double stdDev, double zScores[]) {
    for (int i = 0; i < size; i++) {
        zScores[i] = ((double)scores[i] - average) / stdDev * 10 + 50;
    }
}

// 配列をソートする関数
void sortScores(int scores[], double zScores[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = i + 1; j < size; j++) {
            if (zScores[i] < zScores[j]) {
                // 偏差値が高い順に入れ替え
                double tempZScore = zScores[i];
                zScores[i] = zScores[j];
                zScores[j] = tempZScore;

                // 対応する点数も入れ替え
                int tempScore = scores[i];
                scores[i] = scores[j];
                scores[j] = tempScore;
            }
        }
    }
}

