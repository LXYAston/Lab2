import Lab2

def test_Findminmax():
    Test_arr = [2,4,3,5,1]
    result = Lab2.find_min_max(Test_arr)
    expected = [1, 5]
    assert(result == expected)


def test_CalcAverage():
    Test_arr = [2,4,3,5,1]
    result = Lab2.calc_average(Test_arr) #needs 2 dp rounded
    expected = 3.00
    assert(result == expected)

def test_Calc_median_even():
    Test_arr = [2,4,3,5,1,6]
    result = Lab2.calc_median_temperature(Test_arr)
    expected = 3.5
    assert(result == expected)

def test_Calc_median_odd():
    Test_arr = [2,4,3,5,1]
    result = Lab2.calc_median_temperature(Test_arr)
    expected = 3
    assert(result == expected)

