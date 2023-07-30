
max_weight = 20

elements_amout = int(input("Podaj liczbę elementów: "))
elements: list[float] = []


while len(elements) < elements_amout:

    new_element: str = (input("Podaj wagę elementu: "))
    if new_element.replace(".", "").isdigit():
        element: float = float(new_element)

        if 1 < element <= 10:
            elements.append(element)
        else:
            print("Element jest niewymiarowy, maksymalnie może mieć 10kg")
    else:
        print("Musi być podada liczba! (masa elementu)")


sum_of_elements = sum(elements)

package_amout = 0
packages: list[list[float]] = []
new_package: list[float] = []
biggest_package = []
biggest_package_index = 0

for element in elements:

    if sum(new_package) + element <= max_weight:
        new_package.append(element)

    else:
        packages.append(new_package)
        if sum(biggest_package) < sum(new_package):
            biggest_package = new_package
            biggest_package_index = len(packages) - 1

        new_package = []
        new_package.append(element)


if len(new_package) > 0:
    packages.append(new_package)


print("elementy: ", ", ".join([str(weight) for weight in elements]))
print(
    f"{biggest_package_index=:}, {biggest_package=:}, suma: {sum(biggest_package)}"
    )
print("Ilośc wysłanych paczek", len(packages))
print("suma pustych kilogramów: ", len(packages)*20 - sum(elements))