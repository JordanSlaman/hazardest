<template>
  <div class="row">
    <div class="col" id="redPoints">
      Red
    </div>
    <div class="col" id="blackPoints">
      Black
    </div>
  </div>


  <button @click="points['red']++">
    Red count is: {{ points['red'] }}
  </button>
  <button @click="points['black']++">
    Black count is: {{ points['black'] }}
  </button>

</template>

<script>
import fives from "@/modules/cards/animations/fives";

export default {
  name: "GamePoints",
  data() {
    return {
      points: {
        'red': 0,
        'black': 0
      },
      containers: {
        'red': null,
        'black': null
      }
    }
  },
  watch: {
    points() {
      fives.render_scores(this.containers, this.points)
    }
  },
  mounted() {
    this.containers['red'] = document.getElementById('redPoints');
    this.containers['black'] = document.getElementById('blackPoints');

    fives.render_scores(this.containers, this.points)

  }
}

</script>

<style scoped>

#redPoints {
    /* todo - not this */
  height: 300px;
  min-width: 150px;
}

#blackPoints {
    /* todo - not this */
  height: 300px;
  min-width: 150px;
}

</style>