"""Unit testing file for app.py"""
2	from app import returnBackwardsString
3	import unittest
4	
5	class TestApp(unittest.TestCase):
6	    """Unit tests defined for app.py"""
7	
8	    def test_return_backwards_string(self):
9	        """Test return backwards simple string"""
10	        random_string = "This is my test string"
11	        random_string_reversed = "gnirts tset ym si sihT"
12	        self.assertEqual(random_string_reversed, returnBackwardsString(random_string))
13	
14	if __name__ == "__main__":
15	    unittest.main()
