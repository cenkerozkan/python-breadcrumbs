fizz_buzz_dict_with_step = {
    number: "FizzBuzz" if number % 5 == 0 else "Fizz" for number in range(0, 201, 12)
}
fizz_buzz_dict_without_step = {
    number: "FizzBuzz" if number % 5 == 0 else "Fizz"
    for number in range(0, 201, 12)
    if number % 3 == 0 and number % 4 == 0
}

print(fizz_buzz_dict_with_step)
