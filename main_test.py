import main


def test_menue(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: 'x')
    main.talk_to_user()
    captured = capsys.readouterr()
    assert captured.out == 'Lieber Benutzer, herzlich willkommen zu diesem Programm\n' \
                           '\n' \
                           '==============================================\n' \
                           'Was möchten Sie mit dieser Applikation machen?\n' \
                           'Wählen Sie \'f\' für Fibonacci-Reihe ausgeben\n' \
                           'Wählen Sie \'e\' für Kleines Einmaleins\n' \
                           'Wählen Sie \'g\' für Berechnung Gerade / Ungerade\n' \
                           'Wählen Sie \'x\' um das Programm zu beenden!\n'


def test_fibonacci(monkeypatch, capsys):
    inputs = iter(['f', '12', 'x'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.talk_to_user()
    captured = capsys.readouterr()
    assert captured.out == 'Lieber Benutzer, herzlich willkommen zu diesem Programm\n' \
                           '\n' \
                           '==============================================\n' \
                           'Was möchten Sie mit dieser Applikation machen?\n' \
                           'Wählen Sie \'f\' für Fibonacci-Reihe ausgeben\n' \
                           'Wählen Sie \'e\' für Kleines Einmaleins\n' \
                           'Wählen Sie \'g\' für Berechnung Gerade / Ungerade\n' \
                           'Wählen Sie \'x\' um das Programm zu beenden!\n' \
                           'Which position of the Fibonacci-List do you want to know?\n' \
                           '89\n' \
                           '\n' \
                           '==============================================\n' \
                           'Was möchten Sie mit dieser Applikation machen?\n' \
                           'Wählen Sie \'f\' für Fibonacci-Reihe ausgeben\n' \
                           'Wählen Sie \'e\' für Kleines Einmaleins\n' \
                           'Wählen Sie \'g\' für Berechnung Gerade / Ungerade\n' \
                           'Wählen Sie \'x\' um das Programm zu beenden!\n'


def test_einmaleins(monkeypatch, capsys):
    inputs = iter(['e', '6', 'x'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.talk_to_user()
    captured = capsys.readouterr()
    assert captured.out == 'Lieber Benutzer, herzlich willkommen zu diesem Programm\n' \
                           '\n' \
                           '==============================================\n' \
                           'Was möchten Sie mit dieser Applikation machen?\n' \
                           'Wählen Sie \'f\' für Fibonacci-Reihe ausgeben\n' \
                           'Wählen Sie \'e\' für Kleines Einmaleins\n' \
                           'Wählen Sie \'g\' für Berechnung Gerade / Ungerade\n' \
                           'Wählen Sie \'x\' um das Programm zu beenden!\n' \
                           'Which number do you want to learn?\n' \
                           '0\n' \
                           '6\n' \
                           '12\n' \
                           '18\n' \
                           '24\n' \
                           '30\n' \
                           '36\n' \
                           '42\n' \
                           '48\n' \
                           '54\n' \
                           '60\n' \
                           '\n' \
                           '==============================================\n' \
                           'Was möchten Sie mit dieser Applikation machen?\n' \
                           'Wählen Sie \'f\' für Fibonacci-Reihe ausgeben\n' \
                           'Wählen Sie \'e\' für Kleines Einmaleins\n' \
                           'Wählen Sie \'g\' für Berechnung Gerade / Ungerade\n' \
                           'Wählen Sie \'x\' um das Programm zu beenden!\n'


def test_even_odd(monkeypatch, capsys):
    inputs = iter(['g', '1231', 'x'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.talk_to_user()
    captured = capsys.readouterr()
    assert captured.out == 'Lieber Benutzer, herzlich willkommen zu diesem Programm\n' \
                           '\n' \
                           '==============================================\n' \
                           'Was möchten Sie mit dieser Applikation machen?\n' \
                           'Wählen Sie \'f\' für Fibonacci-Reihe ausgeben\n' \
                           'Wählen Sie \'e\' für Kleines Einmaleins\n' \
                           'Wählen Sie \'g\' für Berechnung Gerade / Ungerade\n' \
                           'Wählen Sie \'x\' um das Programm zu beenden!\n' \
                           'Enter a number to check for odd/even?\n' \
                           'Number 1231 is odd.\n' \
                           '\n' \
                           '==============================================\n' \
                           'Was möchten Sie mit dieser Applikation machen?\n' \
                           'Wählen Sie \'f\' für Fibonacci-Reihe ausgeben\n' \
                           'Wählen Sie \'e\' für Kleines Einmaleins\n' \
                           'Wählen Sie \'g\' für Berechnung Gerade / Ungerade\n' \
                           'Wählen Sie \'x\' um das Programm zu beenden!\n'