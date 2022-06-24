from palindrome.palindrome import palindrome


def test_palindrome_assertion_one():
    assert palindrome.findOrReturnNull('Racecar') == 'racecar'

def test_palindrome_assertion_two():
    assert palindrome.findOrReturnNull('Red rum, sir, is murder') == 'redrumsirismurder'

def test_palindrome_assertion_three():
    assert palindrome.findOrReturnNull('12345') == None

def test_palindrome_assertion_four():
    assert palindrome.findOrReturnNull('123acacacb123') == 'acaca'

def test_palindrome_assertion_five():
    assert palindrome.findOrReturnNull('xx') == None

def test_palindrome_assertion_six():
    assert palindrome.findOrReturnNull('xxx') == 'xxx'

def test_palindrome_assertion_seven():
    assert palindrome.findOrReturnNull('.....x , 1 ?! x......') == 'x1x'

def test_palindrome_assertion_eight():
    assert palindrome.findOrReturnNull('aaa bbb ccc') == 'aaa'

def test_palindrome_assertion_nine():
    assert palindrome.findOrReturnNull('aaa b!..cbcb ccc') == 'bcbcb'

def test_palindrome_assertion_ten():
    assert palindrome.findOrReturnNull('01234!..??**3210') == '012343210'

def test_palindrome_assertion_eleven():
    assert palindrome.findOrReturnNull('-1-2-3-4-3-2-1') == '1234321'

def test_palindrome_assertion_twelve():
    assert palindrome.findOrReturnNull('gfst177!!redivideracabccb') == 'redivider'

def test_palindrome_assertion_thirteen():
    assert palindrome.findOrReturnNull('sdaadrotor776!!deified;;') == 'deified'