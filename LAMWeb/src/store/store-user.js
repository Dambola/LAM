import Vue from 'vue'
import { axios_lam } from '../boot/axios'
import { uid } from 'quasar'

// The data goes here
const state = {
  login: null,
  email: null
};

// Contains not assynchronous -> Change state directly
const mutations = {
  reloadUser (state, payload) {
    state.login = payload.login;
    state.email = payload.email;
  }
};

// Methods Assynchronous (Commits Mutations)
const actions = {
  doLogin ({ commit }, payload) {
    const params = {
        login: payload.username,
        password: payload.password
    };

    return axios_lam.post('auth', params)
    .then(response => {
        return true;
    })
    .finally(function() {
      return false;
    });
  },

  reloadUser({ commit }) {
    axios_lam.get('auth').then(response => {
      const payload = {
        'username': response.data.login,
        'password': response.data.email
      };
      
      commit('reloadTypes', payload);
    });
  },

  register (user) {
    return axios_lam.put('auth', {
      username: user.username,
      email: user.email,
      password: user.password
    });
  },
};

// Get data from a State
const getters = {
  user: (state) => {
    return { login: state.login, email: state.email };
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
};