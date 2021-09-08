import pytest
from solution import multiply

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(multiply(2, 1), 2)
        test.assert_equals(multiply(0, 2), 0)
        test.assert_equals(multiply(8, 57), 456)