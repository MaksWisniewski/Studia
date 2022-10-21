# First, a compact but still too complicated solution:
def checking_unit_tests1():
    unit_test_results = [True, True, True, True, False, True]
    return True if len([unit_test for unit_test in unit_test_results if not unit_test]) == 0 else False


# Arguably almost or fully Pythonic:
def checking_unit_tests2():
    unit_test_results = [True, True, True, True, False, True]
    return not (False in unit_test_results)


def checking_unit_tests3():
    unit_testall_results = [True, True, True, True, False, True]
    return all(unit_testall_results)


print(checking_unit_tests1())
print(checking_unit_tests2())
print(checking_unit_tests3())
