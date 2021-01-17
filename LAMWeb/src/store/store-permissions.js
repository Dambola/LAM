import Vue from 'vue'
import { axios_lam } from '../boot/axios'
import { uid } from 'quasar'

// The data goes here
const state = {
    permissions: []
};

// Contains not assynchronous -> Change state directly
const mutations = {
  reloadPermissions (state, permissions) {
    state.permissions = permissions;
  }
};

// Methods Assynchronous (Commits Mutations)
const actions = {
    reloadPermissions ({ commit }) {
    axios_lam.get('permission').then(response => {
      if (response.data.permissions) {
        commit('reloadPermissions', response.data.permissions);
      }
    }).catch(error => {
      console.log(error.response);
    });
  }
};

// Get data from a State
const getters = {
  permissions: (state) => {
    return state.permissions;
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
};