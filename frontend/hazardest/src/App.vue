<template>
  <component :is="currentView"/>
</template>

<script>

import GameList from './components/pages/GameList.vue'
import GameFrame from "@/components/pages/GameFrame";
import HomePage from './components/pages/HomePage.vue'
import NotFound from './components/pages/NotFound.vue'

import * as Auth from './modules/api/Auth.js'

const routes = {
  '/': HomePage,
  '/games': GameList,
  '/game': GameFrame
}

export default {
  components: {
    HomePage,
    GameList,
    GameFrame
  },
  data() {
    return {
      currentPath: window.location.hash,
      user: null
    }
  },
  methods: {
    getUser() {
      Auth.getUser().then(user => {
        this.user = user
      }).catch(error => {
        console.log(error)
      })
    },
    login() {
      Auth.login('another_admin', 'admin123').then(user => {
        this.user = user
      }).catch(error => {
        console.log(error)
      })
    },
    logout() {
      Auth.logout().then(user => {
        this.user = user
      }).catch(error => {
        console.log(error)
      })
    }
  },
  computed: {
    currentView() {
      return routes[this.currentPath.slice(1) || '/'] || NotFound
    }
  },
  mounted() {
    this.getUser();
    window.addEventListener('hashchange', () => {
      this.currentPath = window.location.hash
    })
  },
  provide() {
    return {
      user: this.user,
      login: this.login,
      logout: this.logout,
    }
  }

}

</script>

<style>

@font-face {
  font-family: "Calligraphy";
  src: local("Calligraphy"), url(./assets/fonts/Calligraphy-D4pm.ttf) format("truetype");
}

</style>
