def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
   
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine

if __name__ == "__main__":
    book_title = "Naruto"
    days_overdue = 5
    fine_amount = calculate_fine(book_title, days_overdue)

    print(f"Book: {book_title}")
    print(f"Days overdue: {days_overdue}")
    print(f"Fine: Rs. {fine_amount}")
