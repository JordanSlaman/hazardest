<template>
  <component :is="currentView"/>
</template>

<script>
import axios from "axios";
import Cookies from 'js-cookie'

import GameList from './components/pages/GameList.vue'
import GameFrame from "@/components/pages/GameFrame";
import HomePage from './components/pages/HomePage.vue'
import NotFound from './components/pages/NotFound.vue'

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
    login() {
      axios.post("http://127.0.0.1:8000/api/users/login/", {}, {
        auth: {
          username: 'another_admin',
          password: 'admin123'
        }
      }).then(res => {
        this.user = res.data;
        console.log(this.user)
      }).catch(error => {
        this.user = null
        console.log("hello", this.user)
        console.log(error)
      })
    },
    logout() {
      axios.post("http://127.0.0.1:8000/api/users/logout/", {}, {
        auth: {
          username: 'another_admin',
          password: 'admin123'
        }
      }).then(res => {
        console.log(res.data)
        this.user = null
      }).catch(error => {
        console.log(error)
      })
    },
    get_user() {
      const csrfToken = Cookies.get('csrftoken');
      axios.get("http://127.0.0.1:8000/api/users/active/?format=json", {headers: {'X-CSRFToken': csrfToken}})
          .then(res => {
            this.user = res.data;
            console.log(this.user)
          })
          .catch(error => {
            this.user = null
            console.log("hello", this.user)
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
    this.get_user();
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
  src: local("Calligraphy"),   url(./assets/fonts/Calligraphy-D4pm.ttf) format("truetype");
}

</style>
