import Vue from 'vue'
import { axios_lam } from '../boot/axios'
import { uid } from 'quasar'

// The data goes here
const state = {
  login: null,
  email: null,
  access_token: null
};

// Contains not assynchronous -> Change state directly
const mutations = {
  doLogin (state, payload) {
    state.login = payload.login;
    state.email = payload.email;
    state.access_token = payload.access_token;
  }
};

// Methods Assynchronous (Commits Mutations)
const actions = {
  doLogin ({ commit }, payload) {
    const params = {
        login: payload.username,
        password: payload.password
    };

    return axios_lam.post('auth', params).then(response => {
        console.log(response);
        if (response.data.access_token) {
            console.log('doing mutation')

            commit('doLogin', {
                login: response.data.login, 
                email: response.data.email, 
                access_token: response.data.access_token
            });
            axios_lam.defaults.headers.common['Authorization'] = response.data.access_token;
            return true;
        }
        return false;
    }).catch(err => {
        console.log(err);
        return false;
    })
  },

  register(user) {
    return axios_lam.put('auth', {
      username: user.username,
      email: user.email,
      password: user.password
    });
  }
};

// Get data from a State
const getters = {
  user: (state) => {
    return { login: state.login, email: state.email };
  },
//   header_token: (state) => {
//     return { Authorization: 'Bearer ' + state.access_token }
//   }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
};