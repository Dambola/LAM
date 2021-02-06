// axios boot file (src/boot/axios.js)

import Vue from 'vue'
import axios from 'axios'
import router from '../router'

// We create our own axios instance and set a custom base URL.
// Note that if we wouldn't set any config here we do not need
// a named export, as we could just `import axios from 'axios'`
const lamapi = axios.create({
  baseURL: process.env.API_URL,
  withCredentials: true,  
})

lamapi.interceptors.response.use(
  (response) => {
    return response
  },

  (error) => {
    const response = error.response;
    if (401 === response.status && response.data.mustReload) {
      router.push('/login');
    }
    return Promise.reject(error)
  }
)

// for use inside Vue files through this.$axios
Vue.prototype.$axios = lamapi

// Here we define a named export
// that we can later use inside .js files:
export { lamapi }