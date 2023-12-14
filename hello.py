#include <stdio.h>
#include <math.h>

// 関数のプロトタイプ宣言
double calculate_mean(int n, int scores[]);
double calculate_std_dev(int n, int scores[], double mean);
void calculate_deviation_values(int n, int scores[], double mean, double std_dev, double deviations[]);
void sort_scores_desc(int n, int scores[], double deviations[]);

int main() {
    // テストの点数データ
    int n = 20;
    int science_scores[] = {65, 80, 67, 35, 58, 60, 72, 75, 68, 92, 36, 50, 25, 85, 46, 42, 78, 62, 84, 70};
    int english_scores[] = {44, 87, 100, 63, 52, 60, 58, 73, 55, 86, 29, 56, 89, 23, 65, 84, 64, 27, 86, 84};

    // 理科の平均点と標準偏差の計算
    double science_mean = calculate_mean(n, science_scores);
    double science_std_dev = calculate_std_dev(n, science_scores, science_mean);

    // 英語の平均点と標準偏差の計算
    double english_mean = calculate_mean(n, english_scores);
    double english_std_dev = calculate_std_dev(n, english_scores, english_mean);

    // 理科と英語のそれぞれの偏差値を計算
    double science_deviations[n];
    double english_deviations[n];
    calculate_deviation_values(n, science_scores, science_mean, science_std_dev, science_deviations);
    calculate_deviation_values(n, english_scores, english_mean, english_std_dev, english_deviations);

    // 点数の高い順に並べ替え
    sort_scores_desc(n, science_scores, science_deviations);
    sort_scores_desc(n, english_scores, english_deviations);

    // 結果の出力
    printf("理科の平均点: %.2f\n", science_mean);
    printf("理科の標準偏差: %.2f\n", science_std_dev);
    printf("理科の合計点: %.2f\n", calculate_mean(n, science_scores));

    printf("\n英語の平均点: %.2f\n", english_mean);
    printf("英語の標準偏差: %.2f\n", english_std_dev);
    printf("英語の合計点: %.2f\n", calculate_mean(n, english_scores));

    printf("\n理科の偏差値:\n");
    for (int i = 0; i < n; i++) {
        printf("%.2f ", science_deviations[i]);
    }

    printf("\n\n英語の偏差値:\n");
    for (int i = 0; i < n; i++) {
        printf("%.2f ", english_deviations[i]);
    }

    printf("\n\n理科の点数（高い順）:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", science_scores[i]);
    }

    printf("\n\n英語の点数（高い順）:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", english_scores[i]);
    }

    return 0;
}

// 平均点の計算
double calculate_mean(int n, int scores[]) {
    double sum = 0;
    for (int i = 0; i < n; i++) {
        sum += scores[i];
    }
    return sum / n;
}

// 標準偏差の計算
double calculate_std_dev(int n, int scores[], double mean) {
    double sum_squared_diff = 0;
    for (int i = 0; i < n; i++) {
        double diff = scores[i] - mean;
        sum_squared_diff += diff * diff;
    }
    return sqrt(sum_squared_diff / n);
}

// 偏差値の計算
void calculate_deviation_values(int n, int scores[], double mean, double std_dev, double deviations[]) {
    for (int i = 0; i < n; i++) {
        deviations[i] = 10 * (scores[i] - mean) / std_dev + 50;
    }
}

// 点数を高い順に並べ替え
void sort_scores_desc(int n, int scores[], double deviations[]) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (deviations[i] < deviations[j]) {
                // 偏差値で並べ替える
                double temp_deviation = deviations[i];
                deviations[i] = deviations[j];
                deviations[j] = temp_deviation;

                // 対応する点数も並べ替える
                int temp_score = scores[i];
                scores[i] = scores[j];
                scores[j] = temp_score;
            }
        }
    }
}

