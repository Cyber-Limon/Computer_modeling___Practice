def city_swap(solution):
    neighborhood = []
    n = len(solution)

    for i in range(n):
        for j in range(i + 1, n):
            new_solution = solution.copy()
            new_solution[i] = solution[j]
            new_solution[j] = solution[i]
            neighborhood.append(new_solution)

    return neighborhood



def opt2(solution):
    neighborhood = []
    n = len(solution)

    for i in range(n - 2):
        for j in range(i + 2, n - 1):
            new_solution = solution[:i + 1] + solution[i + 1:j + 1][::-1] + solution[j + 1:]
            neighborhood.append(new_solution)

        if i != 0:
            new_solution = solution[:i + 1] + solution[i + 1:n][::-1]
            neighborhood.append(new_solution)

    return neighborhood



def shift(solution):
    neighborhood = []
    n = len(solution)

    for k in range(1, n):
        for i in range(n):
            j = (i + k) % n
            new_solution = solution.copy()
            new_solution.insert(j, new_solution.pop(i))

            if new_solution not in neighborhood:
                neighborhood.append(new_solution)

    return neighborhood



def result(algorithm, solution):
     neighborhood = algorithm(solution)
     for index, solution in enumerate(neighborhood, 1):
         print(index, solution)



def main():
    n = int(input("Введите количество городов: "))

    cities = []
    initial_solution = [i for i in range(n)]

    i = 1
    while i <= n:
        distances = list(map(int, input(f"Введите расстояния от {i} города до остальных: ").split()))

        if len(distances) == n:
            cities.append(distances)
            i += 1
        else:
            print("ОШИБКА: некорректный ввод расстояний")

    print("\nМатрица расстояний:")
    for i in cities:
        print(i)

    print("\nНачальное решение:", initial_solution)



    # Окрестности #

    print("\nCitySwap:")
    result(city_swap, initial_solution)

    print("\n2-opt:")
    result(opt2, initial_solution)

    print("\nСдвиги:")
    result(shift, initial_solution)



main()
