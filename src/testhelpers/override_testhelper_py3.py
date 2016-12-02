'''
Created on 01.12.2016

This file causes NameErrors if forward-declarations
of Types are not supported properly.
(unless typechecker.check_override_at_runtime == False)

@author: Stefan Richthofer

todo: involve something like [str, int, 'TestClass2']
'''
from typechecker import override

class TestClass():
	def test_meth0(self, a: int) -> str:
		pass

	def test_meth1(self, a: 'TestArg2') -> str:
		pass

	def test_meth2(self, a: int) -> 'TestResult1':
		pass

class TestClass2(TestClass):
	@override
	def test_meth0(self, a: int) -> str:
		pass

	@override
	def test_meth1(self, a: 'TestArg1') -> str:
		pass

	@override
	def test_meth2(self, a: int) -> 'TestResult2':
		pass

class TestClass3(TestClass):
	@override
	def test_meth1(self, a: 'TestArg1') -> str:
		pass

	@override
	def test_meth2(self, a: int) -> 'TestResult2':
		pass

class TestArg1():
	pass

class TestResult1():
	pass

class TestClass3(TestClass):
	@override
	def test_meth1(self, a: TestArg1) -> str:
		pass

	@override
	def test_meth2(self, a: int) -> 'TestResult2':
		pass

class TestArg2(TestArg1):
	pass

class TestResult2(TestResult1):
	pass