import Deck from 'deck-of-cards';

const deck = Deck();

const fives = {
    'diamonds': deck.cards[43],
    'clubs': deck.cards[30],
    'hearts': deck.cards[17],
    'spades': deck.cards[4],
};

const topCardPositions = {
    0: {
        'x': 6,
        'y': 6,
        'rot': 14
    },
    1: {
        'x': 20,
        'y': 14,
        'rot': 18
    },
    2: {
        'x': 2,
        'y': 32,
        'rot': 0
    },
    3: {
        'x': 2,
        'y': 68,
        'rot': 0
    },
    4: {
        'x': 36,
        'y': 20,
        'rot': 30
    }
}

export default {
    render_scores(containers, points) {
        this.render_score(containers['red'], 'red', points['red'])
        this.render_score(containers['black'], 'black', points['black'])
    },
    render_score(container, team, points) {
        let bottom_card
        let top_card

        if (team === 'red') {
            bottom_card = fives['diamonds']
            top_card = fives['hearts']
        } else if (team === 'black') {
            bottom_card = fives['clubs']
            top_card = fives['spades']
        } else {
            console.error('Invalid team passed, must be "red" or "black"')
        }

        bottom_card.mount(container);
        bottom_card.setSide('front');
        top_card.mount(container);

        let pos_index = points;
        if (points >= 5) {
            bottom_card.setSide('front');
            pos_index -= 5
        }

        top_card.animateTo({
            x: topCardPositions[pos_index]['x'],
            y: topCardPositions[pos_index]['y'],
            rot: topCardPositions[pos_index]['rot']
        });
    }
}

