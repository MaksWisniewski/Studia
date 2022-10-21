def checking_unit_tests():
    unit_test_results = [True, True, True, True, False, True]
    passed_all = True
    for unit_test in unit_test_results:
        if unit_test == False:
            passed_all = False
            break
    return passed_all


checking_unit_tests()
