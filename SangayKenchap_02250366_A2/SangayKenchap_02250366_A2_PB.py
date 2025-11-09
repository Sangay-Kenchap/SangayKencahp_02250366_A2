# Practical Assignment 2 - Part B
# Sorting Algorithms Implementation
# Author: Sangay Kenchap
# Student Number: 02250366

def bubble_sort(names):
    """Bubble Sort Algorithm"""
    n = len(names)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if names[j] > names[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]
    return names


def insertion_sort(scores):
    """Insertion Sort Algorithm"""
    for i in range(1, len(scores)):
        key = scores[i]
        j = i - 1
        while j >= 0 and scores[j] > key:
            scores[j + 1] = scores[j]
            j -= 1
        scores[j + 1] = key
    return scores


def quick_sort(prices, low, high, calls):
    """Quick Sort Algorithm"""
    if low < high:
        pivot_index = partition(prices, low, high)
        calls[0] += 1
        quick_sort(prices, low, pivot_index - 1, calls)
        quick_sort(prices, pivot_index + 1, high, calls)
    return prices


def partition(prices, low, high):
    pivot = prices[high]
    i = low - 1
    for j in range(low, high):
        if prices[j] <= pivot:
            i += 1
            prices[i], prices[j] = prices[j], prices[i]
    prices[i + 1], prices[high] = prices[high], prices[i + 1]
    return i + 1


def main():
    student_names = ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Deki", "Choki",
                     "Sonam", "Pema", "Karma", "Ugyen", "Tashi", "Yeshi", "Thinley", "Dorji"]

    test_scores = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59, 76, 85, 48, 93, 71, 89, 57, 80, 69, 62]

    book_prices = [450, 230, 678, 125, 890, 350, 720, 510, 400, 999, 275, 480, 320, 600, 150]

    while True:
        print("\n=== Sorting Algorithms Menu ===")
        print("1. Bubble Sort - Sort Student Names")
        print("2. Insertion Sort - Sort Test Scores")
        print("3. Quick Sort - Sort Book Prices")
        print("4. Exit program")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Original: {student_names}")
            sorted_names = bubble_sort(student_names.copy())
            print(f"Sorted: {sorted_names}")

        elif choice == '2':
            print(f"Original scores: {test_scores}")
            print("Performing Insertion Sort...")
            sorted_scores = insertion_sort(test_scores.copy())
            print(f"Sorted scores: {sorted_scores}")
            print("Top 5 Scores:")
            for i, score in enumerate(sorted_scores[-1:-6:-1], start=1):
                print(f"{i}. {score}")

        elif choice == '3':
            print(f"Original prices: {book_prices}")
            calls = [0]
            sorted_prices = quick_sort(book_prices.copy(), 0, len(book_prices) - 1, calls)
            print(f"Sorted prices: {sorted_prices}")
            print(f"Recursive calls: {calls[0]}")

        elif choice == '4':
            print("Thank you for using the sorting program!")
            break
        else:
            print("Invalid choice. Please select 1–4.")

        cont = input("Would you like to perform another sort? (y/n): ")
        if cont.lower() != 'y':
            print("Thank you for using the sorting program!")
            break


if __name__ == "__main__":
    main()
