<template>

  <div class="bg-dark text-white">

    <header class="p-3 mb-3">

      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between"
           style="grid-template-columns: 1fr 2fr;">

        <div class="dropdown">
          <a href="#"
             class="header-logo d-flex align-items-center col-lg-4 mb-2 mb-lg-0 link-light text-decoration-none dropdown-toggle"
             id="dropdownNavLink" data-bs-toggle="dropdown" aria-expanded="false">
            Hazardest
          </a>
          <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdownNavLink" style="">
            <li><a class="dropdown-item" href="#/" aria-current="page">Home</a></li>
            <li><a class="dropdown-item" href="#/games" aria-current="page">View Games</a></li>
            <li v-if="user.token"><a class="dropdown-item" href="#">Create Game</a></li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li><a class="dropdown-item" href="#">About</a></li>
          </ul>
        </div>

        <div v-if="user.token" class="d-flex align-items-center">
          <div class="flex-shrink-0 dropdown">
            <a href="#" class="d-block link-light text-decoration-none dropdown-toggle" id="dropdownUser2"
               data-bs-toggle="dropdown" aria-expanded="false">
              <img src="{{ user.gravatarUrl }}" alt="mdo" class="rounded-circle" width="32" height="32">
              {{ user.username }}
            </a>
            <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdownUser2" style="">
              <li><a class="dropdown-item" href="#">Profile</a></li>
              <li>
                <hr class="dropdown-divider">
              </li>
              <li>
                <button @click="user.logout" class="dropdown-item">Log out</button>
              </li>
            </ul>
          </div>
        </div>

        <div v-else class="col-md-3 text-end">
          <button type="button" class="btn btn-outline-primary me-2" data-bs-toggle="modal"
                  data-bs-target="#loginSignupModal">Login / Signup
          </button>
        </div>

      </div>

    </header>

    <LoginSignup/>
  </div>
</template>

<script>
import LoginSignup from "@/components/modals/LoginSignup";
import {useUserStore} from '@/stores/user'

export default {
  name: "HeaderBar",
  components: {LoginSignup},

  setup() {
    const user = useUserStore()
    return {
      user
    }
  },
  mounted() {
    // console.log('USER', this.user)
    // console.log('USERNAME', this.user.username)
  }
}
</script>

<style scoped>

.header-logo {
  font-family: "Calligraphy", Helvetica, Arial, sans-serif;
  font-size: 30pt;
  line-height: 0;
}

/*.header-logo .dropdown-toggle::after {*/
/*  padding-left: 30px;*/
/*}*/

.header-logo.dropdown-toggle::after {
  display: inline-block;
  margin: 8px 0 0 10px;
  vertical-align: .255em;
  content: "";
  border-top: .2em solid;
  border-right: .2em solid transparent;
  border-bottom: 0;
  border-left: .2em solid transparent;
}
</style>
