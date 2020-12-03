// axios boot file (src/boot/axios.js)

import Vue from 'vue'
import axios from 'axios'

// We create our own axios instance and set a custom base URL.
// Note that if we wouldn't set any config here we do not need
// a named export, as we could just `import axios from 'axios'`
const axios_lam = axios.create({
  baseURL: process.env.API_URL
})

// for use inside Vue files through this.$axios
Vue.prototype.$axios = axios_lam

// Here we define a named export
// that we can later use inside .js files:
export { axios_lam }