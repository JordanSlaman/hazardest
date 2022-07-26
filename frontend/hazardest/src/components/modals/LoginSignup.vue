<template>

  <div class="modal" id="loginSignupModal" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <nav class="nav nav-pills nav-fill" id="loginSignupNav">
            <a :class="{ active: navLoginSelected }" class="nav-link" href="#" data-bs-toggle="pill"
               @click="navLoginSelected = true">Login</a>
            <a :class="{ active: !navLoginSelected }" class="nav-link" href="#" data-bs-toggle="pill"
               @click="navLoginSelected = false">Sign-up</a>
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
            <template v-for="(errorMessage, index) in formData.errors.username" :key="index">
              <div class="alert alert-warning p-0" role="alert">{{ errorMessage }}</div>
            </template>

            <!--Email-->
            <div v-if="!navLoginSelected" class="form-floating mb-3">
              <input v-model="formData.fields.email" type="email" class="form-control" id="floatingInput"
                     placeholder="name@example.com">
              <label for="floatingInput">Email address</label>
            </div>
            <template v-for="(errorMessage, index) in formData.errors.email" :key="index">
              <div class="alert alert-warning p-0" role="alert">{{ errorMessage }}</div>
            </template>

            <!--Password-->
            <div class="form-floating mb-3">
              <input v-model="formData.fields.password" type="password" class="form-control" id="floatingPassword"
                     placeholder="Password"
                     style="background-repeat: no-repeat; background-size: auto 50%; background-position: 96% 50%;"
                     autocomplete="off" data-has-passwords-badge="true">
              <label for="floatingPassword">Password</label>
            </div>
            <template v-for="(errorMessage, index) in formData.errors.password" :key="index">
              <div class="alert alert-warning p-0" role="alert">{{ errorMessage }}</div>
            </template>

            <!--Password Confirm-->
            <div v-if="!navLoginSelected" class="form-floating mb-3">
              <input v-model="formData.fields.passwordConfirm" type="password" class="form-control"
                     id="floatingPassword" placeholder="Confirm Password"
                     style="background-repeat: no-repeat; background-size: auto 50%; background-position: 96% 50%;"
                     autocomplete="off" data-has-passwords-badge="true">
              <label for="floatingPassword">Confirm Password</label>
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

            <!--General Error-->
            <template v-for="(errorMessage, index) in formData.errors.generic" :key="index">
              <div class="alert alert-warning p-0" role="alert">{{ errorMessage }}</div>
            </template>

            <!--Signup Disclaimer-->
            <hr class="my-4" v-if="!navLoginSelected">
            <small v-if="!navLoginSelected" class="text-muted">By clicking Sign up, you agree to the terms of
              use.</small>

          </form>

        </div>

      </div>
    </div>
  </div>

</template>

<script>
import {Modal} from 'bootstrap'
import _ from 'lodash';

import {useUserStore} from '@/stores/user'

export default {
  name: "LoginSignup",
  // props: ['navLoginSelected'],
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
          username: [],
          email: [],
          password: [],
          generic: []
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
    hideModal() {
      this.loginSignupModal.hide()
      const modalBackdrops = document.getElementsByClassName('modal-backdrop');
      _.forEach(modalBackdrops, function (modalBackdropElement) {
        modalBackdropElement.remove();
      });
    },
    handleErrors(responseData) {
      const formErrors = this.formData.errors

      responseData['non_field_errors'] ? formErrors.generic = responseData['non_field_errors'] : []
      responseData['username'] ? formErrors.username = responseData['username'] : []
      responseData['email'] ? formErrors.email = responseData['email'] : []
      responseData['password1'] ? formErrors.password = responseData['password1'] : []
    },
    userLogin() {
      const self = this
      const formFields = self.formData.fields

      self.user.login(formFields.username, formFields.password).then(function (response) {
            console.log(response) // required for linting...
            self.hideModal()

            // todo if homepage route to game list
            self.$router.push('/games')
          }
      ).catch(function (error) {
        if (error.response) {
          self.handleErrors(error.response.data)
        }
      });

    },
    userSignup() {
      const self = this
      const formFields = this.formData.fields

      this.user.signup(formFields.username, formFields.email, formFields.password, formFields.passwordConfirm).then(function (response) {
        console.log(response) // required for linting...
        self.hideModal()

        // todo if homepage route to game list
        self.$router.push('/games')
      }).catch(function (error) {
        if (error.response) {
          self.handleErrors(error.response.data)
        }
      });
    },

  },
  mounted() {
    this.loginSignupModal = new Modal(document.getElementById('loginSignupModal'), {})
  }
}

</script>

<style scoped>

</style>