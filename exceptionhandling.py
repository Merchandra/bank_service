# 1
# try:
#     print("A")

# except:
#     print("B")

# print("C")


# 2

try:
    print("A")
    print(10 / 0)
    print("B")

except:
    print("C")

print("D")


# 3
# try:
#     print("A")
#     print(10 / 2)
#     print("B")

# except:
#     print("C")

# print("D")



# 4
# print("A")

# try:
#     print("B")
#     int("hello")
#     print("C")

# except:
#     print("D")

# print("E")
# 5
# try:
#     numbers = [10, 20]
#     print(numbers[5])

# except IndexError:
#     print("Invalid index")

# print("Done")
# 6
# try:
#     print(10 / 0)

# except ValueError:
#     print("Value Error")

# Ask:

# Is the exception handled?

# No. The actual exception is ZeroDivisionError.

# 7
# try:
#     int("hello")

# except ZeroDivisionError:
#     print("A")

# except ValueError:
#     print("B")
# 8
# try:
#     print("A")
#     int("hello")
#     print("B")

# except ValueError:
#     print("C")

# except TypeError:
#     print("D")

# print("E")
# 9
# try:
#     print(10 + "20")

# except TypeError:
#     print("Type problem")

# except ValueError:
#     print("Value problem")
# 10
# try:
#     data = {
#         "name": "Arun"
#     }

#     print(data["age"])

# except KeyError:
#     print("Key missing")



# 1
# try:
#     print("A")
# except:
#     print("B")
# else:
#     print("C")
# finally:
#     print("D")
# 2
# try:
#     print(10/2)
# except:
#     print("Error")
# else:
#     print("Success")
# finally:
#     print("Done")
# 3
# try:
#     print(10/0)
# except:
#     print("Error")
# else:
#     print("Success")
# finally:
#     print("Done")
# 4
# try:
#     int("hello")
# except ValueError:
#     print("Value")
# finally:
#     print("Finally")
# 5
# try:
#     print("A")
#     int("hello")
#     print("B")
# except ValueError:
#     print("C")
# finally:
#     print("D")
# print("E")
# 6
# try:
#     print("A")
#     print(10/2)
# except:
#     print("B")
# else:
#     print("C")
# finally:
#     print("D")
# print("E")
# 7
# try:
#     print("A")
#     print(10/0)
# except ZeroDivisionError as e:
#     print(e)
# 8
# try:
#     numbers=[10]

#     print(numbers[2])

# except Exception as e:

#     print(type(e))
# 9
# try:
#     print(int("100"))

# except ValueError:

#     print("A")

# else:

#     print("B")

# finally:

#     print("C")
# 10
# try:

#     print(int("abc"))

# except Exception as e:

#     print(type(e).__name__)




# 1
# age = -5

# if age < 0:
#     raise ValueError

# print(age)
# 2
# try:

#     raise ValueError("Wrong")

# except ValueError as e:

#     print(e)
# 3
# try:

#     print("A")

#     raise Exception("X")

#     print("B")

# except Exception:

#     print("C")

# print("D")
# 4
# assert 5 > 2

# print("Hello")
# 5
# assert 2 > 5
# 6
# assert 2 > 5, "Invalid"
# 7
# class MyError(Exception):
#     pass

# raise MyError
# 8
# class MyError(Exception):
#     pass

# try:

#     raise MyError("Hello")

# except MyError as e:

#     print(e)
# 9
# try:

#     print(10 / 0)

# except ZeroDivisionError:

#     print("Logged")

#     raise
# 10
# class AgeError(Exception):
#     pass

# age = 25

# if age < 0:
#     raise AgeError

# print("Done")

# import random
# random.seed(10)
# print(random.randint(1,100))