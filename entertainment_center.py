import media
import fresh_tomatoes
"""
Based on file "fresh_tomatoes.py", make all movies into a list.

Based on file "media.py", each movie should
have three arguments(title, poster_image_url, trailer_youtube_url)
"""
a_chinese_odyssey_part_one = media.Movie("A Chinese Odyssey"
                                         "Part One: Pandora's Box",

                                         "https://upload.wikimedia.org/"
                                         "wikipedia/zh/5/5e/"
                                         "A_Chinese_Odyssey_1.jpg",

                                         "https://www.youtube.com/"
                                         "watch?v=niy5PmFzgLA")


a_chinese_odyssey_part_two = media.Movie("A Chinese Odyssey"
                                         "Part Two: Cinderella",

                                         "https://upload.wikimedia.org/"
                                         "wikipedia/zh/thumb/0/0c/"
                                         "A_Chinese_Odyssey_2.jpg/"
                                         "220px-A_Chinese_Odyssey_2.jpg",

                                         "https://www.youtube.com/"
                                         "watch?v=LnNKNApIOAo")


shaolin_soccer = media.Movie("Shaolin Soccer",

                             "https://upload.wikimedia.org/"
                             "wikipedia/zh/thumb/e/ea/%E5%B0%"
                             "91%E6%9E%97%E8%B6%B3%E7%90%83.jpg/"
                             "220px-%E5%B0%91%E6%9E%97%E8%B6%B3%"
                             "E7%90%83.jpg",

                             "https://www.youtube.com/"
                             "watch?v=6FAaOwNnHTA")


chungking_express = media.Movie("Chungking Express",

                                "https://upload.wikimedia.org/"
                                "wikipedia/zh/thumb/c/c0/"
                                "Chungking_Express.jpg/"
                                "220px-Chungking_Express.jpg",

                                "https://www.youtube.com/"
                                "watch?v=Tzz3cdKGUmw")


love_in_a_puff = media.Movie("Love In A Puff",

                             "https://upload.wikimedia.org/"
                             "wikipedia/zh/e/e6/Love_in_a_Puff.jpeg",

                             "https://www.youtube.com/"
                             "watch?v=kTOAhzIHhKU")


love_in_the_buff = media.Movie("Love in the Buff",

                               "https://upload.wikimedia.org/"
                               "wikipedia/zh/7/74/Love_in_the_Buff.jpg",

                               "https://www.youtube.com/"
                               "watch?v=yoF6gwe1UOA")


movies = [a_chinese_odyssey_part_one, a_chinese_odyssey_part_two,
          shaolin_soccer, chungking_express, love_in_a_puff, love_in_the_buff]

fresh_tomatoes.open_movies_page(movies)
