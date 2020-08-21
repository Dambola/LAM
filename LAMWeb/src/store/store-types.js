import Vue from 'vue'
import { axiosInstance } from '../boot/axios'
import authHeader from '../services/header-auth'
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
    axiosInstance.get('type', { headers: authHeader() }).then(response => {
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