import random

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 5

CLOSE_LIMIT = 5      # اختلاف تا ۵: خیلی نزدیک
MEDIUM_LIMIT = 15    # اختلاف تا ۱۵: نزدیک

RANKS = {
    1: "نمونه‌ای",
    2: "بسیار خوبی",
    3: "خوب",
    4: "قبول",
    5: "با شانس بردی!",
}

PERSIAN_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
ENGLISH_DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")


def fa(number):
    """تبدیل عدد به ارقام فارسی برای نمایش."""
    return str(number).translate(PERSIAN_DIGITS)


def read_guess():
    """ورودی را می‌گیرد و تا زمان معتبر بودن آن تکرار می‌کند.
    ورودی نامعتبر از فرصت‌ها کم نمی‌شود."""
    while True:
        text = input("حدس شما: ").strip().translate(ENGLISH_DIGITS)
        try:
            guess = int(text)
        except ValueError:
            print("ورودی نامعتبر است! فقط عدد صحیح وارد کن.")
            continue
        if guess < MIN_NUMBER or guess > MAX_NUMBER:
            print(f"عدد باید بین {fa(MIN_NUMBER)} تا {fa(MAX_NUMBER)} باشد.")
            continue
        return guess


def closeness_hint(diff):
    if diff <= CLOSE_LIMIT:
        return "خیلی نزدیکی!"
    if diff <= MEDIUM_LIMIT:
        return "نزدیکی، ولی هنوز فاصله داری!"
    return "خیلی دوری!"


def play_round():
    secret = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f"\nیک عدد بین {fa(MIN_NUMBER)} تا {fa(MAX_NUMBER)} انتخاب شد. "
          f"حدس بزن!")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        remaining = MAX_ATTEMPTS - attempt + 1
        print(f"\nتلاش {fa(attempt)} از {fa(MAX_ATTEMPTS)}")
        print(f"جان باقی‌مانده: {fa(remaining)}")

        guess = read_guess()

        if guess == secret:
            print("\nآفرین! درست حدس زدی، برنده شدی!")
            print(f"رتبه تو: {RANKS[attempt]}")
            return

        direction = "کوچک‌تر وارد کن" if guess > secret else "بزرگ‌تر وارد کن"
        print(f"{direction} - {closeness_hint(abs(guess - secret))}")

    print("\nمتأسفانه باختی! فرصت‌هایت تمام شد.")
    print(f"عدد مخفی {fa(secret)} بود.")


def ask_play_again():
    while True:
        answer = input("\nآیا می‌خواهی دوباره بازی کنی؟ (بله/خیر): ").strip().lower()
        if answer in ("بله", "آره", "ب", "y", "yes"):
            return True
        if answer in ("خیر", "نه", "خ", "n", "no"):
            return False
        print("لطفاً فقط «بله» یا «خیر» وارد کن.")


def main():
    print("به بازی حدس اعداد خوش آمدی!")
    while True:
        play_round()
        if not ask_play_again():
            print("خداحافظ!")
            break


if __name__ == "__main__":
    main()
