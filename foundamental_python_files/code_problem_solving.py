def send_discount(books_purchased, discount_threshold, bonus_threshold):
    if books_purchased >= bonus_threshold:
        print("Big discount applied!")
    elif books_purchased >= discount_threshold:
        print("Discount applied!")    
    else:
        print("No discount.")
    


send_discount(3, 5, 10)   # Should print 'No discount.'
send_discount(7, 5, 10)   # Should print 'Discount applied!'
send_discount(12, 5, 10)


def categorize_ratings(rating_score):
    number_of_low_ratings = 0
    number_of_medium_ratings = 0
    number_of_high_ratings = 0
    for rating in rating_score:
        if rating <= 4:
            number_of_low_ratings += 1
        elif rating <= 7:
            number_of_medium_ratings += 1
        elif rating <= 10:
            number_of_high_ratings += 1

    print(f'Low: {number_of_low_ratings}')
    print(f'Medium: {number_of_medium_ratings}')
    print(f'High: {number_of_high_ratings}')

categorize_ratings([1, 3, 5, 7, 8, 9])

#students = ["John", "Lisa", "Mary", "Chris", "Linda", "Matt"]
students = []

test_performance = {"John": 87, "Lisa": 90, "Mary":75, "Chris": 100, "Linda": 100, "Matt": 70 }

"""scores = []
for student in students:
    if student in test_performance:
        value = test_performance[student]
        scores.append(value)"""

"""def bubble_sort(score):
    n = len(score)
    for i in range(n):
        for j in range(0, n - i - 1):
            if score[j] > score[j + 1]:
                score[j], score[j + 1] = score[j + 1], score[j]
    return score
sort_function = bubble_sort
sorted_scores = sort_function(scores)
print(sorted_scores)

highest_score = max(sorted_scores)
lowest_score = min(sorted_scores)

print(highest_score)
print(lowest_score)"""

"""def average_class_score(sorted_scores):
    try:
        if not students:
            print("Students list is empty")
            return 0
        else:
            try:                
                average_score = sum(sorted_scores)/len(sorted_scores)
                return average_score
            except ValueError:
                print("Error: Sorted scores list is empty")
                return 0
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")
        return None"""

scores = []
def average_class_score(students, scores):
    try:
        if not students:
            print("Error: Student list is empty")
            return
        elif not scores:
            print("Error: Scores list is empty.")
        else:
            try:
                average_score = sum(scores)/len(scores)
                return average_score
            except ValueError:
                print("Error:  Blank values found in either the students or scores list")
                return
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")
        return


#tests for functionality
average_score = average_class_score(students,scores)
print(average_score)