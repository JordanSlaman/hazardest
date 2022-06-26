//import { Vue, createApp } from 'vue'
import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

//import App from './App.vue'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)


// This imports all the layout components such as <b-container>, <b-row>, <b-col>:
//import { LayoutPlugin } from 'bootstrap-vue'
//Vue.use(LayoutPlugin)

//createApp(App).mount('#app')
