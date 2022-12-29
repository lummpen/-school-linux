import dz_1 as md

def test_not_password():
    assert md.password('password') == False

def test_more_6_characters():
    assert md.password('qwert') == False

def test_not_only_numbers():
    assert md.password(1232121412435) == False