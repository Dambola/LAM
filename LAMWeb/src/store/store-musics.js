import Vue from 'vue'
import { lamapi } from '../boot/axios'
import { uid } from 'quasar'

// The data goes here
const state = {
  musics: {}
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
    lamapi.get('music').then(response => {
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
    const params = {
      name: music.name,
      author: music.author,
      type1: music.type1,
      type2: music.type2,
      type3: music.type3,
    }

    lamapi.put('music', params).then(response => {
      if (response.data.id) {
        let payload = {
          id: response.data.id,
          music: music
        };

        commit('createMusic', payload);
      }
    });
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