import Vue from 'vue'
import { axios_lam } from '../boot/axios'
import { uid } from 'quasar'

// The data goes here
const state = {
  authors: {}
};

// Contains not assynchronous -> Change state directly
const mutations = {
  reloadAuthors (state, authors) {
    state.authors = authors;
  }
};

// Methods Assynchronous (Commits Mutations)
const actions = {
  reloadAuthors ({ commit }) {
    axios_lam.get('author').then(response => {
      if (response.data.authors) {
        commit('reloadAuthors', response.data.authors);
      }
    });
  }
};

// Get data from a State
const getters = {
  authors: (state) => {
    return state.authors;
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
};