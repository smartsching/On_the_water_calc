#this program displays an American flag
STRIPES = 13
UNION_ROWS = 9
UNION_WIDTH = 12
FLAG_WIDTH = 46

for stripe in range(STRIPES):

    # Top 7 stripes contain the blue union
    if stripe < 7:

        # Even stripe rows have 6 stars
        if stripe % 2 == 0:
            stars = "* * * * * * "
        # Odd stripe rows have 5 stars
        else:
            stars = " * * * * * "

        # Alternate stripe character
        if stripe % 2 == 0:
            stripe_part = "=" * (FLAG_WIDTH - UNION_WIDTH)
        else:
            stripe_part = "-" * (FLAG_WIDTH - UNION_WIDTH)

        print(stars.ljust(UNION_WIDTH) + stripe_part)

    # Bottom 6 stripes (no stars)
    else:
        if stripe % 2 == 0:
            print("=" * FLAG_WIDTH)
        else:
            print("-" * FLAG_WIDTH)

print("\n Merica!")