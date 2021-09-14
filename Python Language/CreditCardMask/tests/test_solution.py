import CreditCardMask.problem.solution as sol

def test_blank_CC():
    cc = ''
    r = sol.maskify(cc)
    test_thing = ("masking: {0}".format(cc))
    another_test_thing = ("{0}  matches  {1}".format(cc,r))
    assert r == cc