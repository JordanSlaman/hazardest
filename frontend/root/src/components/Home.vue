<template>
  <div class="container">
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

  <!-- Content here -->
    <div class="row call-to-action">
      <div class="col-8 text-center">
        <h1>Online Euchre</h1>
        <h3><span>{{qty_tables}}</span> Tables</h3>
        <h3>62 Online</h3>
        <button type="submit" class="btn-lg btn-outline-primary">Play Now!</button>
      </div>


      <div class="col-4">
        <form>
          <div class="form-group">
            <label for="username_input">Username</label>
            <input type="text" class="form-control" id="username_input" placeholder="Username">
          </div>
          <div class="form-group">
            <label for="password_input">Password</label>
            <input type="password" class="form-control" id="password_input" placeholder="Password">
          </div>
          <button type="submit" id="btn-register" class="btn btn-primary float-right" @click="register">Register</button>
          <button type="submit" id="btn-login" class="btn btn-secondary float-right" @click="login">Login</button>
        </form>
      </div>
    </div>

    <div id="about" class="row">
      <div class="col">
        <h2>About</h2>
        <h4>Hazardest is a free online multiplayer Euchre card game.</h4>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'index',
    data() {
      return {
        session: {
          username: 'bob',
        },
        qty_tables: 23,
      };
    },
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.navbar {
    background-color: #222;
}


.call-to-action {
    padding-top: 300px;
}

#btn-register {
    margin-left: 15px;
}

#about {
}

footer {
    background: white;
    padding-top: 50px;
}
</style>
