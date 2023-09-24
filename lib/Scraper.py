from bs4 import BeautifulSoup
import requests
import ipdb
from Course import Course
import json


class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        doc = BeautifulSoup(requests.get(
            "http://learn-co-curriculum.github.io/site-for-scraping/courses").text, 'html.parser')
        return doc

    def get_courses(self):
        return self.get_page().select('.post')

    def make_courses(self):
        for course in self.get_courses():
            title = course.select("h2")[0].text if course.select("h2") else ''
            schedule = course.select(
                "em")[0].text if course.select("em") else ''
            description = course.select(
                "p")[0].text if course.select("p") else ''

            new_course = Course(title, schedule, description)
            self.courses.append(new_course)
        return self.courses

    def print_courses(self):
        for course in self.make_courses():
            print(course)


ipdb.set_trace()

# Call the method to see the output
scraper = Scraper()
scraper.print_courses()
