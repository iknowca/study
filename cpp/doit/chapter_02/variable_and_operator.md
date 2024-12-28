# Varialbe and Operator

### L-value and R-value

|L-value| R-value|
|---|---|
|It appears on the left side of assignment operator.|It appears on the right side of assignment operator.|
|Points to a memory location. |It does not point to a memory location.|
|It is valid outside of the expression in which it is used.|It is valid only within the expression in which it is used.|

### type casting

* Implicit type casting
    : It is done automatically by the compiler.
* Explicit type casting
    : It is done by the programmer.

**Explicit casting method**

|Explicit casting method|feature|
|---|---|
|statdc_cast|Any cast that can be logically changed. Conversion between pointers in an inheritance relationship is also supported.|
|const_cast|Only available in pointer and reference types. It is used to remove the const/volatile attribute.|
|reinterpret_cast|It is mainly used to convert a pointer type to another pointer type, or to convert between integer data and pointers. It is very powerful and dangerous because **it ignores the semantics of the type and reinterprets the bits**|
|dynamic_cast|Used for type conversions that support polymorphism. Mainly used for downcasting and to ensure type stability.|