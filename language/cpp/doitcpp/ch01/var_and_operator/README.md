# var and operator

|Explicit Type Conversion Methods | feature |
|---|---|
|`static_cast<type>(target)`| Logically convertible types. Supports conversion between pointers in an inheritance relationship |
|`const_cast<type>(target)`| Used in pointer and reference types. Used when removing const and volatile|
|`reinterpret_cast<type>(target)`| Identical to a standar explicit type conversion. The target of a conversion using const cannot be used.|
|`dynamic_cast<type>(target)`| Used for type conversion between class pointer and reference variables. Used for safe downcasting.|

