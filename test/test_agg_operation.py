"""
Basic unit tests for agg_operation
"""
from pymongo_aggregation.aggoperation import DocOperation, \
    match, Example_for_Sample_Op_with_name, lookup, count, sort
import unittest
import datetime

class Test( unittest.TestCase):

    def test_agg_op(self):

        op = DocOperation({"a": "b"})
        self.assertEqual( op.name(), "DocOperation")
        op = match( { "a" : "c"})
        self.assertEqual( op.name(), "match")

    def test_call(self):
        op = match( { "a" : "d"})
        self.assertEqual( { "$match" : {"a" : "d"}}, op())

    def test_op(self):
        op =match()

        self.assertEqual( op(), { "$match" : {}})

    def test_name_override(self):

        op = Example_for_Sample_Op_with_name()
        self.assertEqual( { "$sample" :    {}}, op())

    def test_repr(self):
        op = lookup()
        self.assertEqual( repr(op), "{\'$lookup\': {}}")

    def test_str(self):
        op = lookup()
        self.assertEqual( str(op), '{\'$lookup\': {}}')

    def test_ops_list(self):
        self.assertTrue( "match" in Agg_Operation.ops())
        self.assertFalse( "foobar" in Agg_Operation.ops())
        self.assertFalse( "AggOperation" in Agg_Operation.ops())
        #print("agg ops", AggOperation.ops())

    def test_match(self):
        now = datetime.datetime.utcnow()
        op=match()
        op.set_op( match.date_range_query(date_field="created",
                                          start=now))

        self.assertEqual( op(), {'$match': {'created': {'$gte': now }}})

    def test_count(self):

        op=count("counter")
        #print(op)
        self.assertRaises( ValueError, count, None)

    def test_sort(self):

        op = sort( name=1, date=-1 )
        #print(op)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
