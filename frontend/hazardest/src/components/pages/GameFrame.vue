<template>
  <HeaderBar/>

<!--  Bootstrap css collision?-->
<!--  need to figure out sass or something-->
<!--  <link rel="stylesheet" href="node_modules/deck-of-cards/example/example.css">-->
<!--  <script src="node_modules/deck-of-cards/dist/deck.min.js"></script>-->

  <div id="gameFrame" class="container-fluid">

    <div class="row">
      <div class="col">
        <GamePoints/>
      </div>
      <div class="col">
        Top Player
      </div>
      <div class="col">
        Log & Settings
      </div>
    </div>

<!--    <div class="row">-->
<!--      <div class="col">-->
<!--        Left Player-->
<!--      </div>-->
<!--      <div class="col">-->
<!--        Centre Table-->
<!--      </div>-->
<!--      <div class="col">-->
<!--        Right Player-->
<!--      </div>-->
<!--    </div>-->

<!--    <div class="row">-->
<!--      <div class="col">-->
<!--        ??-->
<!--      </div>-->
<!--      <div class="col">-->
<!--        Active Player-->
<!--      </div>-->
<!--      <div class="col">-->
<!--        ??-->
<!--      </div>-->
<!--    </div>-->
  </div>

</template>

<script>
import HeaderBar from '@/components/trim/HeaderBar.vue'
import GamePoints from "@/components/game/GamePoints";

export default {
  name: "GameFrame",
  components: {
    GamePoints,
    HeaderBar,
  }
}
</script>

<style scoped>
#gameFrame {
  /*background-color: #45a173;*/
  background: url("@/assets/img/bg/denim_bright.webp");

  /* todo - not this */
  height: 1000px;
}
</style>