def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine

if __name__ == "__main__":
    book_title = "Atomic Habits"
    days_overdue = 40
    daily_rate = 5.0
    max_fine = 200.0   # Custom maximum fine cap
    fine_amount = calculate_fine(book_title, days_overdue, daily_rate, max_fine)

    print(f"Book: {book_title}")
    print(f"Days overdue: {days_overdue}")
    print(f"Fine: Rs. {fine_amount}")
