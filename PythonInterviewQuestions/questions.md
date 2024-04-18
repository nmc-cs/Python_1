**1. What is Python?**
- Python is a high level programming language that support many types of programming techniques like object-oriented and functional programming

**2. What is a variable?**
- A variable is a nmae that refers to a value that you set it to. It is used to store data and can be changed later in the program.

**3. What is a namespace?**
- It maps names to objects and provides a waay to avoid naming conflicts in your program

**4. What is the difference between list and tuple?**
- A list is mutable which means their elements can be changed after it has been created.
- A tuple is immutable which means their elements cant be changed after it has been created

**5. How you can convert a number to a string?**
- You can use the str() function
- Example: num = 13,  mumstr = str(num)

**6. What are the rules for local and global variables?**
- Local vairables are defined in a function and can only be accessed inside of the function. Global variables are defined outside of the function and are accessible anywhere in your program.

**7. Explain how to generate random numbers.**
- You can use the random module. You can use functions like random.random() for floating point numbers between 0 and 1 and random.randint(a, b) for integers between a and b.

**8. What is a dictionary?**
- A dictionary is an unordered collection of key value pairs. Each key is unique and is mapped to its own value.

**9. What is the self keyword?**
- Self is used as a name for the first parameter of instance menthods in classes. It refers to the instance of the class itself and allows you to access attributes and methods within a class.

**10. What are loop interruption statements?**
- They are break and continue. Break is used to exit a loop completely and a continue is used to skip over the current loop iteration and go to the next one.

**11. Explain List, Tuple, Set, and Dictionary and provide at least one instance where each of these collection types can be used.**
- A list is an ordered collection of items, used to store sequences of elements.
- A tuple is immutable and an ordered collection of items, used when data should not be changed
- A set is an unorder collection of unique items, used to eliminate duplicates or test well.
- A dictionary is an unordered collection of key value pairs, used for fast lookup and mapping between related items.

**12. How is Exception Handling done?**
- Exception handlin is done using try, except, else and finally commands. Code that can raise an exception is placed inside of a try block, and any exceptions that occur are caught and handled in the except block.

**13. What does ‘#’ symbol do?**
- It is used to indicate a comment and they are ignored by the Python interpreter and are used to add notes or documentation to your code.

**14. Write the command to get all keys from a dictionary.**
- dict = {'a': 1, 'b': 2, 'c': 3}
- keys = dict.keys()

**15. What is range()? Give an example to explain it.**
- range() is a built-in function used to generate a sequence of numbers. It can take 1-3 arguments and it generates numbers from start to stop with what its indicated to do.
- for i in range(1,6,2):
- print(i)

**16. What does the // arithmetic operator do?**
- It performs floor division, which means it divides two numbers and returns the quotient rounded down to the nearest integer.

**17. What is a data type?**
- A data type is a classification of data which tells the compiler or interpreter how the programmer inteds to use the data.

**18. What are the basic data types that are supported by the language?**
- integers, floating-point numbers, strings, booleans, lists, tuples, sets, dictionaries are the main ones.

**19. How do you check whether the two variables are pointing to the same object?**
- You can ust the 'is' operator to check if two variables are pointing to the same object

**20. What is for-else and while-else?**
- An else can be used with for and while loops. The else block is executed if the loop completes without encountering a break statement.

**21. What does immutable mean in the context of programming?**
- Immutable means that the object cannot be changed after it is created. So like tuples, strings and numbers are immutable data types.

**22. What is a list in Python?**
- A list in python is mutable, ordered collection of items. Lists are created using square brackets [] and can contain elements of different data types.

**23. What is a tuple in Python?**
- A tuple in Python is immuatable, ordeered collection of items. Tuples are created using () and can contain elements of different data types.

**24. When do you choose a list over a tuple?**
- You should pick a list over a tuple if you need a collection of items that can be modified after creation. You choose a tuple over a list if you need an immutable collection of items that should not be changed.

**25. How do you get the last value in a list or a tuple?**
- You can use a negative indexing to get the last value in a list or tuple

**26. What is Index Out Of Range Error?**
- It occurs when you try to access an index in a sequence that does not exist.

**27. Why should a program close a file when it is finished using it?**
- A program should close a file when it is finished using it to release system resources and ensure that changes to the file are saved properly.

**28. Assume the variable names references a list of strings like ["John", "Sally", "Dale", "Jose", "Apryl"]. Write code that determines whether 'Sally' is in the names list. If it is, display the message 'Hello Sally'.  Otherwise, display the message 'No Sally.**
- names = ["John", "Sally", "Dale", "Jose", "Apryl"]
- if "Sally" in names:
-     print("Hello Sally")
- else:
 -    print("No Sally")
