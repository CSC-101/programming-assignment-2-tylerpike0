import data
import hw2
import unittest

from data import Point, Rectangle, Duration, Song


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1

    def test_create_rectangle1(self):
        point1 = Point(-10, 5)
        point2 = Point(-20, -5)
        expected = Rectangle(Point(-20, 5), Point(-10,-5))
        actual = hw2.create_rectangle(point1,point2)
        self.assertEqual(expected, actual)

    def test_create_rectangle2(self):
        point1 = Point(5, 3)
        point2 = Point(4, 3)
        expected = Rectangle(Point(4, 3), Point(5,3))
        actual = hw2.create_rectangle(point1,point2)
        self.assertEqual(expected, actual)


    # Part 2

    def test_shorter_duration_than1(self):
        duration1 = Duration(23,53)
        duration2 = Duration(13,57)
        expected = False
        actual = hw2.shorter_duration_than(duration1,duration2)
        self.assertEqual(expected,actual)

    def test_shorter_duration_than2(self):
        duration1 = Duration(15,53)
        duration2 = Duration(15,57)
        expected = True
        actual = hw2.shorter_duration_than(duration1,duration2)
        self.assertEqual(expected,actual)

    # Part 3
    def test_songs_shorter_than1(self):
        songs = [Song("Florence + The Machine", "Lungs",Duration(4, 32)),
                 Song("The Black Keys", "Everlasting Light",Duration(3, 32)),
                 Song("The Arcs", "Keep On Dreamin'",Duration(4, 26))]
        duration = Duration(3,50)
        expected = [Song("The Black Keys", "Everlasting Light",Duration(3, 32))]
        actual = hw2.songs_shorter_than(songs, duration)
        self.assertEqual(expected, actual)

    def test_songs_shorter_than2(self):
        songs = [Song("Tame Impala", "Solitude is Bliss",Duration(2, 13)),
                 Song("Dan Auerbach", "Whispered Words",Duration(5, 32)),
                 Song("Cold War Kids", "We Used To Vacation",Duration(1, 32))]
        duration = Duration(2,13)
        expected = [Song("Cold War Kids", "We Used To Vacation",Duration(1, 32))]
        actual = hw2.songs_shorter_than(songs, duration)
        self.assertEqual(expected, actual)

    # Part 4

    def test_running_time1(self):
        songs = [Song("Tame Impala", "Solitude is Bliss", Duration(2, 13)),
                 Song("Dan Auerbach", "Whispered Words", Duration(5, 32)),
                 Song("Cold War Kids", "We Used To Vacation", Duration(1, 32))]
        playlist = [-1, 0,1,2,3]
        expected = Duration(9,17)
        actual = hw2.running_time(songs, playlist)
        self.assertEqual(expected, actual)

    def test_running_time2(self):
        songs = [Song("Florence + The Machine", "Lungs", Duration(4, 32)),
                 Song("The Black Keys", "Everlasting Light", Duration(3, 32)),
                 Song("The Arcs", "Keep On Dreamin'", Duration(4, 26))]
        playlist = [0,1, 0,2, 1]
        expected = Duration(20,34)
        actual = hw2.running_time(songs, playlist)
        self.assertEqual(expected, actual)
    # Part 5

    def test_validate_route1(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        expected = True
        actual = hw2.validate_route(city_links, route)
        self.assertEqual(expected, actual)

    def test_validate_route2(self):
        city_links = [
            ['san luis obispo', 'atascadero'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        expected = False
        actual = hw2.validate_route(city_links, route)
        self.assertEqual(expected, actual)

    # Part 6

    def test_longest_repetition1(self):
        nums = [1, 1, 2, 2, 1, 1, 1, 3]
        expected = 4
        actual = hw2.longest_repetition(nums)
        self.assertEqual(expected,actual)

    def test_longest_repetition2(self):
        nums = [-1, 5,5,2,2,2,2,4,1,6,6]
        expected = 3
        actual = hw2.longest_repetition(nums)
        self.assertEqual(expected,actual)



if __name__ == '__main__':
    unittest.main()
