import unittest
from employee import Employee

# class TestEmployee(unittest.TestCase):

#     def setUp(self): #will run before every single test
#         pass

#     def tearDown(self):
#         pass

#     def test_email(self):
#         emp1=Employee('Corey','Fat',50000)
#         emp2=Employee('Jim','Hanks',65000)

#         self.assertEqual(emp1.email,'Corey.Fat@gmail.com')
#         self.assertEqual(emp2.email,'Jim.Hanks@gmail.com')

#         emp1.first='John'
#         emp2.first='Jake'

#         self.assertEqual(emp1.email,'John.Fat@gmail.com')
#         self.assertEqual(emp1.email,'Jake.Hanks@gmail.com')

#     def test_fullname(self):
#         emp1=Employee('Corey','Fat',50000)
#         emp2=Employee('Jim','Hanks',65000)

#         self.assertEqual(emp1.fullname,'Corey Fat')
#         self.assertEqual(emp2.fullname,'Jim Hanks')

#         emp1.first='John'
#         emp2.first='Jake'

#         self.assertEqual(emp1.fullname,'John Fat')
#         self.assertEqual(emp2.fullname,'Jake Hanks')

#     def test_apply_raise(self):
#         emp1=Employee('Corey','Fat',50000)
#         emp2=Employee('Jim','Hanks',65000)

#         emp1.apply_raise()
#         emp2.apply_raise()

#         self.assertEqual(emp1.pay,52500)
#         self.assertEqual(emp2.pay,63000)

class TestEmployee(unittest.TestCase):

    def setUp(self): #will run before every single test
        self.emp1=Employee('Corey','Fat',50000)
        self.emp2=Employee('Jim','Hanks',65000)

    def tearDown(self):
        pass

    def test_email(self):
        
        self.assertEqual(self.emp1.email,'Corey.Fat@gmail.com')
        self.assertEqual(self.emp2.email,'Jim.Hanks@gmail.com')

        self.emp1.first='John'
        self.emp2.first='Jake'

        self.assertEqual(self.emp1.email,'John.Fat@gmail.com')
        self.assertEqual(self.emp1.email,'Jake.Hanks@gmail.com')

    def test_fullname(self):

        self.assertEqual(self.emp1.fullname,'Corey Fat')
        self.assertEqual(self.emp2.fullname,'Jim Hanks')

        self.emp1.first='John'
        self.emp2.first='Jake'

        self.assertEqual(self.emp1.fullname,'John Fat')
        self.assertEqual(self.emp2.fullname,'Jake Hanks')

    def test_apply_raise(self):

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay,52500)
        self.assertEqual(self.emp2.pay,63000)




















































if __name__=='__main__':
    unittest.main()