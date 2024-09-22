from mean_var_std import calculate

# Example usage
if __name__ == "__main__":
    try:
        input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        result = calculate(input_list)
        print(result)
    except ValueError as e:
        print(e)
