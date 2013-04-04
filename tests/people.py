import pycomicvine
import datetime
from tests.utils import *

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestPeopleList(ListResourceTestCase):
    def test_get_id_and_name(self):
        self.get_id_and_name_test(
                pycomicvine.People,
                pycomicvine.Person
            )

class TestPersonAttributes(SingularResourceTestCase):
    def setUp(self):
        self.get_random_instance(pycomicvine.People)

    def test_search(self):
        self.search_test(pycomicvine.People, pycomicvine.Person)

    def test_get_all_attributes(self):
        person = self.get_sample(pycomicvine.Person)
        if person != None:
            self.assertIsInstance(
                    person.aliases, 
                    (type(None),list)
                )
            self.assertIsInstance(
                    person.api_detail_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    person.birth, 
                    (type(None), datetime.datetime)
                )
            self.assertIsInstance(
                    person.count_of_issue_appearances,
                    (type(None),int)
                )
            self.assertIsInstance(
                    person.country,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    person.created_characters,
                    pycomicvine.Characters
                )
            self.assertIsInstance(
                    person.date_added,
                    datetime.datetime
                )
            self.assertIsInstance(
                    person.date_last_updated,
                    datetime.datetime
                )
            self.assertIsInstance(
                    person.death, 
                    (type(None), datetime.datetime)
                )
            self.assertIsInstance(
                    person.deck,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    person.description,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    person.email,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    person.gender,
                    unicode
                )
            self.assertIn(
                    person.gender,
                    [u'\u2842', u'\u2640', u'\u26a7']
                )
            self.assertIsInstance(
                    person.hometown,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    person.id,
                    int 
                )
            self.assertIsInstance(
                    person.image,
                    (type(None),dict)
                )
            self.assertIsInstance(
                    person.issue_credits,
                    pycomicvine.Issues
                )
            self.assertIsInstance(
                    person.name,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    person.site_detail_url,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    person.story_arc_credits,
                    pycomicvine.StoryArcs
                )
            self.assertIsInstance(
                    person.volume_credits,
                    pycomicvine.Volumes
                )
            self.assertIsInstance(
                    person.website,
                    (type(None),basestring)
                )
