from Course import Course


class Test_Course:

    def test_title_instance_variable(self):
        "Test setting and getting for title"
        course = Course(title="Programming Robots for Outer Space",
                        schedule="Dummy", description="Dummy")
        assert course.title == "Programming Robots for Outer Space"
        # Add any further assertions if necessary

    def test_schedule_instance_variable(self):
        "Test setting and getting for schedule"
        course = Course(title="Dummy", schedule="Full-Time",
                        description="Dummy")
        assert course.schedule == "Full-Time"
        # Add any further assertions if necessary

    def test_description_instance_variable(self):
        "Test setting and getting for description"
        course = Course(title="Dummy", schedule="Dummy",
                        description="Learn how to program robots to explore the depths of space. Guest lecturer: The Mars Rover")
        assert course.description == "Learn how to program robots to explore the depths of space. Guest lecturer: The Mars Rover"
        # Add any further assertions if necessary
