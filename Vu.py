import matplotlib.pyplot as plt

Terminal = True
Graph = True

f = [0.1, 1, 5, 10, 50, 100, 500, 1000]
Ua1 = [12.5, 12.5, 12.5, 12.25, 3.1, 1.8, 0.45, 0.29]
Ua2 = [6, 6, 6, 6, 2, 1.5, 0.4, 0.24]
Ue = 1

Ua_values = [Ua1, Ua2]
Ua_labels = ['Ua1', 'Ua2']

if Terminal:
    for i, Ua in enumerate(Ua_values):
        solution = [Ua[j] / Ue for j in range(len(Ua))]
        print(f"Solution for {Ua_labels[i]}: {solution}")

if Graph:
    plt.figure(figsize=(8, 5))

    for i, Ua in enumerate(Ua_values):
        solution = [Ua[j] / Ue for j in range(len(Ua))]
        plt.plot(f, solution, marker='o' if i == 0 else 's', linestyle='-', label=f'Solution ({Ua_labels[i]})')

    plt.xlabel('f')
    plt.ylabel('Solution')
    plt.title('Graph of Solution vs. f')
    plt.xscale('log')
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.legend()
    plt.show()
