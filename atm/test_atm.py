import unittest
from .question1 import NumOfNotes
from .question2 import NotesDespensed

#python runs all file before is runs the function

class TestAtm(unittest.TestCase):
    def test_question1(self):
        note_5, note_2, note_1 = NumOfNotes(471)
        self.assertEqual(note_5,94)
        self.assertEqual(note_2,0)
        self.assertEqual(note_1,1)

    def test_question2(self):
        one_1, two_2, five_5, ten_10, twenty_20, fifty_50 = NotesDespensed(100, 200, 300, 400, 500, 600)
        self.assertEqual(one_1, 100)
        self.assertEqual(two_2, 100)
        self.assertEqual(five_5, 60)
        self.assertEqual(ten_10, 40)
        self.assertEqual(twenty_20, 25)
        self.assertEqual(fifty_50, 12)



#only run if the this particular file is ran
if __name__ == "__main__":
    unittest.main()      