<template>
  <!--  HomePage Hero -->
  <div id="homepage-hero" class="bg-dark text-secondary px-4 py-5 text-center">
    <div class="py-5">
      <h1 id="homepage-logo" class="text-white">Hazardest</h1>
      <div class="col-lg-6 mx-auto">
        <p class="fs-5 mb-4">Online Euchre</p>
      </div>
    </div>

    <div class="col-lg-6 mx-auto">
      <img src="https://getbootstrap.com/docs/5.2/examples/heroes/bootstrap-docs.png"
           class="img-fluid border rounded-3 shadow-lg mb-4" alt="Example image" loading="lazy" width="700"
           height="500">
    </div>

    <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
      <a href="#/games" role="button" class="btn btn-outline-info btn-lg px-4 me-sm-3 fw-bold">Play</a>

      <button v-if="!user.isAuthenticated" type="button"
              class="btn btn-outline-info btn-lg px-4 me-sm-3 fw-bold"
              data-bs-toggle="modal"
              data-bs-target="#loginSignupModal" @click="clickedLogin = true">
        Login
      </button>
      <button v-if="!user.isAuthenticated" type="button"
              class="btn btn-outline-info btn-lg px-4 me-sm-3 fw-bold"
              data-bs-toggle="modal"
              data-bs-target="#loginSignupModal" @click="clickedLogin = false">
        Signup
      </button>
      <button v-if="user.isAuthenticated" type="button"
              class="btn btn-outline-info btn-lg px-4 me-sm-3 fw-bold"
              @click="clickedLogin = true; user.logout()">
        Log out
      </button>
    </div>

    <LoginSignup nav-login-selected="clickedLogin"/>
  </div>


  <!--  includes tooltips!-->
  <!--  Hero Signup-->
  <!--  <div class="container">-->
  <!--    <div class="row align-items-center g-lg-5 py-5">-->
  <!--      <div class="col-lg-7 text-center text-lg-start">-->
  <!--        <h1 class="display-4 fw-bold lh-1 mb-3">Vertically centered hero sign-up form</h1>-->
  <!--        <p class="col-lg-10 fs-4">Below is an example form built entirely with Bootstrap’s form controls. Each-->
  <!--          required form group has a validation state that can be triggered by attempting to submit the form-->
  <!--          without completing it.</p>-->
  <!--      </div>-->
  <!--      <div class="col-md-10 mx-auto col-lg-5">-->
  <!--        <form class="p-4 p-md-5 border rounded-3 bg-light">-->
  <!--          <div class="form-floating mb-3">-->
  <!--            <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">-->
  <!--            <label for="floatingInput">Email address</label>-->
  <!--          </div>-->
  <!--          <div class="form-floating mb-3">-->
  <!--            <input type="password" class="form-control" id="floatingPassword" placeholder="Password"-->
  <!--                   style="background-repeat: no-repeat; background-size: auto 50%; background-position: 96% 50%;"-->
  <!--                   autocomplete="off" data-has-passwords-badge="true">-->
  <!--            <label for="floatingPassword">Password</label>-->
  <!--          </div>-->

  <!--          <div class="checkbox mb-3">-->
  <!--            <label>-->
  <!--              <input type="checkbox" value="remember-me"> Remember me-->
  <!--            </label>-->
  <!--          </div>-->

  <!--          <div class="row">-->
  <!--            <div class="col">-->
  <!--              <button class="w-100 btn btn-lg btn-outline-primary" type="submit">Login</button>-->
  <!--            </div>-->
  <!--            <div class="col">-->
  <!--              <button class="w-100 btn btn-lg btn-primary" type="submit">Sign-up</button>-->
  <!--            </div>-->

  <!--          </div>-->

  <!--          <hr class="my-4">-->
  <!--          <small class="text-muted">By clicking Sign up, you agree to the terms of use.</small>-->
  <!--        </form>-->
  <!--      </div>-->

  <!--    </div>-->
  <!--  </div>-->

  <!--      About-->
  <div class="container">
    <div class="row flex-lg-row-reverse align-items-center g-5 py-5">
      <div class="col-10 col-sm-8 col-lg-6">
        <img src="https://getbootstrap.com/docs/5.2/examples/heroes/bootstrap-docs.png"
             class="d-block mx-lg-auto img-fluid" alt="Bootstrap Themes" loading="lazy" width="700" height="500">
      </div>
      <div class="col-lg-6">
        <h1 class="display-5 fw-bold lh-1 mb-3">About</h1>

        <hr>

        <h5 class="display-5 fw-bold lh-1 mb-3">Euchre</h5>
        <p>Euchre is a trick-taking card game typically played with 4 players.
          https://en.wikipedia.org/wiki/Euchre</p>

        <hr>

        <h5 class="display-5 fw-bold lh-1 mb-3">Hazardest</h5>
        <p>The name Hazardest comes from a book, 'The Law and Practice of the Game of Euchre' written in
          1862.

          In the preliminary we find a quote from Honorable M. C., from the Tennessee State— who was wont emphatically
          to pronounce it the</p>
        <blockquote class="blockquote">
          <p>hazardestest game on the kcards;</p>
        </blockquote>


        <!--        <figure>-->
        <!--  <blockquote class="blockquote">-->
        <!--    <p>A well-known quote, contained in a blockquote element.</p>-->
        <!--  </blockquote>-->
        <!--  <figcaption class="blockquote-footer">-->
        <!--    Someone famous in <cite title="Source Title">Source Title</cite>-->
        <!--  </figcaption>-->
        <!--</figure>-->

        <p>I decided to write a euchre implementation as a python project one day, and later when I was on medical leave
          for terminal cancer I found myself seeking a project again and revisited Hazardest with the intention of
          making it into a playable web game.</p>

        <p>This website is the culmination of that effort.</p>

        <p>My professional background has been in backend web programming and cloud infrastructure, so it has been an
          interesting challenge to ramp up on the world of frontend web development.</p>

        <!--        <div class="d-grid gap-2 d-md-flex justify-content-md-start">-->
        <!--          <button type="button" class="btn btn-primary btn-lg px-4 me-md-2">Primary</button>-->
        <!--          <button type="button" class="btn btn-outline-secondary btn-lg px-4">Default</button>-->
        <!--        </div>-->
      </div>
    </div>
  </div>


  <FooterBar/>
