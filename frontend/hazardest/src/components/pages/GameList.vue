<template>
  <HeaderBar/>

  <div class="container">
    <div class="col">
      <div class="row">
        <button type="button" class="btn btn-lg btn-primary col-4 mx-auto my-lg" data-bs-toggle="modal"
                data-bs-target="#staticBackdrop">
          Create New Game
        </button>
        <div v-if="!this.user" class="alert alert-warning" role="alert">Must be logged in!</div>
      </div>
    </div>
  </div>

  <!-- New Game Modal -->
  <CreateGame/>
<!--  <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"-->
<!--       aria-labelledby="staticBackdropLabel" aria-hidden="true">-->
<!--    <div class="modal-dialog">-->
<!--      <div class="modal-content">-->
<!--        <div class="modal-header">-->
<!--          <h5 class="modal-title" id="staticBackdropLabel">Create New Game</h5>-->
<!--          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>-->
<!--        </div>-->
<!--        <div class="modal-body">-->
<!--          Options?-->
<!--        </div>-->
<!--        <div class="modal-footer">-->
<!--          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>-->
<!--          <button type="button" class="btn btn-primary">Create</button>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->


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
      <tr>
        <td>1,001</td>
        <td>
          <button class="btn btn-sm btn-outline-primary" disabled>slaman</button>
          <button class="btn btn-sm btn-primary">Join</button>
        </td>
        <td>
          <button class="btn btn-sm btn-outline-primary" disabled>krista</button>
          <button class="btn btn-sm btn-primary">Join</button>
        </td>
        <td>Waiting for players!</td>
        <td>11 minutes ago</td>
      </tr>
      <tr>
        <td>1,000</td>
        <td>
          <button class="btn btn-sm btn-outline-primary" disabled>bob</button>
          <button class="btn btn-sm btn-primary">Join</button>
        </td>
        <td>
          <button class="btn btn-sm btn-primary">Join</button>
          <button class="btn btn-sm btn-primary">Join</button>
        </td>
        <td>Waiting for players!</td>
        <td>20 minutes ago</td>
      </tr>
      <tr>
        <td>999</td>
        <td>
          <button class="btn btn-sm btn-secondary" disabled>alice</button>
          <button class="btn btn-sm btn-secondary" disabled>dave</button>
        </td>
        <td>
          <button class="btn btn-sm btn-secondary" disabled>peter</button>
          <button class="btn btn-sm btn-secondary" disabled>jim</button>
        </td>
        <td>In Progress</td>
        <td>45 minutes ago</td>
      </tr>
      <tr>
        <td>998</td>
        <td>
          <button class="btn btn-sm btn-outline-secondary" disabled>slaman</button>
          <button class="btn btn-sm btn-outline-secondary" disabled>jim</button>
        </td>
        <td>
          <button class="btn btn-sm btn-outline-secondary" disabled>krista</button>
          <button class="btn btn-sm btn-outline-secondary" disabled>dave</button>
        </td>
        <td>Finished</td>
        <td>2 hours ago</td>
      </tr>

      </tbody>
    </table>

  </div>
</template>

<script>
import HeaderBar from '../HeaderBar.vue'
import CreateGame from "@/components/modals/CreateGame";

import {useUserStore} from '@/stores/user'

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
  }

}
</script>

<style scoped>

</style>