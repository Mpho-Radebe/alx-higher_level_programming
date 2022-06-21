#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range (list_length):
        new_list.append(0)
        try:
            new_list[-1] = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            pass
    return new_list

if __name__ == "__main__":
    print(list_division([1, 2, 3, 4], [1.0, 0, "H"], 5))
