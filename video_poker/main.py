from flask import Flask, render_template, request, redirect, url_for, jsonify, session, redirect
from video_poker_module.draws import first_draw, second_draw
from video_poker_module.combinations import check_combination
from video_poker_module.winnings import calculate_points

app = Flask(__name__)
app.secret_key = "MySecretKey"

deck = ['2-h', '3-h', '4-h', '5-h', '6-h', '7-h', '8-h', '9-h', '10-h', 'J-h', 'Q-h', 'K-h', 'A-h', '2-d',
        '3-d',
        '4-d', '5-d', '6-d', '7-d', '8-d', '9-d', '10-d', 'J-d', 'Q-d', 'K-d', 'A-d', '2-c', '3-c', '4-c',
        '5-c',
        '6-c', '7-c', '8-c', '9-c', '10-c', 'J-c', 'Q-c', 'K-c', 'A-c', '2-s', '3-s', '4-s', '5-s', '6-s',
        '7-s',
        '8-s', '9-s', '10-s', 'J-s', 'Q-s', 'K-s', 'A-s']

deck_in_game = []

possible_combinations = [
    {"name": "Quinte Flush Royale", "req": "1 quinte flush avec as, roi, dame, valet, 10",
        "pts": "250 fois la mise"},
    {"name": "Quinte Flush", "req": "1 quinte de la même couleur",
        "pts": "50 fois la mise"},
    {"name": "Carre", "req": "4 cartes identiques", "pts": "25 fois la mise"},
    {"name": "Full", "req": "1 paire + 1 brelan", "pts": "9 fois la mise"},
    {"name": "Flush", "req": "5 cartes de la même couleur", "pts": "6 fois la mise"},
    {"name": "Quinte", "req": "5 cartes identiques", "pts": "4 fois la mise"},
    {"name": "Brelan", "req": "3 cartes identiques", "pts": "3 fois la mise"},
    {"name": "Double Paire", "req": "deux fois 2 cartes identiques",
        "pts": "2 fois la mise"},
    {"name": "Paire", "req": "2 cartes identiques", "pts": "1 fois la mise"}
]


@app.route('/play', methods=['POST'])
def keep_cards():
    cards_to_keep = request.get_json()

    new_hand = second_draw(cards_to_keep, session["deck_in_game"])

    combinations = check_combination(new_hand)

    winning_combination = ""
    for item in combinations:
        if combinations[item] == 1:
            winning_combination = item
        elif combinations[item] == 2:
            winning_combination = "Double Paire"

    winnings = calculate_points(combinations, int(session["bet"]))

    new_bankroll = int(session["bankroll"]) - int(session["bet"]) + winnings
    session["bankroll"] = new_bankroll

    return jsonify(new_hand, winning_combination, session['bankroll'])


@app.route('/', methods=['POST', 'GET'])
def index():
    session.clear()
    if request.method == 'POST':
        error = None
        try:
            bankroll = int(request.form['bankroll'])
            bet = int(request.form['bet'])

            if bankroll < bet:
                error = "Votre mise doit etre inférieur a votre cagnotte" 

        except:
            error = "Votre cagnotte et mise doivent être des nombres"

        if error is not None:
            return render_template('index.html', error=error)

        session["bankroll"] = bankroll - bet
        session["bet"] = bet

        return redirect(url_for('game'))

    return render_template('index.html', error="")


@app.route('/game')
def game():
    session["deck_in_game"] = deck.copy()
    hand = first_draw(session["deck_in_game"])

    return render_template('game.html', p_combinations=possible_combinations, hand=hand, bankroll=session["bankroll"], bet=session["bet"], statement="Veuillez séléctionner les cartes que vous voulez garder en main")


if __name__ == "__main__":
    app.run(debug=True)
