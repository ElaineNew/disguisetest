# QA Engineer – Technical Assessment


### Brief

The aim of this assessment is for you to produce a script that tests the functionality of the python module `test_server.pyc`. 

### Expectations / Assumptions

This code test is representative of the automated test environment at Disguise, therefore there are some expectations / assumptions:

- Your code should be in a state where it can be run from the commandline and yield test results.
- For ease of assessment, all your code should only be reliant on Python’s Standard Library for currently available versions of Python 3.
- We expect test coverage to be balanced across the whole functionality of the module. More complex functionality will of course require more test cases.  
- At Disguise we put great emphasis on readable, maintainable code. You will be assessed on this, along with the coverage your tests offer.

### What to include in your submission

- The test script.
- Any notes you might have taken while working with the module.

### How to use the module

1. In your imports: `from test_server import CodeTest`.
2. Call `CodeTest()` to initialise the class. It requires no arguments.
3. `CodeTest()` has two methods you are expected to use: `write_to_server(message: str) -> None` and `read_from_server() -> str`.
4. A specification of commands accepted by `write_to_server()` is provided in the second half of this document.
5. `read_from_server()` is called to obtain confirmation of commands sent.

## Program Specification

### SYNTAX

`write_to_server()` takes a single argument. Operations that take multiple keywords are delineated by a space.
If the syntax is not followed an error is returned on `read_from_server()`.

| Operation | Example |
| :---- | :---- |
| Save result of command to a var | `[VARIABLE] [value] [OPERATOR] [value]` |
| Output result of command | `OUT [value] [OPERATOR] [value]` |
| Set var to a user value | `SET [VARIABLE] [value]` |
| Output the value of a var | `OUT [VARIABLE]` |
| Copy first var to second var | `[VARIABLE] [VARIABLE]` |
| Activate module | `START` |
| Deactivate from module | `EXIT` |

### OPERATORS

Used to perform commands. All operators require two inputs and always return a string.

| Syntax | Operation | Example |
| :---- | :---- | :---- |
| `*` | Repeat the string a number of times | `[string * number]` |
| `+` | Concatenates two strings | `[string + string]` |
| `--` | Remove a number of  characters from back of the string | `[string -- number]` |
| `//` | Remove a number of characters from front of the string | `[string // number]` |

### COMMAND KEYWORDS

There are four variables to store results and two special commands. A command always begins with one of these keywords. The four variables can store strings or numbers.

| Syntax | Operation |
| :---- | :---- |
| `VAR_1` | Write and access variable 1 |
| `VAR_2` | Write and access variable 2 |
| `VAR_3` | Write and access variable 3 |
| `VAR_4` | Write and access variable 4 |
| `OUT` | Output result to network |
| `SET` | Set value of variable 1-4 |

### USER VALUES

User values (referred to as `[value]` in the Syntax section) come in two formats: strings and numbers.

- Strings can be surrounded by single quotes (‘’), this is required if the string contains spaces, but is otherwise optional.
- Strings can be empty, contain keywords and operator characters without breaking the module. Enclosing the string in single quotes may be required to achieve this.  
- When numbers are used to specify quantity, only integers are supported.

### EXAMPLES

#### **Example 1**

| Syntax | Operation |
| :---- | :---- |
| `VAR_1 hello * 5` | Store “`hellohellohellohellohello`” in VAR\_1 |
| `OUT VAR_1 + start` | Output “`hellohellohellohellohellostart`” |

#### **Example 2**

| Syntax | Operation |
| :---- | :---- |
| `VAR_1 world // 3` | Store “`ld`” in VAR\_1 |
| `VAR_2 world -- 3` | Store “`wo`” in VAR\_2 |
| `OUT VAR_1 + VAR_2` | Output “`wold`” |

#### **Example 3**

| Syntax | Operation |
| :---- | :---- |
| `SET VAR_1 example` | Store “`example`” in VAR\_1 |
| `VAR_2 VAR_1 + ‘ case’` | Append “ `case`” to VAR\_1 and store the result in VAR\_2. *Note the use of quotes to store a string with a space.* |
| `OUT VAR_2` | Output “`example case`” |

### ADDITIONAL INFORMATION

- Upon receiving a command that cannot be parsed the module will reply with an error message: “`Error: cannot parse the data: [most recently attempted command]`”.  
- Upon setting a variable, calling `read_from_server()` will return “`info: set variable`”.  
- Upon copying a variable, calling `read_from_server()` will return “`info: variable copied`”.  
