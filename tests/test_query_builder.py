import unittest
from shub_query_adapter.query_builder import QueryBuilder

class TestQueryBuilder(unittest.TestCase):

    def test_basic_query_building(self):
        query = (QueryBuilder()
                 .select()
                 .from_("684510/2/17")
                 .where('status').equals('Scheduled')
                 .and_('gate').equals('A9')
                 .limit(1)
                 .build())
        
        expected_query = {
            "select": [],
            "from": "684510/2/17",
            "where": ["status = \"Scheduled\"", "gate = \"A9\""],
            "limit": 1
        }
        
        self.assertEqual(query, expected_query)

    def test_exists_operator(self):
        query = (QueryBuilder()
                 .select()
                 .from_("684510/2/17")
                 .where('status').exists()
                 .build())
        
        expected_query = {
            "select": [],
            "from": "684510/2/17",
            "where": ["status exists"]
        }
        
        self.assertEqual(query, expected_query)

if __name__ == '__main__':
    unittest.main()
