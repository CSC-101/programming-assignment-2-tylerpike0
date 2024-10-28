from itertools import filterfalse

import data

# Write your functions for each part in the space below.

# Part 1
from data import Point
from data import Rectangle

# Takes in two points and returns the smallest rectangle that contains those points
# Input: Point
# Input: Point
# output: Rectangle
def create_rectangle(point1: Point, point2: Point) -> Rectangle:
    min_x = min(point1.x, point2.x)
    max_x = max(point1.x, point2.x)
    min_y = min(point1.y, point2.y)
    max_y = max(point1.y, point2.y)

    top_left = Point(min_x, max_y)
    bottom_right = Point(max_x, min_y)
    return Rectangle(top_left, bottom_right)



# Part 2
from data import Duration

# takes in two durations and returns true if the first is shorter than the second, else: false
# input: Duration
# input: Duration
# output: bool
def shorter_duration_than(duration1: Duration, duration2: Duration) -> bool:
    if duration1.minutes < duration2.minutes:
        return True
    elif duration1.minutes == duration2.minutes and duration1.seconds < duration2.seconds:
        return True
    else:
        return False


# Part 3

from data import Song

# Takes in a list of songs and returns a list of songs shorter than a given duration
# input: list[Song]
# input: duration
# output: list[Song]
def songs_shorter_than(songs: list[Song], duration: Duration) -> list[Song]:
    shorter_songs = []
    for song in songs:
        if shorter_duration_than(song.duration, duration):
            shorter_songs.append(song)
    return shorter_songs




# Part 4

# takes in a list of songs and a list of indices, and returns the total time of songs at those indices
# input: list[Song]
# input: list[int]
# output: Duration
def running_time(songs: list[Song], playlist: list[int]) -> Duration:
    total_duration = Duration(0, 0)
    for song_index in playlist:
        if song_index >= 0 and song_index < len(songs):
            total_duration = duration_add(total_duration, songs[song_index].duration)

    return total_duration


# takes in two durations and adds them together
# input: Duration
# input: Duration
# output: Duration
def duration_add(duration1: Duration, duration2: Duration) -> Duration:
    seconds = duration1.seconds + duration2.seconds
    minutes = duration1.minutes + duration2.minutes + seconds // 60
    seconds %= 60
    new_time = Duration(minutes, seconds)
    return new_time

# Part 5

# takes in a list of city links and a route and validates whether the route can be made with the given links
# input: list[list[str]]
# input: list[str]
# output: bool
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    if len(route) <= 1:
        return True
    for i in range(len(route) - 1):
        city_pair = [route[i], route[i+1]]
        reverse_city_pair = [route[i+1], route[i]]
        if not (city_pair in city_links or reverse_city_pair in city_links):
            return False
    return True

# Part 6
from typing import Optional

# takes in a list of integers and returns the starting index of the longest repetition in the list
# input: list[int]
# output: int
def longest_repetition(nums: list[int]) -> Optional[int]:
    if len(nums) == 0:
        return None
    current_repeating_number = nums[0]
    repetitions = 0
    current_repetition_start = 0
    current_longest_repetition_start = 0
    current_longest_repetition_count = 0
    for i in range(len(nums)):
        num = nums[i]
        if num == current_repeating_number: # continue repetition
            repetitions += 1
        else: # break repetitions
            # Check for new best
            if repetitions > current_longest_repetition_count:
                current_longest_repetition_count = repetitions
                current_longest_repetition_start = current_repetition_start

            # Reset info
            repetitions = 1
            current_repeating_number = num
            current_repetition_start = i

    return current_longest_repetition_start


