def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
  
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine


if __name__ == "__main__":
    book_title = "The Handbook of Psychology"
    days_overdue = 10
    daily_rate = 15.0   # Fine per day
    fine_amount = calculate_fine(book_title, days_overdue, daily_rate)

    print(f"Book: {book_title}")
    print(f"Days overdue: {days_overdue}")
    print(f"Fine: Rs. {fine_amount}")
