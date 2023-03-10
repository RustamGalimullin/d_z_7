#Задача 1

import numpy as np
import scipy.stats as stats
x1 = np.array([380, 420, 290])
y1 = np.array([140, 360, 200, 900])

stats.mannwhitneyu(x1, y1)

"MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286)"
"pvalue > alpha, H0 - не отвергается с ошибкой alpha = 0.05, выборки статистически одинаковые"


#Задача 2

x1 = np.array([150, 160, 165, 145, 155])
x2 = np.array([140, 155, 150, 130, 135])
x3 = np.array([130, 130, 120, 130, 125])

stats.friedmanchisquare(x1, x2, x3)

"FriedmanchisquareResult(statistic=9.578947368421062, pvalue=0.00831683351100441)"

"Ответ: pvalue < alpha, H0 - отвергается с ошибкой alpha = 0.05, принимается гипотиза Н1 - различия есть."
"Препарат работает."


#задача 3

x1 = np.array([150, 160, 165, 145, 155])
x2 = np.array([140, 155, 150, 130, 135])

stats.wilcoxon(x1, x2)

"WilcoxonResult(statistic=0.0, pvalue=0.0625)"

"Ответ =: Cтатистически значимых различий не обнаружено на уровне значимости alpha = 0.05."
"Препарат не работает."


#задача 4

x1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
x2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
x3 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

stats.kruskal(x1, x2, x3)
"KruskalResult(statistic=5.465564058257224, pvalue=0.0650380998590494)"

"Ответ: pvalue > alpha, H0 - не отвергается с ошибкой alpha = 0.05, различий нет, группы статистически равны"

#задача 5

X = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])

mean = X.mean()
std = X.std(ddof=1)

t_fact = (mean - 2.5) / std * np.sqrt(len(X))
t_fact

"0.563061366180296"

#По таблице для критерия Стьюдента находим t = 1.833 (для = 0.05 и 9 степенями свободы).
#Так как t > t_fact (1.833 > 0.56), то гипотеза верна и изделия соответствуют заявленному размеру.

n = 10
m = 2.5

t = stats.t.ppf(0.975, 9)
print(f"t теор = {t:.2f}")

t = (mean - m) * np.sqrt(n) / std
print(f"t рассч = {t:.3f}")

"t теор = 2.26"
"t рассч = 0.563"

#так как t теор > t рассч, считаем что нулевая гипотеза верна

