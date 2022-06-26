<template>
      <nav class="navbar fixed-top navbar-light bg-faded">
      <a class="navbar-brand" style="color: #aaa" href="#">
        <img src="../assets/hazardest.png" width="38" height="29" class="d-inline-block align-top" alt="">
        hazardest
      </a>

      <ul class="nav justify-content-end">
        <!--<li class="nav-item">-->
        <!--<a class="nav-link active" href="#">Active</a>-->
        <!--</li>-->
        <li class="nav-item">
          <a class="nav-link" href="#about">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://reddit.com/r/hazardest/">Community</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">{{session.username}}</a>
        </li>

      </ul>

    </nav>
</template>

<script>
  export default {
    name: 'hazardest-nav',
    data() {
      return {
        session: {
          username: 'bob',
        },
      };
    },
  };
</script>

<style scoped>

.navbar {
    background-color: #222;
}

</style>