</template>

<script>
import FooterBar from "@/components/trim/FooterBar";
import LoginSignup from "@/components/modals/LoginSignup";
import {useUserStore} from '@/stores/user'

export default {
  name: "HomePage",
  components: {
    FooterBar,
    LoginSignup
  },

  data() {
    return {
      clickedLogin: true
    }
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

#homepage-logo {
  font-family: "Calligraphy", Helvetica, Arial;
  font-size: 180pt;
  line-height: .6;
}

#homepage-hero {
  background-image: url("@/assets/img/bg/wild_oliva.webp");

  background-image: rgba(95, 0, 255, 1.0), url("@/assets/img/bg/wild_oliva.webp");
  background-image: -webkit-radial-gradient(top, rgba(95, 0, 255, 0.5), rgba(0, 0, 0, 0.8)), url("@/assets/img/bg/wild_oliva.webp");
  background-image: -moz-radial-gradient(top, rgba(95, 0, 255, 0.5), rgba(0, 0, 0, 0.8)), url("@/assets/img/bg/wild_oliva.webp");
  background-image: radial-gradient(to bottom, rgba(95, 0, 255, 0.5), rgba(0, 0, 0, 0.8)), url("@/assets/img/bg/wild_oliva.webp");

  /* Only works in FF, todo fux with... */
  background-image: -moz-radial-gradient(top, rgba(95, 0, 255, 0.5), rgba(0, 0, 0, 0.8)), url("@/assets/img/bg/wild_oliva.webp");

  /*  hex 5f00ff */

}
</style>