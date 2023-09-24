class Course:
    def __init__(self, title, schedule, description):
        self.title = title
        self.schedule = schedule
        self.description = description

    def __str__(self):
        course_str = ''
        course_str += f'title: {self.title}\n'
        course_str += f'schedule: {self.schedule}\n'
        course_str += f'description: {self.description}\n'
        course_str += '------------------'
        return course_str
