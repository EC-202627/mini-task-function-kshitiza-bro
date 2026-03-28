def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):

    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine


if __name__ == "__main__":
    book_title = "Hello new world"
    days_overdue = 40
    fine_amount = calculate_fine(book_title, days_overdue)

    print(f"Book: {book_title}")
    print(f"Days overdue: {days_overdue}")
    print(f"Fine: Rs. {fine_amount}")
    if fine_amount == 150.0:
        print("You have accumulated the maximum fine of INR: 150.0")
