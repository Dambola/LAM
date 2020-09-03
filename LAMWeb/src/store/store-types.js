import Vue from 'vue'
import { axios_lam } from '../boot/axios'
import { uid } from 'quasar'

// The data goes here
const state = {
  types: {}
};

// Contains not assynchronous -> Change state directly
const mutations = {
  reloadTypes (state, types) {
    state.types = types;
  }
};

// Methods Assynchronous (Commits Mutations)
const actions = {
  reloadTypes ({ commit }) {
    axios_lam.get('type').then(response => {
      if (response.data.types) {
        commit('reloadTypes', response.data.types);
      }
    });
  }
};

// Get data from a State
const getters = {
  types: (state) => {
    return state.types;
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
};