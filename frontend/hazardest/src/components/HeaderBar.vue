<template>

  <div class="hazardest-header bg-dark text-white">

    <header class="py-3 mb-3">

      <div class="container-fluid d-grid gap-3 align-items-center" style="grid-template-columns: 1fr 2fr;">

        <div class="dropdown">
          <a href="#"
             class="d-flex align-items-center col-lg-4 mb-2 mb-lg-0 link-light text-decoration-none dropdown-toggle"
             id="dropdownNavLink" data-bs-toggle="dropdown" aria-expanded="false">
            <svg class="bi me-2" width="40" height="32">
              <use xlink:href="#bootstrap"></use>
            </svg>
            Hazardest
          </a>
          <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdownNavLink" style="">
            <li><a class="dropdown-item" href="#" aria-current="page">View Games</a></li>
            <li v-if="user"><a class="dropdown-item" href="#">Create Game</a></li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li><a class="dropdown-item" href="#">About</a></li>
          </ul>
        </div>

        <div v-if="user" class="d-flex align-items-center">
          <div class="flex-shrink-0 dropdown">
            <a href="#" class="d-block link-light text-decoration-none dropdown-toggle" id="dropdownUser2"
               data-bs-toggle="dropdown" aria-expanded="false">
              <img src="https://github.com/mdo.png" alt="mdo" class="rounded-circle" width="32" height="32">
              {{ user.username }}
            </a>
            <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdownUser2" style="">
              <li><a class="dropdown-item" href="#">Profile</a></li>
              <li>
                <hr class="dropdown-divider">
              </li>
              <li><a @click="logout" class="dropdown-item" href="#">Log out</a></li>
            </ul>
          </div>
        </div>

        <div v-else class="col-md-3 text-end">
          <button @click="login" type="button" class="btn btn-outline-primary me-2">Login</button>
          <button type="button" class="btn btn-primary">Sign-up</button>
        </div>

      </div>

    </header>
  </div>
</template>

<script>
export default {
  name: "HeaderBar",
  inject: ['user', 'login', 'logout']
}
</script>

<style scoped>

</style>