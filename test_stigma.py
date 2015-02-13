from stigma import StigReport
import pytest

s = StigReport()


class TestBasicFuctions:
	def get_percentage(self, number, total):
		return s.percentage(number,total)

	def test_pct(self):
		assert self.get_percentage(10, 100) == 10


class TestDictionaries:

	def test_severity_dict(self):
		assert type(s.severity_success) == dict
		assert len(s.severity_success) == 4

	def test_metrics_dict(self):
		assert type(s.metrics) == dict
		assert len(s.metrics) == 11


class TestListData:

	def test_lengths(self):
		assert len(s.rule_list) == len(s.pass_fail_list)
		assert len(s.rule_list) == len(s.title_list)
		assert len(s.rule_list) == len(s.description_list)
		assert len(s.rule_list) == len(s.severity_list)
		assert len(s.rule_list) == len(s.severity_list)
		assert len(s.rule_list) == len(s.fix_list)



