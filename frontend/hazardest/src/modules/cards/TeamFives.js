var $container = document.getElementById('container');

var full_deck = Deck();

/* var red_fives = Deck(); */
/* var black_fives = Deck(); */

// Remove 10 cards starting from the 6th
/* var removedCards = deck.cards.splice(5, 10);

removedCards.forEach(function (removedCard) {
    removedCard.unmount();
}); */


// remove 2 splices? one for each side of the 5's

/* _.forEach(red_fives, function(card) {
  card.unmount();
});
_.forEach(black_fives, function(card) {
  card.unmount();
});
 */

// Select the first card
var fives = {
  'diamonds': full_deck.cards[43],
  'clubs': full_deck.cards[30],
  'hearts': full_deck.cards[17],
  'spades': full_deck.cards[4],
};

_.forEach(fives, function(card, key) {
/*   if (key === 'diamonds' || key === 'hearts') {
    card.mount(red_fives);
  } else {
    card.mount(black_fives);
  } */

  card.setSide('front');
  card.enableDragging();
  card.mount($container);



  card.animateTo({
    delay: 0,
    duration: 0,
    ease: 'quartOut',

    x: Math.random() * window.innerWidth - window.innerWidth / 2,
    y: Math.random() * window.innerHeight - window.innerHeight / 2
  });
});


/* red_fives.mount($container); */
/* black_fives.mount($container); */


var point_position = [
    // index 0..10;
    // flipped bool
    // top_card x, y, angle
];
