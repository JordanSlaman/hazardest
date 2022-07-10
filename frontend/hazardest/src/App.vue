<template>
  <HomePage/>
  <HeaderBar/>

  <!--  <img alt="Vue logo" src="./assets/logo.png">-->
  <!--  <h1 :id="magic">{{ message }}</h1>-->
  <!--  <button @click="increment">count is: {{ count }}</button>-->
</template>

<script>
import HomePage from './components/HomePage.vue'
import HeaderBar from './components/HeaderBar.vue'

export default {
  components: {
    HomePage,
    HeaderBar
  },
  data() {
      return {
        name: 'BootstrapVue',
        show: true
      }
    },
}

// export default {
//   data() {
//     return {
//       message: 'Hello World!',
//       count: 0,
//       magic: 'magic'
//     }
//   },
//   methods: {
//     increment() {
//       // update component state
//       this.count++
//     }
//   }
// }
</script>

<style>
</style>
