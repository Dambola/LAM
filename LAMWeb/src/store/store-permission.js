import Vue from 'vue'
import axios from 'axios'
import authHeader from '../services/header-auth'
import { uid } from 'quasar'

const API_URL = 'http://localhost:8081/music';

// The data goes here
const state = {
  permission: {}
};

// Contains not assynchronous -> Change state directly
const mutations = {
  reloadMusics (state, musics) {
    state.musics = musics;
  },
  updateMusic (state, payload) {
    Object.assign(state.musics[payload.id], payload.updates);
  },
  deleteMusic (state, id) { 
    Vue.delete(state.musics, id);
  },
  createMusic (state, payload) {
    Vue.set(state.musics, payload.id, payload.music);
  }
};

// Methods Assynchronous (Commits Mutations)
const actions = {
  reloadMusics ({ commit }) {
    axios.get(API_URL, { headers: authHeader() }).then(response => {
      if (response.data.musics) {
        commit('reloadMusics', response.data.musics);
      }
    });
  },

  updateMusic ({ commit }, payload) {
    commit('updateMusic', payload);
  },

  deleteMusic ({ commit }, id) {
    commit('deleteMusic', id);
  },
  
  createMusic ({ commit }, music) {
    let musicId = uid();
    let payload = {
      id: musicId,
      music: music
    };
    commit('createMusic', payload);
  }
};

// Get data from a State
const getters = {
  musics: (state) => {
    return state.musics;
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
};