import Vue from 'vue'
import { lamapi } from '../boot/axios'
import { uid } from 'quasar'

// The data goes here
const state = {
  login: null,
  email: null
};

// Contains not assynchronous -> Change state directly
const mutations = {
  doLogin (state, payload) {
    console.log('entrou aqui!');
    state.login = payload.login;
    state.email = payload.email;
  }
};

// Methods Assynchronous (Commits Mutations)
const actions = {
  async doLogin ({ commit }, payload) {
    const params = {
        login: payload.username,
        password: payload.password
    };
    
    try {
      const response = await lamapi.post('auth', params);
      const { data } = await response;
      console.log(data);
      commit('doLogin', { login: data.login, email: data.email });
      
    } catch (error) {  
      return false;
    }

    debugger;
    return true;
  }
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