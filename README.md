# pythonday06
This lab is a continuation of **OOP** programming, focusing mainly on interfaces and abstract classes.

## 📚 Abstract Classes and Interfaces in Python
# 1️⃣ Definition
# Abstract Class
An **abstract class** is a class that cannot be instantiated directly and can contain:

- Abstract methods (without implementation)

- Concrete methods (with implementation)

- Attributes

In Python, they are created using **abc.ABC** and **@abstractmethod**.

## Interface
An **interface** is a contract that defines only abstract methods, without attributes or internal logic.
In Python, it is also implemented via abc.ABC, but we avoid adding anything other than abstract methods.

## 2️⃣ Purpose
# Abstract Class
- Allows sharing common code among multiple child classes

- Provides a mandatory structure for certain methods, while leaving freedom for others

# Interface
Used to standardize behavior across different classes, regardless of their hierarchy

Promotes polymorphism: you can handle different objects the same way as long as they implement the interface

## 3️⃣ Advantages
# Abstract Class
- ✔ Reusable code (methods already defined in the parent class)
- ✔ Clear structure for child classes
- ✔ Can combine attributes + abstract methods

# Interface
- ✔ Strong decoupling (classes don’t need to share a common ancestor)
- ✔ More flexible in software architecture
- ✔ Ideal for defining behavior contracts

# 4️⃣ Drawbacks
# Abstract Class
- ❌ Less flexible than interfaces (single inheritance in Python)
- ❌ Risk of unnecessary overload if too much common code is imposed

# Interface
- ❌ No shared code possible
- ❌ May require implementing many methods, even if some aren’t used

# 5️⃣ Conclusion
Use an abstract class if your classes share state and common behavior, but also need to follow specific rules.

Use an interface if you only want to define a common contract for classes that can be completely different.

In Python, both concepts are technically implemented via abc.ABC, but their conceptual role remains different.