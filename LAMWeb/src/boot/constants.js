// axios boot file (src/boot/axios.js)

import Vue from 'vue'

const PERMS = {
  ADD_MUSIC: 0,
  EDT_MUSIC: 1,
  DEL_MUSIC: 2,
};

Vue.prototype.$perms = PERMS


export { PERMS }