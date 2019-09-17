import printtable

def test_multtable():
    assert printtable.get_multtable(7, 3)  == [7, 14, 21]
