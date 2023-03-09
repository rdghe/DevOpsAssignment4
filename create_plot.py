import matplotlib.pyplot as plt


instances = [1, 2, 4, 8]
req_per_sec = [930, 1006, 980, 990]
plt.bar(instances, req_per_sec)
plt.ylabel('Req/Sec');
plt.xlabel('Number of instance');
# plt.show()

plt.savefig('./plot.png')

