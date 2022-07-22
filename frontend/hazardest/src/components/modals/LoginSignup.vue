<template>

  <div class="modal" id="loginSignupModal" tabindex="-1">
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
          <form class="p-4 p-md-5">

            <!--Username-->
            <div class="form-floating mb-3">
              <input v-model="formData.fields.username" type="email" class="form-control" id="floatingInput"
                     placeholder="Username">
              <label for="floatingInput">Username</label>
            </div>
            <div v-if="formData.errors.username" class="alert alert-warning p-0" role="alert">
              {{ formData.errors.username }}
            </div>

            <!--Email-->
            <div v-if="!navLoginSelected" class="form-floating mb-3">
              <input v-model="formData.fields.email" type="email" class="form-control" id="floatingInput"
                     placeholder="name@example.com">
              <label for="floatingInput">Email address</label>
            </div>
            <div v-if="formData.errors.email" class="alert alert-warning p-0" role="alert">
              {{ formData.errors.email }}
            </div>

            <!--Password-->
            <div class="form-floating mb-3">
              <input v-model="formData.fields.password" type="password" class="form-control" id="floatingPassword"
                     placeholder="Password"
                     style="background-repeat: no-repeat; background-size: auto 50%; background-position: 96% 50%;"
                     autocomplete="off" data-has-passwords-badge="true">
              <label for="floatingPassword">Password</label>
            </div>
            <div v-if="formData.errors.password" class="alert alert-warning p-0" role="alert">
              {{ formData.errors.password }}
            </div>

            <!--Password Confirm-->
            <div v-if="!navLoginSelected" class="form-floating mb-3">
              <input v-model="formData.fields.passwordConfirm" type="password" class="form-control"
                     id="floatingPassword" placeholder="Confirm Password"
                     style="background-repeat: no-repeat; background-size: auto 50%; background-position: 96% 50%;"
                     autocomplete="off" data-has-passwords-badge="true">
              <label for="floatingPassword">Confirm Password</label>
            </div>
            <div v-if="formData.errors.passwordConfirm" class="alert alert-warning p-0" role="alert">
              {{ formData.errors.passwordConfirm }}
            </div>

            <!--Submit Button-->
            <div class="form-floating mb-3">
              <button v-if="navLoginSelected"
                      @click="userLogin(formData.fields.username, formData.fields.password)"
                      type="button"
                      class="btn btn-outline-primary w-100">Login
              </button>
              <button
                  v-if="!navLoginSelected"
                  @click="userSignup(formData.fields.username, formData.fields.email, formData.fields.password, formData.fields.passwordConfirm)"
                  type="button" class="btn btn-outline-primary w-100">Sign-up
              </button>
            </div>


            <!--Signup Disclaimer-->
            <hr class="my-4" v-if="!navLoginSelected">
            <small v-if="!navLoginSelected" class="text-muted">By clicking Sign up, you agree to the terms of
              use.</small>


            <!--General Error-->
            <div v-if="formData.errors.generic" class="alert alert-warning p-0" role="alert">
              {{ formData.errors.generic }}
            </div>

          </form>

        </div>

      </div>
    </div>
  </div>

</template>

<script>
import {Modal} from 'bootstrap'

import {useUserStore} from '@/stores/user'

export default {
  name: "LoginSignup",
  data() {
    return {
      // isActive: true,
      navLoginSelected: true,
      loginSignupModal: null,
      formData: {
        submitFailed: false,
        fields: {
          username: '',
          email: '',
          password: '',
          passwordConfirm: ''
        },
        errors: {
          username: '',
          email: '',
          password: '',
          passwordConfirm: '',
          generic: ''
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
    createModal(loginSelected) {
      this.navLoginSelected = !!loginSelected
      this.loginSignupModal.show()
    },
    handleErrors(responseData) {
      const formErrors = this.formData.errors

      if (responseData['non_field_errors']) {
        formErrors.generic = responseData['non_field_errors'][0]
      } else if (responseData['username']) {
        formErrors.username = responseData['username']
      }
    },
    userLogin() {
      const self = this
      const formFields = self.formData.fields

      // formFields.submitFailed = false
      self.user.login(formFields.username, formFields.password).then(function (response) {

        console.log(response.data)  // for linting, maybe shouldn't log the token
        self.loginSignupModal.hide()

        // todo if homepage route to gamelist
        // self.$router.push('/games')

      }).catch(function (error) {
        if (error.response) {
          self.handleErrors(error.response.data)
        } else if (error.request) {
          // The request was made but no response was received
          // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
          // http.ClientRequest in node.js
          console.log(error.request);
        } else {
          // Something happened in setting up the request that triggered an Error
          console.log('Error', error.message);
        }
        console.log(error.config);
      });

    },
    userSignup() {
      const formFields = this.formData.fields
      this.user.signup(formFields.username, formFields.email, formFields.password, formFields.password)
    },

  },
  mounted() {
    this.loginSignupModal = new Modal(document.getElementById('loginSignupModal'), {})
  }
}

</script>

<style scoped>

</style>