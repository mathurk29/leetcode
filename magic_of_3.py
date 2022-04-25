def magic_of_three(num: int) -> int:
    pass
    digits_in_num = 0
    temp = num
    while temp > 0:
        temp = temp // 10
        digits_in_num += 1

    result = 1

    # A slightly better way to escape few divisions. We can compute and directly start from 111... which has no. of digits equal to num.
    # for _ in range(digits_in_num):
    #     result = 10 * result + 1

    while True:
        if result % num == 0:
            return result
        else:
            result = 10 * result + 1


magic_of_three(123)
