def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine

if __name__ == "__main__":
    book_title = " i what to eat your pancreas "
    days_overdue = 5
    daily_rate = 10.0   # Custom fine per day
    fine_amount = calculate_fine(book_title, days_overdue, daily_rate)

    print(f"Book: {book_title}")
    print(f"Days overdue: {days_overdue}")
    print(f"Fine: Rs. {fine_amount}")
