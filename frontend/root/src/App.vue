<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
};
</script>

<style>
#app {
    /* font-family: 'Avenir', Helvetica, Arial, sans-serif; */
    background: #5C258D;  /* fallback for old browsers */
    background: -webkit-linear-gradient(135deg, #5C258D, #4389A2);  /* Chrome 10-25, Safari 5.1-6 */
    background: linear-gradient(135deg, #5C258D, #4389A2); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}
</style>
