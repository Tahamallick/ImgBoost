import matplotlib.pyplot as plt

# Data from the output
methods = ['Sequential', 'Parallel']
times = [1008, 480]
plt.figure(figsize=(8, 5))
plt.bar(methods, times, color=['blue', 'green'])
plt.title('Performance Comparison of Augmentation Methods')
plt.ylabel('Time Taken (seconds)')
plt.xlabel('Methods')

for i, time in enumerate(times):
    plt.text(i, time + 10, f"{time:.1f}s", ha='center', fontsize=12)

plt.savefig('performance_comparison.png')
plt.show()
