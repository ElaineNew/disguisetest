# test_script.py
import unittest
from test_server import CodeTest

class DisguiseTest(unittest.TestCase):
    def setUp(self):
        self.server = CodeTest()
        self.server.write_to_server("START")
        result = self.server.read_from_server()
        assert result == "info: server has been started"

    def tearDown(self):
        self.server.write_to_server("EXIT")
        result = self.server.read_from_server()
        assert result == "info: server has been stopped"

    # 1. test set veriable with string
    def test_set_variable_string(self):
        self.server.write_to_server("SET VAR_1 hello")
        result = self.server.read_from_server()
        self.assertEqual(result, "info: set variable")

        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server() 
        self.assertEqual(result, "hello")

    # 2. test set veriable with space in string with single quote
    def test_set_variable_space_string_quote(self):
        self.server.write_to_server("SET VAR_1 '  he llo'")
        result = self.server.read_from_server()
        self.assertEqual(result, "info: set variable")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server() 
        self.assertEqual(result, "  he llo")

    # 3. test set veriable with pace in string without single quote
    def test_set_variable_space_string_no_quote(self):
        self.server.write_to_server("SET VAR_1   hel lo")
        result = self.server.read_from_server()
        self.assertTrue(
          result.lower().startswith("error"),
          msg="Expected SET with float to fail, but got: " + result
        )

    # 4. test set veriable with special caracters with quote
    def test_set_variable_operators_quote(self):
        self.server.write_to_server("SET VAR_1  '--'")
        result = self.server.read_from_server()
        self.assertEqual(result, "info: set variable")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server() 
        self.assertEqual(result, "--")

    # 5. test set veriable with special caracters without quote
    def test_set_variable_operators_no_quote(self):
        self.server.write_to_server("SET VAR_1 //")
        result = self.server.read_from_server()
        self.assertTrue(
          result.lower().startswith("error"),
          msg="Expected SET with operators without single quotes to fail, but got: " + result
        )

   # 6. test set veriable with keywords with quote
    def test_set_variable_keywords_quote(self):
        self.server.write_to_server("SET VAR_1  'OUT'")
        result = self.server.read_from_server()
        self.assertEqual(result, "info: set variable")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server() 
        self.assertEqual(result, "OUT")

    # 7. test set veriable with keywords without quote
    def test_set_variable_keywords_no_quote(self):
        self.server.write_to_server("SET VAR_1  OUT")
        result = self.server.read_from_server()
        self.assertTrue(
          result.lower().startswith("error"),
          msg="Expected SET with keywords without single quotes to fail, but got: " + result
        )

    # 8. test set veriable with empty string
    def test_set_variable_keywords_empty_string_without_quote(self):
        self.server.write_to_server("SET VAR_1  ")
        result = self.server.read_from_server()
        self.assertEqual(result, "info: set variable")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server() 
        self.assertEqual(result, "")

    # 9. test set veriable with empty string no quote
    def test_set_variable_keywords_empty_string_quote(self):
        self.server.write_to_server("SET VAR_1  ''")
        result = self.server.read_from_server()
        self.assertEqual(result, "info: set variable")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server() 
        self.assertEqual(result, "")

    # 10. test set veriable with int
    def test_set_variable_int(self):
        self.server.write_to_server("SET VAR_1 3")
        result = self.server.read_from_server()
        self.assertEqual(result, "info: set variable")

        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server() 
        self.assertEqual(result, "3")

    # 11. test set veriable with double, should return error
    def test_set_variable_float_error(self):
      self.server.write_to_server("SET VAR_1 3.11")
      result = self.server.read_from_server()
      self.assertTrue(
          result.lower().startswith("error"),
          msg="Expected SET with float to fail, but got: " + result
      )

    # 12. test repeat string * number
    def test_operator_repeat_string_number(self):
        self.server.write_to_server("VAR_1 hi * 3")
        result = self.server.read_from_server()
        self.assertEqual(result, "info: set variable")

        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "hihihi")

    # 13. test repeat number * number
    def test_operator_repeat_number_number(self):
        self.server.write_to_server("VAR_1 3 * 3")
        result = self.server.read_from_server()
        self.assertEqual(result, "info: set variable")

        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "333")

    # 14. test repeat string *  minus number
    def test_operator_repeat_string_minus(self):
        self.server.write_to_server("VAR_1 hi * -1")
        result = self.server.read_from_server()
        self.assertTrue(
          result.lower().startswith("error"),
          msg="Expected repeat with minus on the right to fail, but got: " + result
        )

    # 15. test repeat string * float
    def test_operator_repeat_string_float(self):
        self.server.write_to_server("VAR_1 hi * 3.5")
        result = self.server.read_from_server()
        self.assertTrue(
          result.lower().startswith("error"),
          msg="Expected repeat with float on the right to fail, but got: " + result
        )

    # 16. test repeat string * string
    def test_operator_repeat_string_string(self):
        self.server.write_to_server("VAR_1 hi * test")
        result = self.server.read_from_server()
        self.assertTrue(
          result.lower().startswith("error"),
          msg="Expected repeat with string on the right to fail, but got: " + result
        )

    # 17. test repeat string *  0
    def test_operator_repeat_string_zero(self):
        self.server.write_to_server("VAR_1 hi * 0")
        self.server.read_from_server()
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "")

    # 18. test repeat string * empty
    def test_operator_repeat_string_empty(self):
        self.server.write_to_server("VAR_1 hi * ")
        result = self.server.read_from_server()
        self.assertTrue(
          result.lower().startswith("error"),
          msg="Expected repeat with empty to fail, but got: " + result
        )

    # 19. test repeat empty * empty 
    def test_operator_repeat_empty_empty(self):
        self.server.write_to_server("VAR_1  * ")
        result = self.server.read_from_server()
        self.assertTrue(
          result.lower().startswith("error"),
          msg="Expected repeat with empty to fail, but got: " + result
        )

    # 20. test repeat string * with big number
    def test_operator_repeat_string_big_number(self):
        self.server.write_to_server("VAR_1 hi * 1000")
        result = self.server.read_from_server()
        self.assertEqual(result, "info: set variable")

        self.server.write_to_server("OUT VAR_1")
        value = self.server.read_from_server()
        self.assertEqual(len(value), 2000)
        self.assertTrue(value.startswith("hihihi"))


    # 21. test concat string + string
    def test_concat_string_string(self):
        self.server.write_to_server("VAR_1 hello + world")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "helloworld")

    # 22. test concat string + quoted string
    def test_concat_string_quoted(self):
        self.server.write_to_server("VAR_1 hello + ' there'")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "hello there")

    # 23. test concat string + int
    def test_concat_string_int(self):
        self.server.write_to_server("VAR_1 hi + 123")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "hi123")

    # 24. test concat string + float (should fail)
    def test_concat_string_float(self):
        self.server.write_to_server("VAR_1 hi + 3.14")
        result = self.server.read_from_server()
        self.assertTrue(result.lower().startswith("error"))

    # 25. test concat string + minus
    def test_concat_string_minus(self):
        self.server.write_to_server("VAR_1 hi + -99")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "hi-99")

    # 26. test concat int + string
    def test_concat_int_string(self):
        self.server.write_to_server("VAR_1 42 + end")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "42end")

    # 27. test concat int + int
    def test_concat_int_int(self):
        self.server.write_to_server("VAR_1 3 + 7")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "37") 

    # 28. test concat string + empty
    def test_concat_string_empty(self):
        self.server.write_to_server("VAR_1 hi + ''")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "hi")

    # 29. test concat empty + string
    def test_concat_empty_string(self):
        self.server.write_to_server("VAR_1 '' + world")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "world")

    # 30. test concat empty + empty
    def test_concat_empty_empty(self):
        self.server.write_to_server("VAR_1 '' + ''")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "")

    # 31. test concat string + long string
    def test_concat_string_long(self):
        long_str = "a" * 500
        self.server.write_to_server(f"VAR_1 hello + '{long_str}'")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "hello" + long_str)

    # 32. test concat string + special characters
    def test_concat_string_special_chars(self):
        self.server.write_to_server("VAR_1 hello + '+-*'")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "hello+-*")


    # 33. test trim end string -- number valid
    def test_trim_end_valid(self):
        self.server.write_to_server("VAR_1 hello -- 2")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "hel")

    # 34. test trim end number -- number valid (should fail)
    def test_trim_end_number_target(self):
        self.server.write_to_server("VAR_1 12345 -- 2")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "123")



    # 35. test trim end string -- negative number
    def test_trim_end_negative(self):
        self.server.write_to_server("VAR_1 hello -- -2")
        result = self.server.read_from_server()
        self.assertTrue(result.lower().startswith("error"),
          msg="Expected trim with negative number to fail, but got: " + result
                        )

    # 36. test trim end string -- number equals string length
    def test_trim_end_full(self):
        self.server.write_to_server("VAR_1 hi -- 2")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "")

    # 37. test trim end string -- number greater than string length
    def test_trim_end_exceed_length(self):
        self.server.write_to_server("VAR_1 hi -- 10")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "")

    # 38. test trim end string -- 0
    def test_trim_end_zero(self):
        self.server.write_to_server("VAR_1 hi -- 0")
        self.server.read_from_server()
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "hi")

    # 39. test trim end string -- empty
    def test_trim_end_empty(self):
        self.server.write_to_server("VAR_1 '' -- 1")
        result = self.server.read_from_server()
        self.assertTrue(result.lower().startswith("error"),
          msg="Expected trim empty string to fail, but got: " + result
                        )

    # 40. test trim end string -- string
    def test_trim_end_non_number_string(self):
        self.server.write_to_server("VAR_1 hello -- world")
        result = self.server.read_from_server()
        self.assertTrue(result.lower().startswith("error"),
          msg="Expected trim with non number string to fail, but got: " + result
                        )

    # 41. test trim end string -- character
    def test_trim_end_character(self):
        self.server.write_to_server("VAR_1 hello -- !")
        result = self.server.read_from_server()
        self.assertTrue(result.lower().startswith("error"),
          msg="Expected trim with non number character to fail, but got: " + result
                        )


    # 42. test trim start string // number 
    def test_trim_start_valid(self):
        self.server.write_to_server("VAR_1 hello // 2")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "llo")


    # 43. test trim start number // number  
    def test_trim_start_number_target(self):
        self.server.write_to_server("VAR_1 12345 // 2")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "345")
        

    # 44. test trim start string // negative number
    def test_trim_start_negative(self):
        self.server.write_to_server("VAR_1 hello // -1")
        result = self.server.read_from_server()
        self.assertTrue(result.lower().startswith("error"),
          msg="Expected trim with negative number to fail, but got: " + result
                        )

    # 45. test trim start string // number equals string length
    def test_trim_start_full(self):
        self.server.write_to_server("VAR_1 hi // 2")
        self.server.read_from_server()
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "")

    # 46. test trim start string // number greater than string length
    def test_trim_start_exceed_length(self):
        self.server.write_to_server("VAR_1 hi // 10")
        self.server.read_from_server()
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "")

    # 47. test trim start string // 0
    def test_trim_start_zero(self):
        self.server.write_to_server("VAR_1 hi // 0")
        self.server.read_from_server()
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "hi")

    # 48. test trim start string // empty
    def test_trim_start_empty(self):
        self.server.write_to_server("VAR_1 '' // 1")
        result = self.server.read_from_server()
        self.assertTrue(result.lower().startswith("error"),
          msg="Expected trim empty stirng to fail, but got: " + result
                        )

    # 49. test trim start string // string
    def test_trim_start_non_number_string(self):
        self.server.write_to_server("VAR_1 hello // abc")
        result = self.server.read_from_server()
        self.assertTrue(result.lower().startswith("error"),
          msg="Expected trim with stirng to fail, but got: " + result
                        )

    # 50. test trim start string // character
    def test_trim_start_character(self):
        self.server.write_to_server("VAR_1 hello // $")
        result = self.server.read_from_server()
        self.assertTrue(result.lower().startswith("error"),
          msg="Expected trim with character to fail, but got: " + result
                        )

    # 51. test copy valid
    def test_copy_variable(self):
        self.server.write_to_server("SET VAR_1 copytest")
        self.server.read_from_server()
        self.server.write_to_server("VAR_1 VAR_2")
        result = self.server.read_from_server()
        self.assertEqual(result, "info: variable copied")
        self.server.write_to_server("OUT VAR_2")
        result = self.server.read_from_server()
        self.assertEqual(result, "copytest")

    # 52. copy from uninitialized variable
    def test_copy_uninitialized_variable(self):
        self.server.write_to_server("VAR_3 VAR_4")
        result = self.server.read_from_server()
        self.assertEqual(result, "info: variable copied")
        self.server.write_to_server("OUT VAR_4")
        result = self.server.read_from_server()
        self.assertEqual(result, "")

    # 53. self-copy 
    def test_copy_self(self):
        self.server.write_to_server("SET VAR_1 selfcopy")
        self.server.read_from_server()
        self.server.write_to_server("VAR_1 VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "info: variable copied")
        self.server.write_to_server("OUT VAR_1")
        result = self.server.read_from_server()
        self.assertEqual(result, "selfcopy")

    # 54. chained copy
    def test_copy_chain(self):
        self.server.write_to_server("SET VAR_1 chain")
        self.server.read_from_server()
        self.server.write_to_server("VAR_1 VAR_2")
        self.server.read_from_server()
        self.server.write_to_server("VAR_2 VAR_3")
        self.server.read_from_server()
        self.server.write_to_server("OUT VAR_3")
        result = self.server.read_from_server()
        self.assertEqual(result, "chain")

    # 54. invalid command error
    def test_invalid_command(self):
      invalid_command = "INVALID COMMAND"
      self.server.write_to_server(invalid_command)
      result = self.server.read_from_server()
      expected = f"Error: cannot parse the data: {invalid_command}"
      self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()



# test 4: do not accept set string as operators, with quote
# test 5: accept set string as operators, without quote
# test6: do not accept set string as keywords with quote
# test 8&9: do not  accept set string as  empty string
# test 11: allow float
# test 12: failed to repeat string
# test 13, cannot repeat number
# test 14, suppose to give error
# test 27, concat two number will treat them as number
# test 29, when concat 2 empty strings, var1 has a default value one
# test 35, no error when trim end with negative value
# test 39, no error when trim end empty value
# test 52, uninitialized var will retain value fron former run
# test 54, invalid comman error mismatch
# test 44, no error when trim start with negative value
# test 48, no error when trim start empty value
