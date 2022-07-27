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


        <td>
        <div class="card">
          <ul class="list-group list-group-flush">
            <li class="list-group-item">
              <MicroPlayerProfile v-if="this.playerAt(game.players, 'N')" :player="this.playerAt(game.players, 'N')"/>
              <button v-else class="btn btn-sm btn-outline-primary">Join Game</button>
            </li>
            <li class="list-group-item">
              <MicroPlayerProfile v-if="this.playerAt(game.players, 'S')" :player="this.playerAt(game.players, 'S')"/>
              <button v-else class="btn btn-sm btn-outline-primary">Join Game</button>
            </li>
          </ul>
        </div>
        </td>

        <td>
          <div class="card">
            <ul class="list-group list-group-flush">
              <li class="list-group-item">
                <MicroPlayerProfile v-if="this.playerAt(game.players, 'E')" :player="this.playerAt(game.players, 'E')"/>
                <button v-else :class="{ disabled: !this.user.isAuthenticated}" class="btn btn-sm btn-outline-primary">Join Game</button>
              </li>
              <li class="list-group-item">
                <MicroPlayerProfile v-if="this.playerAt(game.players, 'W')" :player="this.playerAt(game.players, 'W')"/>
                <button v-else :class="{ disabled: !this.user.isAuthenticated}" class="btn btn-sm btn-outline-primary">Join Game</button>
              </li>
            </ul>
          </div>
        </td>

<!--        TODO Join buttons -->

        <!--&lt;!&ndash;          <button class="btn btn-sm btn-outline-primary" disabled>krista</button>&ndash;&gt;-->
        <!--&lt;!&ndash;          <button class="btn btn-sm btn-primary">Join</button>&ndash;&gt;-->
        <!--        </td>-->

        <td>{{ game.game_state }}</td>
        <td>{{ createdAt(game) }}</td>
      </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
import _ from 'lodash'
import moment from 'moment'
import {Tooltip} from 'bootstrap'

import CreateGame from '@/components/modals/CreateGame'
import HeaderBar from '@/components/trim/HeaderBar'
import MicroPlayerProfile from '@/components/trim/MicroPlayerProfile'

import {useUserStore} from '@/stores/user'
import gameApi from '@/modules/api/game'

export default {
  name: "GameList",
  // inject: ['user'],
  components: {
    MicroPlayerProfile,
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
      new Tooltip(document.getElementById('createGameLoggedOutToolTip'))
    }

  },
  methods: {
    createdAt(game) {
      return moment(game.created).fromNow()
    },
    playerAt(players, position) {
      const key = _.findKey(players, function (o) {
        return o.position === position;
      })
      return players[key]
    }
  }

}


// somehow handle player rendering by team/position
// {{ game.players["position"] === "N" }}

</script>

<style scoped>

</style>