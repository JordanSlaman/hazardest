import Deck from 'deck-of-cards';

const deck = Deck();


const suits = {
  /* 'spades': deck.cards.splice(1, 7), */
  /* 'hearts': deck.cards.splice(8, 14),
  'clubs': deck.cards.splice(26, 33),
  'diamonds': deck.cards.splice(1, 7), */
}


//spades
_.forEach(_.range(1, 8), function(value) {
  removedCard = deck.cards[value];
  removedCard.unmount();
})
// clubz
_.forEach(_.range(27, 34), function(value) {
  removedCard = deck.cards[value];
  removedCard.unmount();
})

//hearts
_.forEach(_.range(14, 21), function(value) {
  removedCard = deck.cards[value];
  removedCard.unmount();
})
// diamonds
_.forEach(_.range(40, 47), function(value) {
    removedCard = deck.cards[value];
    removedCard.unmount();
})



/*   _.forIn(suits, function(value, key) {
  console.log(key);
  value.forEach(function(removedCard) {
    removedCard.unmount();
  });
  }); */

deck.flip();
deck.fan();


export default {

}