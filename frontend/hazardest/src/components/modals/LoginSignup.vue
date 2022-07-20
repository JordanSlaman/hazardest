<template>

  <div class="modal fade" id="loginSignupModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
       aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <nav class="nav nav-pills nav-fill" id="loginSignupNav">
            <a class="nav-link active" aria-current="page" href="#" data-bs-toggle="pill"
               @click="navLoginSelected = true">Login</a>
            <a class="nav-link" href="#" data-bs-toggle="pill" @click="navLoginSelected = false">Sign-up</a>
          </nav>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>

        <div class="modal-body">

          <!-- Login-->
          <form v-if="navLoginSelected" class="p-4 p-md-5">
            <div class="form-floating mb-3">
              <input v-model="formData.login.username" type="email" class="form-control" id="floatingInput"
                     placeholder="name@example.com">
              <label for="floatingInput">Username or Email address</label>
            </div>
            <div class="form-floating mb-3">
              <input v-model="formData.login.password" type="password" class="form-control" id="floatingPassword"
                     placeholder="Password"
                     style="background-repeat: no-repeat; background-size: auto 50%; background-position: 96% 50%;"
                     autocomplete="off" data-has-passwords-badge="true">
              <label for="floatingPassword">Password</label>
            </div>

            <button @click="userLogin(formData.login.username, formData.login.password)" type="button"
                    class="btn btn-outline-primary w-100">Login
            </button>
          </form>

          <!-- Signup-->
          <form v-if="!navLoginSelected" class="p-4 p-md-5">
            <div class="form-floating mb-3">
              <input v-model="formData.signup.username" type="username" class="form-control" id="floatingInput"
                     placeholder="coolplayer123">
              <label for="floatingInput">Username</label>
            </div>
            <div class="form-floating mb-3">
              <input v-model="formData.signup.email" type="email" class="form-control" id="floatingInput"
                     placeholder="name@example.com">
              <label for="floatingInput">Email address</label>
            </div>
            <div class="form-floating mb-3">
              <input v-model="formData.signup.password1" type="password" class="form-control" id="floatingPassword"
                     placeholder="Password"
                     style="background-repeat: no-repeat; background-size: auto 50%; background-position: 96% 50%;"
                     autocomplete="off" data-has-passwords-badge="true">
              <label for="floatingPassword">Password</label>
            </div>
            <div class="form-floating mb-3">
              <input v-model="formData.signup.password2" type="passwordConfirm" class="form-control"
                     id="floatingPassword" placeholder="Password"
                     style="background-repeat: no-repeat; background-size: auto 50%; background-position: 96% 50%;"
                     autocomplete="off" data-has-passwords-badge="true">
              <label for="floatingPassword">Confirm Password</label>
            </div>

            <button
                @click="userSignup()"
                type="button" class="btn btn-outline-primary w-100">Sign-up
            </button>

            <hr class="my-4">
            <small class="text-muted">By clicking Sign up, you agree to the terms of use.</small>

          </form>


        </div>

      </div>
    </div>
  </div>

</template>

<script>
// import {Toast} from 'bootstrap'

import {useUserStore} from '@/stores/user'

export default {
  name: "LoginSignup",
  data() {
    return {
      // isActive: true,
      navLoginSelected: true,
      formData: {
        login: {
          username: '',
          password: ''
        },
        signup: {
          username: '',
          email: '',
          password1: '',
          password2: ''
        }
      }
    }
  },
  setup() {
    const user = useUserStore()
    return {
      user
    }
  },
  methods: {
    userLogin() {
      this.user.login(this.formData.login.username, this.formData.login.password).then(res => {
        console.log('success', res.data);

        // todo find a way to dismiss the fucking modal
        // this.isActive = false;

        // todo if homepage route to gamelist
        // this.$router.push('/games')

      }).catch(error => {
        console.log('fail', error);

        // hande errors in UI

      });

      // this.user.login(this.formData.login.username, this.formData.login.password)

    },
    userSignup() {
      this.user.signup(this.formData.signup.username, this.formData.signup.email, this.formData.signup.password1, this.formData.signup.password2)
    }
  }
  // mounted() {
  //   const loginSignupModal = document.getElementById('loginSignupModal');
  //   const loginSignupNav = document.getElementById('loginSignupNav');
  //
  //   loginSignupModal.addEventListener('shown.bs.modal', () => {
  //     loginSignupNav.focus();
  //   });
  // }
}

</script>

<style scoped>

</style>