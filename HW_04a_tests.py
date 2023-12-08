import unittest
from HW_04a import github_parser

class test_github_parser(unittest.TestCase):
    def test_user_ID_name(self):
        self.assertEqual(github_parser('anthonymendo'),
                        [  "Repository Name: amendo Number of commits: 1",
                            "Repository Name: HW-01-Testing-triangle-classification Number of commits: 1",
                            "Repository Name: HW-02A-testing-a-legacy-program Number of commits: 6",
                            "Repository Name: HW00---Tools-Setup-Hello-World Number of commits: 1",
                            "Repository Name: SSW-567 Number of commits: 7" ])
    
    def test_user_ID_name_DNE(self):
        self.assertEqual(github_parser(""), "Repository not found") 

    def test_user_ID_name_rick(self):
        self.assertEqual(github_parser("richkempinski"), 
                        [ "Repository Name: csp Number of commits: 2", 
                            "Repository Name: hellogitworld Number of commits: 30", 
                            "Repository Name: helloworld Number of commits: 6",
                            "Repository Name: Mocks Number of commits: 10",
                            "Repository Name: Project1 Number of commits: 2",
                            "Repository Name: richkempinski.github.io Number of commits: 9",
                            "Repository Name: threads-of-life Number of commits: 1",
                            "Repository Name: try_nbdev Number of commits: 2",
                            "Repository Name: try_nbdev2 Number of commits: 5"])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()