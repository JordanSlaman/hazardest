<template>

  <img class="rounded-circle align-middle" :src="this.gravatarUrl">
  {{player.username}}

</template>

<script>
export default {
  name: "MicroPlayerProfile",
  props: ['player'],
  data() {
    return {
      gravatarUrl: null
      // player: {
      //   username: null,
      //   gravatarUrl: null
      // }
    }
  },
  mounted() {
    console.log(this.player)
    this.gravatarUrl = this.player.gravatar_url + '&s=20'
  }
}
</script>

<style scoped>

</style>