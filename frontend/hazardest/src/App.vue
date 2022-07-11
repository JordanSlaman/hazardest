<template>
  <!--  <HomePage/>-->
  <HeaderBar>{{ user }}</HeaderBar>
  <GameList>{{ user }}</GameList>

  <!--  <img alt="Vue logo" src="./assets/logo.png">-->
  <!--  <h1 :id="magic">{{ message }}</h1>-->
  <!--  <button @click="increment">count is: {{ count }}</button>-->
</template>

<script>
import axios from "axios";
import Cookies from 'js-cookie'

// import HomePage from './components/HomePage.vue'
import HeaderBar from './components/HeaderBar.vue'
import GameList from './components/GameList.vue'

export default {
  components: {
    // HomePage,
    HeaderBar,
    GameList
  },
  data() {
    return {
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
  mounted() {
    this.get_user()
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
</style>
