
import os
f = open("report.txt", "w")

directory = os.getcwd()
files = os.listdir(directory)
new_arr = {os.path.getmtime(x) : x for x in files if x[-3:] == 'log'}


sort = (sorted(new_arr))

t = sort[0] - 404
t2 = 0
sum = 0
for value in sort:
    line = (str(t2+1) + ") Файл \t%-60s выполнялся примерно %.6s %-6s или %.6s минут. Итого - %.6s минут\n" % (str(new_arr[value]), str((value - t)), 'секунд', str(((value - t)/60)), str((sum + (value - t))/60)))
    f.writelines(line)
    sum += (value - t)
    t = value
    t2 += 1

f.writelines("\n Суммарное значение - %.9s сеукнд или примерно %.6s минут (%.3s часов)" % (str((sum)), str((sum/60)), str((sum/3600))))