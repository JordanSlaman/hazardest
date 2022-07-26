<template>
  <HeaderBar/>

  <div class="container">
    <div class="col p-3">
      <div class="row">
        <span class="col-10"></span>
        <button v-if="this.user.isAuthenticated" type="button" class="btn btn-outline-primary col-2 mx-auto my-lg"
                data-bs-toggle="modal"
                data-bs-target="#staticBackdrop">
          New Game
        </button>
        <span v-else id="createGameLoggedOutToolTip" class="col-2" tabindex="0" data-bs-toggle="tooltip"
              data-bs-title="Must be logged in!"
              data-bs-placement="left">
          <button type="button" class="btn btn-outline disabled">New Game</button>
        </span>


      </div>
    </div>
  </div>

  <CreateGame/>

  <div class="container">
    <table class="table table-striped table-sm">
      <thead>
      <tr>
        <th scope="col">Game #</th>
        <th scope="col">Red Team</th>
        <th scope="col">Black Team</th>
        <th scope="col">Status</th>
        <th scope="col">Created</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="game in this.games" :key="game.pk">
        <td>{{ game.pk }}</td>

        <td class="card">
          <ul class="list-group list-group-flush">
              <li class="list-group-item">{{ game.players["position"] === "N" }}</li>
              <li class="list-group-item">{{ game.players["position"] === "S" }}</li>
          </ul>
<!--          <button class="btn btn-sm btn-outline-primary" disabled>slaman</button>-->
<!--          <button class="btn btn-sm btn-primary">Join</button>-->
        </td>

        <td class="card">
            <ul class="list-group list-group-flush">
              <li class="list-group-item"></li>
              <li class="list-group-item">A second item</li>
            </ul>
<!--          <button class="btn btn-sm btn-outline-primary" disabled>krista</button>-->
<!--          <button class="btn btn-sm btn-primary">Join</button>-->
        </td>

        <td>{{ game.game_state }}</td>
        <td>{{ createdAt(game) }}</td>
      </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
import moment from 'moment'
import {Tooltip} from 'bootstrap'
// import * as popper from '@popperjs/core'

import HeaderBar from '@/components/trim/HeaderBar.vue'
import CreateGame from '@/components/modals/CreateGame'

import {useUserStore} from '@/stores/user'
import gameApi from '@/modules/api/game'

export default {
  name: "GameList",
  // inject: ['user'],
  components: {
    CreateGame,
    HeaderBar,
  },
  setup() {
    const user = useUserStore();

    return {
      user
    }
  },
  data() {
    return {
      games: null
    }
  },
  mounted() {
    const self = this
    gameApi.gameList().then(function (response) {
      self.games = response.data
    }).catch(function (error) {
      if (error.response) {
        console.log(error.response)
      }
    });

    if (!self.user.isAuthenticated) {
      const tooltip = new Tooltip(document.getElementById('createGameLoggedOutToolTip'))

      console.log(tooltip)
    }
    // const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    // const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

  },
  methods: {
    createdAt(game) {
      return moment(game.created).fromNow()
    }
  }

}
</script>

<style scoped>

</style>