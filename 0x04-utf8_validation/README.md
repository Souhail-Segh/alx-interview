## 0x04. UTF-8 Validation

UTF-8 is a character encoding standard used for electronic communication. Defined by the Unicode Standard.

# One Byte UTF-8 / ASCII:
Length: 1 byte
Rule: MSB is 0 (first bit)

# Two Bytes UTF-8:
Length: 2 bytes.
Rule: First byte start with 110; Second byte start with 10.

# Three Bytes UTF-8:
Length: 3 bytes.
Rule: First byte start with 1110; Second byte and Third bytes start with 10.

# Three Bytes UTF-8:
Length: 3 bytes.
Rule: First byte start with 11110; Second byte, Third and Fourth bytes start with 10.